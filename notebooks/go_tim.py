import matplotlib.pyplot as plt
import numpy as np

def plot_tim():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.annotate('Way to go, Tim!', (.5, .5), fontsize=20, horizontalalignment='center')
    ax.set_axis_off()
    return fig