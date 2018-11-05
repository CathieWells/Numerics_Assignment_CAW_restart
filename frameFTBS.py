#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:14:49 2018

@author: caw4618
"""

import matplotlib.pyplot as plt

# read in all the linear advection schemes, initial conditions and other
# code associated with this application
from Initial_conditions import *
from LW import *
from FTBS import *
from CTCS import *
from Error_checks import *

### The main code is inside a function to avoid global variables    ###
def FTBS_graph(nx,nt,condition):
    "Advect different initial conditions using FTBS scheme"
    "feed in resolution in both time and space"
    "and preferred initial conditions"

    # Parameters maintained throughout.
    xmin = 0
    xmax = 1
    c = 0.2
    # Derived parameters
    dx = (xmax - xmin)/nx
   
    # spatial points for plotting and for defining initial conditions
    x = np.arange(xmin, xmax, dx)
    
    #Initial Conditions and shifted conditions.
    if condition==1:
        phiOld = cosBell(x, 0, 0.75)
        phiAnalytic= cosBell((x - c*nt*dx)%(xmax - xmin), 0, 0.75)
    elif condition==2:
        phiOld = squareWave(x)
        phiAnalytic = squareWave((x - c*nt*dx)%(xmax - xmin))
    elif condition==3:
        phiOld = mixed(x, 0, 0.1,0.2,0.4)
        phiAnalytic = mixed((x - c*nt*dx)%(xmax - xmin), 0, 0.1,0.2,0.4)
    else:
        print("I do not understand your chosen initial conditions.")
        raise SystemExit
    
    # Advect the profile using finite difference for all the time steps
    phiFTBS= FTBS(phiOld.copy(), c, nt)
    

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
    plt.axhline(0, linestyle=':', color='black')
    plt.ylim([-0.2,1.2])
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('$x$')
    input('press return to save file and continue')
    plt.savefig('graphs_tables/FTBS3.pdf')

### Run the function main defined in this file                      ###
FTBS_graph(40,40,2)
