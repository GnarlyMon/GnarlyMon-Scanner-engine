import csv
import random

def read_tickers(filepath):
    with open(filepath, 'r') as f:
        return [row[0] for row in csv.reader(f)][1:]  # Skip header

def mock_price_data(ticker):
    # Simulate 90 days of prices between $90 and $110
    return [round(random.uniform(90, 110), 2) for _ in range(90)]

def is_90_day_low(prices):
    # Check if the latest price is the lowest in the last 90 days
    return prices[-1] == min(prices)

def run_scan():
    tickers = read_tickers('data/tickers.csv')
    results = []

    for ticker in tickers:
        prices = mock_price_data(ticker)
        if is_90_day_low(prices):
            results.append([ticker, prices[-1]])

    output_path = 'output/breakdown_results.csv'
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Ticker', 'Latest Price'])
        writer.writerows(results)

    print(f"{len(results)} tickers hit 90-day lows. Results saved to {output_path}")

if __name__ == "__main__":
    run_scan()
