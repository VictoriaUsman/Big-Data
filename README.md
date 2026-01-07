# Data Engineering Pipeline (Azure Lakehouse Architecture)






<img width="2224" height="1302" alt="AA258CC9-CB6C-45CA-A91F-4F09F7F33FE0" src="https://github.com/user-attachments/assets/27fb0663-ac03-4de8-857b-379583acb71a" />













## 📌 Project Overview

This project implements an **end-to-end data engineering pipeline** on **Microsoft Azure**, following a **modern lakehouse architecture**. The pipeline ingests data from multiple sources, stores it in a data lake, performs scalable transformations, and serves analytics-ready data for visualization tools.

The design focuses on:

* Scalability
* Separation of raw and transformed data
* Reproducible and maintainable data workflows
* Analytics and BI readiness

---

## 🏗️ Architecture Overview

**High-level flow:**

**Data Sources → Azure Data Factory → ADLS Gen2 (Raw) → Azure Databricks → ADLS Gen2 (Transformed) → Azure Synapse → BI Visualization**

### Architecture Diagram

*(Refer to the diagram included in this repository)*

---

## 🔗 Data Sources

The pipeline ingests data from multiple source systems:

* **HTTP APIs** (via GitHub or external endpoints)
* **Relational Databases** (SQL Tables)

These sources can include transactional data, reference data, or external datasets.

---

## 🚚 Data Ingestion – Azure Data Factory (ADF)

**Azure Data Factory** is used as the orchestration and ingestion layer.

### Responsibilities:

* Connect to HTTP and SQL data sources
* Schedule and automate ingestion pipelines
* Perform basic validation and metadata handling
* Load data into the Raw Data Zone

### Output:

* Data is landed **as-is** into **Azure Data Lake Storage Gen2 (Raw Zone)**

---

## 🗄️ Data Storage – Azure Data Lake Storage Gen2 (ADLS)

The data lake is logically divided into zones:

### 1️⃣ Raw Zone

* Stores unprocessed, source-aligned data
* Preserves original schema and format
* Acts as a system of record

### 2️⃣ Transformed Zone

* Stores cleaned, enriched, and curated datasets
* Optimized for analytics and reporting
* Typically stored in **Parquet / Delta format**

---

## 🔄 Data Transformation – Azure Databricks

**Azure Databricks** is used for large-scale data processing and transformation.

### Transformation Tasks:

* Data cleaning and normalization
* Schema enforcement
* Deduplication and validation
* Business logic transformations
* Enrichment using external datasets

### Enrichment Source:

* **NoSQL Database** (used as a lookup/enrichment table)

### Output:

* Transformed and analytics-ready datasets written back to **ADLS Gen2 (Transformed Zone)**

---

## 🧠 Analytics Layer – Azure Synapse Analytics

**Azure Synapse Analytics** serves as the analytical query layer.

### Responsibilities:

* Query transformed datasets from ADLS
* Create analytical views or tables
* Enable fast SQL-based analytics
* Act as the serving layer for BI tools

---

## 📊 Visualization & Reporting

The final datasets are consumed by BI and analytics tools such as:

* **Power BI**
* **Tableau**
* **Microsoft Fabric**

These tools connect to **Azure Synapse** to enable:

* Interactive dashboards
* Business reports
* Data exploration

---

## 🔐 Security & Governance (Recommended)

Although not explicitly shown in the diagram, best practices include:

* Azure Managed Identities
* Role-Based Access Control (RBAC)
* Data Lake folder-level permissions
* Secrets stored in **Azure Key Vault**
* Monitoring with Azure Monitor & Log Analytics

---

## ⚙️ Technology Stack

| Layer         | Technology                   |
| ------------- | ---------------------------- |
| Ingestion     | Azure Data Factory           |
| Storage       | Azure Data Lake Storage Gen2 |
| Processing    | Azure Databricks             |
| Analytics     | Azure Synapse Analytics      |
| Visualization | Power BI / Tableau / Fabric  |
| Enrichment    | NoSQL Database               |

---

## 🚀 Key Benefits of This Architecture

* Scalable and cloud-native
* Clear separation of concerns (Raw vs Transformed)
* Supports batch and analytical workloads
* BI-ready data model
* Easily extensible for streaming or ML workloads

---

## 📈 Future Enhancements

* Add CI/CD for ADF and Databricks pipelines
* Introduce Delta Lake optimization
* Implement data quality checks
* Enable real-time ingestion using Event Hubs or Kafka
* Add data cataloging with Microsoft Purview

---

## 👤 Author

**Ian C.**
Data Engineering Project – Azure Lakehouse

---

## 📄 License

This project is for educational and portfolio purposes.
