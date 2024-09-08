from warnings import warn

import pandas as pd
from typeguard import typechecked


class Binder:
    @typechecked
    def __init__(self, df: pd.DataFrame) -> None:
        """Initializes the Binder object"""
        self.df = df

    @typechecked
    def bind(self, col_x: str, col_y: str, col_to_bind_by: str) -> pd.DataFrame:
        """Binds values in x and y columns based on z column"""
        for col in [col_x, col_y, col_to_bind_by]:
            assert col in self.df.columns, f"Column {col} not found in the DataFrame"

        df1 = self.df[[col_to_bind_by, col_x]].drop_duplicates()
        df2 = self.df[[col_to_bind_by, col_y]].drop_duplicates()

        out_df = df1.merge(df2, on=col_to_bind_by, how="outer").dropna()

        if out_df[col_y].nunique() < self.df[col_y].nunique():
            missing_values = list(
                set(self.df[col_y].dropna()) - set(out_df[col_y].dropna())
            )
            warn(
                f"{missing_values} {col_y} values cannot be bound to a certain {col_x} "
                f"value via the third variable. Try binning the third variable or set "
                "a lower number of bins."
            )

        return out_df
