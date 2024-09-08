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
    def plot_unbound(self, col_x: str, col_y: str, out_filepath: str) -> None:
        """Plots the data"""
        if not out_filepath.endswith(FileFormat.HTML):
            raise ValueError(
                f"Plots are saved in {FileFormat.HTML} format. Please provide a valid "
                "output filepath"
            )

        fig = px.scatter(
            self.df,
            x=col_x,
            y=col_y,
        )
        fig.show()
        fig.write_html(out_filepath)

    @typechecked
    def plot_bound(self, col_x: str, col_y: str, col_z: str, out_filepath: str) -> None:
        """Plots the data with binding"""
        fig = px.scatter(self.df, x=col_x, y=col_y, hover_data=[col_z])
        fig.show()
        fig.write_html(out_filepath)
