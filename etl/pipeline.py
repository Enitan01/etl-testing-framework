import pandas as pd
from .transformations import (
    standardise_dates,
    clean_nulls,
    map_codes,
    derive_fields
)


def run_pipeline(path):
    # Ingestion
    df = pd.read_csv(path)

    # Transformations
    df = standardise_dates(df)
    df = clean_nulls(df)
    df = map_codes(df)
    df = derive_fields(df)

    # Keep only the expected columns
    df = df[["id", "name", "age", "age_plus_ten"]]

    return df
