import pandas as pd
from typeguard import typechecked


@typechecked
def bin_data(data: pd.Series, n_bins: int, bin_size_max_limit: int = 100) -> pd.Series:
    """Bins values in a series into a specified number of bins"""
    assert (
        1 <= n_bins <= len(data)
    ), f"Invalid number of bins, should be between 1 and {len(data)}"

    bin_size = len(data) // n_bins
    if bin_size >= bin_size_max_limit:
        raise ValueError(
            f"You are creating {n_bins} bins with {bin_size_max_limit} datapoints in "
            "each. Consider increasing the number of bins to make them smaller and "
            "more meaningful."
        )

    print(f"{n_bins} bins created with {bin_size} datapoints in each.")

    return pd.cut(data, bins=n_bins).astype(str)
