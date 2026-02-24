import pandas as pd


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing numerical values with median
    and categorical with mode.
    """
    for col in df.columns:
        if df[col].dtype == "object":
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    return df.drop_duplicates()