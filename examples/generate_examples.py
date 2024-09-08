from src.plotter.runner import Runner

runner = Runner(
    in_filepath="./synthetic_data/synthetic_data.csv", datetime_col="timestamp"
)


for pair in [
    ("capybara", "fox"),
    ("opossum", "capybara"),
    ("otter", "opossum"),
    ("fox", "otter"),
]:
    runner.run(
        col_x=pair[0],
        col_y=pair[1],
        col_to_bind_by="timestamp",
        n_bins=2000,
        bin_size_threshold=100,
        out_filepath=f"examples/{pair[1]}_against_{pair[0]}.html",
        show_fig=False,
    )

for animal in ["capybara", "fox", "opossum", "otter"]:
    runner.run(
        col_x="timestamp",
        col_y=animal,
        out_filepath=f"examples/{animal}_against_time.html",
        show_fig=False,
    )
