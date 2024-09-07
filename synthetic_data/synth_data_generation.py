import numpy as np
import pandas as pd

# Number of rows
N_ROWS = 10000

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

# Column 2: fox (float between 5 and 25, normal distribution), 90% filled, rest NaN
fox = np.random.normal(15, 5, int(N_ROWS * 0.9))
fox = np.clip(fox, 5, 25)  # Limiting fox to the range [5, 25]
fox = np.concatenate([fox, [np.nan] * int(N_ROWS * 0.1)])
np.random.shuffle(fox)

# Column 3: opossum (float between 30 and 40, uniform, increasing), 50% filled, rest NaN
opossum = np.linspace(30, 40, int(N_ROWS * 0.5))
opossum = np.concatenate([opossum, [np.nan] * int(N_ROWS * 0.5)])
np.random.shuffle(opossum)

# Column 4: otter (float between 2 and 22, random, repeating at least 20 times),
# 70% filled, rest NaN
unique_otter = np.random.uniform(2, 22, int(N_ROWS / 20))
otter = np.repeat(unique_otter, 20)[
    : int(N_ROWS * 0.7)
]  # Ensure each value repeats 20 times
otter = np.concatenate([otter, [np.nan] * int(N_ROWS * 0.3)])
np.random.shuffle(otter)

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

df_synthetic.to_csv("./synthetic_data/synthetic_data.csv", index=False)
