import pandas as pd
from utils.validators import (
    validate_no_nulls,
    validate_unique,
    validate_value_range
)

def test_no_nulls():
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "amount": [10, 20, 30]
    })

    assert validate_no_nulls(df, ["id", "amount"])


def test_unique_ids():
    df = pd.DataFrame({
        "id": [1, 2, 3, 3],   # duplicate on purpose
        "value": [10, 20, 30, 40]
    })

    assert validate_unique(df, "id") is False


def test_value_range():
    df = pd.DataFrame({
        "amount": [5, 10, 15]
    })

    assert validate_value_range(df, "amount", min_val=0, max_val=20)
