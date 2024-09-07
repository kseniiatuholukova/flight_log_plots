import pandas as pd
import plotly.express as px
from typeguard import typechecked


class Plotter:
    @typechecked
    def __init__(self, df: pd.DataFrame) -> None:
        """Initializes the Plotter object"""
        self.df = df

    @typechecked
    def plot(self, col_x: str, col_y: str) -> None:
        """Plots the data"""
        fig = px.scatter(self.df, x=col_x, y=col_y)
        fig.show()
