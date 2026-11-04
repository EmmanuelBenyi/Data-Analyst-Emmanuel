"""Pytest configuration: make the repository root importable.

`analysis.py` lives at the repo root, so tests import it from there
regardless of the directory pytest is run from.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
