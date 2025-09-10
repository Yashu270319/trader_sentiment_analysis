import os
from data_loader import load_trader_data, load_sentiment_data
from preprocessing import preprocess_trader_data, preprocess_sentiment_data
from analysis import merge_datasets, daily_summary, sentiment_insights
from visualization import plot_pnl_distribution, plot_trades_per_sentiment

def main():
    # File paths (adjust to your structure)
    trader_path = "data/historical_data.csv"
    sentiment_path = "data/fear_greed_index.csv"
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    # Load
    traders = load_trader_data(trader_path)
    sentiment = load_sentiment_data(sentiment_path)

    # Preprocess
    traders = preprocess_trader_data(traders)
    sentiment = preprocess_sentiment_data(sentiment)

    # Merge + summarize
    merged = merge_datasets(traders, sentiment)
    daily = daily_summary(merged)
    insights = sentiment_insights(daily)

    # Save insights
    daily.to_csv(os.path.join(results_dir, "daily_summary.csv"), index=False)
    insights.to_csv(os.path.join(results_dir, "sentiment_insights.csv"), index=False)

    # Visualize
    plot_pnl_distribution(daily, os.path.join(results_dir, "pnl_distribution.png"))
    plot_trades_per_sentiment(daily, os.path.join(results_dir, "trades_per_sentiment.png"))

if __name__ == "__main__":
    main()