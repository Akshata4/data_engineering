# Data Engineering
This repos will have codes from different data engineering tools

## Data modeling and Data warehousing
#### List of topics
1. Data lake vs data warehouse vs data mart
2. DW Layering
3. Fact and dimension tables
4. Types of fact tables
5. Types of dimension table
6. Star and snowflake schema
7. Slow changing dimension and its type

### Data lake vs data warehouse vs data mart

A data lake is a central repository that stores raw, unprocessed, and unstructured data in its native format. This can include structured data (tables), semi-structured data (logs, JSON), and unstructured data (images, audio, video, documents)

Use case: Storing IoT sensor data, social media feeds, logs, images, and videos.

A data warehouse is a centralized repository that stores processed, cleaned, and structured data, typically from multiple sources, to support business intelligence and analytics.
Optimized for fast SQL queries and reporting.
Complex to set up and maintain, but provides a single source of truth for the organization.

Use case : Historical trend analysis and cross-departmental data integration.

A data mart is a subset of a data warehouse, focused on a specific business line, department, or function (such as sales, finance, or marketing)
Contains summarized and filtered data relevant to a specific team or business unit.

Use case : Department-specific analytics and dashboards.

#### Summary
| Feature            | Data Lake                                  | Data Warehouse                                   | Data Mart                                           |
|--------------------|---------------------------------------------|--------------------------------------------------|-----------------------------------------------------|
| **Data Type**       | Raw, unstructured, any format              | Structured, cleaned, processed                  | Structured, summarized, subject-specific           |
| **Scope**           | Organization-wide, all data               | Organization-wide, integrated                   | Departmental or project-specific                   |
| **Size**            | Very large (petabytes+)                   | Large (100s of GB to petabytes)                 | Small (up to 100 GB)                               |
| **Users**           | Data scientists, engineers                | Analysts, business users, executives            | Departmental analysts, managers                    |
| **Setup Complexity**| Low (store first, process later)          | High (requires ETL, modeling)                   | Low to moderate                                    |
| **Query Performance**| Slower for analytics                     | Fast for analytics                              | Fastest for targeted queries                       |
| **Cost**            | Low for storage, high for compute         | Higher overall                                  | Lower (due to smaller size and focus)              |
| **Typical Use Case**| Machine learning, big data                | BI, reporting, cross-org analytics              | Departmental reporting, quick insights             |

### Data Pipeline Layers

| Layer Name              | Main Function                             | Example Activities/Tools                            |
|-------------------------|--------------------------------------------|-----------------------------------------------------|
| **Source Layer**         | Collect raw data from diverse sources      | Data extraction tools (Fivetran, APIs)              |
| **Staging Layer**        | Temporary storage and light transformation | Data cleansing, validation                          |
| **Integration Layer**    | Data transformation and business logic     | ETL/ELT processes, deduplication                    |
| **Storage/Warehouse Layer** | Store structured, historical data         | Fact/dimension tables, schemas                      |
| **Metadata Layer**       | Manage data definitions and lineage        | Data dictionaries, schema registries                |
| **Access/Presentation**  | User access for analytics and reporting    | BI tools, dashboards, SQL queries                   |

Staging layer can be of 2 types - persistent and non-persistent

### Facts and Dimensions

Fact tables store numbers or measurements about business activities-things you want to count or add up, like sales amount, number of products sold, or total revenue. Each row in a fact table is an event or transaction (like a sale or an order), and it usually includes references (foreign keys) to related details

Dimension tables store descriptive information that gives context to those numbers, such as customer names, product details, dates, or store locations. These tables help you answer questions like "Who bought the product?", "What product was sold?", or "When did the sale happen?"

Fact tables = numbers and results.
Dimension tables = details and descriptions that explain those numbers

