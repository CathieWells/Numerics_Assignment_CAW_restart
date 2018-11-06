#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:23:58 2018

@author: caw4618
"""


    
import matplotlib.pyplot as plt
import numpy as np
import time
# Read in all the linear advection schemes, initial conditions and other
# code associated with this application
from Initial_conditions import *
from LW import *
from FTBS import *
from CTCS import *
from datetime import datetime



#Call functions to solve each scheme to a certain number of time steps
#for fixed spatial resolution. 
#This means advection speed will vary as courant number is fixed.
def comp_cost():
    "Advect the initial cos bell wave conditions using various advection"
    "schemes and compare results"

    # Fixed parameters throughout for all three schemes.
    Xmin = 0
    Xmax = 1
    c = 0.2
    nx=50
    
    
    # Derived parameters for 
    dx = (Xmax - Xmin)/nx
    
    # Spatial points for plotting and for defining initial conditions
    X = np.arange(Xmin, Xmax, dx)
    
    # Initial conditions
    phiOld = cosBell(X, 0, 0.75)
    
    #Set up array to hold timing for each calculation.
    cost=np.zeros((3,10))
    a = np.zeros(1000)
    #Start loop to alter timesteps.
    #Compute end results for times at 10 step intervals.
    for i in range (0,10):
        nt=(i+1)*20
    
        # Advect the profile using finite difference
        #for all the time step variations for each of the three schemes
        #Put these results into a matrix.
        
        
        for j in range (0,1000):
            start = time.time()
            FTBS(phiOld.copy(), c, nt)
            a[j]=float(time.time()-start)
        cost[0][i]=a.min()
        for k in range (0,1000):
            start = time.time()
            CTCS(phiOld.copy(), c, nt)
            a[k]=float(time.time()-start)
        cost[1][i]=a.min()
        for l in range (0,1000):
            start = time.time()
            FTBS(phiOld.copy(), c, nt)
            a[l]=float(time.time()-start)
        cost[2][i]=a.min()
        
    
    #Define x for graph axes
    x=np.arange(20,220,20)
    
    
    #Take each line of the matrix out as an array for plotting.
    FTBS_cost=cost[0]
    CTCS_cost=cost[1]
    LW_cost=cost[2]
    
    
    # Plot the solutions for all schemes on one set of axes.
    font = {'size'   : 20}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(x,FTBS_cost , label='FTBS', color='blue')
    plt.plot(x, CTCS_cost, label='CTCS', color='red')
    plt.plot(x, LW_cost, label='LW', color='green')
    plt.axhline(0, linestyle=':', color='black')
    plt.ylim([-0.001,0.007])
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('$Time steps$')
    plt.ylabel('Computational time(s)')
    #Allow graph to save into graphs_tables folder.
    input('press return to save file and continue')
    plt.savefig('graphs_tables/3scheme_time_analysis', 
    bbox_inches = "tight")
    
comp_cost()


    