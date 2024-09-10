from typing import Optional
from warnings import warn

import pandas as pd
from typeguard import typechecked


class Binder:
    @typechecked
    def __init__(self, df: pd.DataFrame) -> None:
        """Initializes the Binder object"""
        self.df = df

    @typechecked
    def bind(
        self,
        col_x: str,
        col_y: str,
        col_to_bind_by: str,
        colorcode_col: Optional[str] = None,
    ) -> pd.DataFrame:
        """Binds values in x and y columns based on z column"""
        for col in [col_x, col_y, col_to_bind_by, colorcode_col]:
            if col is not None and col not in self.df.columns:
                raise ValueError(f"Column {col} not found in the DataFrame")

        if colorcode_col is not None:
            cols_df_1 = [col_to_bind_by, col_x, colorcode_col]

        else:
            cols_df_1 = [col_to_bind_by, col_x]

        # Create unique combinations of col_to_bind_by with col_x and col_y
        # Colorcode column is added (if provided) to the first binding
        df1 = self.df[cols_df_1].drop_duplicates()
        df2 = self.df[[col_to_bind_by, col_y]].drop_duplicates()

        # Merge unique combinations where col_to_bind_by is the same
        out_df = df1.merge(df2, on=col_to_bind_by, how="inner")

        # Compare the resulting datframe with the original one. If any of the col_y
        # values are missing because there is not a relevant binding value, warn
        # the user
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
