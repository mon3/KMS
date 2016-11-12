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
    Dane = np.loadtxt("srednie.txt")
    T_av = Dane[:,1]
    p_av = Dane[:,3]

    L = 2.3
    v = 4./3. * pi *L*L*L 
    print "v = ", v
    N = 125
    k = 8.31e-3

    # p_av= 3./2 *N*k*T_av/v

    T_av_data = np.arange(0,1600,50)
    # print T_av_data

    p_av_data = np.zeros(len(T_av_data))
   
    j = 0
    for i in T_av_data:
        p_av_data[j]=(3./2.*N*k*i/v)
        j+=1
    
    print p_av_data

    plt.title(r"Zależność $\overline{p}(\overline{T})$", fontsize=20)
    plt.xlabel(r"$\overline{T} ~[K]$", fontsize=18)
    plt.ylabel(r"$\overline{p} ~ [u~ nm^{-1} ~ ps^{-2}]$", fontsize=18)
   
    plt.plot(T_av,p_av,'o', label='symulacja')
    plt.plot(T_av_data,p_av_data,'o', label="teoria")





 



 
    plt.grid()
    plt.legend(loc=4)
    plt.show()



if __name__ == "__main__":
    main()