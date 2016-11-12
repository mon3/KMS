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
    Dane = np.loadtxt("test2.txt")
    a = Dane[:,0]
    V0 = Dane[:,1]
    Vmin = Dane[:,2]
    

    print "min V = ", min(V0)

    plt.title(r"Zależność $V_{min}(a)$", fontsize=20)
    plt.xlabel(r"$a ~[nm]$", fontsize=18)
    plt.ylabel(r"$V_{min} ~ [\frac{kJ}{mol}]$", fontsize=18)
   
    # plt.xticks(np.arange(min(a), max(a), 0.0025))

    plt.plot(a,V0,'o', label='symulacja')
    plt.plot(a[7],V0[7],'o', label='$ a = 0.373, V_{min} = -676.48 $ ')
 



 
    plt.grid()
    plt.legend(loc=4)
    plt.show()



if __name__ == "__main__":
    main()