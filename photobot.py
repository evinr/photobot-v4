import os
import subprocess
import time
import keyboard
import datetime
from relay_open_close import *
# from display_image_fullscreen import * 
from save_latest_image import * 



def display_latest_image():
    #  displays the image fullscreen
    # showPIL(Image.open("/home/" + os.environ['MACHINE_NAME'] + "/latest.jpeg"))
    # PIL is too intense and prevents any interactions after displaying the image
    # going back to using an application to display the image and maintain interactions
    # os.system('eog /home/$MACHINE_NAME/latest.jpeg  --fullscreen') 
    # eog was not displaying an image, so switched to feh which is lighter weight and more versitile
    imagePath = "/home/" + os.environ['MACHINE_NAME'] + "/latest.jpeg"
    subprocess.Popen(['feh', imagePath, '-F'])
    # none of these will launch from the cron job and they do not seem to update the image when running manually
    # showLatestImage()
    # cannot get root crontab to launch as expected, moved feh launching to launch at startup.


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
    # display_latest_image()



# have to pass event into the fuction that is called by the keyboard
def start(event):
    # since the events backup into a queue then we need to check if the timestamp is within 15 seconds
    global last_picuture_date
    time_difference = float(str(datetime.datetime.now().timestamp()-last_picuture_date))
    if time_difference > 5:
        # Gives the participants a chance to get into place
        time.sleep(2)
        take_picture()
        time.sleep(1)
        last_picuture_date = datetime.datetime.now().timestamp()

# needed to prevent too many pictures from being taken when the keyboard is smashed
last_picuture_date = datetime.datetime.now().timestamp() - 15
# On launch set the kiosk image
# display_latest_image()
# Notify we are ready to start
print('Photobot launched! Ready to photograph!')

# using any keyboard press to trigger
keyboard.on_press(start)

# Blocks until you press esc.
keyboard.wait('esc')