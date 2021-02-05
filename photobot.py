import os
import subprocess
import time
import keyboard
from relay_open_close import *
from display_image_fullscreen import * 
from save_latest_image import * 


# Global variable for preventing double button presses
process_active = False


def take_picture():
    # need to block call stack
    # takes like 5 seconds to turn on the lights
    open_relay()

    # captures the image and needs to be the absolute path
    os.system("gphoto2 --capture-image-and-download --filename=./latest.jpeg --force-overwrite")
    
    # turn off the lights
    close_relay()
    
    # takes time to copy image from camera to storage
    time.sleep(1)

    #  displays the image fullscreen
    showPIL(Image.open("./latest.jpeg"))
    
    # copy over image for persistance 
    #copy the pictures with a timestamp
    # timestamps do not work without reliable internet or a battery powered RTC
    # better to use the file names to establish order as a way to ensure we are incrementing the photos into a cronological order
    save-latest-image()
    
    # after running this, does it return cleanly and we can display without comparing hashes
    time.sleep(1)

# have to pass event into the fuction that is called by the keyboard
def start(event):
    process_active = True
    # Gives the participants a chance to get into place
    time.sleep(3)
    take_picture()
    time.sleep(0.2)
    process_active = False
    
print('Photobot launched! Ready to photograph!')

keyboard.on_press(start)

# Blocks until you press esc.
keyboard.wait('esc')