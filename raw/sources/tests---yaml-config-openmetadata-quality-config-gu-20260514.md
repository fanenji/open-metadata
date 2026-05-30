---
type: clip
title: "Tests - YAML Config | OpenMetadata Quality Config Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/tests-yaml"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Tests - YAML Config | OpenMetadata Quality Config Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/tests-yaml

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData QualityTests - YAML Config | OpenMetadata Quality Config GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityOverviewConfigure Data QualityTests - YAML ConfigColumn Tests - YAML ConfigTests - UI ConfigDimensional ValidationData Quality as CodeCustom TestsTest LibraryData ProfilerAlerts & NotificationsIncident ManagerOn this pageTests in the YAML ConfigTable TestsTable Row Count to EqualTable Row Count to be BetweenTable Column Count to EqualTable Column Count to be BetweenTable Column Name to ExistTable Column to Match SetTable Custom SQL TestTable Row Inserted Count To Be BetweenCompare 2 Tables for DifferencesTable Data to Be Fresh [OpenMetadata]Next StepsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Tests in the YAML Config

Here you can see all the supported tests definitions and how to configure them in the YAML config file.

A Test Definition is a generic definition of a test. This Test Definition then gets specified in a Test Case. This Test Case is where the parameter(s) of a Test Definition are specified.

In this section, you will learn what tests we currently support and how to configure them in the YAML/JSON config file.

Table Tests

Column Tests

​Table Tests

Tests applied on top of a Table. Here is the list of all table tests:

Table Row Count to Equal

Table Row Count to be Between

Table Column Count to Equal

Table Column Count to be Between

Table Column Name to Exist

Table Column to Match Set

Table Custom SQL Test

Table Row Inserted Count To Be Between

Compare 2 Tables for Differences

Table Data to Be Fresh [OpenMetadata]

​Table Row Count to Equal

Validate the total row count in the table is equal to the given value.

Dimension:

Integrity

Properties:

value: Expected number of rows.

Behavior

ConditionStatusvalue match the number of rows in the tableSuccess ✅value does not match the number of rows in the tableFailed ❌

YAML Config

- name: myTestName

description: test description

testDefinitionName: tableRowCountToEqual

parameterValues:

- name: value

value: 2

JSON Config

{

"name": "myTestName",

"description": "test description",

"testDefinitionName": "tableRowCountToEqual",

"parameterValues": [

{

"name": "value",

"value": 2

}

]

}

​Table Row Count to be Between

Validate the total row count is within a given range of values.

Dimension:

Integrity

Properties:

minValue: Lower bound of the interval. If informed, the number of rows should be bigger than this number.

maxValue: Upper bound of the interval. If informed, the number of rows should be lower than this number.

Any of those two need to be informed.

Behavior

ConditionStatusThe number of rows in the table is between minValue and maxValueSuccess ✅The number of rows in the table is not between minValue and maxValueFailed ❌

YAML Config

- name: myTestName

description: test description

testDefinitionName: tableRowCountToBeBetween

parameterValues:

- name: minValue

value: 10

- name: maxValue

value: 10

JSON Config

{

"name": "myTestName",

"description": "test description",

"testDefinitionName": "tableRowCountToBeBetween",

"parameterValues": [

{

"name": "minValue",

"value": 10

},

{

"name": "maxValue",

"value": 10

}

]

}

​Table Column Count to Equal

Validate that the number of columns in a table is equal to a given value.

Dimension:

Integrity

Properties

columnCount: Expected number of columns.

Behavior

ConditionStatuscolumnCount matches the number of column in the tableSuccess ✅columnCount does not matches the number of column in the tableFailed ❌

YAML Config

- name: myTestName

description: test description

testDefinitionName: tableColumnCountToEqual

parameterValues:

- name: columnCount

value: 5

JSON Config

{

"name": "myTestName",

"description": "test description",

"testDefinitionName": "tableColumnCountToEqual",

"parameterValues": [

{

"name": "columnCount",

"value": 5

}

]

}

​Table Column Count to be Between

Validate the number of columns in a table is between the given value

Dimension:

Integrity

Properties

minColValue: lower bound

maxColValue: upper bound

Behavior

ConditionStatusThe number of columns in the table is between minColValue and maxColValueSuccess ✅The number of columns in the table is not between minColValue and maxColValueFailed ❌

YAML Config

- name: myTestName

description: test description

testDefinitionName: tableColumnCountToBeBetween

parameterValues:

- name: minColValue

value: 5

- name: maxColValue

value: 10

JSON Config

{

"name": "myTestName",

"description": "test description",

"testDefinitionName": "tableColumnCountToBeBetween",

"parameterValues": [

{

"name": "minColValue",

"value": 5

},

{

"name": "maxColValue",

"value": 10

}

]

}

