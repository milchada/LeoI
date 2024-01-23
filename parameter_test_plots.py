#parameter_test_plots.py

# Formatting your plots in a clear grid, with appropriate labels and colorbars is crucial for readers to understand your point. Here I show how to set up the axis objects for best results.

import matplotlib.pylab as plt
from matplotlib import colors, cm
import numpy as np

#vary this as needed
nrows = 2
ncols = 5
fig, ax  = plt.subplots(nrows=nrows, ncols = ncols, figsize=(ncols*2, nrows*2), sharex=True, sharey=True)
xtix = np.arange(100, 201, 25)
ytix = np.arange(-50, 31, 25)
for a in ax[:, 0]:
    a.set_yticks(ytix)
    a.set_yticklabels(['%d' % x for x in ytix])
for a in ax[1]:
    a.set_xticks(xtix)
    a.set_xticklabels(['%d' % x for x in xtix])
fig.text(0.5, 0, "RA ($^\circ$)", ha='center')
fig.text(0, 0.5, "DEC ($^\circ$)", va='center', rotation='vertical')
plt.tight_layout()
