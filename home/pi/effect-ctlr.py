# coding: utf-8

import FaBo9Axis_MPU9250
from time import sleep
import time
import sys
import random
import OSC

mpu9250 = FaBo9Axis_MPU9250.MPU9250()
state = 0
prev_gyro_x = 0
wah_value = 0
wah_min = 10
wah_max = 127

def send(signal, arg=random.random()):
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 9002))
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/"+signal)
    oscmsg.append(arg)
    c.send(oscmsg)

# Main
 
if __name__ == "__main__":
    try:
        while True:
            gyro = mpu9250.readGyro()
            gyro_z = gyro['z']
            gyro_x = gyro['x']
            wah_delta = (prev_gyro_x - gyro_x) / 2
            if abs(wah_delta) > 5:
                if wah_delta > 0:
                    if wah_value + wah_delta > wah_max:
                        wah_value = wah_max
                    else:
                        wah_value = wah_value + wah_delta
                    send('wah', wah_value)
                else:
                    if wah_value + wah_delta < wah_min:
                        wah_value = wah_min
                    else:
                        wah_value = wah_value + wah_delta
                    send('wah', wah_value)

            if gyro_z > 100:
                state += 1
            else:
                if (state >= 1):
                    send('effect')
                state = 0

            sleep(0.1)

    except KeyboardInterrupt:
        pass

