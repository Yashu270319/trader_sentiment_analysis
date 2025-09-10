import pandas as pd
def preprocess_trader_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleanup for trader dataset."""
    if 'Timestamp' in df.columns:
        ts = df['Timestamp'].astype(str).iloc[0]
        if len(ts) > 10:  # milliseconds
            df['date'] = pd.to_datetime(df['Timestamp'], unit='ms').dt.date
        else:  # seconds
            df['date'] = pd.to_datetime(df['Timestamp'], unit='s').dt.date
    elif 'Timestamp IST' in df.columns:
        df['date'] = pd.to_datetime(df['Timestamp IST']).dt.date
    else:
        raise ValueError("No valid timestamp column found in trader data.")
    return df


def preprocess_sentiment_data(df: pd.DataFrame) -> pd.DataFrame:
    """Format sentiment dataset."""
    if 'timestamp' in df.columns:
        ts = str(df['timestamp'].iloc[0])
        if len(ts) > 10:  # milliseconds
            df['date'] = pd.to_datetime(df['timestamp'], unit='ms').dt.date
        else:
            df['date'] = pd.to_datetime(df['timestamp'], unit='s').dt.date
    elif 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date']).dt.date
    else:
        raise ValueError("No valid date column found in sentiment data.")
    return df[['date', 'value', 'classification']]