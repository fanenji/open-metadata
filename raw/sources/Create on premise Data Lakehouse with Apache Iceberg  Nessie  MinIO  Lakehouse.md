---
title: "Create on premise Data Lakehouse with Apache Iceberg | Nessie | MinIO | Lakehouse"
source: "https://www.youtube.com/watch?v=ihSpLg44JBw"
author:
  - "[[BI Insights Inc]]"
published: 2023-11-16
created: 2026-05-07
description: "In this video cover the data lakehouse. A data lake house is a concept that combines elements of both data lakes and data warehouses to bring us the best of both worlds. It aims to provide a unified p"
tags:
  - "clippings"
topic:
type: "note"
---
![](https://www.youtube.com/watch?v=ihSpLg44JBw)

In this video cover the data lakehouse. A data lake house is a concept that combines elements of both data lakes and data warehouses to bring us the best of both worlds. It aims to provide a unified platform for storing, managing, and analyzing both unstructured data and structured data.  
  
What is Data Lake? https://aws.amazon.com/big-data/datalakes-and-analytics/what-is-a-data-lake/  
  
Link to GitHub repo: https://github.com/hnawaz007/pythondataanalysis/tree/main/data-lakehouse  
  
Link to Data Lake Video:  
On-premis: https://www.youtube.com/watch?v=DLRiUs1EvhM&t  
AWS: https://www.youtube.com/watch?v=KvtxdF7b\_l8  
  
💥Subscribe to our channel:  
https://www.youtube.com/c/HaqNawaz  
  
📌 Links  
\-----------------------------------------  
#️⃣ Follow me on social media! #️⃣  
  
🔗 GitHub: https://github.com/hnawaz007  
📸 Instagram: https://www.instagram.com/bi\_insights\_inc  
📝 LinkedIn: https://www.linkedin.com/in/haq-nawaz/  
🔗 https://medium.com/@hnawaz100  
  
\-----------------------------------------  
  
#dataanalytics #datalakehouse #opensource  
  
Topics covered in this video:  
\==================================  
0:00 - Introduction to Data Lakehouse  
0:53 - Data Lakehouse prominent Features  
1:50 - Data Lake from Previouse session  
2:31 - Data Lakehouse Overview  
3:34 - Tech Stack of on-premise Data Lakehouse  
3:44 - Start Docker Containers  
4:02 - MinIO (S3) Buckets, File(s) & Keys  
4:56 - Configure Dremio  
5:07 - Add MinIO (S3) Source  
5:57 - Add Nessie Catalog  
6:38 - Format File  
7:33 - Create Iceberg Table  
7:59 - Copy Data to Table  
8:35 - SQL DML Operations  
9:47 - Table History and Time Travel  
10:29 - Coming Soon

## Transcript

### Introduzione a Data Lakehouse

**0:00** · hello and uh welcome one and all today we will cover data lak house data Lakehouse is a concept that combines element of both data Lake and data warehouse to bring us the best of both worlds it aims to provide a unified platform for storing managing analyzing both structure and unstructured data the

**0:23** · term is often associated with the evolving landscape of big data and analytics we have covered data Lake in AWS and on premise I will leave the link to both of the videos in the description below data lake house improves upon the capabilities of data Lake it brings features such as schema Evolution transaction consistency and time travel and roll back amongst other features like databases data lake houses support

### Caratteristiche principali di Data Lakehouse

**0:56** · schema Evolution allowing changes to the data structure structure without requiring a full rewrite of the data set this is crucial for handling evolving data sources and changing business requirements data lake houses often Implement transactional capabilities to ensure data consistency this means that right operations are automic and the system maintains a consistent State even in the face of failures or partial updates time travel enables reproducible

**1:28** · queries that use exactly the same table snapshot or lets user easily examine changes version rollbacks allows user quickly to correct Problems by resetting the table to a good State we will build on the data L concept and introduce new

**1:46** · technologies that transform the data Lake to a data lake house previously we have built a data lake with minio a compatible S3 storage layer we'll utilize this to Stage our data for the catalog we have used Hive metast store that allowed us to map S3 files to the tables that enabled us to use quy engine to analyze S3 data this is great as we

### Data Lake dalla sessione precedente

**2:13** · can quy files containing structured and unstructured data however this catalog does not have the capabilities to handle schema changes or to ensure the data is in a consistent State we had to maintain and update the files in S3 in this iteration we replace the hive metast store with project Nessie it works with

### Panoramica di Data Lakehouse

**2:35** · Apachi Iceberg table format a table format allows us to manage the data files in our data leg and brings in the data management capabilities such as the ability to perform DML time travel and roll backs it forms the basis of a data

**2:52** · lake house architecture Nessie holds the reference to the current metadata file changes to the content of the data Lake are recorded in Nessie as commits without copying the actual data Nessie catalog brings in the asset guarantees to any transaction to the iceberg table therefore user get a consistent view of all the data processing engine for this specific demo would be Dro we'll use it

**3:20** · to create Iceberg tables and do various DML operations on the data files all of our raw data files will be stored in the data Lake which is an S3 bucket hosted on Min iio we'll use Docker composed to set up the data lake house with the above text stack Docker desktop is a prerequisite for this let's create the docker containers for S3 Nessie and Dru

### Stack tecnologico di Data Lakehouse on-premise

### Avvio di Docker Contenitori

**3:48** · if you're running this for the first time it'll take some time to download the images from Docker Hub and once the images are downloaded Docker will create and start the containers we'll need to configure our S3 and catalog within our processing engine Dro for S3 we need to

### Bucket, file e chiavi MinIO (S3)

**4:08** · log in and create Keys login credentials are defined in the docker compost file so let's grab those and we'll log into M.O on the following URL and generate the access and the secret key once the keys are generated we can either copy them or download them for later use while are here let's create few buckets one to hold the data files and

**4:35** · another to house the catalog schema we'll call the bucket for the files data Lake and the catalog bucket we'll call it Warehouse in the data Lake bucket let's import a folder with a CSV file in it

**4:51** · we'll import this data into an iceberg table later on let's launch and configure Dro next on the first launch we'll need need to create a user and provide details along with a password once we logged in we'll add an S3 bucket as a source in The Dru first is the S3 bucket that stores the data so under sources we select the S3 provided a name

### Configura Dremio

### Aggiungi sorgente MinIO (S3)

**5:18** · and we'll Supply our access and the secret key and let's uncheck the encrypt Connection checkbox in the advanced option section we find fug connection properties make sure the ctas format is set to Iceberg we Define the S3 endpoint and set it to Min iio in

**5:40** · addition we set the sty access and S3 compatibility to True finally we provide our bucket's name let's go ahead and save these changes upon success we'll see our data Lake bucket as a source in Dro next we add the nessi catalog as a source we Define a name for this and provide the nessi's URL the authentication type is none under storage we provide the same details such as our access and secret key along with

### Aggiungi catalogo Nessie

**6:12** · the connection properties however our root path will be the warehouse bucket with these changes let's save the Nessie source and if this is successful you'll see nessie's catalog as a source in Dro we have our data League bucket and ness's catalog as our sources if you click on the data Lake we see the folder and once we navigate to the next folder in it we see the data files we select the file and on

### Formatta file

**6:42** · this screen we set the format delimiter and the Escape character we make sure our data looks correct before closing this window I see that our column headers are not correct so I'll extract the column names this looks much better let's save the changes this redirect us to the query engine we can run the query against our files here I'll execute the query to see the data this query displays the data in the file our file

**7:13** · changes color and if we expand it it tries to infer schema details from the file however it's not accurate we'll fix it with the iceberg table let's navigate to the nessie's catalog and create a table we can switch the context in the SQL pane once we're in the nessie's catalog I'll paste in a table ddl we are

### Crea tabella Iceberg

**7:37** · creating a table called sales and then asy catalog we Define the data type for each column let's go ahead and execute the script to create the table we can go ahead and select from it it is empty at the moment and it'll take a few seconds before it appears under the catalog now we copy the S3 data in this table using the copy command we specify the file location and the file name once we execute this it returns rows inserted

### Copia dati nella tabella

**8:09** · and it will display the number of Records we have inserted in this case it is 60,000 upon cing the table we see the data in this table now and our date column is picked up as date since this catalog allows us to execute DML operations we can perform update and or delete operations on this table let's go ahead and uh look at few examples let's put a ver clause on this select where product subcategory name equal caps if

### Operazioni SQL DML

**8:41** · we run this this only displays data for caps now we run an update statement against this table let's update the product subcategory name to AWC caps now if we run the same select again we should see the product category name values as AWC caps great this verifies

**9:03** · that we can run DML operations on our data using this catalog also we can see the changes we are making as commits on the left of the SQL pane we can load any of these changes and revert back to check the schema Evolution let's delete the index column this is the column A in our data set after this change our

**9:27** · select should no longer display this column we can also update the column names with an alter statement we can also create views based on this data to Target specific rows for example we can create a view for the us we can check the table history since

### Cronologia della tabella e viaggio nel tempo

**9:47** · ness's catalog keeps track of all the changes and it has a pointer to the current state of the table we can check the table history and see the changes in this table at various stages with the help of the snapshot we can travel back in time and see how this table looked at a particular time in addition we can see the files associated with this table pii

**10:10** · Iceberg brings the database functionality to the data Lake we can execute SQL DML statements against our data Lake files it brings transactional consistency and schema Evolution to the data Lake World feel free to explore further on apachi ice B in the next

### Prossimamente

**10:30** · session we'll explore branching and merging with Nessie this is all on data Lake for now I hope you enjoy the session like share and subscribe take care and I'll see you in the next video