# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
            phi[j] = phiOld[j] - c*\
                     (phiOld[(j)%nx] - phiOld[(j-1)%nx])
        #Move current results into phiOld array, to be referred to for next
        #timestep.
        phiOld = phi.copy()
    #Output phi at final timestep for all x gridpoints.
    return phi
