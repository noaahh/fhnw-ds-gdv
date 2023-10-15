import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv('../data/gapminder_full.csv')


def save_plot(plot, filename):
    try:
        fig = plot.get_figure()
        fig.savefig(f"../report/images/plots/{filename}.png", bbox_inches='tight')
    except AttributeError:
        plt.savefig(f"../report/images/plots/{filename}.png", bbox_inches='tight')


def format_plot(plot, title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)