#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pylab
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from scipy.stats import chisquare
from math import pi

def main():
    matplotlib.rcParams['text.usetex'] = True
    matplotlib.rcParams['text.latex.unicode'] = True
    # Dane = np.loadtxt("/media/monika03/Particles/KMS/vis/out_T500.txt")
    Dane = np.loadtxt("out_T1000_So500_Sd2500_a0-373_v2.txt")
    t = Dane[1:,0]
    T = Dane[1:,3]
    P = Dane[1:,4]

    # P_av = 6.69588328887
    # T_av = 606.742673726
    T_av = 589.17437558
    P_av = 8.09195759115
    H_av = 866.965622045

    print P_av

    t_av = np.zeros(len(T))
    p_av = np.zeros(len(T))
    for i in range(len(T)):
        t_av[i] = T_av
        p_av[i] = P_av



    plt.title(r"Zależność $p_{chwil}(t)$", fontsize=20)
    # plt.xlabel(r"$\overline{T} ~[K]$", fontsize=18)
    plt.xlabel(r"t ~[ps]", fontsize=18)

    plt.ylabel(r"$p_{chwil} ~  [u~ nm^{-1} ~ ps^{-2}]$", fontsize=18)
   
    plt.plot(t,P,'o', label='symulacja')
    plt.plot(t,p_av,'o', label=r'$\bar{p}$')

    # plt.plot(T_av_data,p_av_data,'o', label="teoria")





 



 
    plt.grid()
    plt.legend(loc=1)
    plt.show()



if __name__ == "__main__":
    main()