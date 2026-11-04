# Vancouver Employee Analytics — AWS Data Analytic Platform

Descriptive analysis of City of Vancouver employee remuneration and expenses
for Engineering Services staff earning over $75,000, with a Data Analytic
Platform (DAP) built on AWS and a reproducible Python analysis.

## 📊 Findings at a Glance

**Analysis question:** What are the salary trends and spending patterns for
Engineering Services employees earning over $75,000 annually from 2020 to 2023?

- **Average salary rose every year**, from $90,229.38 in 2020 to $103,556.73
  in 2023, with the largest single-year increase between 2022 and 2023.
- **Average expenses were uneven:** $75.14 in 2020, $242.91 in 2022 (an outlier
  year), and $89.91 in 2023. Treat the expenses trend as indicative only:
  the City of Vancouver data team could not accurately collate expenses for
  these workers, so the expenses figures do not fully reflect the true state
  of spending. (The original analysis published no 2021 expenses row;
  reproducing it from the live data gives $20.50.)
- **Scope:** The dataset as originally analyzed covers 2008–2023 (the live
  portal file now extends to 2025); the analysis focuses on 2020–2023,
  filtered to a single department (Engineering Services) and job title
  (Journeyman-Mechanic).
- **Reproducible:** `analysis.py` reproduces the yearly tables and charts
  from the public dataset — see "Reproduce the Analysis" below.

| Year | Average Salary (CAD) | Average Expenses (CAD) |
|------|----------------------|------------------------|
| 2020 | 90,229.38            | 75.14                  |
| 2021 | 94,910.93            | (no row published)     |
| 2022 | 97,236.69            | 242.91                 |
| 2023 | 103,556.73           | 89.91                  |

## 🗂️ Dataset

**Source:** [Employee Remuneration and Expenses (Earning Over $75,000)](https://opendata.vancouver.ca/explore/dataset/employee-remuneration-and-expenses-earning-over-75000/),
City of Vancouver Open Data Portal.

The dataset holds annual remuneration and expense records for City of
Vancouver employees earning over $75,000 in a calendar year. This project
filters it to Engineering Services, title Journeyman-Mechanic (the post-2023
rename to "Journeyperson - Mechanic" is normalised to the same value),
years 2020–2023.

**Aggregate only:** the source file contains an employee-name column. The
script drops that column immediately after loading and never prints, saves,
or charts any individual-level row — every output is a yearly average.

## ▶️ Reproduce the Analysis

No AWS account needed — the script downloads the public CSV at run time.

```bash
pip install -r requirements.txt
python3 analysis.py
```

The script prints the yearly average remuneration and average expenses
tables, compares them with the original tables, and regenerates the charts
in `charts/` (`salary_trend.svg`, `expenses_trend.svg`).

Two things worth knowing: salary matches the original tables exactly for
2020–2022 (2023 differs by $0.48, consistent with small revisions in the
live source). And 2022 expenses cannot be reproduced from the current file:
22 of the 35 filtered 2022 records have a blank expense, so the reproduced
mean rests on only 13 records — neither that mean ($322.38) nor treating
blanks as zero ($119.74) matches the original $242.91. Blank expenses are
skipped, never counted as zero.

## 🧪 Tests

```bash
pytest
```

Tests cover title normalisation (including the Journeyperson rename and the
excluded hyphen-less variant), the scope filter (department, title, year,
and dropping the name column), missing-expense handling (skipped, not zero;
all-missing gives no average, not zero), and yearly aggregation (means,
counts, and coverage of all years).

## 🧰 Tech Stack

- **AWS S3**: Cloud Storage
- **AWS Glue DataBrew**: Data Profiling & Cleaning
- **AWS Glue Catalog**: Metadata Management
- **AWS Glue ETL (Visual)**: Data Transformation
- **AWS Athena**: SQL querying
- **AWS KMS & IAM**: Encryption and access control
- **Amazon CloudWatch & CloudTrail**: Monitoring and audit logging
- **Python**: pandas, matplotlib (reproducible analysis and charts)

The full AWS platform walkthrough — ingestion, profiling, cleaning,
cataloging, summarization, security, governance, monitoring, architecture,
and the evaluation against AWS Operational Excellence principles — lives in
[docs/aws-walkthrough.md](docs/aws-walkthrough.md).

## 📁 Project Structure

```
.
├── analysis.py            # Reproducible yearly analysis + charts
├── charts/                # salary_trend.svg, expenses_trend.svg
├── docs/
│   └── aws-walkthrough.md # Full AWS platform walkthrough
├── tests/
│   └── test_analysis.py   # Tests for filtering, normalisation, expenses, aggregation
├── requirements.txt
└── LICENSE
```

## 🚀 Future Enhancements

- Integrate with AWS Athena or QuickSight for real-time querying & dashboards
- Incorporate API data sources
- Schedule automated jobs using AWS Lambda

## 📌 License

This project is licensed under the Creative Commons
Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0) — see
[LICENSE](LICENSE). It is for academic demonstration purposes; no
commercial use allowed.

## 🧑‍💼 Author

**Emmanuel Kweku Benyi**
MBA, data analytics, University Canada West (2025) | Data Enthusiast |
Cloud Analytics Developer

- Email: emmanuel_benyi@yahoo.com
- LinkedIn: https://www.linkedin.com/in/emmanuelbenyi
