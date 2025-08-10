import csv
import random
from datetime import datetime

def read_tickers(filepath):
    with open(filepath, 'r') as f:
        return [row[0] for row in csv.reader(f)][1:]  # Skip header

def mock_price_data(ticker):
    # Simulate 30 days of prices between $90 and $110
    return [round(random.uniform(90, 110), 2) for _ in range(30)]

def is_new_high(prices):
    # Check if the latest price is the highest in the last 30 days
    return prices[-1] == max(prices)

def run_scan():
    tickers = read_tickers('data/tickers.csv')
    results = []

    for ticker in tickers:
        prices = mock_price_data(ticker)
        if is_new_high(prices):
            results.append([ticker, prices[-1]])

    output_path = 'output/highs_results.csv'
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Ticker', 'Latest Price'])
        writer.writerows(results)

    print(f"{len(results)} tickers hit new highs. Results saved to {output_path}")

if __name__ == "__main__":
    run_scan()
