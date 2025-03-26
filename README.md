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
> ![Data Ingestion](https://github.com/user-attachments/assets/4c553fd5-3bea-4302-9272-a068cdfac206)
> - Note: A screenshot of the S3 bucket and folder structure taken from my AWS Console. Data was organized in folders based on year and server designation to ensure clarity, versioning, and scalability


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


