#!/usr/bin/python

# Application for reading data from SDS011, SDS018 and SDS021 dust sensors.
# USAGE: "python dust-sensor-read.py" or "python dust-sensor-read.py /dev/ttyUSB1"
#
# Forked from: https://github.com/aqicn/sds-sensor-reader
# Credits: Matjaz Rihtar, Matej Kovacic

import os
import sys
import time
import serial

# Reopen sys.stdout with buffer size 0 (unbuffered)
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w')

# Set default USB port
USBPORT = "/dev/ttyUSB0"


class SDS021Reader:

    def __init__(self, inport):
        self.serial = serial.Serial(port=inport, baudrate=9600)

    def readValue( self ):
        step = 0
        while True: 
            while self.serial.inWaiting() != 0:
                v = ord(self.serial.read())

                if step == 0:
                    if v == 170:
                        step = 1

                elif step == 1:
                    if v == 192:
                        values = [0,0,0,0,0,0,0]
                        step = 2
                    else:
                        step = 0

                elif step > 8:
                    step = 0
                    # Compute PM2.5 and PM10 values
                    pm25 = (values[1]*256 + values[0])/10.0
                    pm10 = (values[3]*256 + values[2])/10.0
                    return [pm25,pm10]

                elif step >= 2:
                    values[step - 2] = v
                    step = step + 1


    def read( self ):
        species = [[],[]]

        while 1:
            try:
                values = self.readValue()
                species[0].append(values[0])
                species[1].append(values[1])
                print("PM2.5: {}, PM10: {}".format(values[0], values[1]))
                time.sleep(1)  # wait for one second
            except KeyboardInterrupt:
                print("Quit!")
                sys.exit()
            except:
                e = sys.exc_info()[0]
                print("Can not read sensor data! Error description: " + str(e))

def loop(usbport):
    print("Starting reading dust sensor on port " + usbport + "...") 
    reader = SDS021Reader(usbport) 
    while 1:
        reader.read()

if len(sys.argv)==2:
    if sys.argv[1].startswith('/dev'):  # Valid are only parameters starting with /dev
        loop(sys.argv[1])
    else:
        loop(USBPORT)
else:
    loop(USBPORT)
