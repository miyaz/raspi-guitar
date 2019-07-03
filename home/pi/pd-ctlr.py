import RPi.GPIO as GPIO
from time import sleep
import subprocess
import random
import time
import OSC

RESET=4
RECORD=17
EFFECT=27

pd_state = 0
state1 = 0 
state2 = 0 
state3 = 0 

GPIO.setmode(GPIO.BCM)
GPIO.setup(RESET, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RECORD, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(EFFECT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def send(signal):
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 9002))
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/"+signal)
    oscmsg.append(random.random())
    c.send(oscmsg)

def poweroff():
    args = ['sudo', 'poweroff']
    print(args)
    subprocess.Popen(args)

def reboot():
    args = ['sudo', 'reboot']
    print(args)
    subprocess.Popen(args)

def pd_start():
    subprocess.Popen(['pd', '-nogui', '/home/pi/pd/hcmpl_lt1.pd'])
    print('pd_start')

def pd_stop():
    subprocess.call(['pkill', 'pd'])
    print('pd_stop')

# Main
 
if __name__ == "__main__":
    try:
        while True:
            if GPIO.input(RESET)==GPIO.HIGH:
                if state1 >= 6:
                    state1 = 0
                    poweroff()
                else:
                    state1 += 1
            else:
                if (3 <= state1 and state1 < 6):
                    reboot()
                elif (1 <= state1 and state1 < 3):
                    if (pd_state == 0):
                        pd_stop()
                        pd_start()
                        pd_state = 1
                    else:
                        send('stop')
                        pd_state = 0
                state1 = 0

            if GPIO.input(RECORD)==GPIO.HIGH:
                state2 += 1
            else:
                if (state2 >= 1):
                    send('record')
                state2 = 0

            if GPIO.input(EFFECT)==GPIO.HIGH:
                state3 += 1
            else:
                if (state3 >= 1):
                    send('effect')
                state3 = 0

            sleep(0.5)

    except KeyboardInterrupt:
        pass

    GPIO.cleanup()

