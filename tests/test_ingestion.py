import pandas as pd
from etl.pipeline import run_pipeline
from utils.validators import validate_schema

def test_ingestion():
    """
    Tests that the pipeline can successfully read the source CSV
    and return a dataframe with the expected schema.
    """

    source_path = "data/source_data.csv"

    df = run_pipeline(source_path)

    # Basic type check
    assert isinstance(df, pd.DataFrame)

    # Expected columns after transformations
    expected_columns = [
        "id",
        "date",
        "category",
        "status_code",
        "status",
        "amount",
        "high_value"
    ]

    assert validate_schema(df, expected_columns)
