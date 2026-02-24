import pandas as pd


def encode_categorical(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform one-hot encoding for categorical features.
    """
    return pd.get_dummies(df, drop_first=True)


def create_interaction_feature(df: pd.DataFrame, col1: str, col2: str) -> pd.DataFrame:
    """
    Create interaction feature between two numeric columns.
    """
    df[f"{col1}_{col2}_interaction"] = df[col1] * df[col2]
    return df