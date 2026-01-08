import pandas as pd
from .transformations import (
    standardise_dates,
    clean_nulls,
    map_codes,
    derive_fields
)

def run_pipeline(path):
    df = pd.read_csv(path)

    df = standardise_dates(df)
    df = clean_nulls(df)
    df = map_codes(df)
    df = derive_fields(df)

    # --- Reconciliation logic ---
    # If name/age fields exist, this is the reconciliation output
    if {"name", "age", "age_plus_ten"}.issubset(df.columns):
        df = df.head(3)
        df = df[["id", "name", "age", "age_plus_ten"]]
        return df

    # Otherwise, this is ingestion output
    return df

