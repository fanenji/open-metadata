---
type: clip
title: "Column Tests - YAML Config | OpenMetadata Quality Config Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/tests-yaml-column-tests"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Column Tests - YAML Config | OpenMetadata Quality Config Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/tests-yaml-column-tests

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData QualityColumn Tests - YAML Config | OpenMetadata Quality Config GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityOverviewConfigure Data QualityTests - YAML ConfigColumn Tests - YAML ConfigTests - UI ConfigDimensional ValidationData Quality as CodeCustom TestsTest LibraryData ProfilerAlerts & NotificationsIncident ManagerOn this pageColumn TestsColumn Values to Be UniqueColumn Values to Be Not NullColumn Values to Match RegexColumn Values to not Match RegexColumn Values to Be in SetColumn Values to Be Not In SetColumn Values to Be BetweenColumn Values Missing Count to Be EqualColumn Values Lengths to Be BetweenColumn Value Max to Be BetweenColumn Value Min to Be BetweenColumn Value Mean to Be BetweenColumn Value Median to Be BetweenColumn Values Sum to Be BetweenColumn Values Standard Deviation to Be BetweenColumn Values To Be At Expected LocationDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Column Tests

Tests applied on top of Column metrics. Here is the list of all column tests:

Column Values to Be Unique

Column Values to Be Not Null

Column Values to Match Regex

Column Values to not Match Regex

Column Values to Be in Set

Column Values to Be Not In Set

Column Values to Be Between

Column Values Missing Count to Be Equal

Column Values Lengths to Be Between

Column Value Max to Be Between

Column Value Min to Be Between

Column Value Mean to Be Between

Column Value Median to Be Between

Column Values Sum to Be Between

Column Values Standard Deviation to Be Between

Column Values To Be At Expected Location

​Column Values to Be Unique

Makes sure that there are no duplicate values in a given column.

Dimension:

Uniqueness

Behavior

ConditionStatuscolumn values are uniqueSuccess ✅column values are not uniqueFailed ❌

Properties

columnValuesToBeUnique: To be set as true. This is required for proper JSON parsing in the profiler module.

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValuesToBeUnique

computePassedFailedRowCount: <true or false>

parameterValues:

- name: columnNames

value: true

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValuesToBeUnique",

"parameterValues": [

{

"name": "columnNames",

"value": true

}

]

}

​Column Values to Be Not Null

Validates that there are no null values in the column.

Dimension:

Completeness

Properties

columnValuesToBeNotNull: To be set as true. This is required for proper JSON parsing in the profiler module.

Behavior

ConditionStatusNo NULL values are present in the columnSuccess ✅1 or more NULL values are present in the columnFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValuesToBeNotNull

computePassedFailedRowCount: <true or false>

parameterValues:

- name: columnValuesToBeNotNull

value: true

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValuesToBeNotNull",

"parameterValues": [

{

"name": "columnValuesToBeNotNull",

"value": true

}

]

}

​Column Values to Match Regex

This test allows us to specify how many values in a column we expect that will match a certain regex expression. Please note that for certain databases we will fall back to SQL LIKE expression. The databases supporting regex pattern as of 0.13.2 are:

redshift

postgres

oracle

mysql

mariaDB

sqlite

clickhouse

snowflake

The other databases will fall back to the LIKE expression

Dimension:

Validity

Properties

regex: expression to match a regex pattern. E.g., [a-zA-Z0-9]{5}.

Behavior

ConditionStatusAll column values match regexSuccess ✅1 or more column values do not match regexFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValuesToMatchRegex

computePassedFailedRowCount: <true or false>

parameterValues:

- name: regex

value: "%something%"

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValuesToMatchRegex",

"parameterValues": [

{

"name": "regex",

"value": "%something%"

}

]

}

​Column Values to not Match Regex

This test allows us to specify values in a column we expect that will not match a certain regex expression. If the test find values matching the forbiddenRegex the test will fail. Please note that for certain databases we will fall back to SQL LIKE expression. The databases supporting regex pattern as of 0.13.2 are:

redshift

postgres

oracle

mysql

mariaDB

sqlite

clickhouse

snowflake

The other databases will fall back to the LIKE expression

Dimension:

Validity

Properties

regex: expression to match a regex pattern. E.g., [a-zA-Z0-9]{5}.

Behavior

ConditionStatus0 column value match regexSuccess ✅1 or more column values match regexFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValuesToMatchRegex

computePassedFailedRowCount: <true or false>

parameterValues:

- name: forbiddenRegex

value: "%something%"

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValuesToMatchRegex",

"parameterValues": [

{

"name": "forbiddenRegex",

"value": "%something%"

}

]

}

​Column Values to Be in Set

