---
source_url: "https://www.dremio.com/blog/experience-the-dremio-lakehouse-hands-on-with-dremio-nessie-iceberg-data-as-code-and-dbt/"
fetched: "2026-04-22"
title: "Dremio Lakehouse in Action with Iceberg & dbt"
author: "- "Alex Merced""
published: "2024-04-25"
clipped_from: obsidian-web-clipper
---
Join the [Dremio/dbt community by joining the dbt slack community](https://www.getdbt.com/community/join-the-community) and joining the **#db-dremio** channel to meet other dremio-dbt users and seek support.

Welcome to the cutting-edge world of the **[Dremio Lakehouse](https://www.dremio.com/solutions/data-lakehouse/)**, where the convergence of data lakes and data warehouses forms a powerful platform for data management and analytics. In this blog, we'll dive into how [Dremio](https://www.dremio.com/get-started), in collaboration with [Nessie](https://www.dremio.com/blog/what-is-nessie-catalog-versioning-and-git-for-data/), [Apache Iceberg](https://www.dremio.com/blog/apache-iceberg-101-your-guide-to-learning-apache-iceberg-concepts-and-practices/), and tools like [dbt](https://www.dremio.com/blog/using-dbt-to-manage-your-dremio-semantic-layer/), revolutionizes data handling by providing a cohesive environment that supports both the vast scalability of data lakes and the refined performance of data warehouses. We’ll take you through a hands-on exercise that showcases the full breadth of Dremio’s capabilities and integrations. From seamless data ingestion to sophisticated data-as-code management, you'll experience how to construct and manage a performant, easy-to-maintain data lakehouse. Whether you're a data engineer, scientist, or analyst, prepare to unlock new insights and efficiencies in your data workflows.

This exercise is based on the demo in [this video](https://youtu.be/gJnlpAeIPUE).

## Setting Up Our Environment

[Reference Git Repository for This Exercise](https://github.com/developer-advocacy-dremio/experience-dremio)

For this exercise, we will be creating an environment on our laptops using [Docker](https://www.docker.com/), so make sure you have Docker installed to do this exercise, if using Docker Desktop you may have to make sure you have at least 6GB of memory allocated to Docker. Open up your preferred IDE or text editor and create a docker-compose.yml in an empty folder with the following:

```
xxxxxxxxxx
```

```
version: "3"
```
```
​
```
```
services:
```
```
# Nessie Catalog Server Using In-Memory Store
```
```
nessie:
```
```
image: projectnessie/nessie:latest
```
```
container_name: nessie
```
```
networks:
```
```
experience-dremio:
```
```
ports:
```
```
- 19120:19120
```
```
# Minio Storage Server
```
```
minio:
```
```
image: minio/minio:latest
```
```
container_name: minio
```
```
environment:
```
```
- MINIO_ROOT_USER=admin
```
```
- MINIO_ROOT_PASSWORD=password
```
```
- MINIO_DOMAIN=storage
```
```
- MINIO_REGION_NAME=us-east-1
```
```
- MINIO_REGION=us-east-1
```
```
networks:
```
```
experience-dremio:
```
```
ports:
```
```
- 9001:9001
```
```
- 9000:9000
```
```
command: ["server", "/data", "--console-address", ":9001"]
```
```
# Dremio
```
```
dremio:
```
```
platform: linux/x86_64
```
```
image: dremio/dremio-oss:latest
```
```
ports:
```
```
- 9047:9047
```
```
- 31010:31010
```
```
- 32010:32010
```
```
environment:
```
```
- DREMIO_JAVA_SERVER_EXTRA_OPTS=-Dpaths.dist=file:///opt/dremio/data/dist
```
```
container_name: dremio
```
```
networks:
```
```
experience-dremio:
```
```
#MongoDB
```
```
mongodb:
```
```
image: mongo:latest
```
```
container_name: mongodb
```
```
environment:
```
```
MONGO_INITDB_ROOT_USERNAME: root
```
```
MONGO_INITDB_ROOT_PASSWORD: example
```
```
ports:
```
```
- "27017:27017"
```
```
networks:
```
```
experience-dremio:
```
```
#Postgres
```
```
postgres:
```
```
image: postgres:latest
```
```
container_name: postgres
```
```
environment:
```
```
POSTGRES_DB: mydb
```
```
POSTGRES_USER: myuser
```
```
POSTGRES_PASSWORD: mypassword
```
```
ports:
```
```
- "5435:5432"
```
```
networks:
```
```
experience-dremio:
```
```
#Superset
```
```
superset:
```
```
image: alexmerced/dremio-superset
```
```
container_name: superset
```
```
networks:
```
```
experience-dremio:
```
```
ports:
```
```
- 8080:8088
```
```
networks:
```
```
experience-dremio:
```

Here is a quick guide on the docker commands we'll use to control our environment:

- **`docker compose up`**: Will spin up all services listed in the docker-compose.yml
- `**docker compose down**`: Will spin down all services listed in the docker-compose.yml
- `**docker compose up serviceName**`: Will spin up the specified service in the docker-compose.yml
- `**docker compose down serviceName**`: will spin down the specified service in the docker-compose.yml
- `**docker compose up -d serviceName**`: Will spin up the specified service in the docker-compose.yml in detached mode (not blocking your terminal)
- `**docker exec -it serviceName command**`: run the specified command inside the specified service

\* For these commands to work, you need to run them in the same folder as the docker-compose.yml

## Try Dremio’s Interactive Demo

Explore this interactive demo and see how Dremio's Intelligent Lakehouse enables Agentic AI

## Setting Up Data in Postgres

The first step is to run our Postgres service. To do so just run the following command:

```
xxxxxxxxxx
```

```
docker compose up -d postgres
```

We will then get into the postgres shell to run some SQL to seed our data.

```
xxxxxxxxxx
```

```
docker exec -it postgres psql -U myuser -d mydb
```

Then let's run the following SQL to create our tables:

```
xxxxxxxxxx
```

```
CREATE TABLE inventory (
```
```
product_id SERIAL PRIMARY KEY,
```
```
product_name VARCHAR(255),
```
```
location_id INTEGER,
```
```
location_name VARCHAR(255),
```
```
quantity_available INTEGER,
```
```
reorder_level INTEGER,
```
```
last_restock_date DATE
```
```
);
```

Now run this SQL to insert our data:

```
xxxxxxxxxx
```

```
INSERT INTO inventory (product_name, location_id, location_name, quantity_available, reorder_level, last_restock_date)
```
```
VALUES
```
```
('Widget A', 1, 'Warehouse X', 150, 50, '2024-04-01'),
```
```
('Widget B', 1, 'Warehouse X', 90, 30, '2024-03-24'),
```
```
('Gadget C', 2, 'Warehouse Y', 200, 75, '2024-04-03'),
```
```
('Gadget D', 2, 'Warehouse Y', 60, 20, '2024-03-20'),
```
```
('Tool E', 3, 'Warehouse Z', 120, 40, '2024-03-15'),
```
```
('Tool F', 3, 'Warehouse Z', 30, 10, '2024-04-05'),
```
```
('Material G', 4, 'Warehouse A', 800, 100, '2024-04-02'),
```
```
('Material H', 4, 'Warehouse A', 500, 150, '2024-03-22'),
```
```
('Component I', 5, 'Warehouse B', 450, 125, '2024-03-18'),
```
```
('Component J', 5, 'Warehouse B', 300, 100, '2024-03-31'),
```
```
('Item K', 1, 'Warehouse X', 240, 100, '2024-04-10'),
```
```
('Item L', 1, 'Warehouse X', 180, 80, '2024-04-11'),
```
```
('Item M', 2, 'Warehouse Y', 220, 90, '2024-04-12'),
```
```
('Item N', 2, 'Warehouse Y', 140, 50, '2024-04-13'),
```
```
('Item O', 3, 'Warehouse Z', 130, 40, '2024-04-14'),
```
```
('Item P', 3, 'Warehouse Z', 110, 30, '2024-04-15'),
```
```
('Item Q', 4, 'Warehouse A', 300, 120, '2024-04-16'),
```
```
('Item R', 4, 'Warehouse A', 450, 150, '2024-04-17'),
```
```
('Item S', 5, 'Warehouse B', 500, 200, '2024-04-18'),
```
```
('Item T', 5, 'Warehouse B', 600, 250, '2024-04-19'),
```
```
('Item U', 1, 'Warehouse X', 500, 200, '2024-04-20'),
```
```
('Item V', 1, 'Warehouse X', 650, 300, '2024-04-21'),
```
```
('Item W', 2, 'Warehouse Y', 550, 220, '2024-04-22'),
```
```
('Item X', 2, 'Warehouse Y', 350, 140, '2024-04-23'),
```
```
('Item Y', 3, 'Warehouse Z', 450, 180, '2024-04-24'),
```
```
('Item Z', 3, 'Warehouse Z', 290, 120, '2024-04-25'),
```
```
('Item AA', 4, 'Warehouse A', 320, 160, '2024-04-26'),
```
```
('Item AB', 4, 'Warehouse A', 410, 205, '2024-04-27'),
```
```
('Item AC', 5, 'Warehouse B', 300, 150, '2024-04-28'),
```
```
('Item AD', 5, 'Warehouse B', 330, 165, '2024-04-29'),
```
```
('Item AE', 1, 'Warehouse X', 320, 120, '2024-05-01'),
```
```
('Item AF', 1, 'Warehouse X', 280, 110, '2024-05-02'),
```
```
('Item AG', 2, 'Warehouse Y', 430, 180, '2024-05-03'),
```
```
('Item AH', 2, 'Warehouse Y', 370, 150, '2024-05-04'),
```
```
('Item AI', 3, 'Warehouse Z', 210, 100, '2024-05-05'),
```
```
('Item AJ', 3, 'Warehouse Z', 190, 90, '2024-05-06'),
```
```
('Item AK', 4, 'Warehouse A', 600, 240, '2024-05-07'),
```
```
('Item AL', 4, 'Warehouse A', 450, 180, '2024-05-08'),
```
```
('Item AM', 5, 'Warehouse B', 680, 270, '2024-05-09'),
```
```
('Item AN', 5, 'Warehouse B', 750, 300, '2024-05-10'),
```
```
('Item AO', 1, 'Warehouse X', 400, 160, '2024-05-11'),
```
```
('Item AP', 1, 'Warehouse X', 330, 130, '2024-05-12'),
```
```
('Item AQ', 2, 'Warehouse Y', 220, 110, '2024-05-13'),
```
```
('Item AR', 2, 'Warehouse Y', 240, 120, '2024-05-14'),
```
```
('Item AS', 3, 'Warehouse Z', 260, 130, '2024-05-15'),
```
```
('Item AT', 3, 'Warehouse Z', 280, 140, '2024-05-16'),
```
```
('Item AU', 4, 'Warehouse A', 500, 250, '2024-05-17'),
```
```
('Item AV', 4, 'Warehouse A', 520, 260, '2024-05-18'),
```
```
('Item AW', 5, 'Warehouse B', 550, 275, '2024-05-19'),
```
```
('Item AX', 5, 'Warehouse B', 570, 285, '2024-05-20');
```
```
​
```
```
CREATE TABLE inventory_staging AS SELECT * FROM inventory;
```
```
​
```
```
INSERT INTO inventory_staging (product_name, location_id, location_name, quantity_available, reorder_level, last_restock_date)
```
```
VALUES
```
```
('Product AZ', 1, 'Warehouse X', 500, 200, '2024-05-21'),
```
```
('Product BA', 1, 'Warehouse X', 480, 190, '2024-05-22'),
```
```
('Product BB', 2, 'Warehouse Y', 450, 225, '2024-05-23'),
```
```
('Product BC', 2, 'Warehouse Y', 430, 215, '2024-05-24'),
```
```
('Product BD', 3, 'Warehouse Z', 400, 200, '2024-05-25'),
```
```
('Product BE', 3, 'Warehouse Z', 380, 190, '2024-05-26'),
```
```
('Product BF', 4, 'Warehouse A', 360, 180, '2024-05-27'),
```
```
('Product BG', 4, 'Warehouse A', 340, 170, '2024-05-28'),
```
```
('Product BH', 5, 'Warehouse B', 320, 160, '2024-05-29'),
```
```
('Product BI', 5, 'Warehouse B', 300, 150, '2024-05-30');
```

Now we can exit the Postgres shell with the command:

```
xxxxxxxxxx
```

```
q
```

## Setting Up Data in MongoDB

Now we will populate data in a Mongo Database, so let's spin up the Mongo service with the following command:

```
xxxxxxxxxx
```

```
docker compose up -d mongodb
```

Then we need to access the MongoDB shell:

```
xxxxxxxxxx
```

```
docker exec -it mongodb mongosh -u root -p example --authenticationDatabase admin
```

Let's switch to a database called "supplychain":

```
xxxxxxxxxx
```

```
use supplychain
```

Now let's add our data into "products" and "products\_staging" collections:

```
xxxxxxxxxx
```

```
db.products.insertMany([
```
```
{ product_id: 1, product_name: "Widget A", category: "Widgets", price: 19.99 },
```
```
{ product_id: 2, product_name: "Widget B", category: "Widgets", price: 21.99 },
```
```
{ product_id: 3, product_name: "Gadget C", category: "Gadgets", price: 29.99 },
```
```
{ product_id: 4, product_name: "Gadget D", category: "Gadgets", price: 24.99 },
```
```
{ product_id: 5, product_name: "Tool E", category: "Tools", price: 9.99 },
```
```
{ product_id: 6, product_name: "Tool F", category: "Tools", price: 14.99 },
```
```
{ product_id: 7, product_name: "Material G", category: "Materials", price: 5.99 },
```
```
{ product_id: 8, product_name: "Material H", category: "Materials", price: 7.99 },
```
```
{ product_id: 9, product_name: "Component I", category: "Components", price: 15.99 },
```
```
{ product_id: 10, product_name: "Component J", category: "Components", price: 13.99 },
```
```
{ product_id: 11, product_name: "Item K", category: "Widgets", price: 22.99 },
```
```
{ product_id: 12, product_name: "Item L", category: "Widgets", price: 23.99 },
```
```
{ product_id: 13, product_name: "Item M", category: "Gadgets", price: 34.99 },
```
```
{ product_id: 14, product_name: "Item N", category: "Gadgets", price: 29.99 },
```
```
{ product_id: 15, product_name: "Item O", category: "Tools", price: 19.99 },
```
```
{ product_id: 16, product_name: "Item P", category: "Tools", price: 24.99 },
```
```
{ product_id: 17, product_name: "Item Q", category: "Materials", price: 15.99 },
```
```
{ product_id: 18, product_name: "Item R", category: "Materials", price: 17.99 },
```
```
{ product_id: 19, product_name: "Item S", category: "Components", price: 25.99 },
```
```
{ product_id: 20, product_name: "Item T", category: "Components", price: 27.99 },
```
```
{ product_id: 21, product_name: "Item U", category: "Widgets", price: 32.99 },
```
```
{ product_id: 22, product_name: "Item V", category: "Widgets", price: 33.99 },
```
```
{ product_id: 23, product_name: "Item W", category: "Gadgets", price: 44.99 },
```
```
{ product_id: 24, product_name: "Item X", category: "Gadgets", price: 39.99 },
```
```
{ product_id: 25, product_name: "Item Y", category: "Tools", price: 29.99 },
```
```
{ product_id: 26, product_name: "Item Z", category: "Tools", price: 34.99 },
```
```
{ product_id: 27, product_name: "Item AA", category: "Materials", price: 25.99 },
```
```
{ product_id: 28, product_name: "Item AB", category: "Materials", price: 27.99 },
```
```
{ product_id: 29, product_name: "Item AC", category: "Components", price: 35.99 },
```
```
{ product_id: 30, product_name: "Item AD", category: "Components", price: 37.99 },
```
```
{ product_id: 31, product_name: "Item AE", category: "Widgets", price: 28.99 },
```
```
{ product_id: 32, product_name: "Item AF", category: "Widgets", price: 29.99 },
```
```
{ product_id: 33, product_name: "Item AG", category: "Gadgets", price: 39.99 },
```
```
{ product_id: 34, product_name: "Item AH", category: "Gadgets", price: 35.99 },
```
```
{ product_id: 35, product_name: "Item AI", category: "Tools", price: 21.99 },
```
```
{ product_id: 36, product_name: "Item AJ", category: "Tools", price: 22.99 },
```
```
{ product_id: 37, product_name: "Item AK", category: "Materials", price: 16.99 },
```
```
{ product_id: 38, product_name: "Item AL", category: "Materials", price: 18.99 },
```
```
{ product_id: 39, product_name: "Item AM", category: "Components", price: 26.99 },
```
```
{ product_id: 40, product_name: "Item AN", category: "Components", price: 28.99 },
```
```
{ product_id: 41, product_name: "Item AO", category: "Widgets", price: 33.99 },
```
```
{ product_id: 42, product_name: "Item AP", category: "Widgets", price: 34.99 },
```
```
{ product_id: 43, product_name: "Item AQ", category: "Gadgets", price: 45.99 },
```
```
{ product_id: 44, product_name: "Item AR", category: "Gadgets", price: 40.99 },
```
```
{ product_id: 45, product_name: "Item AS", category: "Tools", price: 30.99 },
```
```
{ product_id: 46, product_name: "Item AT", category: "Tools", price: 35.99 },
```
```
{ product_id: 47, product_name: "Item AU", category: "Materials", price: 26.99 },
```
```
{ product_id: 48, product_name: "Item AV", category: "Materials", price: 28.99 },
```
```
{ product_id: 49, product_name: "Item AW", category: "Components", price: 36.99 },
```
```
{ product_id: 50, product_name: "Item AX", category: "Components", price: 38.99 },
```
```
]);
```
```
​
```
```
db.products_staging.insertMany([
```
```
{ product_id: 51, product_name: "Product AZ", category: "Widgets", price: 40.99 },
```
```
{ product_id: 52, product_name: "Product BA", category: "Widgets", price: 41.99 },
```
```
{ product_id: 53, product_name: "Product BB", category: "Gadgets", price: 42.99 },
```
```
{ product_id: 54, product_name: "Product BC", category: "Gadgets", price: 43.99 },
```
```
{ product_id: 55, product_name: "Product BD", category: "Tools", price: 44.99 },
```
```
{ product_id: 56, product_name: "Product BE", category: "Tools", price: 45.99 },
```
```
{ product_id: 57, product_name: "Product BF", category: "Materials", price: 46.99 },
```
```
{ product_id: 58, product_name: "Product BG", category: "Materials", price: 47.99 },
```
```
{ product_id: 59, product_name: "Product BH", category: "Components", price: 48.99 },
```
```
{ product_id: 60, product_name: "Product BI", category: "Components", price: 49.99 }
```
```
]);
```

After running these queries, we can leave the Mongo Shell with the command:

```
xxxxxxxxxx
```

```
exit
```

## Setting Up our Minio Data Lake and Nessie Catalog

Now it is time to spin up our Minio object storage-based data lake and create a bucket to store our Apache Iceberg tables, which a Nessie catalog will catalog. We can spin up these services with the command:

```
xxxxxxxxxx
```

```
docker compose up -d minio nessie
```

Head over to localhost:9001 in your browser and log in to the Minio dashboard with the username "admin" and password "password."

Once you are logged in, create a bucket called "warehouse," and we have everything we need. Feel free to visit this dashboard after we make some Apache Iceberg tables to see the created files.

![](https://www.dremio.com/wp-content/uploads/2024/04/image-72.png)

## Connecting Our Data Sources to Dremio

Next, it is time to start Dremio and get our data sources connected. Let's get Dremio started with the following command:

```
xxxxxxxxxx
```

```
docker compose up -d dremio
```

After a minute or two, Dremio should be up and running and we can visit it in the browser at localhost:9047 where we'll have to create our initial user account:

![](https://www.dremio.com/wp-content/uploads/2024/04/image-73.png)

Once you are inside Dremio, we can begin adding our data sources by clicking the "Add Source" button in the bottom left corner.

### Add Our Nessie Source

- Select Nessie from "Add Source"
- On the General Tab
	- name: nessie
		- URL: http://nessie:19120/api/v2
		- auth: none
![](https://www.dremio.com/wp-content/uploads/2024/04/image-74.png)

- On the Storage tab:
	- root path: warehouse
		- access key: admin
		- secret key: password
		- connection properties:
		- fs.s3a.path.style.access: true
				- fs.s3a.endpoint: minio:9000
				- dremio.s3.compat: true
		- Encrypt Connection: false
![](https://www.dremio.com/wp-content/uploads/2024/04/image-76.png)

### Add Our Postgres Source

Now let’s add a Postgres source with the following settings:

- Name: postgres
- Host: postgres
- Port: 5432
- Database Name: mydb
- Username: myuser
- Password: mypassword
![](https://www.dremio.com/wp-content/uploads/2024/04/image-77.png)

### Add Our MongoDB Source

Now let’s add a MongoDB source with the following settings:

- Name: mongodb
- Host: mongodb
- Port: 27017
- Auth Database Name: admin
- Username: root
- Password: example
![](https://www.dremio.com/wp-content/uploads/2024/04/image-78.png)

## Creating Our Apache Iceberg Tables

Now that our data sources are connected to Dremio a few things are now possible:

- Dremio has full DDL/DML capabilities with Apache Iceberg catalog sources like Nessie, Apache Hive and Glue.
- Dremio can federate queries between all connected sources

The benefit here is we can easily use [SQL to ingest data from different data sources into our](https://www.dremio.com/blog/ingesting-data-into-apache-iceberg-tables-with-dremio-a-unified-path-to-iceberg/) Apache Iceberg catalogs. Here are some examples of patterns you may use:

- **CREATE TABLE AS (CTAS)** for creating new Iceberg tables from existing data sources
- **INSERT INTO SELECT** to add records or do incremental appends to our Apache Iceberg tables from other sources
- **MERGE INTO** to run upserts into that update and insert records into our Apache Iceberg tables
- **COPY INTO** to insert data from Parquet, CSV and JSON files on your data lake into APache Iceberg tables

We will take our "products" and "inventory" tables and make them Apache Iceberg tables cataloged by Nessie and stored in Minio. But before we do that, we want to organize the data in our catalog into different "Data Products," so in the Nessie catalog, create a "supply chain" folder. We could apply any three-layer pattern we like inside the folder, such as bronze/silver/gold, raw/business/application, etc. In this case, I will use Raw/Curated/Production semantics, making a folder for each layer.

![](https://www.dremio.com/wp-content/uploads/2024/04/image-79.png)

We can head to the Dremio SQL editor and run the following SQL.

```
xxxxxxxxxx
```

```
-- POSTGRES TO APACHE ICEBERG
```
```
CREATE TABLE nessie.supplychain.raw.inventory AS SELECT * FROM postgres.public.inventory;
```
```
​
```
```
-- MONGODB TO APACHE ICEBERG
```
```
CREATE TABLE nessie.supplychain.raw.products AS SELECT * FROM mongodb.supplychain.products;
```

Run the SQL:

![](https://www.dremio.com/wp-content/uploads/2024/04/image-80.png)

You will now find the raw Apache Iceberg tables in your Nessie catalog supplychain.raw folder signified by purple table icons that signal a physical dataset. You can additionally head back to minio to find the files stored in the warehouse bucket we created earlier. Congrats, you've just ingested data into Apache Iceberg.

Keep in mind that while we are using the Dremio UI to enter this SQL manually, Dremio has JDBC, ODBC, Apache Arrow Flight, and a REST API interface that can be used to send SQL to Dremio externally via Orchestration tools, BI Tools, Python Notebooks, or any other tool that can leverage these open interfaces. This makes it easy to automate work to Dremio via SQL, including administrative tasks like creating users, setting permissions, and more.

## Ingesting Data using Nessie's Data as Code Capabilities

Let's assume the data in our staging tables has been coming over time and that we now need to ingest into our existing tables. In this scenario, we will assume our dataset is append-only, so only new records should be added, and no old records need to be updated. This means we should probably use INSERT INTO over MERGE INTO for this work.

It isn't just any old catalog tracking our Apache Iceberg tables; it is a Nessie catalog, meaning we can use catalog-level versioning to isolate the work on our tables from our user's querying production data.

Let's create a branch, ingest the new data, and confirm that the changes only appear on the Branch.

```
xxxxxxxxxx
```

```
-- Create the Branch
```
```
CREATE BRANCH IF NOT EXISTS ingest IN nessie;
```
```
-- Switch to Branch
```
```
USE BRANCH ingest IN NESSIE;
```
```
​
```
```
-- Update Inventory
```
```
INSERT INTO nessie.supplychain.raw.inventory
```
```
SELECT *
```
```
FROM postgres.public."inventory_staging"
```
```
WHERE product_id > (SELECT COALESCE(MAX(product_id), 0) FROM nessie.supplychain.raw.inventory);
```
```
-- Update Products
```
```
INSERT INTO nessie.supplychain.raw.products
```
```
SELECT *
```
```
FROM mongodb.supplychain."products_staging"
```
```
WHERE product_id > (SELECT COALESCE(MAX(product_id), 0) FROM nessie.supplychain.raw.products);
```
```
​
```
```
-- Compare Tables Between Branches
```
```
SELECT * FROM nessie.supplychain.raw.inventory AT BRANCH "main";
```
```
SELECT * FROM nessie.supplychain.raw.inventory AT BRANCH ingest;
```
```
SELECT * FROM nessie.supplychain.raw.products AT BRANCH "main";
```
```
SELECT * FROM nessie.supplychain.raw.products AT BRANCH ingest;
```

If you look over the results of each query, you'll see more records in the ingest branch than in the main branch. The where clause in our insert into statements facilitates incremental appends, only adding records with IDs that don't yet exist in the target table.  
  
We can run data quality checks using raw SQL or tools like Great Expectations without worrying that production queries are seeing the yet-to-be-validated data. Once the data is validated to your liking, we can merge and publish the changes to all our tables in the catalog from the ingest branch

```
xxxxxxxxxx
```

```
-- Merge Branches
```
```
MERGE BRANCH ingest INTO main IN nessie;
```
```
​
```
```
-- Confirm that it worked
```
```
SELECT * FROM nessie.supplychain.raw.inventory AT BRANCH "main";
```
```
SELECT * FROM nessie.supplychain.raw.inventory AT BRANCH ingest;
```
```
SELECT * FROM nessie.supplychain.raw.products AT BRANCH "main";
```
```
SELECT * FROM nessie.supplychain.raw.products AT BRANCH ingest;
```

That's all it takes, again any SQL can be externally sent to Dremio so you can use Orchestration tools to orchestrate CI/CD pipelines that:

1. Create a Branch
2. Ingest Data
3. Run Validation and Quality Checks
4. If Validations are successful, merge the branch publishing the data
5. If Validations fail, do not merge and deliver an error report to the engineer

## Curating Our Semantic Layer with dbt

On top of our raw data, we will want to create layers of virtual views of the data to serve the different needs of our data consumers. This can be done by the Data Engineer or by Data Analysts/Scientists using dbt to efficiently orchestrate the SQL needed to craft your layers of views.

To use dbt you'll need to have Python installed and install the following Python library:

```
xxxxxxxxxx
```

```
pip install dbt-dremio
```

Once this is installed in the activated Python environment, you can run the following command to create our debt project.

```
xxxxxxxxxx
```

```
dbt init supplychainviews
```

This will begin a series of questions to configure your dbt profile:

1. Select Dremio as the Database
2. Choose software with username and password
3. host is 127.0.0.1
4. port is 9047
5. enter your username
6. enter your password
7. false for using SSL
8. put down nessie for object storage source (can be any object storage or apache iceberg catalog source)
9. put supplychain.raw as the schema (the sub namespace in the source, where tables will materialize by default)
10. put down nessie for space (this can be any nessie catalog or dremio software space)
11. put supplychain.raw for schema (sub namespace within the space where views will be created by default)
12. choose the default for threads

Your dbt profile is now configured and should be ready to go. If you ever need to update it you should find the yaml file with the different dbt profiles in the ~/.dbt folder.

We want to edit this section of the dbt\_project.yaml file:

```
xxxxxxxxxx
```

```
# In this example config, we tell dbt to build all models in the example/
```
```
# directory as views. These settings can be overridden in the individual model
```
```
# files using the \`{{ config(...) }}\` macro.
```
```
models:
```
```
supplychainviews:
```
```
# Config indicated by + and applies to all files under models/example/
```
```
example:
```
```
+materialized: view
```

This is the section where we define how our models will be categorized (a model is an SQL statement whose results will be made into a table or view in Dremio). So write no, we only have one category of views, for example. This means it will look for SQL files in the models/example folder whenever we run debt; let's create something more aligned with our data products structure.

```
xxxxxxxxxx
```

```
models:
```
```
supplychainviews:
```
```
# Config indicated by + and applies to all files under models/#####
```
```
raw:
```
```
+database: nessie
```
```
+schema: supplychain.raw
```
```
+materialized: table
```
```
curated:
```
```
+database: nessie
```
```
+schema: supplychain.curated
```
```
+materialized: view
```
```
production:
```
```
+database: nessie
```
```
+schema: supplychain.production
```
```
+materialized: view
```

So, the +database and +schema determine where a view or table will be created with models in a certain category, and the +materialized determines whether the model's result will be a view (no copying data) or a table (writing new data copies).

So, as we have it, I only want tables to materialize in my raw layers and for my curated and production layers to be views created in their respective locations.

We need to create a raw, curated, and production folder within the models folder to house my dbt models.

![](https://www.dremio.com/wp-content/uploads/2024/04/image-81.png)

We are going to make two views, so we'll need two models:

- models/curated/inv\_prod\_curated\_join.sql (this will be the raw join of our product and inventory table)
- models/production/inv\_prod\_view.sql (this will be the join only showing the columns we want end users to see)

The inv\_prod\_curated\_join.sql file should look like:

```
xxxxxxxxxx
```

```
SELECT * FROM nessie.supplychain.raw.inventory as i INNER JOIN nessie.supplychain.raw.products as p ON i.product_id = p.product_id;
```

Then the inv\_prod\_view.sql file should look like:

```
xxxxxxxxxx
```

```
SELECT
```
```
product_id,
```
```
location_name,
```
```
product_name,
```
```
price
```
```
FROM
```
```
{{ ref('inv_prod_curated_join') }}
```

You may notice the odd-looking `***{{ ref('inv_prod_curated_join') }}***` which uses a templating syntax called "jinja." This syntax allows us to call Python functions in our SQL expressions. In this case, the "ref" function will enable us to refer to another model by its filename. When dbt sees this, it knows that this model depends on the referenced model being run first, and this ensures that dbt runs all your SQL models in the correct order every time. There are many other functions that DBT makes available for all sorts of use cases, such as one-time configurations and so on.

We can now run these models by simply running the command:

```
xxxxxxxxxx
```

```
dbt run
```

\* Make sure to run this command in the same folder at your dbt\_project.yml

When you run this command, dbt will assess all your models to determine the order they need to be run in, then establish a connection using the profile we created when we ran "dbt init" and run the SQL, creating views and tables in the order we specified. When it is done, we should be able to head back to Dremio and see our views in the curated and production folders.

![](https://www.dremio.com/wp-content/uploads/2024/04/image-82.png)

We've now curated the views and can query them from Dremio. What if, later on we decided we wanted a few more columns in my production views, we can just update our inv\_prod\_view dbt model to something like this:

```
xxxxxxxxxx
```

```
SELECT
```
```
product_id,
```
```
location_name,
```
```
product_name,
```
```
price
```
```
reorder_level,
```
```
quantity_available as quantity
```
```
FROM
```
```
{{ ref('inv_prod_curated_join') }}
```

Then, we can just run our dbt models, and the additional columns will be available the next time we query the view; this makes it very easy to make requested updates to your modeling.

![](https://www.dremio.com/wp-content/uploads/2024/04/image-83.png)

The great thing about using dbt to track all your SQL is you can check your dbt project into version control with git. This gives you two layers of observability into changes.

- All changes to your tables and views in a Nessie catalog create commits, allowing you to time travel the catalog and see who made what changes.
- git can track changes to the raw SQL code, giving you another layer of visibility into your historical modeling and where changes are coming from.

## Accelerating Our Datasets with Reflections

Now that we have our data connected, ingested, and curated in Dremio, we can begin delivering a BI Dashboard from our data. BI Dashboards are usually the result of running process-intensive aggregation queries against our data. While Dremio [provides performance equal to or faster than the top data warehousing solution,](https://www.dremio.com/blog/how-dremio-delivers-fast-queries-on-object-storage-apache-arrow-reflections-and-the-columnar-cloud-cache/) our BI Dashboards and compute bills will be better served by pre-computing these aggregate computations. Traditionally, analysts would accomplish this [by creating BI Cubes or Extracts](https://www.dremio.com/blog/bi-dashboard-acceleration-cubes-extracts-and-dremios-reflections/) that would usually be housed within the BI tool, which wouldn't be helpful to other teams using a different BI tool with the same data. Also, extracts and cubes would require much maintenance and configuration, making them not a perfect solution.

With Dremio, acceleration on the raw or aggregate level can be done to benefit any team using the same data in any tool and requires much less effort on behalf of the engineer or the analyst. This acceleration feature is called reflections; essentially, Dremio will create managed materializations as Apache Iceberg tables in your data lake and swap them out when it accelerates a query on the source table/view or child views of the source. This can be done as easy as flipping a switch.

Let's enable reflections on our production views by opening them and clicking on the "edit" button. This will take us to a screen where we can edit things like the dataset's wiki page and reflections.

![](https://www.dremio.com/wp-content/uploads/2024/04/image-84.png)

Once we are in the edit view of the dataset, click on the reflections tab at the top to go to the reflections screen. Here, we can enable aggregate reflections and select which measures and dimensions we want to optimize for.

![](https://www.dremio.com/wp-content/uploads/2024/04/image-85.png)

Once we see the green checkmark confirming the reflection is created, Dremio will use these reflections to accelerate any aggregate queries on these dimensions and measures. Reflections are refreshed on a cadence to reflect the most up-to-date information. Dremio also has reflection recommendations, which will identify opportunities to speed up queries and lower costs using reflections and suggest them to you.

## Building our BI Dashboard

So now, nothing is standing between us and building performant BI dashboards from which we can get valuable business insights. We will be using the [open-source Apache Superset to build our dashboards](https://www.dremio.com/blog/bi-dashboards-101-with-dremio-and-superset/) which we can start with (if you need to free up memory, feel free to spin down MongoDB and postgres at this point):

```
xxxxxxxxxx
```

```
docker compose up -d superset
```

This will spin up the docker container with Superset which will still need to be initialized with the following command:

```
xxxxxxxxxx
```

```
docker exec -it superset superset init
```

After a few minutes, you should be able to login to superset at localhost:8080 using the username "admin" and the password "admin" to login ([rebuild the underlying image to change these](https://github.com/developer-advocacy-dremio/quick-guides-from-dremio/blob/main/guides/superset-dremio.md)).

Click on "settings" and select "database connections." We will create a new connection. From the create connection modal, select "Other" as your database. To connect Apache Superset to Dremio, pass in the following URL with your Dremio username and password.

```
xxxxxxxxxx
```

```
dremio+flight://USERNAME:PASSWORD@dremio:32010/?UseEncryption=false
```

![](https://www.dremio.com/wp-content/uploads/2024/04/image-86.png)

Once the connection is created, we can click the + sign at the top right corner, and next, we will add a dataset, adding our production dataset.

![](https://www.dremio.com/wp-content/uploads/2024/04/image-87.png)

Once the dataset is added, we can create a pie chart, with the dimension being the location\_name and the metric being the sum of the quantity.

![](https://www.dremio.com/wp-content/uploads/2024/04/image-88.png)

Next, let's create a chart showing the product as the dimension and the sum of the quantity as the metric.

![](https://www.dremio.com/wp-content/uploads/2024/04/image-89.png)

Now, with these two charts saved, let's create a new dashboard and these two charts to it!

![](https://www.dremio.com/wp-content/uploads/2024/04/image-90.png)

## Conclusion

We have seen the entire Dremio Lakehouse lifecycle, from data ingestions to BI Dashboards. At this point, you can shut down all the containers we've spun up running.

```
xxxxxxxxxx
```

```
docker compose down
```

The Dremio Lakehouse experience offers an easy and fast way to deliver data to all those business-critical use cases. While you can deploy [Dremio as self-managed software in a Kubernetes environment](https://docs.dremio.com/current/get-started/kubernetes-quickstart), you can get some nice bonuses when working with a [Dremio Cloud Managed environment](https://docs.dremio.com/cloud/get-started/) such as:

- Text-to-SQL features to make it even easier for less technical users to generate the views of the data they need
- Generative AI Wiki generation to make it even easier to document your datasets
- Integrated Nessie-based lakehouse catalog that provides a robust UI for commit/branch/tag observability and management along with automated table management features.
- Robust autoscaling features to make sure you always have the performance you need without risking the cost of dangling instances
- Not having to manage manual software upgrades

Learn more about [Dremio](https://www.dremio.com/get-started); below are some additional exercises if you liked this one to keep learning more about what Dremio offers.

- [Getting Started with Nessie, Dremio and Apache Iceberg on your Laptop](https://www.dremio.com/blog/intro-to-dremio-nessie-and-apache-iceberg-on-your-laptop/)
- [From MongoDB to Apache Iceberg to BI Dashboard](https://www.dremio.com/blog/from-mongodb-to-dashboards-with-dremio-and-apache-iceberg/)
- [From SQLServer to Apache Iceberg to BI Dashboard](https://www.dremio.com/blog/from-sqlserver-to-dashboards-with-dremio-and-apache-iceberg/)
- [From Postgres to Apache Iceberg to BI Dashboard](https://www.dremio.com/blog/from-postgres-to-dashboards-with-dremio-and-apache-iceberg/)
- [Creating BI Dashboards with AWS Glue and Dremio](https://www.dremio.com/blog/bi-dashboards-with-apache-iceberg-using-aws-glue-and-apache-superset/)
- [Running Graph Queries on Apache Iceberg Tables with Puppygraph and Dremio](https://www.dremio.com/blog/run-graph-queries-on-apache-iceberg-tables-with-dremio-puppygraph/)
- [Streaming to a Data Lakehouse with Upsolver and Dremio](https://www.dremio.com/blog/streaming-and-batch-data-lakehouses-with-apache-iceberg-dremio-and-upsolver/)
- [BI Dashboards 101 with Dremio and Apache Superset](https://www.dremio.com/blog/bi-dashboards-101-with-dremio-and-superset/)