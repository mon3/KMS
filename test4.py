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
    # Dane = np.loadtxt("/media/monika03/Particles/KMS/vis/out_T500.txt")
    Dane = np.loadtxt("out_T500_So500_Sd2500_a0-373_v2.txt")
    t = Dane[1:,0]
    T = Dane[1:,3]
    P = Dane[1:,4]


    # Dane1 = np.loadtxt("/media/monika03/Particles/KMS/vis/out_T1000.txt")
    Dane1 = np.loadtxt("out_T1000_So500_Sd2500_a0-373_v2.txt")

    t1 = Dane1[1:,0]
    T1 = Dane1[1:,3]
    P1 = Dane1[1:,4]


    # Dane2 = np.loadtxt("/media/monika03/Particles/KMS/vis/out_T1500.txt")
    Dane2 = np.loadtxt("out_T1500_So500_Sd2500_a0-373_v2.txt")

    t2 = Dane2[1:,0]
    T2 = Dane2[1:,3]
    P2 = Dane2[1:,4]


    # Dane3 = np.loadtxt("/media/monika03/Particles/KMS/vis/out_T2000.txt")
    Dane3 = np.loadtxt("out_T2000_So500_Sd2500_a0-373_v2.txt")

    t3 = Dane3[1:,0]
    T3 = Dane3[1:,3]
    P3 = Dane3[1:,4]
    
    # plt.title(r"Zależność $T_{chwil}(t)$", fontsize=20)
    # plt.xlabel(r"$t ~[ps]$", fontsize=18)
    # plt.ylabel(r"$T_{chwil} ~ [K]$", fontsize=18)

    plt.title(r"Zależność $T_{chwil}(t)$", fontsize=20)
    plt.xlabel(r"$t ~[ps]$", fontsize=18)
    plt.ylabel(r"$T_{chwil} ~ [K]$", fontsize=18)
   
    plt.plot(t,T,'o', label='T = 500 K')
    plt.plot(t1,T1,'o', label='T = 1000 K')
    plt.plot(t2,T2,'o', label='T = 1500 K')
    plt.plot(t3,T3,'o', label='T = 2000 K')



 



 
    plt.grid()
    plt.legend(loc=4)
    plt.show()



if __name__ == "__main__":
    main()