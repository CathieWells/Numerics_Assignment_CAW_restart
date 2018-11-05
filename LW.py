# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
#Create Lax Wendroff code.
def LW(phiOld, c, nt):
    "Linear advection of profile in phiOld using LW, Courant number c"
    "for nt time-steps"
    #Set space to follow length of initial data given.
    nx = len(phiOld)

    # new time-step array for phi
    phi = phiOld.copy()

    # LW for each time-step
    for it in range(nt):
        # Loop through all space using remainder after division (%)
        # to cope with periodic boundary conditions
        for j in range(nx):
            phi[j] = phiOld[j] - 0.5*c*\
                     (phiOld[(j+1)%nx] - phiOld[(j-1)%nx])\
                     +0.5*c**2*\
                     (phiOld[(j+1)%nx] - 2*phiOld[(j)%nx]+phiOld[(j-1)%nx])
        
        # update arrays for next time-step
        phiOld = phi.copy()

    return phi

