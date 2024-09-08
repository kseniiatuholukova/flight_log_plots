from pathlib import Path
from typing import Optional

from typeguard import typechecked

from src.plotter.binder import Binder
from src.plotter.defaults import ColName
from src.plotter.plotter import Plotter
from src.plotter.reader import Reader
from src.plotter.utils import bin_data


class Runner:
    @typechecked
    def __init__(self, in_filepath: str, datetime_col: Optional[str]) -> None:
        """Initializes the Runner object"""
        self.in_filepath = in_filepath
        reader = Reader(Path(in_filepath))

        if datetime_col is not None:
            reader.set_datetime(datetime_col)

        self.df = reader.df

    @typechecked
    def run(
        self,
        col_x: str,
        col_y: str,
        col_to_bind_by: Optional[str] = None,
        n_bins: Optional[int] = None,
        out_filepath: Optional[str] = "plot.html",
        bind: bool = False,
    ) -> None:
        """Runs binning, binding, and plotting on a given DataFrame"""
        if bind and (col_to_bind_by is None):
            raise ValueError("Bind set to True, but the binding column is not provided")

        if n_bins is not None:
            self.df[ColName.BINS] = bin_data(self.df[col_to_bind_by], n_bins)
            col_to_bind_by = ColName.BINS

        plotter = Plotter(self.df)

        if bind:
            binder = Binder(self.df)

            self.df = binder.bind(col_x=col_x, col_y=col_y, col_z=col_to_bind_by)
            plotter.plot_bound(
                col_x=col_x,
                col_y=col_y,
                col_z=col_to_bind_by,
                out_filepath=out_filepath,
            )

        else:
            plotter.plot_unbound(col_x=col_x, col_y=col_y, out_filepath=out_filepath)
