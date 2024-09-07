from typing import Optional

from typeguard import typechecked

from src.plotter.binder import Binder
from src.plotter.defaults import ColName
from src.plotter.plotter import Plotter
from src.plotter.reader import Reader
from src.plotter.utils import bin_data


class Runner:
    @typechecked
    def __init__(self, in_filepath: str) -> None:
        """Initializes the Runner object"""
        self.in_filepath = in_filepath
        self.df = Reader(in_filepath).df

    def run(
        self,
        col_x: str,
        col_y: str,
        col_to_bind_by: Optional[str],
        n_bins: Optional[int],
        out_filepath: Optional[str],
        bind: bool = False,
    ) -> None:
        """Runs binning, binding, and plotting on a given DataFrame"""
        if bind and (col_to_bind_by is None):
            raise ValueError("Bind set to True, but the binding column is not provided")

        if n_bins is not None:
            self.df[ColName.BINS] = bin_data(self.df[col_to_bind_by], n_bins)
            col_to_bind_by = ColName.BINS

        if bind:
            binder = Binder(self.df)
            self.df = binder.bind(col_x=col_x, col_y=col_y, col_z=col_to_bind_by)

        plotter = Plotter(self.df, out_filepath)
        plotter.plot(col_x, col_y)
        # if bind and no
