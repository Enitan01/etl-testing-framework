import pandas as pd

def validate_schema(df: pd.DataFrame, expected_columns: list) -> bool:
    """
    Validates that the dataframe contains the expected columns.
    Order does not matter.
    """
    return set(df.columns) == set(expected_columns)


def validate_no_nulls(df: pd.DataFrame, columns: list) -> bool:
    """
    Ensures specified columns contain no null values.
    """
    return df[columns].isnull().sum().sum() == 0


def validate_unique(df: pd.DataFrame, column: str) -> bool:
    """
    Ensures a column contains unique values.
    """
    return df[column].is_unique


def validate_value_range(df: pd.DataFrame, column: str, min_val=None, max_val=None) -> bool:
    """
    Validates that values in a column fall within a specified range.
    """
    if min_val is not None and (df[column] < min_val).any():
        return False
    if max_val is not None and (df[column] > max_val).any():
        return False
    return True

def validate_source_to_target(source_df: pd.DataFrame, target_df: pd.DataFrame, key_columns: list) -> bool:
    """
    Validates that our source and target datasets match on key columns.
    Useful for source-to-target reconciliation tests.
    """
    merged = source_df.merge(target_df, on=key_columns, how='outer', indicator=True)
    return (merged['_merge'] == 'both').all()


