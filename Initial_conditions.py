#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:10:03 2018

@author: caw4618
"""

import numpy as np

#Sets up a square wave for use in advection schemes.
def squareWave(x,alpha=0.1,beta=0.3):
    "A square wave as a function of position, x, which is 1 between alpha"
    "and beta and zero elsewhere. The initialisation is conservative so"
    "that each phi contains the correct quantity integrated over a region"
    "a distance dx/2 either side of x"
    #Sets up an array .
    phi = np.zeros_like(x)
    #Creates uniform grid spacing across 0 to 1.
    dx = x[1] - x[0]
    # Creates square wave as zero until wave.
    for j in range(1,len(x)-1):
        #Gives position of edges of the grid box, west and east. 
        xw = x[j] - 0.5*dx
        xe = x[j] + 0.5*dx
        
        #Calculates phi at each spatial position based on given parameters.
        phi[j] = max((min(beta, xe) - max(alpha, xw))/dx, 0)
    #Returns array of initial phi values at each x grid position.
    return phi

#Sets up a bell wave based on cosine curve for use in advection schemes.
def cosBell(x, alpha=0, beta=0.5):
    "Function defining a cosine bell as a function of position, x"
    "between alpha and beta with default parameters 0, 0.5"
    #Using parameters set in function definition, creates bell wave.
    width = beta - alpha
    #Use of lambda allows single line definition.
    bell = lambda x: 0.5*(1 - np.cos(2*np.pi*(x-alpha)/width))
    #Gives zero except in defined range where bell occurs.
    return np.where((x<beta) & (x>=alpha), bell(x), 0.)

#Sets up a wave incorporating both a bell curve and a square wave.
#Parameters are set from previous functions.
def mixed(x, a, b, c, d):
    "A square wave in one location and a cosine bell in another"
    #Gives zero except in defined range where bell or square wave occurs.
    return 1-(1-cosBell(x, a, b))*(1-squareWave(x, c, d))