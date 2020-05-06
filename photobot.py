import os
import RPi.GPIO as GPIO
import serial 
import subprocess
import time

#Setup for the button
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Setup for the USB relay
relay = serial.Serial(
port='/dev/ttyUSB0',
baudrate=9600
)
relay.open

#Global variable for preventing double button presses
process_active = False


def open_relay():
    relay.write('A00101A2'.decode('hex'))
    
def close_relay():
    relay.write('A00100A1'.decode('hex'))

def take_picture():
    # need to block call stack
    os.system("gphoto2 --capture-image-and-download --filename=/home/caleb/latest.jpeg --force-overwrite")
    # takes time to copy image over
    time.sleep(1)
    close_relay()
    # copy over image for persistance 
    save_picture()
    # after running this, does it return cleanly and we can display without comparing hashes
    time.sleep(1)

def start():
    process_active = True
    time.sleep(3)
    # takes like 5 seconds to open
    open_relay()
    take_picture()
    
print('Photobot launched! Ready to photograph!')
while True:
    input_state = GPIO.input(18)

    if input_state == False and process_active is False:
        print('Button Pressed')
        start();
        time.sleep(0.2)

