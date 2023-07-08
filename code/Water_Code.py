import RPi.GPIO as GPIO
import time
import os

import string

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_Relay = 4

GPIO.setup(GPIO_Relay, GPIO.OUT)

file_path = r'/home/pi/Desktop/Fire_Detection_Pump/yolov5/det_res.txt';

if __name__ == '__main__':
    print('[INFO]')
    while True:
        f1 = open(file_path,'r')
        Txt_Data = f1.read()
        if "Fire" in Txt_Data:
            GPIO.output(GPIO_Relay, True)
            print('Pump On')
        else:
            GPIO.output(GPIO_Relay, False)
            print('Pump Off')
        time.sleep(0.3)
