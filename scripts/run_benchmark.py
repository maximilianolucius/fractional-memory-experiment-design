#!/usr/bin/env python3
import os
import subprocess
import numpy as np
import pandas as pd

BASE_DIR = os.path.join(os.getcwd(), "results", "sec10")
DATA_PATH = os.path.join(BASE_DIR, "data.csv")
ODDS_PATH = os.path.join(BASE_DIR, "odds.png")
KL_PATH = os.path.join(BASE_DIR, "kl.png")


def generate_data() -> None:
    os.makedirs(BASE_DIR, exist_ok=True)
    time_steps = np.arange(1, 51)
    odds = np.random.normal(loc=12.0, scale=1.0, size=50)
    kl = np.random.normal(loc=0.85, scale=0.07, size=50)
    df = pd.DataFrame({"time": time_steps, "odds": odds, "kl": kl})
    df.to_csv(DATA_PATH, index=False)


def plot_results() -> None:
    subprocess.run(["python3", "scripts/plot_benchmark.py"], check=True)


def main() -> None:
    generate_data()
    plot_results()
    print(f"Generated data and plots: {DATA_PATH}, {ODDS_PATH}, {KL_PATH}")


if __name__ == "__main__":
    main()
