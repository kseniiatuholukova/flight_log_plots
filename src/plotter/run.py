from src.plotter.runner import Runner

if __name__ == "__main__":
    runner = Runner(
        in_filepath="./synthetic_data/synthetic_data.csv", datetime_col="timestamp"
    )

    runner.run(
        col_x="capybara",
        col_y="fox",
        col_to_bind_by="timestamp",
        n_bins=None,
        bin_size_max_limit=100,
        out_filepath="../plot_1.html",
        show_fig=True,
    )

    runner.run(
        col_x="timestamp",
        col_y="capybara",
        out_filepath="../plot_2.html",
        show_fig=True,
    )
