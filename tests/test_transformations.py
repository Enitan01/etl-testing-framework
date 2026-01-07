import pandas as pd
from etl.transformations import (
    standardise_dates,
    clean_nulls,
    map_codes,
    derive_fields
)

def test_standardise_dates():
    df = pd.DataFrame({
        "date": ["2024/01/01", "01-02-2024", None]
    })

    result = standardise_dates(df)

    # All values should be converted to YYYY-MM-DD or NaT
    assert result["date"].iloc[0] == "2024-01-01"
    assert result["date"].iloc[1] == "2024-01-02"
    assert result["date"].iloc[2] is None or pd.isna(result["date"].iloc[2])


def test_clean_nulls():
    df = pd.DataFrame({
        "category": ["A", None, "B"]
    })

    result = clean_nulls(df)

    assert result["category"].tolist() == ["A", "Unknown", "B"]


def test_map_codes():
    df = pd.DataFrame({
        "status_code": [1, 0, 1]
      })

    result = map_codes(df)

    assert result["status"].tolist() == ["Active", "Inactive", "Active"]


def test_derive_fields():
    df = pd.DataFrame({
        "amount": [50, 150, 200]
    })

    result = derive_fields(df)

    assert result["high_value"].tolist() == [False, True, True]


