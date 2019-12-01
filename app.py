#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(18, GPIO.OUT)

    for i in range(10):
        print('LED on')
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        print('LED off')
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
