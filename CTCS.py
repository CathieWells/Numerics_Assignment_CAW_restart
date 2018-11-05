# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
#Create Centred in Time Centred in Space code.
def CTCS(phiOld, c, nt):
    "Linear advection of profile in phiOld using CTCS, Courant number c"
    "for nt time-steps"
    #Set space to follow length of initial data given.
    nx = len(phiOld)

    # new time-step array for phi as scheme requires centring in time.
    phi1 = phiOld.copy()
    phi2 = phiOld.copy()
    phi3 = phiOld.copy()
    # FTCS to generate first line of new data.
    for j in range(nx):
        phi2[j] = phiOld[j] - 0.5*c*\
        (phiOld[(j+1)%nx] - phiOld[(j-1)%nx])    
    # CTCS for each time-step after the first line has been generated
    for it in range(nt-1):
        # Loop through all space using remainder after division (%)
        # to cope with periodic boundary conditions
        for j in range(nx):
            phi3[j] = phi1[j] - c*(phi2[(j+1)%nx] - phi2[(j-1)%nx])
            # update arrays for next time-step
            phi1=phi2.copy()
            phi2=phi3.copy()
     

    return phi2

