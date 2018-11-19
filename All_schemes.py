#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 19:51:37 2018

@author: caw4618
"""
#Open necessary code.
import numpy as np
#Create Forwards in Time Backwards in Space code.
def FTBS(phiOld, c, nt):
    "Linear advection of profile in phiOld using FTBS, Courant number c"
    "for nt time-steps"
#Set number of space time steps to follow length of initial data given.
    nx = len(phiOld)

#Create an array to store the current copy of phi values at x gridpoints.
    phi = phiOld.copy()

# For each of the nt time steps, go through the loop.
    for it in range(nt):
#Calculate new time step phi based on previous time step phi in
#current and previous positions.
# Use mod nx on spatial position to allow looping of values, 
#thus giving periodic boundary conditions.
        for j in range(nx):
            phi[j] = phiOld[j] - c*(phiOld[(j)%nx] - phiOld[(j-1)%nx])
#Move current results into phiOld array, to be referred to for next
#timestep.
        phiOld = phi.copy()
#Output phi at final timestep for all x gridpoints.
    return phi

#Create Centred in Time Centred in Space code.
def CTCS(phiOld, c, nt):
    "Linear advection of profile in phiOld using CTCS, Courant number c"
    "for nt time-steps"
#Set space to follow length of initial data given.
    nx = len(phiOld)

#New time-step array for phi as scheme requires centring in time.
    phi = phiOld.copy()
    phi1 = phiOld.copy()
    phi2 = phiOld.copy()
    
# FTCS to generate first line of new data.
    for j in range(nx):
        phi2[j] = phiOld[j] - 0.5*c*(phiOld[(j+1)%nx] - phiOld[(j-1)%nx])    
# CTCS for each time-step after the first line has been generated.
    for it in range(nt-1):
# Loop through all space using mod nx to ensure periodic
# boundary conditions.
        for j in range(nx):
            phi[j] = phi1[j] - c*(phi2[(j+1)%nx] - phi2[(j-1)%nx])
# Update arrays for next time-step.
        phi1=phi2.copy()
        phi2=phi.copy()
     
    return phi

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

#Create Warming and Beam code.
def WB(phiOld, c, nt):
    "Linear advection of profile in phiOld using WB, Courant number c"
    "for nt time-steps"
#Set space to follow length of initial data given.
    nx = len(phiOld)

#Sets up an array for newly calculated phi values.
    phi = phiOld.copy()

# WB for each time-step using simplified equation with no half steps.
    for it in range(nt):
#Using mod nx on spatial positions ensures periodic boundary conditions.
        for j in range(nx):
            phi[j] = phiOld[(j)%nx] - 0.5*c*\
                     (3*phiOld[(j)%nx]-4*phiOld[(j-1)%nx] +phiOld[(j-2)%nx])\
                     +0.5*c**2*\
                     (phiOld[(j)%nx] - 2*phiOld[(j-1)%nx]+phiOld[(j-2)%nx])
        
#Sends previous phi values to phiOld array and loops round to 
#calculate phi at new time step.
        phiOld = phi.copy()
#Returns phi values at each spatial step for final time step.
    return phi

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