# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 05:18:45 2020

@author: kartik

This code provides several signal functions to be used for filtering or similar applications.
"""

import math as m
import numpy as np

def Sinusoidal(r):
    '''
    1. if r = 0 : Simple Sinusoidal Function
    2. if r < 0 : Real and Imaginary parts are sinusoidal multiplied with a decaying exponential.
       Such signals arise in stable systems.
    3. if r > 0 : Real and Imaginary parts are sinusoidal multiplied with a growing exponential.
       Such signals arise in unstable systems.
       
    User can modify disturbances and signal duration within the function itself
    '''

    # The Sensor Signal
    dt = 0.1
    t = np.arange(0,50,dt)
    Y = [((3*m.exp(r*t)*m.sin(t + 3) + 2) + np.random.normal(0,dt))for t in range(len(t))]
    
    # Adding Disturbances to the Signal
    
    Y[100] += 2.4
    Y[150] -= 2.6
    Y[200] += 6.1
    Y[250] -= 2.4
    Y[350] += 3.9
    
    D1 = 24*np.random.normal(0,0.4,8) 
    D2 = 12*np.random.normal(0,0.1,6) 
    D3 = 18*np.random.normal(0,0.2,4) 
    D4 = 24*np.random.normal(0,0.3,5) 
    
    Y[175:175 + len(D1)] = D1
    Y[275:275 + len(D2)] = D2
    Y[375:375 + len(D3)] = D3
    Y[475:475 + len(D4)] = D4
    
    # Signal Measures
    
    Mean_of_Signal = np.mean(Y)
    Standard_deviation = np.std(Y)
    Mean_line = np.ones(len(Y), dtype = int)*Mean_of_Signal
    Bound_1 = np.ones(len(Y), dtype = int)*(Mean_of_Signal+Standard_deviation)
    Bound_2 = np.ones(len(Y), dtype = int)*(Mean_of_Signal-Standard_deviation)
    
    return [Y, Mean_of_Signal, Standard_deviation, Mean_line, Bound_1, Bound_2]

def SignalA(f):
    '''
    f = frequency of signal
    
    User can modify disturbances and signal duration within the function itself
    '''

    # The Sensor Signal
    dt = 0.1
    t = np.arange(0,50,dt)
    Y = [((4*m.sin(f*t + 3) + 6*m.cos(f*t + 3) + 2) + np.random.normal(0,dt))for t in range(len(t))]
    
    # Adding Disturbances to the Signal
    
    Y[120] += 4.6
    Y[180] -= 6.2
    Y[230] += 6.8
    Y[210] -= 5.4
    Y[390] += 4.5
    
    D1 = 20*np.random.normal(0,0.6,4) 
    D2 = 18*np.random.normal(0,0.2,9) 
    D3 = 16*np.random.normal(0,0.7,7) 
    D4 = 24*np.random.normal(0,0.9,3) 
    
    Y[150:150 + len(D1)] = D1
    Y[250:250 + len(D2)] = D2
    Y[350:350 + len(D3)] = D3
    Y[450:450 + len(D4)] = D4
    
    # Signal Measures
    
    Mean_of_Signal = np.mean(Y)
    Standard_deviation = np.std(Y)
    Mean_line = np.ones(len(Y), dtype = int)*Mean_of_Signal
    Bound_1 = np.ones(len(Y), dtype = int)*(Mean_of_Signal+Standard_deviation)
    Bound_2 = np.ones(len(Y), dtype = int)*(Mean_of_Signal-Standard_deviation)
    
    return [Y, Mean_of_Signal, Standard_deviation, Mean_line, Bound_1, Bound_2]
    