Validate values form a set are present in a column.

Dimension:

Validity

Properties

allowedValues: List of allowed strings or numbers.

Behavior

ConditionStatusmatchEnum is false and 1 or more values from allowedValues is found in the columnSuccess ✅matchEnum is true and all columns have a value from allowedValuesSuccess ✅matchEnum is false 0 value from allowedValues is found in the columnFailed ❌matchEnum is true and 1 or more columns does not have a vluae from allowedValuesFailed ❌

YAML Config

- name: myTestName

testDefinitionName: columnValuesToBeInSet

columnName: columnName

computePassedFailedRowCount: <true or false>

parameterValues:

- name: allowedValues

value: '["forbidden1", "forbidden2"]'

- name: matchEnum

value: ""  # or true

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValuesToBeInSet",

"parameterValues": [

{

"name": "allowedValues",

"value": [

"forbidden1",

"forbidden2"

]

},

{

"name": "matchEnum",

"value": ""

}

]

}

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValuesToBeInSet",

"parameterValues": [

{

"name": "allowedValues",

"value": [

"forbidden1",

"forbidden2"

]

}

]

}

​Column Values to Be Not In Set

Validate that there are no values in a column in a set of forbidden values.

Dimension:

Validity

Properties

forbiddenValues: List of forbidden strings or numbers.

Behavior

ConditionStatus0 value from forbiddenValues is found in the columnSuccess ✅1 or more values from forbiddenValues is found in the columnFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValuesToBeNotInSet

computePassedFailedRowCount: <true or false>

parameterValues:

- name: forbiddenValues

value: ["forbidden1", "forbidden2"]

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValuesToBeNotInSet",

"parameterValues": [

{

"name": "forbiddenValues",

"value": [

"forbidden1",

"forbidden2"

]

}

]

}

​Column Values to Be Between

Validate that the values of a column are within a given range.

Only supports numerical types.

Dimension:

Accuracy

Properties

minValue: Lower bound of the interval. If informed, the column values should be bigger than this number.

maxValue: Upper bound of the interval. If informed, the column values should be lower than this number.

Any of those two need to be informed.

Behavior

ConditionStatusvalue is between minValue and maxValueSuccess ✅value is greater than minValue if only minValue is specifiedSuccess ✅value is less then maxValue if only maxValue is specifiedSuccess ✅value is not between minValue and maxValueFailed ❌value is less than minValue if only minValue is specifiedFailed ❌value is greater then maxValue if only maxValue is specifiedFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValuesToBeBetween

computePassedFailedRowCount: <true or false>

parameterValues:

- name: minValue

value: ["forbidden1", "forbidden2"]

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValuesToBeBetween",

"parameterValues": [

{

"name": "minValue",

"value": [

"forbidden1",

"forbidden2"

]

}

]

}

​Column Values Missing Count to Be Equal

Validates that the number of missing values matches a given number. Missing values are the sum of nulls, plus the sum of values in a given list which we need to consider as missing data. A clear example of that would be NA or N/A.

Dimension:

Completeness

Properties

missingCountValue: The number of missing values needs to be equal to this. This field is mandatory.

missingValueMatch (Optional): A list of strings to consider as missing values.

Behavior

ConditionStatusNumber of missing value is equal to missingCountValueSuccess ✅Number of missing value is not equal to missingCountValueFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValuesMissingCountToBeEqual

parameterValues:

- name: missingValueMatch

value: ["NA", "N/A"]

- name: missingCountValue

value: 100

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValuesMissingCountToBeEqual",

"parameterValues": [

{

"name": "missingValueMatch",

"value": [

"NA",

"N/A"

]

},

{

"name": "missingCountValue",

"value": 100

}

]

}

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValuesMissingCountToBeEqual",

"parameterValues": [

{

"name": "missingValueMatch",

"value": [

"NA",

"N/A"

]

},

{

"name": "missingCountValue",

"value": 100

}

]

}

​Column Values Lengths to Be Between

Validates that the lengths of the strings in a column are within a given range.

Only supports concatenable types.

Dimension:

Accuracy

Properties

minLength: Lower bound of the interval. If informed, the string length should be bigger than this number.

maxLength: Upper bound of the interval. If informed, the string length should be lower than this number.

Any of those two need to be informed.

Behavior

ConditionStatusvalue length is between minLength and maxLengthSuccess ✅value length is greater than minLength if only minLength is specifiedSuccess ✅value length is less then maxLength if only maxLength is specifiedSuccess ✅value length is not between minLength and maxLengthFailed ❌value length is less than minLength if only minLength is specifiedFailed ❌value length is greater then maxLength if only maxLength is specifiedFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValueLengthsToBeBetween

