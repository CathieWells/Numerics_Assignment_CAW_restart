#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:14:49 2018

@author: caw4618
"""

import matplotlib.pyplot as plt
import numpy as np
# read in all the linear advection schemes, initial conditions and other
# code associated with this application.
from Initial_conditions import *
from LW import *
from WB import *
from Combi import *
from Error_checks import *
from tabulate import tabulate

#The main_square function allows all three schemes to be compared at once
#looking at both graphing and a table of errors. 
#Function is called using resolution parameters.
def con_square(nx,nt,c):
    "Advect the initial square wave conditions using various advection schemes"
    "and compare results"

# Fixed parameters throughout for all three schemes.
    xmin = 0
    xmax = 1
   
    
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
    phiLW = LW(phiOld.copy(), c, nt)
    phiWB = WB(phiOld.copy(), c, nt)
    phiCombi = Combi(phiOld.copy(),c,nt)
    
# Calculate and structure error norms in a table.
    Scheme=["LW","WB","Combi"]
    l2_error=[l2ErrorNorm(phiLW, phiAnalytic),\
    l2ErrorNorm(phiWB, phiAnalytic),l2ErrorNorm(phiCombi, phiAnalytic)]
    linf_error=[lInfErrorNorm(phiLW, phiAnalytic),\
    lInfErrorNorm(phiWB, phiAnalytic),lInfErrorNorm(phiCombi, phiAnalytic)]
    table=zip(Scheme,l2_error,linf_error)
    
#Set up array for min_max data.
    min_max=np.zeros((7,nt))
#Check max and min at each timestep for each scheme:
    for i in range (nt+1):
        min_max[0][i-1]=np.min(LW(phiOld.copy(), c, i))
        min_max[1][i-1]=np.max(LW(phiOld.copy(), c, i))
        min_max[2][i-1]=np.min(WB(phiOld.copy(), c, i))
        min_max[3][i-1]=np.max(WB(phiOld.copy(), c, i))
        min_max[4][i-1]=np.min(Combi(phiOld.copy(), c, i))
        min_max[5][i-1]=np.max(Combi(phiOld.copy(), c, i))
        min_max[6][i-1]=i
        
#Send table to figures folder. 
    file=open("figures/Conclusion_Square_errors_%d_%d.txt"%(nx,nt),"w")
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
    plt.plot(x, phiLW, label='LW', color='green')
    plt.plot(x, phiWB, label='WB', color='orange')
    plt.plot(x, phiCombi, label='Combi', color='cyan')
    plt.axhline(0, linestyle=':', color='black')
    plt.ylim([-0.4,1.5])
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('$x$')
    plt.ylabel('phi(x)')
#Allow graph to save into graphs_tables folder.
#File name reflects resolution to avoid overwriting.
    plt.savefig('figures/conclusion_square_analysis_%d_%d.pdf'%(nx,nt), 
    bbox_inches = "tight")
    
#Plot bounds at each timestep for each scheme.
    x=min_max[6]
    font = {'size'   : 20}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(x, min_max[0], label='Min for LW', color='blue',\
    linestyle='--', linewidth=2)
    plt.plot(x, min_max[1], label='Max for LW', color='red',\
    linestyle='--', linewidth=2)
    plt.plot(x, min_max[2], label='Min for WB', color='green',\
             linestyle='--', linewidth=2)
    plt.plot(x, min_max[3], label='Max for WB', color='purple',\
             linestyle='--', linewidth=2)
    plt.plot(x, min_max[4], label='Min for Combi', color='pink',\
             linestyle='--', linewidth=2)
    plt.plot(x, min_max[5], label='Max for Combi', color='brown',\
             linestyle='--', linewidth=2)
    plt.plot((0, nt), (0, 0), label='Min bound',color='darkolivegreen',\
             linestyle=':', linewidth=1)
    plt.plot((0, nt), (1, 1), label='Max bound',color='midnightblue',\
             linestyle=':', linewidth=1)
    plt.ylim([-1,2])
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('no of time steps')
    plt.ylabel('phi(x)')
#Allow graph to save into figures folder.
#File name reflects resolution to avoid overwriting.
    plt.savefig('figures/conclusion_min_max_square_analysis_%d.pdf'%(nx), 
    bbox_inches = "tight")
    

    return()
con_square(40,80,0.5)









