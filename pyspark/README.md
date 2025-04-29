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
