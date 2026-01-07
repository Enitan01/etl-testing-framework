import pandas as pd

def standardise_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts date columns to a standard YYYY-MM-DD format.
    Assumes a column named 'date' exists in the dataset.
    """
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')
    return df


def clean_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans null values by replacing them with defaults.
    Example: replace missing 'category' with 'Unknown'.
    """
    if 'category' in df.columns:
        df['category'] = df['category'].fillna('Unknown')
    return df


def map_codes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps raw codes to human-readable labels.
    Example: 1 -> 'Active', 0 -> 'Inactive'
    """
    if 'status_code' in df.columns:
        mapping = {1: 'Active', 0: 'Inactive'}
        df['status'] = df['status_code'].map(mapping)
    return df


def derive_fields(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates derived fields based on business logic.
    Example: flag records where amount > 100.
    """
    if 'amount' in df.columns:
        df['high_value'] = df['amount'] > 100
    return df



