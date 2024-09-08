from pathlib import Path
from typing import Optional

from typeguard import typechecked

from src.plotter.binder import Binder
from src.plotter.defaults import ColName, FileFormat
from src.plotter.plotter import Plotter
from src.plotter.reader import Reader
from src.plotter.utils import bin_data


class Runner:
    @typechecked
    def __init__(self, in_filepath: str, datetime_col: Optional[str] = None) -> None:
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
        bin_size_threshold: Optional[int] = None,
        out_filepath: Optional[str] = "".join(["plot", FileFormat.HTML]),
        show_fig: bool = False,
    ) -> None:
        """Runs binning, binding, and plotting on a given DataFrame"""
        for col in [col_x, col_y, col_to_bind_by]:
            if col is not None and col not in self.df.columns:
                raise ValueError(f"Column {col} not found in the DataFrame")

        if n_bins is not None:
            self.df[ColName.BIN] = bin_data(
                self.df[col_to_bind_by],
                n_bins,
                bin_size_threshold=bin_size_threshold,
            )

        if col_to_bind_by is not None:
            col_to_bind_by = ColName.BIN if n_bins is not None else col_to_bind_by
            binder = Binder(self.df)
            bound_df = binder.bind(
                col_x=col_x,
                col_y=col_y,
                col_to_bind_by=col_to_bind_by,
            )

            plotter = Plotter(bound_df)

            plotter.plot(
                col_x=col_x,
                col_y=col_y,
                out_filepath=out_filepath,
                hover_data_col=col_to_bind_by,
                show_fig=show_fig,
            )

        else:
            plotter = Plotter(self.df)

            plotter.plot(
                col_x=col_x,
                col_y=col_y,
                out_filepath=out_filepath,
                show_fig=show_fig,
            )