​Table Column Name to Exist

Validate a column name is present in the table

Dimension:

Integrity

Properties

columnName: the name of the column to check for

Behavior

ConditionStatuscolumnName exists in the set of column name for the tableSuccess ✅columnName does not exists in the set of column name for the tableFailed ❌

YAML Config

- name: myTestName

description: test description

testDefinitionName: tableColumnNameToExist

parameterValues:

- name: columnName

value: order_id

JSON Config

{

"myTestName": "myTestName",

"testDefinitionName": "tableColumnNameToExist",

"parameterValues": [

{

"name": "columnName",

"value": "order_id"

}

]

}

​Table Column to Match Set

Validate a list of table column name matches an expected set of columns

Dimension:

Integrity

Properties

columnNames: comma separated string of column name

ordered: whether the test should check for column ordering. Default to False

Behavior

ConditionStatus[ordered=False] columnNames matches the list of column names in the table regardless of the orderSuccess ✅[ordered=True] columnNames matches the list of column names in the table in the corresponding order (e.g. ["a","b"] == ["a","b"]Success ✅[ordered=FALSE] columnNames does no match the list of column names in the table regardless of the orderFailed ❌[ordered=True] columnNames does no match the list of column names in the table and/or the corresponding order (e.g. ["a","b"] != ["b","a"]Failed ❌

YAML Config

- name: myTestName

description: test description

testDefinitionName: tableColumnToMatchSet

parameterValues:

- name: columnNames

value: "col1, col2, col3"

- name: ordered

value: true

JSON Config

{

"myTestName": "myTestName",

"testDefinitionName": "tableColumnToMatchSet",

"parameterValues": [

{

"name": "columnNames",

"value": "col1, col2, col3"

},

{

"name": "ordered",

"value": true

}

]

}

​Table Custom SQL Test

Write you own SQL test. When writting your query you can use 2 strategies:

ROWS (default): expects the query to be written as SELECT <field>, <field> FROM <foo> WHERE <condition>. Note if your query returns a large amount of rows it might cause an “Out Of Memeory” error. In this case we recomend you to use the COUNT strategy.

COUNT: expects the query to be written as SELECT COUNT(<field>) FROM <foo> WHERE <condition>.

How to use the Threshold Parameter?

The threshold allows you to define a limit for which you test should pass or fail - by defaut this number is 0. For example if my custom SQL query test returns 10 rows (or a COUNT value of 10) and my threshold is 5 the test will fail. If I update my threshold to 11 on my next run my test will pass.

When configuring a Table Custom SQL Test, specify the table using the format database.schema.table.

Using only the table name may not work, as it depends on the SQL engine’s requirements.

Properties

sqlExpression: SQL expression

strategy: one of ROWS or COUNT

threshold: an integer defining the threshold above which the test should fail (default to 0 if not specified)

Behavior

ConditionStatussqlExpression returns row <= threshold (default to 0)Success ✅sqlExpression returns row > threshold (default to 0)Failed ❌

Example

SELECT

customer_id

FROM DUAL

WHERE lifetime_value < 0;

SELECT

customer_id

FROM DUAL d

INNER JOIN OTHER o ON d.id = o.id

WHERE lifetime_value < 0;

YAML Config

- name: myTestName

description: test description

testDefinitionName: tableCustomSQLQuery

parameterValues:

- name: sqlExpression

value: >

SELECT

customer_tier

FROM DUAL

WHERE customer_tier = 'GOLD' and lifetime_value < 10000;

JSON Config

{

"name": "myTestName",

"description": "test description",

"testDefinitionName": "tableCustomSQLQuery",

"parameterValues": [

{

"name": "sqlExpression",

"value": "SELECT  customer_tier FROM DUAL  WHERE customer_tier = 'GOLD' and lifetime_value < 10000;"

}

]

}

​Table Row Inserted Count To Be Between

Validate the number of rows inserted for the defined period is between the expected range

The Table Row Inserted Count To Be Between cannot be executed against tables that have configured a partition in OpenMetadata. The logic of the test performed will be similar to executing a Table Row Count to be Between test against a table with a partition configured.

Dimension:

Integrity

Properties

Min Row Count: Lower bound

Max Row Count: Upper bound

Column Name: The name of the column used to apply the range filter

Range Type: One of HOUR, DAY, MONTH, YEAR

Interval: The range interval (e.g. 1,2,3,4,5, etc)

Behavior

ConditionStatusNumber of rows is between Min Row Count and Max Row CountSuccess ✅Number of rows is not between Min Row Count and `Max Row CountFailed ❌

YAML Config

- name: myTestName

description: test description

testDefinitionName: tableRowInsertedCountToBeBetween

parameterValues:

- name: min

value: 10

- name: max

value: 100

- name: columnName

value: colA

- name: rangeType

value: DAY

- name: rangeInterval

value: 1

JSON Config

{

"name": "myTestName",

"description": "test description",

"testDefinitionName": "tableRowInsertedCountToBeBetween",

"parameterValues": [

{

"name": "min",

"value": 10

},

{

"name": "max",

"value": 100

},

{

"name": "columnName",

"value": "colA"

},

{

"name": "rangeType",

"value": "DAY"

},

{

"name": "rangeInterval",

"value": 1

}

]

}

​Compare 2 Tables for Differences

Compare 2 tables for differences. Allows a user to check for integrity.

Supports comparing tables across different services.

For example, you can compare a table in Snowflake with a table in Redshift.

Supported connectors:

Snowflake

BigQuery

Athena

Redshift

Postgres

MySQL

MSSQL

Oracle

Trino

SAP Hana

Dimension:

Consistency

Properties

keyColumns: The key column to use as the key for the comparison. Resolves to the primary key (if defined) if not set

useColumns: The columns against which the comparison will done. If not provided it will use all the columns

table2: The table against which the comparison will be done. Must be the fully qualified name as defined in OpenMetadata

threshold: The threshold of different rows above which the test should fail — default to 0

where: Any where clause to pass

caseSensitiveColumns: Whether the column comparison should be case sensitive or not. Default to false.

Behavior

ConditionStatusNumber of rows is greater than the threshold (default to 0)Failed ❌Number of rows is less than or equal to the thresholdSuccess ✅

YAML Config

name: myName

entityLink: '<#E::table::postgres_rds.TESTDB.snowflake_db_test.dim_data_columns>'

testDefinition: tableDiff

testSuite: postgres_rds.TESTDB.snowflake_db_test.dim_data_columns.testSuite

parameterValues:

- name: keyColumns

value: '["id"]'

- name: useColumns

value: '["name_column_name"]'

- name: table2

value: redshift_dbt.dev.dbt_jaffle.boolean_test

- name: threshold

value: 10

- name: where

value: id != 999

- name: caseSensitiveColumns

value: false

JSON Config

{

"name": "myName",

"entityLink": "<#E::table::postgres_rds.TESTDB.snowflake_db_test.dim_data_columns>",

"testDefinition": "tableDiff",

"testSuite": "postgres_rds.TESTDB.snowflake_db_test.dim_data_columns.testSuite",

"parameterValues": [

{

"name": "keyColumns",

"value": "[\"id\"]"

},

{

"name": "useColumns",

"value": "[\"name_column_name\"]"

},

{

"name": "table2",

"value": "redshift_dbt.dev.dbt_jaffle.boolean_test"

},

{

"name": "threshold",

"value": 10

},

{

"name": "where",

"value": "id != 999"

},

{

"name": "caseSensitiveColumns",

"value": false

}

]

}

​Table Data to Be Fresh [OpenMetadata]

Validate the freshness of a table’s data.

Dimension:

Accuracy

Properties

column: the colummn that will be used to chech the table freshness

timeSinceUpdate: (in seconds) The data is expected to be updated within this number of seconds. If the time since the last update is greater than this value, the test will fail.

Behavior

ConditionStatusTime since update is greater than timeSinceUpdateFailed ❌Time since update is less than or equal to timeSinceUpdateSuccess ✅

YAML Config

name: myName

entityLink: '<#E::table::postgres_rds.TESTDB.snowflake_db_test.dim_data_columns>'

testDefinition: tableDataToBeFresh

testSuite: postgres_rds.TESTDB.snowflake_db_test.dim_data_columns.testSuite

parameterValues:

- name: column

value: id

- name: timeSinceUpdate

value: 30

JSON Config

{

"name": "myName",

"displayName": "dim_data_columns_table_data_to_be_fresh_NeUs",

"entityLink": "<#E::table::postgres_rds.TESTDB.snowflake_db_test.dim_data_columns>",

"testDefinition": "tableDataToBeFresh",

"testSuite": "postgres_rds.TESTDB.snowflake_db_test.dim_data_columns.testSuite",

"parameterValues": [

{

"name": "column",

"value": "id"

},

{

"name": "timeSinceUpdate",

"value": 30

}

]

}

​Next Steps

Column Tests - YAML ConfigConfigure column-level data quality tests including uniqueness, null checks, regex patterns, value sets, and statistical validations.Was this page helpful?YesNoSuggest editsRaise issueConfigure Data Quality | Official DocumentationPreviousColumn Tests - YAML Config | OpenMetadata Quality Config GuideNext⌘I
