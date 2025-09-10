import pandas as pd

def merge_datasets(traders: pd.DataFrame, sentiment: pd.DataFrame) -> pd.DataFrame:
    """Merge trader and sentiment data on date."""
    merged = pd.merge(traders, sentiment, on="date", how="inner")
    return merged

def daily_summary(merged: pd.DataFrame) -> pd.DataFrame:
    """Aggregate trades by day."""
    grouped = merged.groupby(['date', 'classification']).agg(
        total_closed_pnl=('Closed PnL', 'sum'),
        trades=('Account', 'count'),
        Avg_price = ('Size USD', 'mean')
    ).reset_index()
    return grouped

def sentiment_insights(summary: pd.DataFrame) -> pd.DataFrame:
    """Get median/mean stats by sentiment classification."""
    return summary.groupby('classification').agg(
        median_pnl=('total_closed_pnl', 'median'),
        mean_pnl=('total_closed_pnl', 'mean'),
        avg_trades=('trades', 'mean')
    ).reset_index()