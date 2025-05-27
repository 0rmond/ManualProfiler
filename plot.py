import time
from functools import partial

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.special import erf as err_fun
from scipy.optimize import curve_fit

def init_plot():
    """Initialises an interactive plot.
    Returns:
        - Figure
        - Axis
        - errorbar Line Collection
    """

    plt.ion()
    f, ax = plt.subplots()
    ax.set_xlabel(r"Knife Translation $[\mu m]$")
    ax.set_ylabel(r"Measured power $[W]$")
    line_collection  = ax.errorbar([0,0], [0,0], yerr=[0,0], xerr=[0,0], marker='x', color="white")
    return f, ax, line_collection

def update_plot(fname, f, old_line_collection):
    """Removes existing lines from a plot and replaces with a new line plotted from fname file
    Returns:
        - new errobar Line Collection
    """

    data = pd.read_csv(fname, index_col=0, names=[str(n) for n in range(0, 10)])
    xs = data.index.values
    xerrs = np.array([20 for x in xs])
    ys = data.mean(axis=1)
    yerrs = data.std(axis=1)/np.sqrt(len(data.columns))

    error_bar_props = dict(ecolor="tab:red", elinewidth=1)
    marker_props = dict(marker='x', color="black", ms=15, lw=0)

    ax = f.get_axes()[0]
    new_line_collection = ax.errorbar(xs, ys, xerr=xerrs, yerr=yerrs, **error_bar_props, **marker_props, label=f"test {len(xs)}")

    old_line_collection.remove()

    f.canvas.draw()
    f.canvas.flush_events()
    time.sleep(0.1)
    return new_line_collection
