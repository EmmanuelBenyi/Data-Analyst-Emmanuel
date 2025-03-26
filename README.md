# Data-Analyst-Emmanuel
# 📌Project title
Design and Implementation of a Data Analytic Platform (DAP) on AWS for the City of Vancouver

# 📝Project Description
This project showcases the end-to-end development of a Data Analytic Platform (DAP) hosted on Amazon Web Services (AWS) to support the City of Vancouver’s transition to a cloud-based analytics infrastructure. The dataset analyzed includes employee remuneration and expenses for individuals earning over $75,000 annually. The platform enables descriptive analysis of salary trends and expenditures, particularly within the engineering services department, using a structured ETL pipeline.

The implementation involves:

✅ Data ingestion using Amazon S3

✅ Data profiling and cleaning with AWS Glue DataBrew

✅ Metadata organization via AWS Glue Data Catalog

✅ Data summarization and transformation with AWS Glue Visual ETL

✅ Each step includes configuration, screenshots, and justification for choices, aiming for scalability, accuracy, and performance.

# 🎯 Project Objective
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

## ⚙️ Methodology
The methodology for this project follows a structured Extract-Transform-Load (ETL) approach using AWS-native services. The aim was to build a robust and scalable Data Analytic Platform (DAP) that supports descriptive analytics for the City of Vancouver's employee remuneration dataset.

# 🔽 1. Data Ingestion
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

# 2. 🔍 Data Profiling
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

## 🧹 3. Data Cleaning
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

## 🧹 3. Data Cleaning
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

## 📊 5. Data Summarization
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

## 🧱 Platform Architecture

### 🔄 Data Flow Overview


### 📊 Key Components
| Stage | Service | Description |
|-------|---------|-------------|
| Data Ingestion | Amazon S3 | Upload and organize raw CSV datasets |
| Data Profiling | AWS Glue DataBrew | Analyze structure, types, and anomalies |
| Data Cleaning | AWS Glue DataBrew | Standardize and clean inconsistencies |
| Data Cataloging | AWS Glue Catalog | Organize metadata and schema |
| Data Summarization | AWS Glue ETL | Generate aggregate reports and visuals |

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


