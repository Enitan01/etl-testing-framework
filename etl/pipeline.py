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

    return df
