#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pylab
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from scipy.stats import chisquare

def linear(x,a,b):
    return a*x + b

def func(x, a, b,c):
    return a * x*x+b*x+c

def sqrt_func(x, a, b,c):
    return a * np.power(x,b)+c

def main():
    matplotlib.rcParams['text.usetex'] = True
    matplotlib.rcParams['text.latex.unicode'] = True
    Dane = np.loadtxt("out.txt")
    H = Dane[:,1]
    tau = np.empty(len(H))
    tau.fill(2e-3)

   
    # plt.title(r"Kalibracja energetyczna detektora d8", fontsize=20)
    # plt.xlabel(r"kanał", fontsize=18)
    # plt.ylabel("U [mV]", fontsize=18)
   
    plt.plot(H, tau,'o', label='dane eksperymentalne')
 
    plt.grid()
    plt.legend(loc=4)
    plt.show()



if __name__ == "__main__":
    main()