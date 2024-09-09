from warnings import warn

import pandas as pd
from typeguard import typechecked


@typechecked
def bin_data(data: pd.Series, bin_size: int = 5) -> pd.Series:
    """Bins values in a series into a specified number of bins"""
    assert (
        1 <= bin_size <= len(data)
    ), f"Invalid bin_size, should be between 1 and {len(data)}"

    n_bins = len(data) // bin_size

    if bin_size >= 100:
        warn(
            f"You are creating {n_bins} bins with {bin_size} datapoints in each. "
            "Consider reducing bin size to make the bins more meaningful."
        )

    bins = pd.cut(data, bins=n_bins).astype(str)

    print(f"{n_bins} bins created with {bin_size} datapoints in each.")

    return bins
