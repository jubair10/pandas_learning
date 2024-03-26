# Data Analysis

Data analysis is a process of inspecting, cleansing, transforming, and modeling data with the goal of discovering useful information, informing conclusions, and supporting decision-making. It is also commonly referred to as data mining and exploratory data analysis.

## Importance of Pandas in Python

1. **Analyzing Big Data**: Pandas allows us to analyze big data and make conclusions based on statistical theories.

2. **Data Cleaning**: Pandas can clean messy data sets and make them readable and relevant.

3. **Handling Missing Data**: Pandas provides easy handling of missing data (represented as NaN) in floating-point as well as non-floating-point data.

4. **Size Mutability**: Columns can be inserted and deleted from DataFrame and higher-dimensional objects.

5. **Data Manipulation**: Pandas facilitates data set merging, joining, flexible reshaping, and pivoting of data sets. It also provides Series functionality.

## Introduction to Pandas

1. **Origin**: The name "pandas" is a combination of "panel data" and "Python data analysis." It was created by Wes McKinney in 2008.

2. **Purpose**: Pandas is a Python library designed for working with data sets.

3. **Functionality**: It offers functions and methods for analyzing, cleaning, exploring, and manipulating data.

4. **Data Formats**: Pandas can handle various data formats, including CSV, TXT, HTML, JSON, ZIP, etc.

5. **Read and Write**: It provides capabilities to read and write data structures from/to different formats.

## Three Data Structures in Pandas

### 1. Series

A Series is a one-dimensional labeled array capable of holding any data type. It can be created using `pd.Series(data)`.

### 2. DataFrames

DataFrames are two-dimensional data structures with columns, similar to tables in a relational database. They are the primary data structure used in pandas for data manipulation.

### 3. Panel

A Panel is a three-dimensional container of data. It is less commonly used compared to Series and DataFrames and is mainly used for working with three-dimensional data sets.

Pandas offers a comprehensive set of tools for data analysis and manipulation in Python, making it a powerful library for various data-related tasks.



### Difference between DataFrame and Series

#### DataFrame

|   | Name  | Age | City       |
|---|-------|-----|------------|
| 0 | John  | 30  | New York   |
| 1 | Alice | 25  | Los Angeles|
| 2 | Bob   | 35  | Chicago    |

#### Series

- **Name**: [John, Alice, Bob]
- **Age**: [30, 25, 35]
- **City**: [New York, Los Angeles, Chicago]
