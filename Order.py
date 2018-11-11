#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:52:34 2018

@author: caw4618
"""
import matplotlib.pyplot as plt
import numpy as np
import math
# Read in relevant linear advection scheme, initial conditions and other
# code associated with this application
from Initial_conditions import *
from CTCS import *
from FTBS import *
from LW import *
from Error_checks import *
from math import log
#Choose Courant number and condition (1:Cos Bell, 2:Square Wave 3:Mixed)
def error_graph(c,condition):
    #Set spatial range and speed.
    Xmin=0
    Xmax=1
    u=5
    #Set up array for results
    error_space=np.zeros((4,20))
    #Put space intervals into top line of array.
    error_space[0]=np.arange(0.01,0.21,0.01)
    #For each interval work out dx and dependent variables.
    for i in range (1,21):
        dx=error_space[0][i-1]
        nx=int((Xmax-Xmin)/dx)
        dt=dx*c/u
        nt=int(1/dt)
        X=np.arange(Xmin,Xmax,dx)
        #Generate initial conditions and final analytic solution.
        if condition==1:
            phiOld=cosBell(X,0,0.75)
            phiAnalytic=cosBell((X-c*nt*dx)%(Xmax-Xmin),0,0.75)
        elif condition==2:
            phiOld=squareWave(X)
            phiAnalytic=squareWave((X-c*nt*dx)%(Xmax-Xmin))
        else:
            phiOld=mixed(X,0,0.1,0.2,0.4)
            phiAnalytic=mixed((X-c*nt*dx)%(Xmax-Xmin),0,0.1,0.2,0.4)
        #Work out numerical model and mean square error using each method.
        phi1=FTBS(phiOld.copy(),c,nt)
        error_space[1][i-1]=(l2ErrorNorm(phi1,phiAnalytic))
        phi2=CTCS(phiOld.copy(),c,nt)
        error_space[2][i-1]=(l2ErrorNorm(phi2,phiAnalytic))
        phi3=LW(phiOld.copy(),c,nt)
        error_space[3][i-1]=(l2ErrorNorm(phi3,phiAnalytic))
    
    x=error_space[0]
    #Graph answers for when this finally works properly!
    # Plot inital conditions, analytic result and numerical model for
    #for given resolution.
    font = {'size'   : 20}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(x,x*(error_space[1][0]/error_space[0][0]),label='First Order',
             color='midnightblue',linestyle=':')
    plt.plot(x,(x**2)*(error_space[2][0]/(error_space[0][0])**2),label='Second Order',
             color='darkolivegreen',linestyle=':')
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
    plt.savefig('graphs_tables/Error_analysis_%d.pdf'%(condition), 
    bbox_inches = "tight")
    return()
error_graph(0.2,1)




