#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 08:44:43 2018

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


#Function to find rate of convergence for bell and square waves.
def con_graph():
    "Advect bell and square initial conditions using various advection"
    "schemes and compare results for rates of convergence" 

    # Fixed parameters throughout for all three schemes.
    xmin = 0
    xmax = 10
    c = 0.2
    nx=100
    Totalt=10
    u=2
    
    # Derived parameters
     error_space[0]=np.arange(0.01,0.21,0.01)
    dx = (xmax - xmin)/nx
    dt = c*dx/u
    # Spatial points for plotting and for defining initial conditions
    x = np.arange(xmin, xmax, dx)
    #Set up array for convergence results from loop.
    converg=np.zeros((2,3))
    #Set counter.
    i=1
    while i <=2:
        if i==1:
            # Initial conditions
            phiOld = cosBell(x, 0, 0.75)
            # Exact solution is the initial condition shifted around the domain
            phiAnalytic = cosBell((x - c*nt*dx)%(xmax - xmin), 0, 0.75)
        else:
            # Initial conditions
            phiOld = squareWave(x)
            # Exact solution is the initial condition shifted around the domain
            phiAnalytic = squareWave((x - c*nt*dx)%(xmax - xmin))
            
        # Advect the profile using finite difference
        #for all the time steps for each of the three schemes
        phiFTBS = FTBS(phiOld.copy(), c, nt)
        phiCTCS = CTCS(phiOld.copy(), c, nt)
        phiLW = LW(phiOld.copy(), c, nt)
    
        # Calculate rates of convergence and send to array.
        converg[i-1]=[Con_Rate(phiFTBS, phiAnalytic),\
        Con_Rate(phiCTCS, phiAnalytic),Con_Rate(phiLW, phiAnalytic)]
        #Update counter
        i=i+1
            
    print(converg)       
    #Set up table.       
    Scheme=["FTBS","CTCS","LW"]    
    table=zip(Scheme,converg[0],converg[1])
    #Send table to graphs_tables folder. 
    file=open("graphs_tables/Con_rates.txt","w")
    file.write(tabulate(table, headers=\
    ["Scheme", "Bell","Square"]\
    ,floatfmt=".3f",tablefmt='orgtbl'))
    file.close()
   
con_table()
 
