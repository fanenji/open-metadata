---
title: "Loading Parquet in PostgreSQL via DuckDB: Testing queries and exploring the Core"
source: https://medium.com/@ahuarte/loading-parquet-in-postgresql-via-duckdb-testing-queries-and-exploring-the-core-1d667ae67dc2
author:
  - "[[ah]]"
published: 2023-11-05
created: 2026-04-08
description: "Loading Parquet in PostgreSQL via DuckDB: Testing queries and exploring the Core In the realm of data management and analytics, PostgreSQL has long been a popular choice as an open-source relational …"
tags:
  - clippings
  - duckdb
  - parquet
topic:
type: note
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*p_kafhoO6TGx4g_QAGjIMw.png)

In the realm of data management and analytics, [**PostgreSQL**](https://www.postgresql.org/) has long been a popular choice as an open-source relational database management system. It offers robust features for handling structured data. However, when it comes to managing and analyzing large volumes of data efficiently, other technologies like [**Parquet**](https://parquet.apache.org/) and [**DuckDB**](https://duckdb.org/) have made their mark.

In this article, we’ll delve into the process of integrating ***DuckDB*** into ***PostgreSQL*** to load ***Parquet*** files as foreign tables, providing a powerful solution for data analytics.

One of the crucial elements that make this integration possible is the [**DuckDB FDW (Foreign Data Wrapper)**](https://github.com/alitrack/duckdb_fdw), an opensource *PostgreSQL* extension that allows us to load *DuckDB* into *PostgreSQL*.

## Understanding the Components

Before we embark on our exploration, let’s briefly introduce the key components involved:

1. **PostgreSQL**: *PostgreSQL* is a powerful, open-source relational database management system known for its reliability and scalability. It excels in handling structured data and is a top choice for many organizations.
2. **Parquet**: *Parquet* is an open-source columnar storage file format that excels in storing and processing large datasets efficiently. It is particularly well-suited for analytical workloads and is a popular choice for data warehousing and data lakes.
3. **DuckDB**: *DuckDB* is another open-source project that focuses on analytical query processing. It is designed for high-performance analytical workloads, making it an ideal candidate for accelerating complex queries.
4. **DuckDB FDW:** Foreign data wrapper extension to connect *PostgreSQL* to *DuckDB* databases.

The integration of *DuckDB* into *PostgreSQL* allows you to load Parquet files as foreign tables. This brings the power of both *DuckDB’s* query processing capabilities and *Parquet’s* efficient storage format to *PostgreSQL*.

In the fantastic article by [Paul Ramsey](https://www.crunchydata.com/blog/parquet-and-postgres-in-the-data-lake), we can learn about other similar integration, but in this case, using the [parquet-fdw](https://github.com/adjust/parquet_fdw/) plugin to load *Parquet* into the database.

In this article, we will utilize the *DuckDB FDW* to load data via the *DuckDB* engine and harness the excellent data access performance that this in-process SQL OLAP database offers.

## The Integration Process

To test the integration, we need a set of input data. We will use data with a substantial number of records to evaluate performance. For our testing, we will utilize a subset of the renowned ‘NYC Taxi Data’ dataset, consisting of three files named “taxi\_2019\_XX.parquet,” which are available for download from the following.

Let’s proceed with the process!

### Step 1: Build & install DuckDB FDW into PostgreSQL

We begin by installing *DuckDB* on our system and the *PostgreSQL* extension. Detailed installation instructions are available on the related [repo](https://github.com/alitrack/duckdb_fdw#installation).

### Step 2: Configure PostgreSQL

In this step, we configure *PostgreSQL* to enable the loading of *Parquet* data as foreign tables. We create a server for *DuckDB*, specifying connection details to our *DuckDB* instance.

```c
CREATE EXTENSION duckdb_fdw;
CREATE SERVER duckdb_svr \
     FOREIGN DATA WRAPPER duckdb_fdw OPTIONS (database ':memory:');
```

The special value *:memory:* is used to create an in-memory database where no data is persisted to disk (i.e., all data is lost when you exit the process). This setting is right for our use case, we only want to read *Parquet* files.

### Step 3: Create a Foreign Table

With the configuration in place, we create a foreign table in *PostgreSQL* that represents the *Parquet* dataset. This foreign table establishes a seamless connection to *DuckDB*, providing direct access to the data within the *Parquet* files.

```c
CREATE FOREIGN TABLE public.taxi_table (
    vendor_id             text,
    pickup_at             timestamp,
    dropoff_at            timestamp,
    passenger_count       int,
    trip_distance         double precision,
    rate_code_id          text,
    store_and_fwd_flag    text,
    pickup_location_id    int,
    dropoff_location_id   int,
    payment_type          text,
    fare_amount           double precision,
    extra                 double precision,
    mta_tax               double precision,
    tip_amount            double precision,
    tolls_amount          double precision,
    improvement_surcharge double precision,
    total_amount          double precision,
    congestion_surcharge  double precision
)
SERVER duckdb_svr
OPTIONS (
    table 'read_parquet("/home/xyz/Downloads/taxi-data/*.parquet")'
);
```

### Step 4: Query the Data

Now that we have set up the foreign table, we can run SQL queries against it, benefiting from *DuckDB’s* outstanding analytical query processing performance.

```c
SELECT count(*) FROM public.taxi_table;
```

Wow! 21 million records in less than 400 MB of Parquet file size. Impressive data compression.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*723zwaV0WhYuA2Q7XOG-aQ.png)

SELECT count(\*) FROM public.taxi\_table;

We’re going to check the SQL execution plan to see what *PostgreSQL* is doing:

![](https://miro.medium.com/v2/resize:fit:1202/format:webp/1*_u7GCuqsts-rOKYQm6wVUg.png)

SELECT count(\*) FROM public.taxi\_table;

Great, *PostgreSQL* completely delegates the execution to the extension, and therefore to *DuckDB*. Response time is fantastic, well done *DuckDB*!

Let’s see what’s in the tables:

![](https://miro.medium.com/v2/resize:fit:1296/format:webp/1*XNMnJJlV17FLiedlsQgxxA.png)

SELECT \* FROM public.taxi\_table LIMIT 1000;

Let’s try something more complex…

```c
SELECT 
    vendor_id, passenger_count, count(*) 
FROM 
    public.taxi_table 
GROUP BY 
    vendor_id, passenger_count 
ORDER BY 
    vendor_id, passenger_count
;
```
![](https://miro.medium.com/v2/resize:fit:1354/format:webp/1*j-_uHZk52Un1i5FsCgzGHQ.png)

```c
SELECT 
    * 
FROM 
    public.taxi_table 
WHERE 
    vendor_id = '1' 
    AND 
    pickup_at >= '2019-06-01 00:00:00' 
    AND 
    dropoff_at <= '2019-06-02 00:00:00'
;
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nuuvimf73Zzd6OZWeMpOfw.png)

Well, around 4 seconds to retrieve 90,000 records is not bad, considering that the data is not partitioned (for example, by the ‘ *vendor\_id* ’ column), I’m retrieving all fields from the table (not the best practice, you should always fetch only what you need), and the files are on my old Laptop with a 9-year-old SATA disk that has seen better days;-)

Let’s check the SQL execution plan:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*xm7cBiqpzVJGiZTObxUItA.png)

Alright, everything delegated to *DuckDB*, *PostgreSQL* just waiting for results.

Let’s try an aggregate function in the *SELECT* clause:

```c
SELECT 
    vendor_id, 
    min(passenger_count) AS min_pgc, 
    max(passenger_count) AS max_pgc, 
    count(*) 
FROM 
    public.taxi_table 
GROUP BY 
    vendor_id 
ORDER BY 
    vendor_id
;
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GVo_S8fNKyrvSZ3Bfy5XTg.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2fGXyLf404Ncx9zZRgsy9Q.png)

Everything’s in order.

### Step 5: When things are not so pretty

Let’s see what *PostgreSQL* does with this query:

```c
SELECT 
    vendor_id, 
    passenger_count, 
    count(*) AS nr, 
    avg(trip_distance) AS avg_dist, 
    array_agg(trip_distance) AS distances
FROM 
    public.taxi_table 
WHERE 
    pickup_at >= '2019-06-01 00:00:00' 
    AND 
    dropoff_at <= '2019-06-01 00:02:00'
GROUP BY
    vendor_id, passenger_count
ORDER BY
    vendor_id, passenger_count
;
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ZI-dN3-ZPbY_8M2WBHjw0g.png)

Perfect results, but let’s check the execution plan:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Dwyo8KgcQEu9UAoLlhJLIQ.png)

*PostgreSQL* has broken down the query into two stages. The first one sent to *DuckDB* applies only the *WHERE* clause without grouping, and the second stage is executed with the *PostgreSQL* engine, where grouping is applied to the first subset of records obtained:

- First stage in the SQL execution plan (For *DuckDB*):
```c
-> Foreign Scan:
   SELECT 
       "vendor_id", 
       "passenger_count", 
       "trip_distance" 
   FROM 
       read_parquet("/data/taxi-data/*.parquet") 
   WHERE
       "pickup_at" >= '2019-06-01 00:00:00'
       AND
       "dropoff_at" <= '2019-06-01 00:02:00' 
   ORDER BY 
       "vendor_id" ASC NULLS LAST, "passenger_count" ASC NULLS LAST
```
- Second stage (For *PostgreSQL*):
```c
-> GroupAggregate:
   Output: 
      vendor_id, 
      passenger_count, 
      count(*), 
      avg(trip_distance), 
      array_agg(trip_distance)
   Group Key: 
      taxi_table.vendor_id, taxi_table.passenger_count
```

It doesn’t seem too serious, but consider a scenario where we have a query that, when grouped, returns very few records, but without grouping (what *DuckDB* is returning for *PostgreSQL* to perform the final grouping), there are thousands and thousands of records. We are wasting resources, sending many data between stages, and degrading response time; not leveraging the columnar data structure of *Parquet* and performance of *DuckDB*, right?

Let’s take a look at the source code of the plugin to see what’s happening. The extension only supports a subset of [functions](https://github.com/alitrack/duckdb_fdw/blob/main/deparse.c#L836) in the *SELECT* clause, and *“array\_agg”* is not among them (only *“sum”, “min”, “max”, “avg”* and *“count”* are managed). So, *PostgreSQL* can’t delegate the grouping to *DuckDB* because the plugin doesn’t support that function. It makes sense what’s happening.

But why not change this? Adding that function alongside the plugin would be a significant improvement in many scenarios, wouldn’t it? Let’s go for it.

I have implemented the code (available in this [pull request](https://github.com/alitrack/duckdb_fdw/pull/21)) mostly to add support to manage list types in the plugin. Functions like “array\_agg” return arrays of values. Let’s see what happens with the query again:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yphnVq8QQ2NfOhN5UorKog.png)

Great, *PostgreSQL* now recognizes that the *“array\_agg”* function can also be processed in the extension, so it delegates all the work to the remote server and thus to *DuckDB*. Everything is executed in a single step, and the crucial part is that grouping is applied during the reading from the *Parquet* data source.

Yes, I know, this query doesn’t get the performance almost improved, but in this case, the amount of data I’m retrieving is minimal. I simply used it as an example for educational purposes. I’m sure you’ll find a use case that can benefit from it and show the improvement:-)

It’s been a fun journey for me, and I hope it has been interesting for you as well. If the code is deemed valuable, I hope it will be merged into the repository.

## Conclusion

In conclusion, by integrating *DuckDB FDW* in *PostgreSQL* to load *Parquet* files as foreign tables, we unlock a powerful solution for data analytics. This combination of *PostgreSQL’s* reliability, Parquet’s storage efficiency, and *DuckDB’s* query processing speed elevates data management and analysis to a new level. It’s an ideal choice for organizations looking to enhance their data analytics while maintaining their existing *PostgreSQL* infrastructure.

## Thanks to

- Thanks to people and organizations who develop amazing open source stuff; [PostgresSQL](https://www.postgresql.org/), [DuckDB](https://duckdb.org/), [Parquet](https://parquet.apache.org/) are indeed essential components in the world of data tooling, and they’ve made a significant impact on data management and analysis.
- Thanks to the team in [duckdb\_fdw](https://github.com/alitrack/duckdb_fdw) for developing this great piece of software, this integration is very useful!

Open source communities thrive on recognition and support from users like you!

[![ah](https://miro.medium.com/v2/resize:fill:96:96/0*WFenTrK43JIkmiyg)](https://medium.com/@ahuarte?source=post_page---post_author_info--1d667ae67dc2---------------------------------------)

[![ah](https://miro.medium.com/v2/resize:fill:128:128/0*WFenTrK43JIkmiyg)](https://medium.com/@ahuarte?source=post_page---post_author_info--1d667ae67dc2---------------------------------------)

[13 following](https://medium.com/@ahuarte/following?source=post_page---post_author_info--1d667ae67dc2---------------------------------------)

## Responses (4)

S Parodi

What are your thoughts?  

```c
Thanks, none update about parquet_fdw.
```

```c
Have tried the above example and got duckdb_fdw installed thanks to rpm by Pigsy :https://repo.pigsty.io/yum/pgsql/el8.x86_64/duckdb_fdw_16-1.1.2-1PIGSTY.el8.x86_64.rpmhttps://repo.pigsty.cc/yum/pgsql/el8.x86_64/libduckdb-1.1.2-1PIGSTY.el8.x86_64.rpm…more
```

```c
really interesting. but: i am jus a usere and not familliar with make-processes and alike. serching for duckdb_fdw and mac os didn\`t return feasable results and the repo-page https://github.com/alitrack/duckdb_fdw#installation was far too tough for me. are there any ready-to use solutions (for postgreSQL 17) thx
```