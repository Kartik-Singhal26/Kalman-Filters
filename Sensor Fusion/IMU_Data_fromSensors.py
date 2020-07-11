import csv
import numpy as np
import math as m

'''
We first define the sensor readings. 
Two sensors: Accelerometer and Gravity sensor are used for obtaining
position coordinates in X-Y-Z coordinates.

'''
Data = csv.reader(open('ArduinoSensorValues.csv'), quoting = csv.QUOTE_NONNUMERIC)

SensorData = []
for row in Data:
    SensorData.append(row)
 
def createdata(index):
    sensor_val = []
    n = 113
    for i in range(n):
        val = SensorData[i][index]
        sensor_val.append(val)
    
    sensor_val = np.array(sensor_val)
    AnyNaN = np.isnan(sensor_val)
    sensor_val[AnyNaN] = 0
    return sensor_val

Accelerometer_x = createdata(0)  
Accelerometer_y = createdata(1)  
Accelerometer_z = createdata(2)  
Gravity_x = createdata(3)    
Gravity_y = createdata(4)  
Gravity_z = createdata(5)  

def SensorValues():
    #Converting the sensor values into Degrees
    dT = 0.025
    Acc_xAngle = []
    Acc_yAngle = []
        
    Gyro_xAngle = []
    Gyro_yAngle = []
    Gyro_zAngle = []
    for i in range(113):
        Acc_x = (180/m.pi)*m.atan2(Accelerometer_x[i], (m.sqrt(Accelerometer_y[i]**2 + Accelerometer_z[i]**2))) #theta_acc
        Acc_y = (180/m.pi)*m.atan2(Accelerometer_y[i], (m.sqrt(Accelerometer_x[i]**2 + Accelerometer_z[i]**2))) #phi_acc 
        Acc_xAngle.append(Acc_x)
        Acc_yAngle.append(Acc_y)
        
        Gyro_x = (180/m.pi)*Gravity_x[i] * 0.11 * dT # phi_dot 
        Gyro_x += Gyro_x                            
        Gyro_y = (180/m.pi)*Gravity_y[i] * 0.2 * dT # theta_dot 
        Gyro_y += Gyro_y     
        Gyro_z = (180/m.pi)*Gravity_z[i] * 0.2 * dT 
        Gyro_z += Gyro_z         
        Gyro_xAngle.append(Gyro_x)
        Gyro_yAngle.append(Gyro_y)
        Gyro_zAngle.append(Gyro_z)
        
    return [Acc_xAngle, Acc_yAngle, Gyro_xAngle, Gyro_yAngle, Gyro_zAngle]




