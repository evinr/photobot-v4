import os
import subprocess
import time
import keyboard
from relay_open_close import *
from display_image_fullscreen import * 
from save_latest_image import * 


# Global variable for preventing double button presses
process_active = False

def display_latest_image():
    #  displays the image fullscreen
    # showPIL(Image.open("/home/" + os.environ['MACHINE_NAME'] + "/latest.jpeg"))
    # PIL is too intense and prevents any interactions after displaying the image
    # going back to using an application to display the image and maintain interactions
    # os.system('eog /home/$MACHINE_NAME/latest.jpeg  --fullscreen') # Needs x11 forwarding enabled to work
    imagePath = "/home/" + os.environ['MACHINE_NAME'] + "/latest.jpeg"
    print(imagePath)
    subprocess.Popen(['eog', imagePath, '--fullscreen'])


def take_picture():
    # need to block call stack
    # takes like 5 seconds to turn on the lights
    open_relay()

    # captures the image and needs to be the absolute path
    os.system("gphoto2 --capture-image-and-download --filename=/home/$MACHINE_NAME/latest.jpeg --force-overwrite")
    
    # turn off the lights
    close_relay()
    
    # takes time to copy image from camera to storage
    time.sleep(1)

    # copy over image for persistance 
    #copy the pictures with a timestamp
    # timestamps do not work without reliable internet or a battery powered RTC
    # better to use the file names to establish order as a way to ensure we are incrementing the photos into a cronological order
    saveLastImage()

    #  displays the image fullscreen
    # showPIL(Image.open("/home/" + os.environ['MACHINE_NAME'] + "/latest.jpeg"))
    # PIL is too intense and prevents any interactions after displaying the image
    # going back to using an application to display the image and maintain interactions
    display_latest_image()
    
    # after running this, does it return cleanly and we can display without comparing hashes
    time.sleep(1)

# have to pass event into the fuction that is called by the keyboard
def start(event):
    # TODO: create histerisis that limits presses to once every 15 seconds
    process_active = True
    # Gives the participants a chance to get into place
    time.sleep(3)
    take_picture()
    time.sleep(0.2)
    process_active = False

# On launch set the kiosk image

display_latest_image()
print('Photobot launched! Ready to photograph!')

keyboard.on_press(start)

# Blocks until you press esc.
keyboard.wait('esc')