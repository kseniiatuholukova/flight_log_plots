import pandas as pd
from typeguard import typechecked


@typechecked
def bin_data(data: pd.Series, n_bins: int) -> pd.Series:
    """Bins values in a series into a specified number of bins"""
    assert (
        1 <= n_bins <= len(data)
    ), f"Invalid number of bins, should be between 1 and {len(data)}"

    return pd.cut(data, bins=n_bins).astype(str)
