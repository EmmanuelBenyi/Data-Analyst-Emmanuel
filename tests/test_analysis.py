"""Tests for analysis.py.

Pure functions only: no network access, no files written. Synthetic
frames stand in for the City of Vancouver open-data CSV.
"""
import math

import pandas as pd
import pytest

from analysis import YEARS, apply_filter, normalise_title, yearly_averages

COLUMNS = ["name", "department", "title", "year", "remuneration", "expenses"]


def make_frame(rows):
    """Build a frame with the dataset's columns from dict rows."""
    return pd.DataFrame(rows, columns=COLUMNS)


def matching_row(**overrides):
    row = {
        "name": "Doe, Jane",
        "department": "Engineering Services",
        "title": "Journeyman - Mechanic",
        "year": 2020,
        "remuneration": 90000.0,
        "expenses": 100.0,
    }
    row.update(overrides)
    return row


# --- Title normalisation -------------------------------------------------


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("Journeyman - Mechanic", "journeyman - mechanic"),
        ("  Journeyman - Mechanic  ", "journeyman - mechanic"),
        ("JOURNEYMAN - MECHANIC", "journeyman - mechanic"),
        ("Journeyperson - Mechanic", "journeyman - mechanic"),
        ("Journeyperson - mechanic", "journeyman - mechanic"),
        ("Journeyman Mechanic", "journeyman mechanic"),
    ],
)
def test_normalise_title(raw, expected):
    assert normalise_title(raw) == expected


# --- Filtering ------------------------------------------------------------


def test_filter_keeps_only_scope_rows():
    frame = make_frame(
        [
            matching_row(),  # kept
            matching_row(department="  ENGINEERING SERVICES  "),  # kept: case/space-insensitive
            matching_row(title="Journeyperson - Mechanic"),  # kept: post-2023 rename normalised
            matching_row(title="Journeyman Mechanic"),  # excluded: hyphen-less variant
            matching_row(department="Parks and Recreation"),  # excluded: wrong department
            matching_row(year=2024),  # excluded: outside 2020-2023
            matching_row(year=2019),  # excluded: outside 2020-2023
        ]
    )
    filtered = apply_filter(frame)
    assert len(filtered) == 3
    assert set(filtered["title"].map(normalise_title)) == {"journeyman - mechanic"}
    assert set(filtered["year"]) == {2020}


def test_filter_drops_name_column():
    """Aggregate only: individual identifiers must not survive filtering."""
    filtered = apply_filter(make_frame([matching_row()]))
    assert "name" not in filtered.columns


# --- Missing expenses ------------------------------------------------------


def test_missing_expenses_skipped_not_zero():
    """Blank expenses are skipped by the mean, not treated as zero."""
    frame = make_frame(
        [
            matching_row(year=2020, remuneration=90000.0, expenses=200.0),
            matching_row(year=2020, remuneration=100000.0, expenses=float("nan")),
        ]
    )
    summary = yearly_averages(apply_filter(frame))
    row_2020 = summary[summary["year"] == 2020].iloc[0]
    assert row_2020["records"] == 2
    assert row_2020["records_with_expenses"] == 1
    assert row_2020["avg_expenses"] == pytest.approx(200.0)
    assert row_2020["avg_remuneration"] == pytest.approx(95000.0)


def test_all_expenses_missing_gives_nan_not_zero():
    frame = make_frame([matching_row(year=2021, expenses=float("nan"))])
    summary = yearly_averages(apply_filter(frame))
    row_2021 = summary[summary["year"] == 2021].iloc[0]
    assert row_2021["records_with_expenses"] == 0
    assert math.isnan(row_2021["avg_expenses"])


# --- Yearly aggregation ----------------------------------------------------


def test_yearly_aggregation_means_and_counts():
    frame = make_frame(
        [
            matching_row(year=2020, remuneration=90000.0, expenses=100.0),
            matching_row(year=2020, remuneration=100000.0, expenses=300.0),
            matching_row(year=2021, remuneration=80000.0, expenses=50.0),
        ]
    )
    summary = yearly_averages(apply_filter(frame))
    row_2020 = summary[summary["year"] == 2020].iloc[0]
    row_2021 = summary[summary["year"] == 2021].iloc[0]
    assert row_2020["records"] == 2
    assert row_2020["avg_remuneration"] == pytest.approx(95000.0)
    assert row_2020["avg_expenses"] == pytest.approx(200.0)
    assert row_2021["records"] == 1
    assert row_2021["avg_remuneration"] == pytest.approx(80000.0)


def test_yearly_aggregation_covers_all_years():
    """Years with no rows still appear (reindexed to YEARS)."""
    frame = make_frame([matching_row(year=2020)])
    summary = yearly_averages(apply_filter(frame))
    assert list(summary["year"]) == YEARS
    # A year with no rows appears with missing (NaN) aggregates, not zeros.
    row_2023 = summary[summary["year"] == 2023].iloc[0]
    assert math.isnan(row_2023["records"])
    assert math.isnan(row_2023["avg_remuneration"])
