## Data-Analyst-Emmanuel
## 📌PROJECT TITLE
Design and Implementation of a Data Analytic Platform (DAP) on AWS for the City of Vancouver

## 📝Project Description
This project showcases the end-to-end development of a Data Analytic Platform (DAP) hosted on Amazon Web Services (AWS) to support the City of Vancouver’s transition to a cloud-based analytics infrastructure. The dataset analyzed includes employee remuneration and expenses for individuals earning over $75,000 annually. The platform enables descriptive analysis of salary trends and expenditures, particularly within the engineering services department, using a structured ETL pipeline.

The implementation involves:

✅ Data ingestion using Amazon S3

✅ Data profiling and cleaning with AWS Glue DataBrew

✅ Metadata organization via AWS Glue Data Catalog

✅ Data summarization and transformation with AWS Glue Visual ETL

✅ Each step includes configuration, screenshots, and justification for choices, aiming for scalability, accuracy, and performance.

## 🎯 Project Objective
To build a scalable, secure, and cost-effective cloud-based Data Analytic Platform on AWS that enables the City of Vancouver to perform descriptive analytics on employee compensation data. The platform facilitates data-driven insights by automating data ingestion, cleaning, cataloging, and summarization processes using AWS-native tools.

## 🗂️ Dataset Description
**Source**: [Vancouver Open Data Portal](https://opendata.vancouver.ca/explore/dataset/employee-remuneration-and-expenses-earning-over-75000)
The dataset used in this project is titled "Employee Remuneration and Expenses (Earning Over $75,000)", sourced from the City of Vancouver Open Data Portal.

This dataset contains annual remuneration and expense records for City of Vancouver engineering employees, specifically JourneyMan Mechanics who earned more than $75,000 in a calendar year. It provides transparency in public sector compensation and supports data-driven decision-making regarding staffing, budgeting, and departmental spending.

# 📁 Key Features:
- Time Range: 2008–2023
- 📁 CSV format
- 👥 500+ records
- 💰 Focus: Salaries, Benefits, Expenses
- Columns:

  - Name: Employee's full name

  - Department: The department the employee belongs to (e.g., Engineering Services)

  - Job Title: Employee’s role or position

  - Year: Reporting year for the salary and expenses

  - Remuneration: Total earnings, including base salary and overtime

  - Expenses: Claimed and approved work-related expenses

## ⚙️ METHODOLOGY
The methodology for this project follows a structured Extract-Transform-Load (ETL) approach using AWS-native services. The aim was to build a robust and scalable Data Analytic Platform (DAP) that supports descriptive analytics for the City of Vancouver's employee remuneration dataset.

# 🔽 1. DATA INGESTION
  - Tool Used: Amazon S3

  - The raw dataset (CSV format) was sourced from the City of Vancouver Open Data Portal and uploaded into an Amazon S3 bucket named city-vancouver-data.

Data ingestion is the foundational step in developing the **Data Analytic Platform (DAP)** for the City of Vancouver. It involves importing raw data into a cloud environment for processing and analysis. In this project, the dataset titled **“Employee Remuneration and Expenses (Earning Over $75,000)”**, sourced from the [City of Vancouver Open Data Portal](https://opendata.vancouver.ca/), was selected for analysis due to its rich insights into public employee compensation trends.

To begin, I logged into the **AWS Management Learner Lab Console** and navigated to the **Amazon S3** service—Amazon's scalable object storage solution. I initiated the ingestion process by creating a new bucket named **`city-vancouver-data`**, ensuring the name was unique across the AWS region. The selected region for storage was **US East (N. Virginia)**, which offers high availability and compatibility with other AWS services used in this project.

To maintain a structured and scalable approach to data organization, I created a logical folder hierarchy within the S3 bucket:
- **`employee-remuneration/`** – Base directory indicating the nature of the dataset.
- **`year=2025/`** – A subfolder to group data based on the reporting year, enabling efficient time-based partitioning and future automation.
- **`server=COVS-Emma/`** – A further subfolder used to identify the specific server or job context used for processing the dataset.

This layered structure supports best practices in cloud storage by improving **clarity, retrieval speed**, and **pipeline automation** down the line. It also aligns well with AWS Glue partitioning conventions, which enhances compatibility with query engines like AWS Athena and Amazon Redshift Spectrum.

The dataset file, named **`city-van-emp-rem-cln-emma_part00000.csv`** (36.1 KB), was then uploaded into the designated folder. It contains records of employees earning over $75,000, including salary, job title, department, and expense data. The file was stored using the **Standard Storage Class**, which ensures immediate accessibility with no additional retrieval costs—ideal for frequently accessed datasets in analytics workflows.

Importantly, the file format chosen was **CSV (Comma-Separated Values)**. This format was selected due to its wide compatibility with AWS services, ease of parsing, and suitability for tabular datasets. It also allows for seamless integration with tools like **AWS Glue DataBrew**, which would be used in the next stage for profiling and cleaning.

This step ensures that the data is securely stored in the cloud, properly organized, and readily accessible for downstream processing tasks such as profiling, transformation, and summarization.

Figure: 1.1 Existing file in the S3 bucket following the data ingestion process.
> ![Screenshot (20)](https://github.com/user-attachments/assets/a318e57a-0acb-4980-a6c6-dacd549996d9)
> - Note: A screenshot of the S3 bucket and folder structure taken from my AWS Console. Data was organized in folders based on year and server designation to ensure clarity, versioning, and scalability

# 2. 🔍 DATA PROFILING
  - Tool Used: AWS Glue DataBrew
  - The dataset was imported into AWS Glue DataBrew to assess data quality, structure, and completeness.
  - Profiling results identified data types, null values, and column distributions—crucial for planning cleaning steps.
    
Data profiling is a critical step in building a reliable and trustworthy Data Analytic Platform (DAP), as it helps to evaluate the structure, quality, completeness, and consistency of a dataset before it undergoes any transformation or analysis. In this project, profiling was performed using AWS Glue DataBrew, a visual data preparation tool that provides advanced insights into dataset characteristics without writing code.

The dataset in focus—city-van-emp-rem-cln-emma_part00000.csv—was previously uploaded to the Amazon S3 raw bucket (city-vancouver-data). This raw dataset was imported into AWS Glue DataBrew where a profiling job was created and executed to inspect the dataset’s schema, data types, missing values, outliers, and distributions.

# 📊 Profiling Insights:
  - Total Records: 508 rows
  - Total Columns: 6

Detected Data Types:

  - 🟦 Year: Integer – Represents the calendar year of the remuneration data

  - 🟨 Remuneration & Expenses: Double – Numerical columns storing monetary values

  - 🟩 Name, Department, Job Title: String – Text fields describing employee attributes

The profiling summary gave a clear picture of the dataset's structural integrity. For example:

  - The “Year” column showed no missing values and confirmed consistent integer types across all entries.

  - The “Remuneration” and “Expenses” columns were originally detected as double, suitable for precision, but they were later transformed for aggregation operations.

  - The categorical columns such as “Department” and “Job Title” showed a limited set of values, which is helpful for filtering and grouping in future steps.

No major anomalies (such as null values or data type mismatches) were observed at this stage.
Understanding these characteristics is crucial, as it ensures:
  - Proper data type enforcement during cleaning
  - Appropriate aggregation functions can be applied during summarization
  - Effective visualizations and statistical insights can be generated

The profiling job also produced a summary report, which was stored in a transformation S3 bucket named city-van-data-trf-emma. This step lays the groundwork for accurate, efficient data cleaning and transformation in the next stages of the ETL pipeline.

Figure: 1.2 Data Profile Overview.
![Screenshot (21)](https://github.com/user-attachments/assets/c0dbaf0c-1598-477d-a624-26f2ca607a96)
Note: A screenshot of the DataBrew profiling interface, showcasing the column summaries and profiling statistics from my AWS Console.

## 🧹 3. DATA CLEANING
  - Tool Used: AWS Glue DataBrew
  - Inconsistencies in data types were resolved (e.g., converting numeric columns to appropriate formats).
  - Columns were standardized, and unnecessary entries (e.g., duplicates) were handled.
  - A reusable DataBrew recipe was created and applied through a cleaning job, then stored in a transformed S3 bucket.
Data cleaning is a vital step in the data pipeline that ensures the dataset is accurate, consistent, and suitable for analysis. In this project, AWS Glue DataBrew was used to systematically clean the Employee Remuneration and Expenses dataset after profiling revealed its structure and characteristics. Cleaning was necessary to enforce data type consistency, resolve formatting issues, and prepare the dataset for reliable transformation and analysis downstream.

# 🛠️ Cleaning Process Overview
Once the dataset city-van-emp-rem-cln-emma_part00000.csv was successfully imported into DataBrew, a custom cleaning recipe was developed to apply a series of transformation steps. These steps were recorded under the recipe name CityVanEmpRem-Prj-Emma-recipe, allowing for reusability and version control across future datasets.

Key transformations and adjustments included:

  - # 🔢 1. Data Type Standardization
The Remuneration column, originally of type Double, was converted to Integer. This change ensures uniformity across financial figures, simplifies statistical calculations, and improves compatibility with downstream aggregations.

The Expenses column was similarly converted from Double to Integer to align it with the Remuneration field, ensuring seamless numerical operations when both are analyzed or summarized.

The conversions help prevent errors or misinterpretations in arithmetic operations, especially during aggregations (e.g., sum, average) and visualization rendering.

  - # ✅ 2. Validation of Data Integrity
After conversion, each field was validated to ensure the values were within expected ranges.

No missing values, nulls, or NaNs were detected during this phase, confirming the dataset’s high integrity.

Similarly, no duplicate rows were found, eliminating the need for deduplication steps.

  - # 🧪 3. Schema Conformity Check
The schema was aligned to match what would be defined in the AWS Glue Data Catalog later on.

All string-type fields such as Name, Department, and Job Title were checked for formatting issues (e.g., trailing spaces or inconsistent capitalization), although none required modification in this version of the dataset.

  - # 📦 4. Execution and Storage
A DataBrew job named city-van-emp-rem-cln-emma was executed to apply the cleaning recipe to the dataset.

Upon successful execution, the cleaned dataset was saved to a designated transformation S3 bucket (city-van-data-trf-emma) for further processing.

The job log and outputs were reviewed to ensure successful transformation with no job errors.

  - # 🔁 5. Reusability and Automation
The cleaning recipe was built to be modular and reusable, meaning it can be applied automatically to similar datasets in the future—saving time and reducing the risk of manual errors.

With minimal adjustments, this recipe can accommodate future datasets for other years or departments.

This data cleaning step guarantees that the dataset meets the necessary standards for quality and consistency, which are essential for accurate data cataloging, querying, visualization, and reporting. It also ensures that subsequent stages—like summarization and dashboard integration—are based on solid, reliable data.

Figure 1.3: Data Cleaning Recipe.
![Screenshot (24)](https://github.com/user-attachments/assets/a306ee63-0ed7-4a19-b244-927cc44f3792)
Figure 1.4: A Successful Cleaning Job
![Screenshot (25)](https://github.com/user-attachments/assets/e96506a1-6780-42f7-b596-ddc373257c4a)
Note: Screenshots of the recipe and successful cleaning job are provided in Figures 1.2 and 1.3 respectively

## 🧹 3. DATA CATALOGING
  - Tool Used: AWS Glue DataBrew
  - Inconsistencies in data types were resolved (e.g., converting numeric columns to appropriate formats).
  - Columns were standardized, and unnecessary entries (e.g., duplicates) were handled.
  - A reusable DataBrew recipe was created and applied through a cleaning job, then stored in a transformed S3 bucket.
    
Once the dataset has been cleaned and validated, the next essential stage in the Data Analytic Platform (DAP) workflow is Data Cataloging. This process involves structuring and registering the dataset as metadata, enabling efficient discovery, querying, and integration with various analytics services within the AWS ecosystem.

In this project, AWS Glue Data Catalog was used as the metadata repository. This service acts as a central metadata store that makes data readily accessible to tools such as AWS Athena, Amazon Redshift Spectrum, and Amazon QuickSight for querying, visualization, and reporting.

# 🧱 Steps in the Data Cataloging Process
  # 📁 1. Creating a Glue Database
To begin cataloging, a new database was created in AWS Glue named city-van-data-catalog-emma. This database serves as a logical container that holds the metadata for one or more tables. Creating a dedicated database ensures a clean separation of datasets, facilitates management, and supports modular growth of the platform.

  - 📌 This step allows for logical organization of datasets by project, source, or year.

  - 📌 The database creation step is a prerequisite for managing data tables and schema definitions.

  # 🔍 2. Registering the Cleaned Dataset
Once the database was created, the cleaned dataset—stored in the transformation S3 bucket city-van-data-trf-emma—was registered as a table within this database.

The table schema includes details such as:

- Column names (e.g., Name, Job Title, Department, Remuneration, Expenses, Year)

- Data types (e.g., String, Integer)

- Data location (S3 path)

This registration makes the dataset queryable via SQL-like interfaces in tools like AWS Athena, and it ensures schema consistency across tools.

  # 🔄 3. Creating and Configuring a Crawler
To automate the process of metadata extraction, a Glue Crawler was created with the identifier emp-rem-crw-emma.

The crawler was configured to:

  - Scan the S3 path where the cleaned dataset is stored

  - Detect the schema automatically (column types, formats, partitions)

  - Populate or update the metadata in the Glue Data Catalog

This automation removes the need for manual schema definition and supports future data changes (e.g., schema evolution or new file uploads).

After running the crawler, a metadata table was created and successfully linked to the transformation S3 bucket.

  # 🧠 4. Why Data Cataloging Matters
  - Enables schema validation and data discovery across AWS services.

  - Ensures consistent data definitions for querying and reporting tools.

  - Acts as the bridge between raw storage (S3) and analytical services like Athena (for SQL queries) and QuickSight (for dashboards).

  - Supports partitioning, versioning, and access control through IAM and Glue policies.

This step ensures that the cleaned dataset is now not just stored, but also structured and accessible, allowing both technical and non-technical users to query and explore the data seamlessly.
Figure 1.5: A Database Created
![Screenshot (27)](https://github.com/user-attachments/assets/cd0782f7-3d2b-408c-a2cf-46e6531c976b)
Figure 1.6: A Detailed Data Catalog Table
![Screenshot (14)](https://github.com/user-attachments/assets/96543116-7a95-43d6-83d3-b9db6cffedf8)
Figure 1.7: A Successful Crawler Job Run
![Screenshot (26)](https://github.com/user-attachments/assets/b4f7cf58-77bf-4069-bfea-d2a2b0a676e2)
Note: Figures 1.5 and 1.6 show the newly created database and metadata table; Figure 1.7 illustrates the successful crawler job execution.

## 📊 5. DATA SUMMARIZATION
  - Tool Used: AWS Glue Visual ETL
  - The dataset was filtered and aggregated based on specific timeframes (e.g., 2020–2023).
  - Summary statistics (average remuneration, total expenses, etc.) were computed.
  - The output was stored in both Parquet and CSV formats in a curated S3 bucket, optimized for performance and readability.
    
Data Summarization marks the final and crucial step in the Data Analytic Platform (DAP) workflow. At this stage, the cleaned and cataloged data is transformed and aggregated to derive high-level insights and improve interpretability for end-users. The goal is to condense raw records into meaningful summaries using statistical computations and prepare the dataset for analysis, visualization, or reporting.

In this project, AWS Glue Visual ETL (Extract, Transform, Load) was employed to perform these summarization tasks through a user-friendly interface without writing code. The outputs were stored in a curated S3 bucket named city-van-data-cur-emma, representing the final, analysis-ready dataset.

  # 🧱 Process Overview
  
    # 📤 1. Dataset Retrieval
The summarization process began by retrieving the cleaned dataset from the AWS Glue Data Catalog, which ensured that the most up-to-date and validated version of the data was being used. This seamless integration with Data Catalog supports schema enforcement, data lineage tracking, and compatibility with transformation tools.

    # ✂️ 2. Schema Optimization
Before applying aggregation, the schema was reviewed and optimized:
  - The Department column was dropped because all records belonged to a single department, which added no analytical value.
  - The dataset was filtered to include only records between the years 2020 and 2023, focusing the analysis on recent and relevant trends.
These preprocessing steps reduced data redundancy and improved clarity in the final report.

        # 🧮 3. Aggregation and Transformation
Using AWS Glue’s Visual ETL interface, the following summarization steps were performed:
  - Group By Year – The dataset was grouped by the Year field to analyze trends over time.

Aggregate Columns:
  - Remuneration – Average remuneration computed per year
  - Expenses – Average expense per year
A Timestamp column was added dynamically to record the exact time the data was summarized, which helps in tracking data currency and processing frequency.
These transformations resulted in a concise, year-wise summary that captures essential financial trends across the selected period.

        # 📦 4. Output Formatting and Storage
To ensure the output is both system- and user-friendly, the summarized dataset was exported in two formats:
  - Parquet (with Snappy Compression): Used for internal system processing
                                       Offers better performance for large-scale queries
                                       Partitioned by Year for optimized querying in tools like Athena and Redshift Spectrum

  - CSV (Uncompressed): Ideal for human consumption or simple external use
                        Easily downloadable and readable in Excel or basic data tools
                        Both output formats were stored in the curated S3 bucket (city-van-data-cur-emma), completing the data transformation pipeline.

    # ✅ Benefits of Summarization
    - Simplifies analysis by reducing complexity in the original dataset
    - Enables faster queries and reporting through compression and partitioning
    - Prepares data for visualization tools like Amazon QuickSight or external dashboards
   
  Figure 1.8: An ETL pipeline
  ![Screenshot (15)](https://github.com/user-attachments/assets/97839f75-0404-4b7c-b3f3-87db88b59847)
  Figure 1.9: A Summarized Data Report for System Readers
  ![Screenshot (29)](https://github.com/user-attachments/assets/86ef2a5c-b8b3-444b-93d5-653f531c3b37)
  Figure 1.10: A Summarized Data Report for Users 
  ![Screenshot (30)](https://github.com/user-attachments/assets/ac1f069d-9e3d-4c05-b76b-df95f4962f69)
Note: Figure 1.8 illustrates the complete Visual ETL pipeline; Figures 1.9 and 1.10 display the resulting summarized datasets for both system integration and user viewing.

The successful design and implementation of the Data Analytic Platform (DAP) on AWS for the City of Vancouver demonstrates the effectiveness of cloud-native tools in enabling scalable, secure, and cost-efficient data analytics solutions. By leveraging services such as Amazon S3, AWS Glue DataBrew, AWS Glue Data Catalog, and AWS Glue Visual ETL, this project established a structured ETL pipeline that transforms raw municipal data into actionable insights.

Each stage—from data ingestion to summarization—was strategically planned and executed to ensure data integrity, performance optimization, and analytical readiness. The platform not only supports descriptive analysis on employee remuneration and expenses but also provides a foundation for future enhancements such as real-time analytics, dashboard integration, or predictive modeling.

Ultimately, this project highlights how governments and organizations can adopt cloud technologies to improve decision-making, transparency, and data accessibility—laying the groundwork for a more data-driven public service.

## 6. DATA ANALYSIS
As a part of the data analytic platform, I have worked on the analysis of yearly salary trends for the employees working within the Engineering Services department. After completing the data cleaning and cataloging steps, I queried the cleaned dataset in Amazon S3 using AWS Athena. To achieve this, I wrote an SQL query to compute the average salary, total salary paid, and the number of employees in the Engineering Services department for every year.

This has allowed me to observe changes in compensation over time within the department, Journeyman-Mechanic. The topic seemed the right one for analysis since Engineering Services is a key function within the Vancouver municipality, and salary trends can provide critical information about budgeting, workforce, and operational efficiency. By collating the data based on the year, filtering the information by the department, I can meaningfully summarize it to support data-driven decision-making for the City of Vancouver.

The first descriptive analysis question for this data-driven decision is to analyze the average salary or remuneration trends of City of Vancouver engineering employees earning above $75,000 annually. As depicted in figure 1.2, this trend is observed over a period of four years beginning from 2020 t0 2023 and it shows a steady increase in the average salaries over the years. From 2020 to 2023, the average salary increased more than 13%. Most of the annual compensation hikes occurred between 2022 and 2023, with an average increase of more than $6,300, mostly resulting from inflation adjustments, contractual raises, or promotion. This increasing trend seems to be affecting how high-earning employees of the city will be compensated in the future, a factor which may be put into consideration while planning budgets, human resources policies, and long-term financial strategies of the City of Vancouver

Figure 2.1: Athena Query to Answer Descriptive Analysis Question I
![Screenshot (77)](https://github.com/user-attachments/assets/e1400f87-20b9-4080-9716-c4c58197b40a)
Note: A screenshot of the result of an SQL query to determine the average salary using my AWS Athena Console 

In an attempt to answer the second description analysis question that queries the spending habits of Journeyman-Mechanics over the years. It is quite unfortunate that the City of Vancouver data team could not accurately collate the expenses of these engineering services workers over the years hence making this analysis unable to reflect the true state on the matter. However, with the little information gathered for this analysis, the year 2020 saw the average of employee expenses land at about $75, the lowest ever recorded by the dataset. In 2022, one would have experienced a phenomenal uplift with average expenses hitting around $243 thus indicating possibly increased activities, travelling, reimbursement, or operating costs that year. The average has been reduced to $89.91 in 2023, indicating either minimal expenses activity or stricter expenditure control. The trend seems non-linear, with an outlier in the year 2022, a steep rise and fall which typically imply temporary projects or minimal events in 2020, or a change in costing policy, auditing, or reporting. What sets this trend apart is its potential to measure cost control by the City of Vancouver and to bring forth the identification of budget anomalies or possibly plan the next budget for employee expenditures. Figure 2.2 summarize the trend as seen.

Figure 2.2: Athena Query to Answer Descriptive Analysis Question II
![Screenshot (78)](https://github.com/user-attachments/assets/1eb7afe8-5749-4ac2-a596-8f737bceff06)
Note: A screenshot of the result of an SQL query to determine the average expenses using my AWS Athena Console.

## 7. 🔐 DATA SECURITY
Implementing robust data security measures is a critical aspect of the Data Analytic Platform (DAP) developed for the City of Vancouver. Given the sensitivity of the dataset—particularly employee remuneration and other personal information—it was imperative to enforce strict controls and protections throughout the entire data lifecycle, from ingestion to transformation and summarization.

🛡️ Identity and Access Management (IAM)
To enforce access control, AWS Identity and Access Management (IAM) was utilized to define fine-grained permissions for different user roles and services. Specific IAM policies were configured to:
  - Grant least privilege access, ensuring users and roles only have access to the exact resources they need.
  - Restrict access to specific S3 buckets and folders (e.g., raw, transformed, and curated layers) based on user roles such as data engineer, analyst, or admin.
  - Control access to AWS services such as Glue, Athena, and DataBrew by attaching appropriate service-level permissions to roles.

This approach enhances internal data governance, limits human error, and protects against unauthorized access.

🔒 Data Encryption at Rest and In Transit
To ensure that data is protected both at rest and in transit, several layers of encryption were implemented:
  - Encryption at Rest: All Amazon S3 buckets—city-vancouver-data (raw), city-van-data-trf-emma (transformed), and city-van-data-cur-emma (curated)—were configured with AWS Key Management Service (KMS) to enable server-side encryption (SSE-KMS). This provides an additional layer of key management and audit logging.
  - Encryption in Transit: SSL/TLS encryption was enforced for all communications between AWS services, including data transfers between AWS Glue, Athena, and S3. This ensures that sensitive data is not exposed during transmission.

📂 Versioning and Replication
To further enhance data integrity, continuity, and recovery options:
  - Versioning was enabled on all S3 buckets to maintain historical versions of datasets. This ensures that changes to the data are tracked over time and can be rolled back if necessary—critical for audit trails, debugging, or rollback after accidental deletions.
  - Cross-Region Replication (CRR) or backup replication rules were configured so that each object stored in the primary S3 bucket is automatically copied to a secondary backup bucket. This provides an effective disaster recovery mechanism, supporting compliance with data retention policies and ensuring high availability of critical datasets.

🧠 Security Best Practices Followed:
  - IAM Role Separation: Different roles for ingestion, transformation, and analysis stages.
  - Bucket Policies and ACLs: Applied restrictive permissions and denied public access.
  - Logging and Monitoring: (Optional but recommended) Enable AWS CloudTrail and Amazon S3 Access Logs to track access and modifications to data resources.

Figure 2.3: A successfully created AWS KMS
![Screenshot (59)](https://github.com/user-attachments/assets/661059f9-5c3a-418f-b5e3-8351083320dc)

Figure 2.4: Data Replication Rule in S3 raw bucket (city-vancouver-data)
![Screenshot (63)](https://github.com/user-attachments/assets/d5835701-d8e0-4f9f-81ff-4e4979d442df)

Figure 2.5: Data Encryption Applied in S3 raw bucket (city-vancouver-data)
![Screenshot (61)](https://github.com/user-attachments/assets/7c32ac3d-53a9-4026-8686-fed8ff4d07a4)

Figure 2.6: Bucket Versioning enabled in S3 raw bucket (city-vancouver-data)
![Screenshot (62)](https://github.com/user-attachments/assets/f5d880f0-661e-4fca-a7b7-fded7e8d9ea0)

Figure 2.7: Bucket Versioning enabled in S3 transform bucket (city-van -data-trf-emma)
![Screenshot (64)](https://github.com/user-attachments/assets/2bf6cba8-5802-450a-bc8e-b89dadb47b11)

Figure 2.8: Data Encryption Applied in S3 transform bucket (city-van -data-trf-emma)
![Screenshot (65)](https://github.com/user-attachments/assets/bd3a1a9b-9be5-46a4-bce4-22e8e6146fcf)

Figure 2.9: Replication Rule enabled in S3 transform bucket (city-van -data-trf-emma)
![Screenshot (66)](https://github.com/user-attachments/assets/dcd23a1f-1589-4d87-be4a-df229e6faf24)

Figure 2.10: Bucket Versioning enabled in S3 curated bucket (city-van -data-cur-emma)
![Screenshot (67)](https://github.com/user-attachments/assets/65d250b1-0179-481c-835f-e96f2e54b496)

Figure 2.11: Data Encryption Applied in S3 curated bucket (city-van -data-cur-emma)
![Screenshot (62)](https://github.com/user-attachments/assets/c5765cc6-1ceb-437f-9a08-e25de381f4b8)

Figure 2.12: Replication Rules enabled in S3 curated bucket (city-van -data-cur-emma)
![Screenshot (69)](https://github.com/user-attachments/assets/76826da1-3e39-4313-9a8c-e92d51df1659)

Note: Figures 2.3 to 2.12 are screenshoots from my AWS Console illustrating the IAM roles, S3 bucket policies, encryption settings, versioning status, and replication rules configured throughout the platform.

These security configurations not only comply with cloud data protection standards but also align with the City of Vancouver’s need for confidentiality, integrity, and availability of sensitive employee data. The layered security approach ensures that data is protected across all touchpoints—making the platform trustworthy and enterprise-ready.

### 8. 🧭 DATA GOVERNANCE
Data governance is a foundational pillar of any reliable data platform, ensuring that data is accurate, consistent, discoverable, secure, and trustworthy across its lifecycle. In the context of this project, implementing strong data governance practices was essential for enabling informed decision-making and fostering confidence in the analytics outcomes delivered to the City of Vancouver.

# 📚 Metadata Management with AWS Glue Data Catalog
At the heart of this governance strategy is the use of AWS Glue Data Catalog to manage and organize metadata—information about the datasets. For each dataset ingested and processed, metadata such as column descriptions, data types, sources, and schema versions were documented. This metadata not only enhances transparency but also empowers users across teams (e.g., analysts, engineers, auditors) to discover, understand, and use the data effectively.

By providing a centralized data inventory, the Data Catalog serves as a data discovery hub, helping avoid duplication, supporting data lineage tracking, and encouraging secure collaboration within and across departments.

# 🧪 Data Quality Checks and Governance Rules
To ensure high-quality data, specific governance rules were enforced as part of the ETL process using AWS Glue:

  - Completeness	"name" field ≥ 95% populated
  - Uniqueness	"remuneration" field > 99% unique values
  - Freshness	"year" field must be within last 1500 days
These thresholds were incorporated into the transformation phase of the ETL workflow to ensure only high-quality, up-to-date data progresses through the pipeline. Any datasets that failed to meet these criteria were flagged and separated for review.

# 🔄 Automated ETL Pipeline
An automated ETL (Extract, Transform, Load) pipeline was designed and implemented using AWS Glue to streamline data processing and reduce human errors:

  1. Extraction Phase:
    - Data is extracted from Amazon S3 (transformed bucket), representing cleaned datasets ready for final checks.
    - This stage ensures a consistent and repeatable data retrieval process.

  2. Transformation Phase:
    - The extracted data is subjected to cleaning, enrichment, and quality validation based on the governance rules mentioned above.
    - AWS Glue jobs are used to apply transformations and validate fields according to the defined governance framework.

  3. Loading Phase:
    - After validation, datasets are automatically sorted into organized S3 folders:
      - ✅ Passed folder: Data that meets all quality checks and is ready for summarization or analysis.
      - ❌ Failed folder: Data that fails validation and requires review or remediation.

This folder-based classification in Amazon S3 supports traceability, accountability, and continuous improvement by making it easy to identify and investigate problematic data records.

# ⚙️ Governance Benefits
  - ✅ Consistency: Standardized schemas and transformation rules ensure uniformity across datasets.

  - ✅ Trustworthiness: Only validated data enters the analysis layer, improving confidence in results.

  - ✅ Auditability: Clear lineage and versioning provide historical insight and support compliance.

  - ✅ Automation: Reduces manual intervention, speeds up processing, and supports scale.

  - ✅ Enablement for Advanced Analytics: Well-governed data lays the foundation for future use cases such as predictive modeling, ML pipelines, and real-time dashboards.

Figure 2.13: ETL Pipeline for Data Quality Control
![Screenshot (70)](https://github.com/user-attachments/assets/5b187ab0-44c9-40e9-b2fb-2c4e3cef30f5)

Figure 2.14: Failed Folder in S3 Transformed Bucket
![Screenshot (72)](https://github.com/user-attachments/assets/4e45859e-440c-44e4-affb-bf55c1a49a1d)

Figure 2.15: Passed Folder in S3 Transformed Bucket
![Screenshot (71)](https://github.com/user-attachments/assets/1444ecd3-a78a-43fc-b91a-831980b80492)
Note: Theses screenshots (Figures 2.13 - 2.15) from my AWS Console illustrate how governance is enforced through metadata, rule application, and folder-based output segmentation in S3.

With governance deeply integrated into the platform design, the City of Vancouver can be confident in the reliability, traceability, and utility of the insights generated through this system—ensuring responsible data stewardship and long-term sustainability.


### 9. 📡 DATA MONITORING
In any data analytics environment—especially one that serves critical public sector operations—continuous monitoring is essential for ensuring the reliability, performance, security, and integrity of data workflows. For the Data Analytic Platform (DAP) built for the City of Vancouver, a comprehensive data monitoring strategy was implemented using AWS-native services, including Amazon CloudWatch and AWS CloudTrail.

# 📊 Real-Time Monitoring with Amazon CloudWatch
Amazon CloudWatch was configured to oversee and track the behavior of key components in the platform, primarily focusing on AWS Glue jobs and Amazon S3 buckets.

Key features and metrics monitored:

  # AWS Glue Jobs:
    - Job execution status (success/failure)
    - Duration of ETL runs
    - Error logs and exceptions
    - Job retries and failure rates
    - Start and end timestamps for job steps

  # S3 Buckets:
    - Bucket size and object count over time
    - Monitoring of storage costs and growth trends
    - Alerts on unauthorized access or unusually high data write volumes

  # Custom CloudWatch Alarms were created to proactively flag issues such as:
    - Glue job failures
    - ETL jobs exceeding expected runtime thresholds
    - Ingestion delays or missing scheduled executions
    - Storage thresholds being approached in critical S3 buckets

These alarms were configured to trigger notifications via Amazon SNS (Simple Notification Service), ensuring that issues are brought to attention in real-time, reducing downtime or data processing lags.

# 🔐 User Activity Tracking with AWS CloudTrail
While CloudWatch monitors service performance and operations, AWS CloudTrail was activated to track user and API-level activity across the platform. This included:

  - Logging of user logins, role assumptions, and policy changes
  - Monitoring of API calls made to services such as S3, Glue, Athena, IAM, etc.
  - Capturing changes to bucket permissions, data access patterns, and IAM role usage

CloudTrail provided an audit trail that is invaluable for:
  - Troubleshooting and Root Cause Analysis: Quickly identifying the origin of an error or unauthorized change
  - Compliance and Data Integrity: Demonstrating adherence to security and governance policies
  - Access Forensics: Verifying who accessed what data, when, and from where

# 📈 Dashboarding and Automation
To visualize platform performance and maintain a centralized view, CloudWatch Dashboards were created to present real-time metrics and historical trends. These dashboards included:

  - ETL job duration trends over time
  - Frequency of job failures
  - Data ingestion volumes per day
  - Alert history and system uptime

Threshold-based triggers were also set up for automated responses, such as:
  - Initiating fallback Glue jobs on failure
  - Sending notifications to administrators or analysts
  - Marking data as stale when ingestion jobs are delayed beyond set limits

# ✅ Benefits of Data Monitoring
  - Early Problem Detection: Identify and resolve errors before they impact users or downstream processes.
  - Performance Optimization: Track and analyze job duration to reduce runtime and improve efficiency.
  - Security and Compliance: Maintain visibility into all actions across the platform to ensure accountability.
  - Data Freshness Assurance: Monitoring ingestion frequency ensures that stakeholders always have access to current and reliable data.

Figure 2.16: An Implemented CloudWatch Dashboard
![Screenshot (80)](https://github.com/user-attachments/assets/17d6c488-3b83-4241-806e-9be93892c504)

Figure 2.17: An Implemented CloudTrail log
![Screenshot (74)](https://github.com/user-attachments/assets/c00f17e1-2d31-4440-86b7-906010069be8)

Note: These screenshots (Figures 2.16 and 2.16) from my AWS Console provide a visual walkthrough of how CloudWatch and CloudTrail were configured to support proactive and comprehensive data monitoring.

By deploying real-time and historical monitoring tools, the City of Vancouver’s data analytics platform remains resilient, transparent, and secure, with full visibility into its operations—critical for maintaining trust and data quality across public-sector data initiatives.


## 🧱 Platform Architecture

## 🖼️ Visual Architecture & Data Insights

### 🏗️ Platform Architecture Diagram
Figure 2.18: DAP diagram in Draw.io
![Screenshot (7)](https://github.com/user-attachments/assets/f691fc5c-7c27-4ef4-8ad6-c832538281ed)

The diagram above illustrates the full **Data Analytic Platform (DAP)** implementation for the City of Vancouver, designed using draw.io. It visually represents the **end-to-end flow** from data ingestion to analytics, highlighting the key AWS services and roles involved:

- **AWS EC2 Virtual Servers** host general and specific service components for employee remuneration data, including a web application layer.
- **Amazon S3** is used for multi-stage data storage: raw ingestion, transformation outputs, and curated summaries.
- **AWS Glue DataBrew** is used to profile and clean incoming CSV datasets.
- **AWS Glue ETL Jobs** automate data transformation and summarization workflows, using metadata rules for data quality validation.
- **AWS Glue Data Catalog** acts as a metadata layer, allowing datasets to be queried using **AWS Athena** or visualized in **Amazon QuickSight**.
- **IAM roles** and **CloudWatch monitoring** ensure that access is secure and workflows are operationally sound.
- Data is also partitioned and labeled in S3 by year and server (`/employee-remuneration/year=2025/server=COVS-Emma`) for efficient querying and storage management.

This architecture ensures a scalable, maintainable, and secure analytics solution tailored to public-sector data governance requirements.



### 📊 Sample Data Visualization

Figure 2.19: A bar chart showing the maximum remuneration for City of Vancouver engineering service employees
![Screenshot (8)](https://github.com/user-attachments/assets/a8d98f8c-0582-4469-bf06-be9931707b02)


The image above shows a **column chart** depicting **maximum remuneration trends over time** for the *Engineering Services* department, specifically for the **Journeyman - Mechanic** title. This visualization, created using the Vancouver Open Data Portal’s analysis interface, clearly demonstrates a consistent upward trend in compensation between **2008 and 2023**.

#### Key Highlights:
- **X-axis:** Represents the year
- **Y-axis:** Shows the maximum recorded salary per year
- **Filtered by:** Department = Engineering Services, Title = Journeyman - Mechanic
  
The chart supports decision-makers by revealing salary growth trends and potential areas for policy adjustments or budget forecasting.


### 🔍 Importance of Visualization & Architecture

Combining a well-structured data architecture with clear, visual representations of trends enables:
- **Informed decision-making**
- **Policy evaluation** based on actual trends
- **Improved transparency** in public sector compensation
- **Scalability** to extend the analysis to other departments or data domains



### 🔄 Data Flow Overview

The data analytic platform is built on a modular pipeline architecture that allows for the seamless flow of data from multiple input sources to final analytical outputs. This end-to-end pipeline leverages key AWS services to ensure scalability, automation, and data quality throughout the lifecycle. Here's a breakdown of the data flow:

  📥 1. Data Ingestion from Multiple Sources
The system is designed to collect data from a variety of input sources, including:

  - CSV files exported from internal systems or open data portals

  - Relational databases such as MySQL or PostgreSQL via data connectors (optional future integration)

  - Cloud APIs or third-party services (e.g., HR platforms or finance systems)

This diverse sourcing enables the platform to accommodate structured and semi-structured data from various departments within the City of Vancouver.

All ingested data is stored in Amazon S3, specifically in a well-structured bucket (city-vancouver-data) that organizes files by year and processing context (e.g., /employee-remuneration/year=2025/server=COVS-Emma). This structure supports traceability, easy partitioning, and optimized access.

  🧹 2. Data Cleaning and Transformation
Once the data is ingested, it is passed through AWS Glue DataBrew, a visual, no-code tool used for:

  - Profiling the dataset to identify data types, distributions, and missing values
  - Detecting and resolving data quality issues such as inconsistencies, duplicates, and null entries
  - Applying custom transformation recipes that prepare the dataset for analysis

This step ensures that only validated and standardized data proceeds through the pipeline.

  📦 3. Data Storage and Layered Architecture
The cleaned dataset is saved back into Amazon S3 in a transformed bucket (city-van-data-trf-emma). After summarization and final processing, it is stored in a curated bucket (city-van-data-cur-emma) in both CSV and Parquet formats to support different use cases:
  - Parquet for performance-optimized querying with Athena or Redshift
  - CSV for human-readable outputs and reporting
    
Each layer of storage—raw, transformed, and curated—follows a clear directory structure that supports data versioning, partitioning, and backup.

  📚 4. Metadata Management and Cataloging
To support data discovery and governance, all processed datasets are registered in the AWS Glue Data Catalog. Metadata such as:
  - Column names and data types
  - Table structure
  - Source and update frequency

These are stored and made accessible to analytics services like AWS Athena (for SQL queries) and Amazon QuickSight (for dashboards). A Glue Crawler is configured to scan the updated data in S3 and automatically update the catalog when new files are added.


### 📊 Key Components
| Stage | Service | Description |
|-------|---------|-------------|
| Data Ingestion | Amazon S3 | Upload and organize raw CSV datasets |
| Data Profiling | AWS Glue DataBrew | Analyze structure, types, and anomalies |
| Data Cleaning | AWS Glue DataBrew | Standardize and clean inconsistencies |
| Data Cataloging | AWS Glue Catalog | Organize metadata and schema |
| Data Summarization | AWS Glue ETL | Generate aggregate reports and visuals |
| Data Analysis | AWS Athena | Use SQL to query datasets |
| Data Security | AWS KMS & IAM | Assign roles and restricts accessibility to authorized users |
| Data Governance | AWS Glue ETL | Provide data quality checks and ensures freshness of datasets |
| Data Monitoring | AWS CloudWatch & CloudTrail | Monitors AWS Glue jobs and S3 Buckets in realtime | 

---

## 📈 Descriptive Analysis Focus
**Question:** _What are the salary trends and spending patterns for engineering service employees earning over $75,000 annually from 2020 to 2023?_

Includes:
- Annual salary and expense trends
- Departmental breakdowns
- Statistical summaries

---

## 📸 Screenshots
> 📍 _All implementation steps include screenshots in the main report file._  
- AWS S3 bucket setup  
- DataBrew profiling & cleaning  
- AWS Glue Catalog and Crawlers  
- ETL workflows and output samples

---

## 💵 Estimated Cost
A monthly AWS cost estimate was generated using the **AWS Pricing Calculator**, accounting for:
- S3 storage (Standard class)
- Glue DataBrew jobs
- Glue ETL pipelines
- Minimal cost projections for a prototype phase

---

## 🧰 Tech Stack
- **AWS S3**: Cloud Storage
- **AWS Glue DataBrew**: Data Profiling & Cleaning
- **AWS Glue Catalog**: Metadata Management
- **AWS Glue ETL (Visual)**: Data Transformation
- **Python (optional)**: Data validation/scripting

---

## 📄 Report
The full technical report is included in this repository:
📘 `Data Analytic Platform COV - Emmanuel.docx`

---

## 🚀 Future Enhancements
- Integrate with AWS Athena or QuickSight for real-time querying & dashboards
- Incorporate API data sources
- Schedule automated jobs using AWS Lambda

---

## 🧑‍💼 Author
**Emmanuel Kweku Benyi**  
MBA Candidate | Data Enthusiast | Cloud Analytics Developer

---

## 📬 Contact
📧 Email: [emmanuel_benyi@yahoo.com]  
🔗 LinkedIn: [https://www.linkedin.com/in/emmanuel-kweku-benyi-245544150/]  
💼 Portfolio: [your personal site if any]

---

## 📌 License
This project is for academic demonstration purposes. No commercial use allowed.