computePassedFailedRowCount: <true or false>

parameterValues:

- name: minLength

value: 50

- name: maxLength

value: 100

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValueLengthsToBeBetween",

"parameterValues": [

{

"name": "minLength",

"value": 50

},

{

"name": "maxLength",

"value": 100

}

]

}

​Column Value Max to Be Between

Validate the maximum value of a column is between a specific range

Only supports numerical types.

Dimension:

Accuracy

Properties

minValueForMaxInCol: lower bound

maxValueForMaxInCol: upper bound

Behavior

ConditionStatuscolumn max value is between minValueForMaxInCol and maxValueForMaxInColSuccess ✅column max value is greater than minValueForMaxInCol if only minValueForMaxInCol is specifiedSuccess ✅column max value is less then maxValueForMaxInCol if only maxValueForMaxInCol is specifiedSuccess ✅column max value is not between minValueForMaxInCol and maxValueForMaxInColFailed ❌column max value is less than minValueForMaxInCol if only minValueForMaxInCol is specifiedFailed ❌column max value is greater then maxValueForMaxInCol if only maxValueForMaxInCol is specifiedFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValueMaxToBeBetween

parameterValues:

- name: minValueForMaxInCol

value: 50

- name: maxValueForMaxInCol

value: 100

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValueMaxToBeBetween",

"parameterValues": [

{

"name": "minValueForMaxInCol",

"value": 50

},

{

"name": "maxValueForMaxInCol",

"value": 100

}

]

}

​Column Value Min to Be Between

Validate the minimum value of a column is between a specific range

Only supports numerical types.

Dimension:

Accuracy

Properties

minValueForMinInCol: lower bound

maxValueForMinInCol: upper bound

Behavior

ConditionStatuscolumn min value is between minValueForMinInCol and maxValueForMinInColSuccess ✅column min value is greater than minValueForMinInCol if only minValueForMinInCol is specifiedSuccess ✅column min value is less then maxValueForMinInCol if only maxValueForMinInCol is specifiedSuccess ✅column min value is not between minValueForMinInCol and maxValueForMinInColFailed ❌column min value is less than minValueForMinInCol if only minValueForMinInCol is specifiedFailed ❌column min value is greater then maxValueForMinInCol if only maxValueForMinInCol is specifiedFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValueMinToBeBetween

parameterValues:

- name: minValueForMinInCol

value: 10

- name: maxValueForMinInCol

value: 50

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValueMinToBeBetween",

"parameterValues": [

{

"name": "minValueForMinInCol",

"value": 10

},

{

"name": "maxValueForMinInCol",

"value": 50

}

]

}

​Column Value Mean to Be Between

Validate the mean of a column is between a specific range

Only supports numerical types.

Dimension:

Accuracy

Properties

minValueForMeanInCol: lower bound

maxValueForMeanInCol: upper bound

Behavior

ConditionStatuscolumn mean value is between minValueForMeanInCol and maxValueForMeanInColSuccess ✅column mean value is greater than minValueForMeanInCol if only minValueForMeanInCol is specifiedSuccess ✅column mean value is less then maxValueForMeanInCol if only maxValueForMeanInCol is specifiedSuccess ✅column mean value is not between minValueForMeanInCol and maxValueForMeanInColFailed ❌column mean value is less than minValueForMeanInCol if only minValueForMeanInCol is specifiedFailed ❌column mean value is greater then maxValueForMeanInCol if only maxValueForMeanInCol is specifiedFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValueMeanToBeBetween

parameterValues:

- name: minValueForMeanInCol

value: 5

- name: maxValueForMeanInCol

value: 10

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValueMeanToBeBetween",

"parameterValues": [

{

"name": "minValueForMeanInCol",

"value": 5

},

{

"name": "maxValueForMeanInCol",

"value": 10

}

]

}

​Column Value Median to Be Between

Validate the median of a column is between a specific range

Only supports numerical types.

Dimension:

Accuracy

Properties

minValueForMedianInCol: lower bound

maxValueForMedianInCol: upper bound

Behavior

ConditionStatuscolumn median value is between minValueForMedianInCol and maxValueForMedianInColSuccess ✅column median value is greater than minValueForMedianInCol if only minValueForMedianInCol is specifiedSuccess ✅column median value is less then maxValueForMedianInCol if only maxValueForMedianInCol is specifiedSuccess ✅column median value is not between minValueForMedianInCol and maxValueForMedianInColFailed ❌column median value is less than minValueForMedianInCol if only minValueForMedianInCol is specifiedFailed ❌column median value is greater then maxValueForMedianInCol if only maxValueForMedianInCol is specifiedFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValueMedianToBeBetween

parameterValues:

- name: minValueForMedianInCol

