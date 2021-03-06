#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:14:49 2018

@author: caw4618
"""


#Read in extra code.
import matplotlib.pyplot as plt
import numpy as np
# Read in all the linear advection schemes, initial conditions and other
# code associated with this application
from Initial_conditions import *
from LW import *
from FTBS import *
from CTCS import *
from Error_checks import *
from tabulate import tabulate


def main(nx,nt,c,type):
    "Advect given initial conditions using various advection schemes and"
    "compare results"

# Fixed parameters throughout for all three schemes.
    xmin = 0
    xmax = 1
   
    
# Derived parameters.
    dx = (xmax - xmin)/nx
    
# Spatial points for plotting and for defining initial conditions.
    x = np.arange(xmin, xmax, dx)

# Initial conditions
# Exact solution is the initial condition shifted around the domain
    if type=='square':
        phiOld = squareWave(x)
        phiAnalytic = squareWave((x - c*nt*dx)%(xmax - xmin))
    elif type=='cos':
        phiOld = cosBell(x, 0, 0.75)
        phiAnalytic = cosBell((x - c*nt*dx)%(xmax - xmin), 0, 0.75)
    elif type=='sine':
        phiOld = sineWave(x)
        phiAnalytic = sineWave((x - c*nt*dx)%(xmax - xmin))
    else:
        phiOld = mixed(x, 0, 0.1,0.2,0.4)
        phiAnalytic = mixed((x - c*nt*dx)%(xmax - xmin), 0, 0.1,0.2,0.4)
        
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
    
#Set up array for min_max data.
    min_max=np.zeros((7,nt))
#Check max and min at each timestep for each scheme:
    for i in range (nt+1):
        min_max[0][i-1]=np.min(FTBS(phiOld.copy(), c, i))
        min_max[1][i-1]=np.max(FTBS(phiOld.copy(), c, i))
        min_max[2][i-1]=np.min(CTCS(phiOld.copy(), c, i))
        min_max[3][i-1]=np.max(CTCS(phiOld.copy(), c, i))
        min_max[4][i-1]=np.min(LW(phiOld.copy(), c, i))
        min_max[5][i-1]=np.max(LW(phiOld.copy(), c, i))
        min_max[6][i-1]=i
        
#Send table to figures folder. 
    file=open("figures/Table_errors_%d_%d_%s.txt"%(nx,nt,type),"w")
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
    plt.ylim([-0.4,1.5])
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('$x$')
    plt.ylabel('phi(x)')
#Allow graph to save into figures folder.
#File name reflects resolution to avoid overwriting.
    plt.savefig('figures/3scheme_sanalysis_%d_%d_%s.pdf'%(nx,nt,type), 
    bbox_inches = "tight")
    
#Plot bounds at each timestep for each scheme.
    x=min_max[6]
    font = {'size'   : 20}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(x, min_max[0], label='Min for FTBS', color='blue',\
    linestyle='--', linewidth=2)
    plt.plot(x, min_max[1], label='Max for FTBS', color='red',\
    linestyle='--', linewidth=2)
    plt.plot(x, min_max[2], label='Min for CTCS', color='green',\
             linestyle='--', linewidth=2)
    plt.plot(x, min_max[3], label='Max for CTCS', color='purple',\
             linestyle='--', linewidth=2)
    plt.plot(x, min_max[4], label='Min for LW', color='pink',\
             linestyle='--', linewidth=2)
    plt.plot(x, min_max[5], label='Max for LW', color='brown',\
             linestyle='--', linewidth=2)
    plt.plot((0, 40), (0, 0), label='Min bound',color='darkolivegreen',\
             linestyle=':', linewidth=1)
    plt.plot((0, 40), (1, 1), label='Max bound',color='midnightblue',\
             linestyle=':', linewidth=1)
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('no of time steps')
    plt.ylabel('phi(x)')
#Allow graph to save into figures folder.
#File name reflects resolution to avoid overwriting.
    plt.savefig('figures/min_max_analysis_%d_%s.pdf'%(nx,type), 
    bbox_inches = "tight")
    
    return()


    

   