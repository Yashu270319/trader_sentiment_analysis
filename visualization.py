import matplotlib.pyplot as plt
import pandas as pd

def plot_pnl_distribution(summary: pd.DataFrame, save_path: str):
    plt.figure(figsize=(8,5))
    summary.boxplot(column='total_closed_pnl', by='classification')
    plt.title("PnL distribution by Sentiment")
    plt.suptitle("")
    plt.xlabel("Sentiment")
    plt.ylabel("Closed PnL")
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()

def plot_trades_per_sentiment(summary: pd.DataFrame, save_path: str):
    plt.figure(figsize=(8,5))
    summary.groupby('classification')['trades'].sum().plot(kind='bar')
    plt.title("Number of Trades per Sentiment")
    plt.ylabel("Trades")
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()