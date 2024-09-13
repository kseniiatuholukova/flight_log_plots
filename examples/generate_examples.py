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

runner.run(
    col_x="fox",
    col_y="opossum",
    col_z="otter",
    col_to_bind_by="timestamp",
    colorcode_col="mode",
    bin_size=5,
    out_filepath="examples/output/fox_against_opossum_against_otter.html",
    show_fig=True,
)


runner_real = Runner(
    in_filepath="./real_data/rssi-dist-azimuth-13.09.2024.csv", datetime_col="TimeUS"
)

runner_real.run(
    col_x="Dist",
    col_y="Azimuth",
    col_to_bind_by="TimeUS",
    bin_size=5,
    colorcode_col="RSSI",
    out_filepath="examples/output/rssi_against_distance_1.html",
    show_fig=True,
)

runner_real.run(
    col_x="Dist",
    col_y="Azimuth",
    col_z="RSSI",
    col_to_bind_by="TimeUS",
    colorcode_col="RSSI",
    bin_size=5,
    out_filepath="examples/output/rssi_against_dist_against_azimuth_1.html",
    show_fig=True,
)
