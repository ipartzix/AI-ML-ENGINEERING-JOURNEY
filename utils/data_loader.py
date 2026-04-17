import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    Args:

        file_path (str): Path to the CSV file.
    Returns:

        pd.DataFrame: Loaded dataset.
    """
    try:
        df = pd.read_csv(file_path)

        print(f"Data loaded successfully. Shape: {df.shape} - data_loader.py:16")
        
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading file: {e}")
