# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:39:58 2020

@author: kartik

This code implements a Kalman Filter for outlier rejection in a 1-D signal.
Mahalanobis Distance is used for dealing with the outliers.
"""

import math as m
import numpy as np
import matplotlib.pyplot as plt
import Signals

# The Sensor Signal

[Y, Mean_of_Signal, Standard_deviation, Mean_line, Bound_1, Bound_2] = Signals.SignalA(-0.05)

fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.plot(Y, label = "Sensor Signal", color = 'Blue')
ax1.plot(Mean_line,  label = "mean", color = 'Grey', linestyle = '-')
ax1.plot(Bound_1, label = "Standard Deviation", color = 'Grey',  linestyle = '--')
ax1.plot(Bound_2,  color = 'Grey',  linestyle = '--')
ax1.set_xlabel("Time")
ax1.set_ylabel("Sensor Signal")
ax1.legend() 

# The Kalman Filter

State_Estimate = np.zeros((len(Y),1)) # Y = Sensor Signal
P = np.zeros((len(Y),1)) # Predicition Covariance Matrix 
P[0] = 0.48
I = np.eye(1)
# Initialize Covariance Matrices

A = np.array([1]) # State Transition Matrix
B = np.array([1]) # Observation Matrix
w = np.array([0.4]) # Process Noise Covariance Matrix 
v = np.array([0.09]) # Measurement Noise Covariance Matrix

Input_Matrix = np.array([0])
Control_Matrix = np.array([0])


for i in range(len(Y)):
    State_Estimate[0] = Y[0]
    
    # Prediction Step
    State_Estimate[i] = np.dot(A, State_Estimate[i-1]) + np.dot(Control_Matrix, Input_Matrix)
    P[i] = np.dot(A, np.dot(P[i], A.T)) + w
    
    # Measurement
    Residual = Y[i] - B*State_Estimate[i]
    Residual_ee = np.dot(B, np.dot(P[i], B.T)) + v
    MLB_Distance = m.sqrt((Residual**2)/Residual_ee)
    Eps = 0.01 # Constant
    MLBD_weighted = 1/(1 + m.exp(-MLB_Distance + Eps))
    
    delta = 0.8 #Constant [Modify this to tune for different signals]
    v = np.array([[delta*MLBD_weighted]])
    K = np.dot(P[i], np.dot(B.T, (1/Residual_ee)))
    
    # Update
    State_Estimate[i] += np.dot(K, np.dot(Residual, K))
    P[i] = np.dot((I - np.dot(K, B)), P[i])
    
    print('Iteration number: ', i+1)
    
# Plot the filtered Signal

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.plot(Y, label = "Sensor Signal", color ='blue')
ax2.plot(State_Estimate, label = "Filtered Signal",  linewidth = 3, color = 'green')
ax2.set_xlabel("Time")
ax2.set_ylabel("Signal")
ax2.legend()
