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

#The main_square function allows all three schemes to be compared at once
#looking at both graphing and a table of errors. 
#Function is called using resolution parameters.
def main_square(nx,nt):
    "Advect the initial square wave conditions using various advection schemes"
    "and compare results"

    # Fixed parameters throughout for all three schemes.
    xmin = 0
    xmax = 1
    c = 0.2
    
    # Derived parameters
    dx = (xmax - xmin)/nx
    
    # Spatial points for plotting and for defining initial conditions
    x = np.arange(xmin, xmax, dx)

    # Initial conditions
    phiOld = squareWave(x)
    # Exact solution is the initial condition advected.
    phiAnalytic = squareWave((x - c*nt*dx)%(xmax - xmin))

    # Advect the profile using finite difference
    #for all the time steps for each of the three schemes
    phiFTBS = FTBS(phiOld.copy(), c, nt)
    phiCTCS = CTCS(phiOld.copy(), c, nt)
    phiLW = LW(phiOld.copy(), c, nt)
    
    # Calculate and structure error norms in a table.
    Scheme=["FTBS","CTCS","LW"]
    l2_error=[l2ErrorNorm(phiFTBS, phiAnalytic),\
    l2ErrorNorm(phiCTCS, phiAnalytic),l2ErrorNorm(phiLW, phiAnalytic)]
    linf_error=[lInfErrorNorm(phiFTBS, phiAnalytic),\
    lInfErrorNorm(phiCTCS, phiAnalytic),lInfErrorNorm(phiLW, phiAnalytic)]
    table=zip(Scheme,l2_error,linf_error)
    
    #Send table to graphs_tables folder. 
    file=open("graphs_tables/Square_errors_%d_%d.txt"%(nx,nt),"w")
    file.write(tabulate(table, headers=\
    ["Scheme", "l2 error norm","linf error norm"]\
    ,floatfmt=".3f",tablefmt='orgtbl'))
    file.close()
    
    
    # Plot the solutions for all schemes on one set of axes.
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
    #Allow graph to save into graphs_tables folder.
    #File name reflects resolution to avoid overwriting.
    input('press return to save file and continue')
    plt.savefig('graphs_tables/3scheme_square_analysis_%d_%d.pdf'%(nx,nt), 
    bbox_inches = "tight")
    
main_square(40,40)





