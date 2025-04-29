## df.collect()

### How It Works
#### Action Trigger:
Executes the entire logical plan (DAG) built by previous transformations (e.g., filter, select) and fetches results from all executors.

#### Data Transfer:
Moves the entire dataset from worker nodes to the driver's memory.

#### Output:
Returns a Python list where each element is a pyspark.sql.Row object representing a DataFrame row.
