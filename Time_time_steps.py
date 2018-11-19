#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:23:58 2018

@author: caw4618
"""


#Read in extra code.   
import matplotlib.pyplot as plt
import numpy as np
import time
# Read in all the linear advection schemes, initial conditions and other
# code associated with this application
from Initial_conditions import *
from LW import *
from FTBS import *
from CTCS import *


#Call functions to solve each scheme to a certain number of time steps
#for fixed spatial resolution. 
#This means advection speed will vary as courant number is fixed.
def comp_time_cost(type):
    "Advect the initial conditions fed in using various advection"
    "schemes for given c and time process"

# Fixed parameters throughout for all three schemes.
    xmin = 0
    xmax = 1
    nx=100
    c=0.5
    
    
# Derived parameters for 
    dx = (xmax - xmin)/nx
    
# Spatial points for plotting and for defining initial conditions
    x = np.arange(xmin, xmax, dx)
  
#Set up array to hold timing for each calculation.
    cost=np.zeros((6,10))
    a = np.zeros(20)
#Specifiy initial conditions to use for input name.
    if type=='square':
        phiOld = squareWave(x)
    else:
        phiOld = cosBell(x, 0, 0.75)
#Start loop to alter timesteps.
#Compute end results for times at 20 step intervals.
    for i in range (0,10):
        nt=(i+1)*20
#Collect time for each scheme at each time step once.
        start = time.time()
        FTBS(phiOld.copy(), c, nt)
        cost[3][i]=float(time.time()-start)
        start = time.time()
        CTCS(phiOld.copy(), c, nt)
        cost[4][i]=float(time.time()-start)
        start = time.time()
        LW(phiOld.copy(), c, nt)
        cost[5][i]=float(time.time()-start)
        
# Advect the profile using finite difference/volume
#for all the time step variations for each of the three schemes
#Put timings for each time step into an array.
#Put minimum time from each array into a 2D array.
        
        for j in range (0,20):
            start = time.time()
            FTBS(phiOld.copy(), c, nt)
            a[j]=float(time.time()-start)
        cost[0][i]=a.min()
        for k in range (0,20):
            start = time.time()
            CTCS(phiOld.copy(), c, nt)
            a[k]=float(time.time()-start)
        cost[1][i]=a.min()
        for l in range (0,20):
            start = time.time()
            LW(phiOld.copy(), c, nt)
            a[l]=float(time.time()-start)
        cost[2][i]=a.min()
 
#Define x for graph axes
    X=np.arange(20,220,20)
    
    
# Plot the solutions for all schemes on one set of axes for single timing.
    font = {'size'   : 20}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(X,cost[3] , label='FTBS', color='blue',\
             linestyle='--', marker='s')
    plt.plot(X, cost[4], label='CTCS', color='green',\
             linestyle='--', marker='^')
    plt.plot(X, cost[5], label='LW', color='pink',\
             linestyle='--', marker='o')
    plt.axhline(0, linestyle=':', color='black')
    plt.ylim([-0.001,0.03])
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('No. of time steps')
    plt.ylabel('Computational time(s)')
#Allow graph to save into figures folder.
    plt.savefig('figures/3scheme_single_time_analysis_%s.pdf'%(type), 
    bbox_inches = "tight")
    
    
# Plot the solutions for all schemes on one set of axes for min over 100.
    font = {'size'   : 20}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(X,cost[0] , label='FTBS', color='blue',\
             linestyle='--', marker='s')
    plt.plot(X, cost[1], label='CTCS', color='green',\
             linestyle='--', marker='^')
    plt.plot(X, cost[2], label='LW', color='pink',\
             linestyle='--', marker='o')
    plt.axhline(0, linestyle=':', color='black')
    plt.ylim([-0.001,0.03])
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('No. of time steps')
    plt.ylabel('Computational time(s)')
#Allow graph to save into figures folder.
    plt.savefig('figures/3scheme_100min_time_analysis_%s.pdf'%(type), 
    bbox_inches = "tight")
    return()
    
comp_time_cost('cos')
comp_time_cost('square')
    


    