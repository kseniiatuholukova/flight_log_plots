import numpy as np
import pandas as pd

# Number of rows
N_ROWS = 10000

np.random.seed(0)

# Column 0: Timestamps, continuous but with uneven intervals
start_time = pd.Timestamp("2023-01-01")
time_deltas = np.random.exponential(
    scale=3600, size=N_ROWS
).cumsum()  # Exponentially distributed intervals
timestamps = start_time + pd.to_timedelta(time_deltas, unit="s")

# Column 1: capybara (float between 20 and 80), 80% of rows filled, rest NaN
capybara = np.random.uniform(20, 80, int(N_ROWS * 0.8))
capybara = np.concatenate([capybara, [np.nan] * int(N_ROWS * 0.2)])
np.random.shuffle(capybara)

# Column 2: fox (float, normal distribution, mean 15, stdev 5), 90% filled, rest NaN
fox = np.random.normal(15, 5, int(N_ROWS * 0.9))
fox = np.concatenate([fox, [np.nan] * int(N_ROWS * 0.1)])
np.random.shuffle(fox)

# Column 3: opossum (float between 30 and 40, uniform)
opossum = np.linspace(30, 40, N_ROWS)

# Column 4: otter (float between 2 and 22, random, repeating at least 20 times),
unique_otter = np.random.uniform(2, 22, N_ROWS)
otter = np.repeat(unique_otter, 20)[:N_ROWS]  # Ensure each value repeats 20 times

# Creating the DataFrame
df_synthetic = pd.DataFrame(
    {
        "timestamp": timestamps,
        "capybara": capybara,
        "fox": fox,
        "opossum": opossum,
        "otter": otter,
    }
)

# make opossum and otter columns sorted
df_synthetic["opossum"] = np.sort(df_synthetic["opossum"])
df_synthetic["otter"] = np.sort(df_synthetic["otter"])

# Making opossum and otter data more sparse (by 50% and 30% respectively)
nan_indices_opossum = np.random.choice(
    df_synthetic.index, size=int(0.5 * N_ROWS), replace=False
)
df_synthetic.iloc[nan_indices_opossum, 3] = np.nan

nan_indices_otter = np.random.choice(
    df_synthetic.index, size=int(0.3 * N_ROWS), replace=False
)
df_synthetic.iloc[nan_indices_otter, 4] = np.nan

df_synthetic["mode"] = np.concatenate(
    [
        ["auto"] * int(N_ROWS // 5),
        ["hyjavto"] * int(N_ROWS // 2.5),
        ["bizhymo tudy!"] * int(N_ROWS // 3),
        ["de ja nahuj?"]
        * int(N_ROWS - (N_ROWS // 5) - (N_ROWS // 2.5) - (N_ROWS // 3)),
    ]
)

df_synthetic.to_csv("./synthetic_data/synthetic_data.csv", index=False)
