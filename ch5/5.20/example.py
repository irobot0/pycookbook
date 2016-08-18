#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You want to read and write data over a serial port, typically to interact with
some kind of hardware device (e.g., a robot or sensor).
"""


"""
SOLUTION
"""

import serial

ser = serial.Serial('/dev/ttys000', # Device name varies
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)

ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()
