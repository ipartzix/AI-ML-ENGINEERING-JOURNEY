import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder


def load_csv(path):
    """Load CSV file into a DataFrame."""
    return pd.read_csv(path)


def encode_labels(df, column):
    """Encode categorical labels as integers."""
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    return df, le


def _build_scaler(method='standard'):
    if method == 'standard':
        return StandardScaler()
    elif method == 'minmax':
        return MinMaxScaler()
    else:
        raise ValueError("method must be 'standard' or 'minmax'")


def fit_scaler(X_train, method='standard'):
    """Fit a scaler on training features only."""
    scaler = _build_scaler(method)
    scaler.fit(X_train)
    return scaler


def transform_features(X, scaler):
    """Transform features using a pre-fitted scaler."""
    return scaler.transform(X)


def scale_train_test(X_train, X_test, method='standard'):
    """Scale train/test without leakage (fit on train, transform both)."""
    scaler = fit_scaler(X_train, method=method)
    X_train_scaled = transform_features(X_train, scaler)
    X_test_scaled = transform_features(X_test, scaler)
    return X_train_scaled, X_test_scaled, scaler


def scale_features(X, method='standard'):
    """
    Backward-compatible helper that fits and transforms a single dataset.

    Note:
        Use `scale_train_test` after splitting to avoid train-test leakage.
    """
    scaler = fit_scaler(X, method=method)
    X_scaled = transform_features(X, scaler)
    return X_scaled, scaler


def split_data(X, y, test_size=0.2, random_state=42):
    """Split features and labels into training and test sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
