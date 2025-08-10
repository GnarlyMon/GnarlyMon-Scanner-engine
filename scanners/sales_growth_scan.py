import csv
import random

def read_tickers(filepath):
    with open(filepath, 'r') as f:
        return [row[0] for row in csv.reader(f)][1:]  # Skip header

def mock_sales_data():
    # Simulate 3 quarters of sales (in millions)
    return [round(random.uniform(100, 200), 2) for _ in range(3)]

def has_growth(sales):
    # Check for sequential growth: Q1 < Q2 < Q3
    return sales[2] > sales[1] > sales[0]

def run_scan():
    tickers = read_tickers('data/tickers.csv')
    results = []

    for ticker in tickers:
        sales = mock_sales_data()
        if has_growth(sales):
            results.append([ticker] + sales)

    output_path = 'output/sales_growth_results.csv'
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Ticker', 'Q1 Sales', 'Q2 Sales', 'Q3 Sales'])
        writer.writerows(results)

    print(f"{len(results)} tickers showed sales growth. Results saved to {output_path}")

if __name__ == "__main__":
    run_scan()
