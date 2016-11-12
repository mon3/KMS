#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pylab
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from scipy.stats import chisquare

def main():
    matplotlib.rcParams['text.usetex'] = True
    matplotlib.rcParams['text.latex.unicode'] = True
    Dane = np.loadtxt("test1.txt")
    H = Dane[:,0]
    t = Dane[:,1]

    
    plt.title(r"Zależność $\overline{H}(\tau)$", fontsize=20)
    plt.xlabel(r"$\tau ~[ps]$", fontsize=18)
    plt.ylabel(r"$\overline{H} ~ \frac{kJ}{mol}$", fontsize=18)
   
    plt.semilogy(t,H,'o', label='symulacja')
 



 
    plt.grid()
    plt.legend(loc=4)
    plt.show()



if __name__ == "__main__":
    main()