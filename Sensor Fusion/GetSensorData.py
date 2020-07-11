import csv
import matplotlib.pyplot as plt
import numpy as np
import math as m

'''
We first define the sensor readings. 
Two sensors: Accelerometer and Gravity sensor are used for obtaining
position coordinates in X-Y-Z coordinates.

'''
Data = csv.reader(open('imu_data.csv'), quoting = csv.QUOTE_NONNUMERIC)

SensorData = []
for row in Data:
    SensorData.append(row)
 
def createdata(index):
    sensor_val = []
    n = 1999
    for i in range(n):
        val = SensorData[i][index]
        sensor_val.append(val)
    
    sensor_val = np.array(sensor_val)
    AnyNaN = np.isnan(sensor_val)
    sensor_val[AnyNaN] = 0
    return sensor_val

Accelerometer_x = createdata(0) / 16384
Accelerometer_y = createdata(1) / 16384 
Accelerometer_z = createdata(2) / 16384
Gravity_x = createdata(3) / 23580   
Gravity_y = createdata(4) / 23580
Gravity_z = createdata(5) / 23580

#Converting the sensor values into Degrees
Acc_xAngle = (180/m.pi)*np.arctan(Accelerometer_x, (np.sqrt(np.power(Accelerometer_y,2) + np.power(Accelerometer_z,2)))) #theta_acc
Acc_yAngle = (180/m.pi)*np.arctan(Accelerometer_y, (np.sqrt(np.power(Accelerometer_x,2) + np.power(Accelerometer_z,2)))) #phi_acc 
Acc_zAngle = (180/m.pi)*np.arctan((np.sqrt(np.power(Accelerometer_y,2) + np.power(Accelerometer_z,2))), Accelerometer_z) 

dT = 0.185

Gyro_xAngle = (m.pi)*Gravity_x 
Gyro_xAngle += Gyro_xAngle * dT             # phi_d
Gyro_yAngle = (m.pi)*Gravity_y 
Gyro_yAngle += Gyro_yAngle * dT             # theta_d
Gyro_zAngle = (m.pi)*Gravity_z 
Gyro_zAngle += Gyro_zAngle * dT             # psi_d

#plt.plot(Gyro_zAngle)
#plt.plot(Acc_zAngle)


