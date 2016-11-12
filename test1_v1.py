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
    Dane = np.loadtxt("tau_4e10.txt")
    H = Dane[1:,1]
    t = Dane[1:,0]

    Dane1 = np.loadtxt("tau_3e10.txt")
    H1 = Dane1[1:,1]
    t1 = Dane1[1:,0]

    Dane2 = np.loadtxt("tau_2_5_e10.txt")
    H2 = Dane2[1:,1]
    t2 = Dane2[1:,0]

    Dane3 = np.loadtxt("tau_2_25e10.txt")
    H3 = Dane3[1:,1]
    t3 = Dane3[1:,0]


    Dane4 = np.loadtxt("tau_5e10.txt")
    H4 = Dane4[1:,1]
    t4 = Dane4[1:,0]
   
    # plt.title(r"Kalibracja energetyczna detektora d8", fontsize=20)
    # plt.xlabel(r"kanał", fontsize=18)
    # plt.ylabel("U [mV]", fontsize=18)
   
    plt.semilogy(t,H,'o', label='tau=4e-3')
    plt.semilogy(t1,H1,'o', label='tau=3e-3')
    plt.semilogy(t2,H2,'o', label='tau=2.5e-3')
    plt.semilogy(t3,H3,'o', label='tau=2.25e-3')
    plt.semilogy(t4,H4,'o', label='tau=5e-3')



 
    plt.grid()
    plt.legend(loc=4)
    plt.show()



if __name__ == "__main__":
    main()