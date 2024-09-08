# flight_log_plots
Plotting log data

python==3.12

To contribute to the repo, please install pre-commits

```
pip install pre-commit
pre-commit install
```

Disclaimer: this is a very WIP version that consumes csv files.

Sample plots can be found in `examples`

To use the plotter with your files, go to `src/plotter/run.py` and change the arguments

### TODO
1. Add json parser so that the module generates required dataframes from json files
2. Would be nice to have color coding (e.g., for flight mode etc)
3. .... 