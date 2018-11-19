# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Import necessary code.
import numpy as np
#Create Lax Wendroff code.
def LW(phiOld, c, nt):
    "Linear advection of profile in phiOld using LW, Courant number c"
    "for nt time-steps"
#Set space to follow length of initial data given.
    nx = len(phiOld)

#Sets up an array for newly calculated phi values.
    phi = phiOld.copy()

# LW for each time-step using simplified equation with no half steps.
    for it in range(nt):
#Using mod nx on spatial positions ensures periodic boundary conditions.
        for j in range(nx):
            phi[j] = phiOld[(j)%nx] - 0.5*c*\
                     (phiOld[(j+1)%nx] - phiOld[(j-1)%nx])\
                     +0.5*c**2*\
                     (phiOld[(j+1)%nx] - 2*phiOld[(j)%nx]+phiOld[(j-1)%nx])
        
#Sends previous phi values to phiOld array and loops round to
#calculate phi at new time step.
        phiOld = phi.copy()
#Returns phi values at each spatial step for final time step.
    return phi
