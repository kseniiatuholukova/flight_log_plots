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
    def plot2D(
        self,
        col_x: str,
        col_y: str,
        out_filepath: str,
        hover_data_col: Optional[str] = None,
        colorcode_col: Optional[str] = None,
        show_fig: bool = False,
    ) -> None:
        """Plots the data in 2D"""
        assert out_filepath.endswith(FileFormat.HTML), (
            f"Plots are saved in {FileFormat.HTML} format. Please provide a valid "
            "output filepath"
        )

        for col in [col_x, col_y, hover_data_col, colorcode_col]:
            if col is not None and col not in self.df.columns:
                raise ValueError(f"Column {col} not found in the DataFrame")

        print(f"Plotting... {col_y} vs {col_x}")

        # fill NaN values in colorcode_col with 0 so as to avoid plotly error
        if colorcode_col is not None:
            self.df[colorcode_col] = self.df[colorcode_col].fillna(0)

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

    @typechecked
    def plot3D(
        self,
        col_x: str,
        col_y: str,
        col_z: str,
        out_filepath: str,
        colorcode_col: Optional[str] = None,
        hover_data_col: Optional[str] = None,
        show_fig: bool = False,
    ) -> None:
        """Plots the data in 3D"""
        assert out_filepath.endswith(FileFormat.HTML), (
            f"Plots are saved in {FileFormat.HTML} format. Please provide a valid "
            "output filepath"
        )

        for col in [col_x, col_y, col_z, colorcode_col, hover_data_col]:
            if col is not None and col not in self.df.columns:
                raise ValueError(f"Column {col} not found in the DataFrame")

        print(f"Plotting... {col_z} vs {col_y} vs {col_x}")

        # fill NaN values in colorcode_col with 0 so as to avoid plotly error
        if colorcode_col is not None:
            self.df[colorcode_col] = self.df[colorcode_col].fillna(0)

        if hover_data_col is not None and colorcode_col is not None:
            fig = px.scatter_3d(
                self.df,
                x=col_x,
                y=col_y,
                z=col_z,
                hover_data=[hover_data_col],
                color=colorcode_col,
            )

        elif hover_data_col is not None and colorcode_col is None:
            fig = px.scatter_3d(
                self.df,
                x=col_x,
                y=col_y,
                z=col_z,
                hover_data=[hover_data_col],
            )

        elif hover_data_col is None and colorcode_col is not None:
            fig = px.scatter_3d(
                self.df,
                x=col_x,
                y=col_y,
                z=col_z,
                color=colorcode_col,
            )

        elif hover_data_col is None and colorcode_col is None:
            fig = px.scatter_3d(
                self.df,
                x=col_x,
                y=col_y,
                z=col_z,
            )

        if show_fig:
            fig.show()

        fig.write_html(out_filepath)

        print(f"Plot saved at: {out_filepath}")
