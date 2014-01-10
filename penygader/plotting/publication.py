# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:24:02 2012

@author: Stuart Mumford

This module imports matplotlib with customisations I use when creating
figures for inclusion in print publications.

Usage
-----

>>> from penygader.plotting.publication import *

>>> plt.plot(x,y)
>>> thick_ticks(plt.gca())
>>> plt.show()
"""
import matplotlib as mpl
#Do rcParams bit
mpl.rcParams['axes.linewidth'] = 1.7
mpl.rcParams['xtick.major.pad'] = 7
mpl.rcParams['ytick.major.pad'] = 5
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = ['Time New Roman']
mpl.rcParams.update({'font.size': 15})

import matplotlib.pyplot as plt


__all__ = ['mpl', 'plt', 'thick_ticks', 'tex_fonts']


def tex_fonts():
    mpl.rcParams['ps.useafm'] = True
    mpl.rcParams['pdf.use14corefonts'] = True
    mpl.rcParams['text.usetex'] = True

def thick_ticks(ax):
    for line in ax.yaxis.get_ticklines(minor=True) + ax.xaxis.get_ticklines(minor=True):
        line.set_markersize(4.5)
        line.set_markeredgewidth(1)
    for line in ax.yaxis.get_ticklines() + ax.xaxis.get_ticklines():
        line.set_markersize(7)
        line.set_markeredgewidth(1.5)
