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

Accelerometer_x = createdata(0)*180/m.pi      
Accelerometer_y = createdata(1)*180/m.pi      
Accelerometer_z = createdata(2)*180/m.pi      
Gravity_x = createdata(3)*180/m.pi    
Gravity_y = createdata(4)*180/m.pi      
Gravity_z = createdata(5)*180/m.pi      

def SensorValues():
    #Converting the sensor values into Degrees
    Acc_xAngle = np.arctan2(Accelerometer_x, (np.sqrt(np.power(Accelerometer_y,2) + np.power(Accelerometer_z,2)))) #theta_acc #pitch
    Acc_yAngle = np.arctan2(Accelerometer_y, (np.sqrt(np.power(Accelerometer_x,2) + np.power(Accelerometer_z,2)))) #phi_acc #roll

    dT = 0.245

    Gyro_xAngle = Gravity_x * 0.23 * dT 
    Gyro_xAngle += Gyro_xAngle             # phi_dot
    Gyro_yAngle = Gravity_y * 0.14 * dT
    Gyro_yAngle += Gyro_yAngle             # theta_dot
    Gyro_zAngle = Gravity_z * 0.25 * dT 
    Gyro_zAngle += Gyro_zAngle             # psi_dot 

    return [Acc_xAngle, Acc_yAngle, Gyro_xAngle, Gyro_yAngle, Gyro_zAngle]

#[Acc_xAngle, Acc_yAngle, Gyro_xAngle, Gyro_yAngle, Gyro_zAngle] = SensorValues()
