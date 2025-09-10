import pandas as pd

def load_trader_data(path: str) -> pd.DataFrame:
    """Load historical trader data (Hyperliquid style)."""
    return pd.read_csv(path)

def load_sentiment_data(path: str) -> pd.DataFrame:
    """Load Bitcoin Fear & Greed Index data."""
    return pd.read_csv(path)