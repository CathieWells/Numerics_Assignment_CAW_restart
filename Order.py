#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:52:34 2018

@author: caw4618
"""
import matplotlib.pyplot as plt
import numpy as np
import math
from tabulate import tabulate
# Read in relevant linear advection scheme, initial conditions and other
# code associated with this application
from Initial_conditions import *
from CTCS import *
from FTBS import *
from LW import *
from Error_checks import *
from math import log
#Choose Courant number and condition details.  Include short condition 
#description for file names.
def error_graph(c,initial_condition,condition,u):
    #Set spatial range and speed.
    Xmin=0
    Xmax=1

    #Values of nx to test
    nx_values=[4,8,16,32,64,128,256,512,1024]    
    #Set up array for results
    error_space=np.zeros((4,len(nx_values)))
    #Put space intervals into top line of array.
    #error_space[0]=np.linspace(0.001,0.02,num_dxs)
    #For each interval work out dx and dependent variables.
    for i in range(len(nx_values)):        
        nx=nx_values[i]
        dx=(Xmax-Xmin)/nx
        dt=dx*c/u
        nt=int(1/dt)#TODO: Rounding is not ideal
        X=np.linspace(Xmin,Xmax,nx)
        #Generate initial conditions and final analytic solution.
        phiOld=initial_condition(X) #
        phiAnalytic=initial_condition((X-c*nt*dx)%(Xmax-Xmin))


        #Work out numerical model and mean square error using each method.
        error_space[0][i]=dx
        phi1=FTBS(phiOld.copy(),c,nt)
        error_space[1][i]=(l2ErrorNorm(phi1,phiAnalytic))
        phi2=CTCS(phiOld.copy(),c,nt)
        error_space[2][i]=(l2ErrorNorm(phi2,phiAnalytic))
        phi3=LW(phiOld.copy(),c,nt)
        error_space[3][i]=(l2ErrorNorm(phi3,phiAnalytic))
    order_array=np.zeros((3,8))   
    for m in range (0,3):
        for k in range (0,8):
            order_array[m][k]=(np.log(error_space[m+1][k+1])\
             -np.log(error_space[m+1][k]))/(np.log(error_space[0][k+1])\
             -np.log(error_space[0][k]))
    #Print values for rate of convergence in a table.
    for m in range (0,3):
        l2_norm=error_space[m+1]
        conv_rate=order_array[m]
        table=zip(nx_values,l2_norm,conv_rate)
    
        #Send table to graphs_tables folder. 
        file=open("order_figs/Errors_%d_%d_%d_%s.txt"%(100*c,m,10*u,condition),"w")
        file.write(tabulate(table, headers=\
        ["No. spatial steps", "l2 error norm","rate of convergence"]\
        ,floatfmt=".3f",tablefmt='orgtbl'))
        file.close()
    
    
    
    x=error_space[0]
    #Graph answers for when this finally works properly!
    # Plot inital conditions, analytic result and numerical model for
    #for given resolution.
    font = {'size'   : 20}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(x,x*(error_space[1][8]/error_space[0,8]),label='First Order',
             color='midnightblue',linestyle=':')
    plt.plot(x,(x**2)*(error_space[2][8]/(error_space[0][8])**2),
             label='Second Order', color='darkolivegreen',linestyle=':')
    plt.plot(x, error_space[1], label='FTBS', color='red',
             linestyle='--', linewidth=2,marker='x')
    plt.plot(x, error_space[2], label='CTCS', color='blue', 
             linestyle='--', linewidth=2,marker='*')
    plt.plot(x, error_space[3], label='LW', color='green',
             linestyle='--', linewidth=2,marker='s')
    plt.axhline(0, linestyle=':', color='black')
    plt.legend(bbox_to_anchor=(1.15 , 1.1))
    plt.xlabel('dx')
    plt.ylabel('L2 error norm')
    plt.xscale('log')
    plt.yscale('log')
    #Save each graph to the graphs_tables folder to be used in report.
    #Allow graph to save into graphs_tables folder.
    #File name reflects resolution to avoid overwriting.
    input('press return to save file and continue')
    plt.savefig('order_figs/Error_analysis_%d_%d_%s.pdf'%(100*c,10*u,condition), 
    bbox_inches = "tight")
    return()


error_graph(0.25,lambda X:cosBell(X,0.0,0.75),'bell',4)

#error_graph(0.4,lambda X:mixed(X,0.0,0.1,0.2,0.4),'mixed',2)
#error_graph(0.4,lambda X:squareWave(X),'square',2)




