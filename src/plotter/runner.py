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
    def __init__(
        self,
        in_filepath: str,
        datetime_col: Optional[str] = None,
    ) -> None:
        """
        Initializes the Runner object

        Args:
            in_filepath (str): Path to the input file. Should end in ".csv", ".tsv",
                ".xls", or ".xlsx".
            datetime_col (str, optional): Name of the datetime column in the
                DataFrame. If specified, the values are treated as timestamps.
                Defaults to None.
        """
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
        bin_size: Optional[int] = None,
        colorcode_col: Optional[str] = None,
        out_filepath: Optional[str] = "".join(["plot", FileFormat.HTML]),
        show_fig: bool = False,
    ) -> None:
        """
        Runs binning, binding, and plotting on a given DataFrame

        Args:
        col_x (str): Name of the column to be plotted on the x-axis
        col_y (str): Name of the column to be plotted on the y-axis
        col_to_bind_by (str, optional): Name of the column with a third
            variable to bind by. If not provided, x is plotted directly against y.
            Defaults to None.
        bin_size (int, optional): Number of data points in a bin. Defaults to None.
        colorcode_col (str, optional): Name of the column to color-code the plot.
            Defaults to None.
        out_filepath (str, optional): Path to save the plot. Should end with ".html".
            Defaults to "plot.html".
        show_fig (bool, optional): If True, the plot is displayed in the browser.
            Defaults to False.
        """
        for col in [col_x, col_y, col_to_bind_by, colorcode_col]:
            if col is not None and col not in self.df.columns:
                raise ValueError(f"Column {col} not found in the DataFrame")

        if bin_size is not None:
            self.df[ColName.BIN] = bin_data(
                data=self.df[col_to_bind_by],
                bin_size=bin_size,
            )

        if col_to_bind_by is not None:
            col_to_bind_by = ColName.BIN if bin_size is not None else col_to_bind_by
            binder = Binder(self.df)
            bound_df = binder.bind(
                col_x=col_x,
                col_y=col_y,
                col_to_bind_by=col_to_bind_by,
                colorcode_col=colorcode_col,
            )

            plotter = Plotter(bound_df)

            plotter.plot(
                col_x=col_x,
                col_y=col_y,
                out_filepath=out_filepath,
                hover_data_col=col_to_bind_by,
                colorcode_col=colorcode_col,
                show_fig=show_fig,
            )

        else:
            plotter = Plotter(self.df)

            plotter.plot(
                col_x=col_x,
                col_y=col_y,
                colorcode_col=colorcode_col,
                out_filepath=out_filepath,
                show_fig=show_fig,
            )
