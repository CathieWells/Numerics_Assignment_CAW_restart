#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:14:49 2018

@author: caw4618
"""

import matplotlib.pyplot as plt

# Read in relevant linear advection scheme, initial conditions and other
# code associated with this application
from Initial_conditions import *
from LW import *
from Error_checks import *

#This code will allow generation of LW results for each of the
#initial conditions, where 1 is cos bell, 2 is square wave and 3 is mixed.
#The resolution can also be changed to allow for comparison, with number
#of time steps for both space (nx) and time (nt) required in function call.
def LW_graph(nx,nt,condition):
    "Advect different initial conditions using FTBS scheme"
    "feed in resolution in both time and space"
    "and preferred initial conditions"

    # Constants assigned for all calculations.
    xmin = 0
    xmax = 1
    c = 0.2
    
    # Calculated value from constants and user specified nx value.
    dx = (xmax - xmin)/nx
   
    # Spatial points for plotting and for defining initial conditions
    x = np.arange(xmin, xmax, dx)
    
    #Initial Conditions and shifted conditions, using if to allow
    #user to specify, via third function call parameter, 
    #which initial wave to use.
    #System exit included where initial conditions not called appropriately.
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
    
    # Call in numeriucal advection code from function LW.
    phiLW= LW(phiOld.copy(), c, nt)
    

    # Plot inital conditions, analytic result and numerical model for
    #for given resolution.
    font = {'size'   : 20}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(x, phiOld, label='Initial', color='black')
    plt.plot(x, phiAnalytic, label='Analytic', color='black', 
             linestyle='--', linewidth=2)
    plt.plot(x, phiLW, label='LW', color='blue')
    plt.axhline(0, linestyle=':', color='black')
    plt.ylim([-0.2,1.2])
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('$x$')
    plt.ylabel('$phi(x)$')
    #Save each graph to the graphs_tables folder to be used in report.
    #Allow graph to save into graphs_tables folder.
    #File name reflects resolution to avoid overwriting.
    input('press return to save file and continue')
    plt.savefig('graphs_tables/LW_analysis_%d_%d_%d.pdf'%(nx,nt,condition))

LW_graph(100,100,2)
