# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:21:27 2021

@author: m200646
"""

import serial
import win32com.client
import math

def setup():
    global baudRate
    global serialTimeout
    global ser
    baudRate = 19200
    serialTimeout = 1
    listCOM()
    chooseCOM()
    try:
        ser = serial.Serial(comPort, baudRate, timeout=serialTimeout)
        commandInput()
    except:
        print("Count not establish connection.")
        print("Double check the COM port and that the Arduino is powered on and try again.")

def listCOM():
    wmi = win32com.client.GetObject("winmgmts:")
    print("------------------------------------------------------")
    print("List of available COM Ports:\n")
    for serial in wmi.InstancesOf("Win32_SerialPort"):
        print(serial.Name, serial.Description)
    print("------------------------------------------------------")

def chooseCOM():
    global comPort
    print("")
    print('Enter the COM port for "Arduino Uno"')
    comPort = input("e.g. 'COM1' or 'COM3': ")
    
def commandInput():
    while True:
        try:
            pumpVal = float(input("Command: "))
            if ((pumpVal > 0) and (pumpVal <= 48)):
                ardCmd = math.floor((pumpVal - 6.323) / 0.1701)
                test = str(ardCmd)
                ardCmdStr = str(ardCmd) + '00'
                ardCmdByte = bytes(ardCmdStr, 'utf-8')
                ser.write(ardCmdByte)
                print("Success")
            elif (pumpVal > 48):
                ser.write(b'25500')
                print("Maximum pump value is 48")
            else:
                ser.write(b'10')
                print("Stopped")
        except:
            print("Quitting...")
            ser.write(b'10')
            ser.close()
            break

if __name__ == "__main__":
    setup()