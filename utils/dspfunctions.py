# Imports
import math # because i love math even more <3
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd

### === PLOTS

# function, which formats the output of the plot ticks
def integer_millions_format(x, pos):
    """The two args are the value and tick position"""
    return f'{int(x/1e6)}m'

def float_millions_format(x, pos):
    """The two args are the value and tick position"""
    return f'{float(x/1e6)}m'

# function, which is used to plot the estimated to actual sales in the first part of the notebook.
def plot_estimated_to_actual_sales(dataset, estimated, actual):

    plt.plot(estimated, label = "Estimated sales", c = "orange")
    plt.plot(actual, label = "Actual sales", c = "blue")

    plt.title("Estimated to overall sales in Diamond Comics")
    plt.xlabel("Year")
    plt.ylabel("USD")

    plt.xticks(dataset.index[::2])

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(integer_millions_format))

    plt.legend()
    plt.show()

# function, which is used to plot the sales as a barchart 
# it also has a functionallity to rename the y axis depending on the sales count
def plot_sales(titles, sales, title):

    plt.bar(titles, sales)

    plt.xlabel("Books")
    plt.ylabel("Sold units")

    plt.title(title)
    plt.xticks([])

    plt.ylim(0, 2_300_000)

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(float_millions_format))

    plt.show()

# function, which is used to plot the publishers on a bar plot
def plot_publishers(publishers):

    plt.bar(publishers.index, publishers.values)

    plt.xlabel("Demographic")
    plt.ylabel("Count")
    plt.title("Count of Demographic")

    plt.xticks(rotation='vertical')

    plt.show()

# ------------------------------------------------------------
# Data Science Project Functions
# This file contains the functions that would be useful later
# Deyan Sirakov | 2023
# ------------------------------------------------------------