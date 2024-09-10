from typing import Optional

import pandas as pd
import plotly.express as px
from typeguard import typechecked

from src.plotter.defaults import FileFormat


class Plotter:
    @typechecked
    def __init__(self, df: pd.DataFrame) -> None:
        """Initializes the Plotter object"""
        self.df = df

    @typechecked
    def plot(
        self,
        col_x: str,
        col_y: str,
        out_filepath: str,
        hover_data_col: Optional[str] = None,
        colorcode_col: Optional[str] = None,
        show_fig: bool = False,
    ) -> None:
        """Plots the data"""
        assert out_filepath.endswith(FileFormat.HTML), (
            f"Plots are saved in {FileFormat.HTML} format. Please provide a valid "
            "output filepath"
        )

        for col in [col_x, col_y, hover_data_col, colorcode_col]:
            if col is not None and col not in self.df.columns:
                raise ValueError(f"Column {col} not found in the DataFrame")

        print(f"Plotting... {col_y} vs {col_x}")

        if hover_data_col is not None and colorcode_col is not None:
            fig = px.scatter(
                self.df,
                x=col_x,
                y=col_y,
                hover_data=[hover_data_col],
                color=colorcode_col,
            )

        elif hover_data_col is not None and colorcode_col is None:
            fig = px.scatter(
                self.df,
                x=col_x,
                y=col_y,
                hover_data=[hover_data_col],
            )

        elif hover_data_col is None and colorcode_col is not None:
            fig = px.scatter(
                self.df,
                x=col_x,
                y=col_y,
                color=colorcode_col,
            )

        else:
            fig = px.scatter(
                self.df,
                x=col_x,
                y=col_y,
            )

        if show_fig:
            fig.show()

        fig.write_html(out_filepath)

        print(f"Plot saved at: {out_filepath}")
