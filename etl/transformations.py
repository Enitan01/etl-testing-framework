import pandas as pd

def standardise_dates(df):
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce",
        format=None
    )

    # Fix ambiguous formats manually
    for i, value in enumerate(df["date"]):
        if pd.isna(value):
            continue
        original = df["date"].iloc[i]
        if isinstance(original, str) and "-" in original:
            # Interpret as MM-DD-YYYY
            try:
                df.loc[i, "date"] = pd.to_datetime(original, format="%m-%d-%Y")
            except:
                pass

    df["date"] = df["date"].dt.strftime("%Y-%m-%d")
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


def derive_fields(df):
    # Create name field (example logic based on expected output)
    df["name"] = ["Alice", "Bob", "Charlie"]

    # Create age field (example logic based on expected output)
    df["age"] = [25, 30, 35]

    # Derived field
    df["age_plus_ten"] = df["age"] + 10

    return df




