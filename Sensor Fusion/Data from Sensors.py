import csv
import matplotlib.pyplot as plt
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
    for i in range(113):
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


#Converting the sensor values into Degrees
Acc_xAngle = (180/m.pi)*np.arctan(Accelerometer_x, (np.sqrt(np.power(Accelerometer_y,2) + np.power(Accelerometer_z,2)))) 
Acc_yAngle = (180/m.pi)*np.arctan(Accelerometer_y, (np.sqrt(np.power(Accelerometer_x,2) + np.power(Accelerometer_z,2)))) 
Acc_zAngle = (180/m.pi)*np.arctan((np.sqrt(np.power(Accelerometer_y,2) + np.power(Accelerometer_z,2))), Accelerometer_z) 

dT = 0.01

Gyro_xAngle = (180/m.pi)*Gravity_x * 0.11
Gyro_xAngle += Gyro_xAngle * dT   
Gyro_yAngle = (180/m.pi)*Gravity_y * 0.2
Gyro_yAngle += Gyro_yAngle * dT
Gyro_zAngle = (180/m.pi)*Gravity_z * 0.15
Gyro_zAngle += Gyro_zAngle * dT 

#plt.plot(Gyro_zAngle)
#plt.plot(Acc_zAngle)


