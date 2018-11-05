#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:14:49 2018

@author: caw4618
"""

import matplotlib.pyplot as plt
import numpy as np
# read in all the linear advection schemes, initial conditions and other
# code associated with this application
from Initial_conditions import *
from LW import *
from FTBS import *
from CTCS import *
from Error_checks import *
from tabulate import tabulate

### The main code is inside a function to avoid global variables    ###
def main():
    "Advect the initial conditions using various advection schemes and"
    "compare results"

    # Parameters
    xmin = 0
    xmax = 1
    nx = 40
    nt = 40
    c = 0.2

    # Derived parameters
    dx = (xmax - xmin)/nx
    
    # spatial points for plotting and for defining initial conditions
    x = np.arange(xmin, xmax, dx)

    # Initial conditions
    phiOld = squareWave(x)
    # Exact solution is the initial condition shifted around the domain
    phiAnalytic = squareWave((x - c*nt*dx)%(xmax - xmin))

    # Advect the profile using finite difference
    #for all the time steps for each of the three schemes
    phiFTBS = FTBS(phiOld.copy(), c, nt)
    phiCTCS = CTCS(phiOld.copy(), c, nt)
    phiLW = LW(phiOld.copy(), c, nt)
    
    # Calculate and print out error norms in a table.
    Scheme=["FTBS","CTCS","LW"]
    l2_error=[l2ErrorNorm(phiFTBS, phiAnalytic),l2ErrorNorm(phiCTCS, phiAnalytic),l2ErrorNorm(phiLW, phiAnalytic)]
    linf_error=[lInfErrorNorm(phiFTBS, phiAnalytic),lInfErrorNorm(phiCTCS, phiAnalytic),lInfErrorNorm(phiLW, phiAnalytic)]
    table=zip(Scheme,l2_error,linf_error)
    print(tabulate(table, headers=["Scheme", "l2 error norm", "linf error norm"],floatfmt=".3f",tablefmt='orgtbl'))
    

    # Plot the solutions
    font = {'size'   : 20}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(x, phiOld, label='Initial', color='black')
    plt.plot(x, phiAnalytic, label='Analytic', color='black', 
             linestyle='--', linewidth=2)
    plt.plot(x, phiFTBS, label='FTBS', color='blue')
    plt.plot(x, phiCTCS, label='CTCS', color='red')
    plt.plot(x, phiLW, label='LW', color='green')
    plt.axhline(0, linestyle=':', color='black')
    plt.ylim([-0.2,1.2])
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('$x$')
    plt.ylabel('phi(x)')
    input('press return to save file and continue')
    plt.savefig('graphs_tables/3scheme_square_analysis.pdf')

### Run the function main defined in this file                      ###
main()

