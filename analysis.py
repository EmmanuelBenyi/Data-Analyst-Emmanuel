"""Reproduce the README's yearly averages for City of Vancouver employees
in Engineering Services with the title Journeyman - Mechanic, 2020-2023.

Source (City of Vancouver Open Data Portal, public open data):
  Dataset page:
    https://opendata.vancouver.ca/explore/dataset/employee-remuneration-and-expenses-earning-over-75000/
  CSV export used by this script (Opendatasoft v2.1 API):
    https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/employee-remuneration-and-expenses-earning-over-75000/exports/csv?lang=en&timezone=America%2FVancouver

  The live file is semicolon-delimited, UTF-8 with a BOM, with columns
  year, name, department, title, remuneration, expenses.

Scope and filter (exactly as documented in the README):
  * department, case-insensitively and after stripping whitespace, is
    "Engineering Services";
  * title, case-insensitively and after stripping whitespace, is
    "Journeyman - Mechanic". The post-2023 rename to "Journeyperson -
    Mechanic" is normalised to the same value, but it does not affect
    2020-2023 (no Journeyperson rows occur in those years). The
    hyphen-less variant "Journeyman Mechanic" (one record per year) is
    NOT included: the README's 508-record total for 2008-2023 is matched
    only by the hyphenated title, and its salary figures are matched
    exactly on that basis (see notes printed by this script).
  * year is 2020, 2021, 2022 or 2023.

  The live dataset has since grown beyond the README's scope (it now
  runs to 2025); filtering to 2020-2023 keeps the comparison like-for-like.

AGGREGATE ONLY: the source file contains an employee-name column.
This script drops that column immediately after loading and never
prints, saves, or charts any individual-level row. Every output below
is a yearly average (plus record counts, so denominators are visible).

Expenses and missing values: yearly average expenses are computed with
pandas' default mean, which skips blank (missing) expense values rather
than treating them as zero. This matters for 2022, where 22 of the 35
filtered records have a blank expense in the live file, so the 2022
average expenses rest on only 13 records. The script prints the
non-blank count alongside each average so that denominator is explicit.
Treating blanks as zero instead would give 119.74 for 2022; neither
figure reproduces the README's 2022 expenses value of 242.91 (see the
comparison printed at the end of the run).

Usage:
  python3 analysis.py
Requires: pandas, matplotlib. No other files are needed: the dataset
is downloaded from the public URL above at run time, and the raw CSV
is never written to disk. Charts are written as SVG (text) files to
charts/salary_trend.svg and charts/expenses_trend.svg next to this script.
"""

import io
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

DATASET_URL = (
    "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/"
    "employee-remuneration-and-expenses-earning-over-75000/exports/csv"
    "?lang=en&timezone=America%2FVancouver"
)
DATASET_PAGE = (
    "https://opendata.vancouver.ca/explore/dataset/"
    "employee-remuneration-and-expenses-earning-over-75000/"
)

DEPARTMENT = "engineering services"
TITLE = "journeyman - mechanic"
YEARS = [2020, 2021, 2022, 2023]

# README values, for the comparison printed at the end (not used in any
# computation). The README expenses table has no 2021 row.
README_SALARY = {2020: 90229.38, 2021: 94910.93, 2022: 97236.69, 2023: 103556.73}
README_EXPENSES = {2020: 75.14, 2022: 242.91, 2023: 89.91}


def normalise_title(value: str) -> str:
    """Lower-case, strip, and map the post-2023 'journeyperson' rename."""
    return str(value).strip().lower().replace("journeyperson", "journeyman")


def load_and_filter(url: str) -> pd.DataFrame:
    """Download the CSV, drop the name column, and apply the scope filter."""
    with urllib.request.urlopen(url) as response:
        raw = response.read()
    df = pd.read_csv(io.BytesIO(raw), sep=";", encoding="utf-8-sig")
    # Aggregate only: discard individual identifiers before any analysis.
    df = df.drop(columns=["name"], errors="ignore")
    filtered = df[
        (df["department"].astype(str).str.strip().str.lower() == DEPARTMENT)
        & (df["title"].map(normalise_title) == TITLE)
        & (df["year"].isin(YEARS))
    ].copy()
    return filtered


def yearly_averages(filtered: pd.DataFrame) -> pd.DataFrame:
    """Yearly record counts and mean remuneration / mean expenses."""
    summary = (
        filtered.groupby("year")
        .agg(
            records=("remuneration", "size"),
            records_with_expenses=("expenses", "count"),
            avg_remuneration=("remuneration", "mean"),
            avg_expenses=("expenses", "mean"),
        )
        .reindex(YEARS)
        .reset_index()
    )
    return summary


def save_chart(summary: pd.DataFrame, column: str, title: str, path: Path) -> None:
    """Save a yearly trend line chart as SVG (UTF-8 text, not PNG)."""
    fig, ax = plt.subplots()
    ax.plot(summary["year"], summary[column], marker="o")
    for year, value in zip(summary["year"], summary[column]):
        ax.annotate(f"{value:,.2f}", (year, value), textcoords="offset points",
                    xytext=(0, 8), ha="center")
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel("CAD")
    ax.set_xticks(summary["year"])
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, format="svg")
    plt.close(fig)


def main() -> None:
    print(f"Dataset page: {DATASET_PAGE}")
    print(f"CSV download: {DATASET_URL}")
    filtered = load_and_filter(DATASET_URL)
    summary = yearly_averages(filtered)

    print("\nFilter: department = Engineering Services, "
          "title = Journeyman - Mechanic, years 2020-2023")
    print(f"Filtered records, 2020-2023: {len(filtered)}")
    print("\nAverage remuneration (CAD) by year:")
    print(summary[["year", "records", "avg_remuneration"]]
          .to_string(index=False, float_format=lambda v: f"{v:,.2f}"))
    print("\nAverage expenses (CAD) by year "
          "(blank expenses skipped, not counted as zero):")
    print(summary[["year", "records", "records_with_expenses", "avg_expenses"]]
          .to_string(index=False, float_format=lambda v: f"{v:,.2f}"))

    charts_dir = Path(__file__).resolve().parent / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)
    salary_path = charts_dir / "salary_trend.svg"
    expenses_path = charts_dir / "expenses_trend.svg"
    save_chart(summary, "avg_remuneration",
               "Average remuneration — Engineering Services, "
               "Journeyman - Mechanic (CAD)", salary_path)
    save_chart(summary, "avg_expenses",
               "Average expenses — Engineering Services, "
               "Journeyman - Mechanic (CAD)", expenses_path)
    print(f"\nCharts written: {salary_path}\n                {expenses_path}")

    print("\nComparison with the README tables (reproduced minus README):")
    for _, row in summary.iterrows():
        year = int(row["year"])
        sal_diff = row["avg_remuneration"] - README_SALARY[year]
        print(f"  {year} salary:   reproduced {row['avg_remuneration']:,.2f} "
              f"vs README {README_SALARY[year]:,.2f} "
              f"(difference {sal_diff:+,.2f})")
        if year in README_EXPENSES:
            exp_diff = row["avg_expenses"] - README_EXPENSES[year]
            print(f"  {year} expenses: reproduced {row['avg_expenses']:,.2f} "
                  f"vs README {README_EXPENSES[year]:,.2f} "
                  f"(difference {exp_diff:+,.2f})")
        else:
            print(f"  {year} expenses: reproduced {row['avg_expenses']:,.2f} "
                  f"vs README (no row published for this year)")


if __name__ == "__main__":
    main()
