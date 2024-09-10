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
        colorcode_col="mode",
        bin_size=5,
        out_filepath=f"examples/output/{pair[1]}_against_{pair[0]}.html",
        show_fig=False,
    )

for animal in ["capybara", "fox", "opossum", "otter"]:
    runner.run(
        col_x="timestamp",
        col_y=animal,
        colorcode_col="mode",
        out_filepath=f"examples/output/{animal}_against_time.html",
        show_fig=False,
    )
