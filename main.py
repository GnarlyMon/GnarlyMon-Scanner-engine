import os
from scans import scan_momentum, scan_growth, scan_downside  # adjust to match your module names

def run_all_scans():
    print("Running momentum scan...")
    scan_momentum.run()

    print("Running growth scan...")
    scan_growth.run()

    print("Running downside scan...")
    scan_downside.run()

if __name__ == "__main__":
    run_all_scans()
