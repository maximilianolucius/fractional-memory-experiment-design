#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.join(os.getcwd(), "results", "sec10")
DATA_PATH = os.path.join(BASE_DIR, "data.csv")
ODDS_PATH = os.path.join(BASE_DIR, "odds.png")
KL_PATH = os.path.join(BASE_DIR, "kl.png")


def plot() -> None:
    df = pd.read_csv(DATA_PATH)
    plt.figure(figsize=(6, 4))
    plt.plot(df["time"], df["odds"], marker="o", label="Posterior Odds")
    plt.xlabel("Time")
    plt.ylabel("Odds")
    plt.title("Posterior Odds over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(ODDS_PATH)
    plt.close()

    plt.figure(figsize=(6, 4))
    plt.plot(df["time"], df["kl"], marker="o", color="orange", label="KL Divergence")
    plt.xlabel("Time")
    plt.ylabel("KL")
    plt.title("Cumulative KL Divergence over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(KL_PATH)
    plt.close()


if __name__ == "__main__":
    plot()
