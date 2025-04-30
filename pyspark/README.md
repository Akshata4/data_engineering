# PySpark & Spark Architecture Quick Reference

This guide provides a concise overview of Spark’s architecture, lazy evaluation, DataFrame API, and essential PySpark operations for data engineering and analytics.

---

## Table of Contents

1. [Spark Architecture](#spark-architecture)
2. [Lazy Evaluation](#lazy-evaluation)
3. [Actions vs Transformations](#actions-vs-transformations)
4. [PySpark DataFrame API](#pyspark-dataframe-api)
    - [DataFrame Creation](#dataframe-creation)
    - [Reading Files](#reading-files)
    - [Inspecting DataFrames](#inspecting-dataframes)
    - [Common DataFrame Operations](#common-dataframe-operations)
    - [Writing Data](#writing-data)
    - [Optimizations](#optimizations)
    - [Schema Management](#schema-management)
    - [Performance Tips](#performance-tips)
5. [Reading Data from URLs](#reading-data-from-urls)
6. [Useful Examples](#useful-examples)

---

## Spark Architecture

- **Driver:** Central coordinator that runs your application, creates the SparkContext, and schedules tasks.
- **Executors:** Worker processes on cluster nodes that execute tasks and store data.
- **Cluster Manager:** Allocates resources and manages nodes. Examples: Standalone, YARN, Kubernetes.
- **RDDs (Resilient Distributed Datasets):** Immutable, distributed collections with fault tolerance.
- **DataFrames:** Higher-level, table-like abstraction for structured data, supporting SQL-like operations.

**Workflow Example:**
1. Driver submits job to cluster manager.
2. Cluster manager allocates executors.
3. Executors process data in parallel (using RDDs/DataFrames).
4. Results are combined and returned to the driver.

---

## Lazy Evaluation

- **Transformations** (e.g., `filter`, `map`) are **lazy**: Spark builds a logical plan but doesn’t execute until an **action** is called.
- **Actions** (e.g., `collect`, `count`, `show`) trigger execution of the plan.
- **Benefits:** Optimizes execution, avoids unnecessary computations, and enables fault tolerance.

**Example:**
`df = spark.read.csv("data.csv")
filtered = df.filter(df["age"] > 30) # Lazy
filtered.show() # Action triggers execution  `


---

## Actions vs Transformations

| Aspect           | Transformations                  | Actions                      |
|------------------|----------------------------------|------------------------------|
| Purpose          | Build new RDDs/DataFrames        | Return results or write data |
| Execution        | Lazy (not immediate)             | Eager (triggers execution)   |
| Return Type      | New RDD/DataFrame                | Non-RDD value or file output |
| Examples         | `map`, `filter`, `select`, `join`| `collect`, `count`, `show`   |

---

## PySpark DataFrame API

### DataFrame Creation

`from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.appName("DataFrameDemo").getOrCreate()`

`From list of tuples
data = [("Alice", 25), ("Bob", 30)]
df = spark.createDataFrame(data, ["name", "age"])

From Row objects
rows = [Row(name="Cathy", age=28)]
df_row = spark.createDataFrame(rows)`



## df.collect()

### How It Works
#### Action Trigger:
Executes the entire logical plan (DAG) built by previous transformations (e.g., filter, select) and fetches results from all executors.

#### Data Transfer:
Moves the entire dataset from worker nodes to the driver's memory.

#### Output:
Returns a Python list where each element is a pyspark.sql.Row object representing a DataFrame row.

#### Note:
Suitable for datasets that fit in the driver's memory. For large datasets, use take(n), show(), or write results to storage
Alternatives to Avoid OOM
take(n): Retrieve first n rows.

show(n): Display n rows without full data transfer.

Write to Disk: Use df.write.csv() or similar methods for large results.

## df.take()n vs df.show()
### Key Comparison

| Feature              | `take(n)`                     | `show(n)`                     |
|----------------------|-------------------------------|-------------------------------|
| **Return Type**      | `list[Row]`                   | `None` (prints output)        |
| **Data Size**        | Brings `n` rows to driver     | Streams rows (avoids full     |
|                      | memory                        | transfer to driver)           |
| **Formatting**       | Raw `Row` objects             | Pretty-printed table          |
| **Common Uses**      | Programmatic access to data   | Quick data inspection         |
