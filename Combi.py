#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 19:51:37 2018

@author: caw4618
"""
#New scheme combining LW and WB.
def Combi(phiOld, c, nt):
    "Linear advection of profile in phiOld using LW, Courant number c"
    "for nt time-steps after a discontinuity and WB before"
#Set space to follow length of initial data given.
    nx = len(phiOld)
    dx =1/nx
#Sets up an array for newly calculated phi values.
    phi = phiOld.copy()
    
#LW and WB for each time-step using simplified equation with no half steps.
    for i in range(nt):
#Using mod nx on spatial positions ensures periodic boundary conditions.
        for j in range(nx):
#Code for LW if after centre of square wave and WB before.
            if j*dx<=(0.2+i*dx*c):
                phi[j]=phi[j] = phiOld[(j)%nx] - 0.5*c*\
                     (3*phiOld[(j)%nx]-4*phiOld[(j-1)%nx] +phiOld[(j-2)%nx])\
                     +0.5*c**2*\
                     (phiOld[(j)%nx] - 2*phiOld[(j-1)%nx]+phiOld[(j-2)%nx])
            else:
                phi[j]=phiOld[(j)%nx] - 0.5*c*\
                     (phiOld[(j+1)%nx] - phiOld[(j-1)%nx])\
                     +0.5*c**2*\
                     (phiOld[(j+1)%nx] - 2*phiOld[(j)%nx]+phiOld[(j-1)%nx])
#Sends previous phi values to phiOld array and loops round to 
#calculate phi at new time step.
        phiOld = phi.copy()
#Returns phi values at each spatial step for final time step.
    return phi


