# adapted from
# http://bkanuka.com/articles/native-latex-plots/

import numpy as np
import matplotlib as mpl
mpl.use('pgf')

def figsize(scale, golden_mean=(np.sqrt(5.0)-1.0)/2.0):   # Golden ratio
    fig_width_pt = 469.755                          # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    fig_size = [fig_width,fig_height]
    return fig_size

pgf_with_latex = {                      # setup matplotlib to use latex for output
    "pgf.texsystem": "pdflatex",        # change this if using xetex or lautex
    "text.usetex": True,                # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 10,               # LaTeX default is 10pt font.
    "font.size": 10,
    "legend.fontsize": 8,               # Make the legend/label fonts a little smaller
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.figsize": figsize(0.9),     # default fig size of 0.9 textwidth
    "figure.autolayout": True,          # fix issues with labels being cut off
    "pgf.preamble": [
        r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
        r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
        ]
    }
import matplotlib.pyplot as plt
mpl.rcParams.update(pgf_with_latex)
def savefig(filename):
    # This file is the one that will be included
    plt.savefig('{}.pgf'.format(filename))
    # This file is generated for previewing
    plt.savefig('{}.pdf'.format(filename))

from scipy import signal

############################################
# n_BodePlots.tex
############################################
# Decomposing the transfer function:
# 100 * (s/10**3 + 1) / [(s/10**6 + 1)(s/10**8 + 1)]
# Define a vector of omegas that we are going to plot
w = np.logspace(0, 11, 12)
# Magnitude
const_offset = [40] * 12
zero1 = [0] * 4 + [20, 40, 60, 80, 100, 120, 140, 160]
pole1 = [0] * 7 + [-20, -40, -60, -80, -100]
pole2 = [0] * 9 + [-20, -40, -60]
plt.clf() # Clear the figure
width = 0.7 # Figure width
weight = 0.8 # line weight
fig = plt.figure(figsize=figsize(width,.7))
ax = fig.add_subplot(111)
ax.semilogx(w, const_offset, lw=weight, label="constant")
ax.semilogx(w, zero1, lw=weight, label="zero 1")
ax.semilogx(w, pole1, lw=weight, label="pole 1")
ax.semilogx(w, pole2, lw=weight, label="pole 2")
ax.semilogx(w,
        np.sum([const_offset, zero1, pole1, pole2], axis=0),
        lw=1, label="sum", c='black')
ax.set_xlabel(r"$\omega$ (rad/s)")
ax.set_ylabel(r"$\mid H(\omega)\mid (dB)$")
ax.legend()
savefig('n_BodePlots_ex1a')

# Phase
p_const_offset = [0] * 12
p_zero1 = [0] * 3 + [45] + [90] * 8
p_pole1 = [0] * 6 + [-45] + [-90] * 5
p_pole2 = [0] * 8 + [-45] + [-90] * 3
plt.clf()
fig = plt.figure(figsize=figsize(width,.7))
ax = fig.add_subplot(111)
ax.semilogx(w, p_const_offset, lw=weight, label="constant")
ax.semilogx(w, p_zero1, lw=weight, label="zero 1")
ax.semilogx(w, p_pole1, lw=weight, label="pole 1")
ax.semilogx(w, p_pole2, lw=weight, label="pole 2")
ax.semilogx(w,
        np.sum([p_const_offset, p_zero1, p_pole1, p_pole2], axis=0),
        lw=1, label="sum", c='black')
ax.set_xlabel(r"$\omega$ (rad/s)")
ax.set_ylabel(r"$\angle H(\omega) (^{\circ})$")
ax.legend()
savefig('n_BodePlots_ex1b')

# Compare approximation with exact
s = signal.lti([0.1, 100], [10**-14, 10**-6 + 10**-8, 1])
w_exact, mag, phase = signal.bode(s, w=np.logspace(0, 11, 1200))
plt.clf()
fig, axarr = plt.subplots(2, sharex=True, figsize=figsize(width))
axarr[0].semilogx(w_exact, mag, lw=weight, label="exact")
axarr[0].semilogx(w,
        np.sum([const_offset, zero1, pole1, pole2], axis=0),
        lw=weight, label="approximation")
axarr[0].set_ylabel(r"$\mid H(\omega)\mid (dB)$")
axarr[0].legend()
axarr[1].semilogx(w_exact, phase, lw=weight, label="exact")
axarr[1].semilogx(w,
        np.sum([p_const_offset, p_zero1, p_pole1, p_pole2], axis=0),
        lw=weight, label="approximation")
axarr[1].set_ylabel(r"$\angle H(\omega) (^{\circ})$")
axarr[1].set_xlabel(r"$\omega$ (rad/s)")
axarr[1].legend()
savefig('n_BodePlots_ex1c')

############################################
# q_bode.tex
############################################
# Part A
w = np.logspace(5, 11, 7)
const_offset = [180] * 7
zero = [0] * 5 + [20, 40]
pole1 = [-100, -120, - 140, -160, -180, -200, -220]
pole2 = [0] * 3 + [-20, -40, -60, -80]
plt.clf()
width = 1
fig, axarr = plt.subplots(2, sharex=True, figsize=figsize(width, 1))
axarr[0].semilogx(w, const_offset, lw=weight, label="Constant")
axarr[0].semilogx(w, zero, lw=weight, label="Simple Zero")
axarr[0].semilogx(w, pole1, lw=weight, label="Pole @ origin")
axarr[0].semilogx(w, pole2, lw=weight, label="Simple Pole")
axarr[0].semilogx(w,
        np.sum([const_offset, zero, pole1, pole2], axis=0),
        lw=1, label="sum", c='black')
axarr[0].set_ylabel(r"$\mid H(\omega)\mid (dB)$")
axarr[0].set_yticks(np.linspace(-200, 200, 11))
axarr[0].legend()

a_const_offset = [0] * 7
a_zero = [0] * 4 + [45] + [90] * 2
a_pole1 = [-90] * 7
a_pole2 = [0] * 2 + [-45] + [-90] * 4

axarr[1].semilogx(w, a_const_offset, lw=weight, label="Constant")
axarr[1].semilogx(w, a_zero, lw=weight, label="Simple Zero")
axarr[1].semilogx(w, a_pole1, lw=weight, label="Pole @ origin")
axarr[1].semilogx(w, a_pole2, lw=weight, label="Simple Pole")
axarr[1].semilogx(w,
        np.sum([a_const_offset, a_zero, a_pole1, a_pole2], axis=0),
        lw=1, label="sum", c='black')
axarr[1].set_ylabel(r"$\angle H(\omega) (^{\circ})$")
axarr[1].set_xlabel(r"$\omega$ (rad/s)")
axarr[1].set_yticks(np.linspace(-180, 180, 5))
axarr[1].legend()
savefig('q_bode_a')

