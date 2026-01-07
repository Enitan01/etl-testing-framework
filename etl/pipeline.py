import pandas as pd
from .transformations import (
    standardise_dates,
    clean_nulls,
    map_codes,
    derive_fields
)

def run_pipeline(source_path: str) -> pd.DataFrame:
    """
    Simulates a simple ETL pipeline:
    1. Read raw source data
    2. Apply transformation functions
    3. Return curated dataframe
    """

    # Ingestion
    df = pd.read_csv(source_path)

    # Transformations
    df = standardise_dates(df)
    df = clean_nulls(df)
    df = map_codes(df)
    df = derive_fields(df)

    return df