value: 5

- name: maxValueForMedianInCol

value: 10

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValueMedianToBeBetween",

"parameterValues": [

{

"name": "minValueForMedianInCol",

"value": 5

},

{

"name": "maxValueForMedianInCol",

"value": 10

}

]

}

​Column Values Sum to Be Between

Validate the sum of a column is between a specific range

Only supports numerical types.

Dimension:

Accuracy

Properties

minValueForColSum: lower bound

maxValueForColSum: upper bound

Behavior

ConditionStatusSum of the column values is between minValueForColSum and maxValueForColSumSuccess ✅Sum of the column values is greater than minValueForColSum if only minValueForColSum is specifiedSuccess ✅Sum of the column values is less then maxValueForColSum if only maxValueForColSum is specifiedSuccess ✅Sum of the column values is not between minValueForColSum and maxValueForColSumFailed ❌Sum of the column values is less than minValueForColSum if only minValueForColSum is specifiedFailed ❌Sum of the column values is greater then maxValueForColSum if only maxValueForColSum is specifiedFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValueMedianToBeBetween

parameterValues:

- name: minValueForMedianInCol

value: 5

- name: maxValueForMedianInCol

value: 10

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValueMedianToBeBetween",

"parameterValues": [

{

"name": "minValueForMedianInCol",

"value": 5

},

{

"name": "maxValueForMedianInCol",

"value": 10

}

]

}

​Column Values Standard Deviation to Be Between

Validate the standard deviation of a column is between a specific range

Only supports numerical types.

Dimension:

Accuracy

Properties

minValueForStdDevInCol: lower bound

minValueForStdDevInCol: upper bound

Behavior

ConditionStatuscolumn values standard deviation is between minValueForStdDevInCol and minValueForStdDevInColSuccess ✅column values standard deviation is greater than minValueForStdDevInCol if only minValueForStdDevInCol is specifiedSuccess ✅column values standard deviation is less then minValueForStdDevInCol if only minValueForStdDevInCol is specifiedSuccess ✅column values standard deviation is not between minValueForStdDevInCol and minValueForStdDevInColFailed ❌column values standard deviation is less than minValueForStdDevInCol if only minValueForStdDevInCol is specifiedFailed ❌column values standard deviation is greater then minValueForStdDevInCol if only minValueForStdDevInCol is specifiedFailed ❌

YAML Config

- name: myTestName

description: test description

columnName: columnName

testDefinitionName: columnValueStdDevToBeBetween

parameterValues:

- name: minValueForStdDevInCol

value: 5

- name: maxValueForStdDevInCol

value: 10

JSON Config

{

"name": "myTestName",

"description": "test description",

"columnName": "columnName",

"testDefinitionName": "columnValueStdDevToBeBetween",

"parameterValues": [

{

"name": "minValueForStdDevInCol",

"value": 5

},

{

"name": "maxValueForStdDevInCol",

"value": 10

}

]

}

​Column Values To Be At Expected Location

Validate the reference value for a column is a the expected geographic location

Data will be temporarely stored in memory while the test case is running to validate the location. Not data will be permanently stored.

France is the only supported location at this time. To add any additional location please reach out to the team in our slack support channel

Dimension:

Accuracy

Properties

locationReferenceType: the type of location refernce CITY or POSTAL_CODE

longitudeColumnName: longitude column name

latitudeColumnName: latitude column name

radius: radius in meter from which the location can be from the expected lat/long — acts as a buffer

Behavior

ConditionStatuscolumn values lat/long is within the polygon of the column reference (+/- radius)Success ✅column values lat/long is outside the polygon of the column reference (+/- radius)Failed ❌

YAML Config

- name: ExpectedGeoLocation

testDefinitionName: ColumnValuesToBeAtExpectedLocation

columnName: "Code Insee"

parameterValues:

- name: locationReferenceType

value: POSTAL_CODE

- name: longitudeColumnName

value: "Coordonnée Y"

- name: latitudeColumnName

value: "Coordonnée X"

- name: radius

value: "1000"

JSON Config

{

"name": "ExpectedGeoLocation",

"testDefinitionName": "ColumnValuesToBeAtExpectedLocation",

"columnName": "Code Insee",

"parameterValues": [

{

"name": "locationReferenceType",

"value": "POSTAL_CODE"

},

{

"name": "longitudeColumnName",

"value": "Coordonnée Y"

},

{

"name": "latitudeColumnName",

"value": "Coordonnée X"

},

{

"name": "radius",

"value": "1000"

}

]

}

Was this page helpful?YesNoSuggest editsRaise issueTests - YAML Config | OpenMetadata Quality Config GuidePreviousTests - UI Config | OpenMetadata Quality Config GuideNext⌘I
