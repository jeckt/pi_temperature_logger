#!/usr/bin/env python

import RPi.GPIO as GPIO
import Adafruit_DHT
import datetime
import time

DATA_FILE = 'data.csv'

def log(temperature, humidity):
    now = datetime.datetime.utcnow()
    timestamp = now.strftime('%d-%b-%Y %H:%M:%S')

    print(
            f'{timestamp} >> Temp={temperature:0.1f}C Humdity={humidity:0.1f}%'
        )
    with open(DATA_FILE, 'a') as f:
        f.write(f'{timestamp},{temperature},{humidity}\n')

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    DHTSensor = Adafruit_DHT.DHT11
    DATA_PIN = 23

    open(DATA_FILE, 'w').close()
    print('Start logging temperature and humidity')
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHTSensor, DATA_PIN)
        log(temperature, humidity)
        time.sleep(5 * 60)
