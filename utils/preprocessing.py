import pandas as pd


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing numerical values with median
    and categorical with mode.
    """
    for col in df.columns:
        series = df[col]
        if series.dtype == "object":
            mode_values = series.mode(dropna=True)
            fill_value = mode_values.iloc[0] if not mode_values.empty else "Unknown"
            df[col] = series.fillna(fill_value)
        else:
            non_null_values = series.dropna()
            fill_value = non_null_values.median() if not non_null_values.empty else 0
            df[col] = series.fillna(fill_value)
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    return df.drop_duplicates()
