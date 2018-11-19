#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:13:42 2018

@author: caw4618
"""
#Read in extra code.
import numpy as np
import math

#Calculates the mean square error between analytic and modelled results.
def l2ErrorNorm(phi, phiExact):
    "Calculates the l2 error norm (RMS error) of phi in comparison to"
    "phiExact"
    
# Reads phi and phiExact in from frame file.
    phiError = phi - phiExact
    l2 = np.sqrt(sum(phiError**2)/sum(phiExact**2))
    return l2

#Calculates the L inifinity norm between analytic and modelled results.
def lInfErrorNorm(phi, phiExact):
    "Calculates the linf error norm (maximum normalised error) in comparison"
    "to phiExact"
#Reads phi and phiExact in from frame file.
    phiError = phi - phiExact
    return np.max(np.abs(phiError))/np.max(np.abs(phiExact))




