from pathlib import Path

import pandas as pd
from typeguard import typechecked

from src.plotter.defaults import FileFormat


class Reader:
    @typechecked
    def __init__(self, filepath: Path) -> None:
        """Reads a file to a pandas DataFrame."""
        assert filepath.exists(), f"File not found: {filepath}"
        assert (
            str(filepath)
            .lower()
            .endswith(
                (FileFormat.CSV, FileFormat.TSV, FileFormat.XLS, FileFormat.XLSX),
            )
        ), (
            f"Invalid file format: {filepath}. Only {FileFormat.CSV}, "
            f"{FileFormat.TSV}, {FileFormat.XLS}, {FileFormat.XLSX} files are "
            "supported."
        )

        if str(filepath).lower().endswith(FileFormat.CSV):
            self.df = pd.read_csv(filepath)
        elif str(filepath).lower().endswith(FileFormat.TSV):
            self.df = pd.read_csv(filepath, sep="\t", low_memory=False)
        elif str(filepath).lower().endswith((FileFormat.XLS, FileFormat.XLSX)):
            self.df = pd.read_excel(filepath)
        else:
            raise ValueError(
                f"Invalid file format: {filepath}. Only {FileFormat.CSV}, "
                f"{FileFormat.TSV}, {FileFormat.XLS}, f{FileFormat.XLSX} files are "
                "supported."
            )
