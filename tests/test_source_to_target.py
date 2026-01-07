import pandas as pd
from utils.validators import validate_source_to_target

def test_source_to_target_match():
    """
    Ensures that our source and target datasets match on key columns.
    """

    # Simulated source data
    source_df = pd.DataFrame({
        "id": [1, 2, 3],
        "value": ["A", "B", "C"]
    })

    # Simulated target data (matching)
    target_df = pd.DataFrame({
        "id": [1, 2, 3],
        "value": ["A", "B", "C"]
    })

    assert validate_source_to_target(source_df, target_df, ["id", "value"])


def test_source_to_target_mismatch():
    """
    Ensures that mismatched datasets fail validation.
    """
source_df = pd.DataFrame({
        "id": [1, 2, 3],
        "value": ["A", "B", "C"]
    })

    # Target has a mismatch on id=3
target_df = pd.DataFrame({
        "id": [1, 2, 3],
        "value": ["A", "B", "X"]
    })

    assert validate_source_to_target(source_df, target_df, ["id", "value"]) is False

