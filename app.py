#!/usr/bin/env python

#import RPi.GPIO as GPIO
import datetime
import time

if __name__ == '__main__':
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(18, GPIO.OUT)
    """

    i = 0

    data_file = 'data.csv'
    open(data_file, 'w').close()

    print('Start logging temperature and humidity')
    while True:
        now = datetime.datetime.utcnow()
        timestamp = now.strftime('%d-%b-%Y %H:%M:%S')
        humidity, temperature = (60.0, 27.0)

        print(
            f'{timestamp} >> Temp={temperature:0.1f}C Humdity={humidity:0.1f}%'
        )
        with open(data_file, 'a') as f:
            f.write(f'{timestamp},{temperature},{humidity}\n')

        time.sleep(1)

        if i >= 3:
            break

        i += 1
