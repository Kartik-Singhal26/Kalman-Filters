# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 03:36:24 2020

@author: kartik
"""
from IMU_Data_fromSensors import SensorValues
import numpy as np
import math as m
import matplotlib.pyplot as plt

#Sensor Values
dT = 0.245
n = 113 #Instances of Data
Acc_xAngle, Acc_yAngle, Gyro_xAngle, Gyro_yAngle, Gyro_zAngle = SensorValues()

def KalmanFilter():
    
    StateEstimate = np.zeros((4,1))
    
    #System Matrices
    A = np.array([[1, -dT, 0, 0], [0, 1, 0, 0], [0, 0, 1, -dT], [0, 0, 0, 1]]) # Current System to Next State
    B = np.array([[dT, 0, 0, 0], [0, 0, dT, 0]]).T # Inputs to Next State
    C = np.array([[1, 0, 0, 0], [0, 0, 1, 0]]) # System States to Measured States
    
    P = np.eye(len(StateEstimate)); # Error Covariance Matrix
    Q = np.eye(len(StateEstimate)) * 2 # Covariance Matrix of Process Noise
    R = np.eye(2) * 15 # Covariance Matrix of Measurement Noise
    I = np.eye(len(StateEstimate)); # Identity Matrix
    
    phi_d = Gyro_xAngle
    theta_d = Gyro_yAngle
    phi_acc = Acc_yAngle
    theta_acc = Acc_xAngle
    phi_G = 0
    theta_G = 0
    
    #Calculate Accelerometer sensor Offsets
    phi_off = 0
    theta_off = 0
    
    for i in range(1,n):
        phi_off += phi_acc[i]
        theta_off += theta_acc[i]
    
    phi_off = phi_off/n
    theta_off = theta_off/n
    
    #Initialize Pitch and Roll Arrays
    Pitch = []
    Roll = []
    
    # In loop
    for i in range(n):
        
        phi_acc[i] -= phi_off
        theta_acc[i] -= theta_off
        
        phi_d = Gyro_xAngle[i] + m.sin(phi_G) * m.tan(theta_G) * Gyro_yAngle[i] + m.cos(phi_G) * m.tan(theta_G) * Gyro_zAngle[i]
        theta_d = m.cos(phi_G) * Gyro_yAngle[i] - m.sin(phi_G) * Gyro_zAngle[i]
        
        #Prediction
        Input_vector = np.array([[phi_d], [theta_d]])
        
        StateEstimate = np.dot(A,StateEstimate) + np.dot(B, Input_vector)
        P = np.dot(A, np.dot(P,A.T)) + Q
    
        #Update
        Measurement_vector = np.array([[phi_acc[i]], [theta_acc[i]]])   

        Y_T = Measurement_vector - np.dot(C,StateEstimate)
        S = np.dot(C,np.dot(P,C.T)) + R
        K = np.dot(P,np.dot(C.T, np.linalg.inv(S))) #Kalman Gain
    
        StateEstimate += np.dot(K,Y_T)
        P = np.dot((I - np.dot(K,C)),P)
        
        phi_G = StateEstimate[0]
        theta_G = StateEstimate[2]
        
        Pitch.append(phi_G)
        Roll.append(theta_G)
        
        #Print Results
        print('Iteration Number =', i+1 )
        print('Phi: ', str(phi_G) + '  Theta: ', str(theta_G))
        
    return Pitch, Roll

# Simulate the Kalman Filter for Sensor Data Fusion

Pitch, Roll = KalmanFilter()

#Print
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.plot(Pitch, label = "Pitch", color ='blue')
ax1.plot(Acc_xAngle, label = "Acceleremoter", color ='orange')
ax1.plot(Gyro_xAngle, label = "Gyroscope", color ='green')
ax1.set_ylabel("Pitch")
ax1.set_xlabel("Instance")
ax1.legend()

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.plot(Roll, label = "Roll", color ='blue')
ax2.plot(Acc_yAngle, label = "Acceleremoter", color ='orange')
ax2.plot(Gyro_yAngle, label = "Gyroscope", color ='green')
ax2.set_ylabel("Roll")
ax2.set_xlabel("Instance")
ax2.legend()

