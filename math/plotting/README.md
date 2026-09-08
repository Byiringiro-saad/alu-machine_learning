# Plotting

Introduction to data visualization with `matplotlib`. Each script in this
directory generates one plot from a small dataset built with `numpy`.

## Learning Objectives

- What is a plot?
- What is a scatter plot? line graph? bar graph? histogram?
- What is matplotlib?
- How to plot data with matplotlib
- How to label a plot
- How to scale an axis
- How to plot multiple sets of data at the same time

## Requirements

- Ubuntu 16.04 LTS, Python 3.5
- numpy 1.15, matplotlib 3.0
- Every file starts with `#!/usr/bin/env python3`, ends with a newline and is
  executable
- Code follows `pycodestyle` 2.5
- Every module and function is documented
- No imports other than `numpy` and `matplotlib.pyplot`

## Tasks

| File | Description |
|------|-------------|
| `0-line.py` | Line graph of `y = x^3` drawn as a solid red line |
| `1-scatter.py` | Scatter plot of men's height vs weight in magenta |
| `2-change_scale.py` | Exponential decay of C-14 with a logarithmic y-axis |
| `3-two.py` | Decay of C-14 and Ra-226 on one plot with a legend |
| `4-frequency.py` | Histogram of student grades with bins every 10 units |
| `5-all_in_one.py` | The five previous plots arranged in a single 3x2 figure |
| `6-bars.py` | Stacked bar chart of fruit owned by each person |
| `100-gradient.py` | Scatter plot of mountain elevation with a colorbar (advanced) |
| `101-pca.py` | 3D scatter of the Iris dataset reduced with PCA (advanced, needs `pca.npz`) |

## Usage

```bash
chmod +x *.py
./1-scatter.py
```

Each script opens a window with the plot.
