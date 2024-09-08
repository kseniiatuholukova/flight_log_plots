from warnings import warn

import pandas as pd
from typeguard import typechecked


class Binder:
    @typechecked
    def __init__(self, df: pd.DataFrame) -> None:
        """Initializes the Binder object"""
        self.df = df

    @typechecked
    def bind(self, col_x: str, col_y: str, col_z: str) -> pd.DataFrame:
        """Binds values in x and y columns based on z column"""
        for col in [col_x, col_y, col_z]:
            assert col in self.df.columns, f"Column {col} not found in the DataFrame"

        df1 = self.df[[col_z, col_x]].drop_duplicates()
        df2 = self.df[[col_z, col_y]].drop_duplicates()

        out_df = df1.merge(df2, on=col_z, how="outer").dropna()

        if out_df[col_y].nunique() < self.df[col_y].nunique():
            missing_values = list(set(self.df[col_y]) - set(out_df[col_y]))
            warn(
                f"Values {missing_values} cannot be bound to a certain {col_z} value "
                f"via {col_z}. Try binning {col_z} or setting a lower number of bins."
            )

        return out_df
