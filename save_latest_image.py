import glob
import re
import os
import subprocess
import time
   
 # read all files to find the last image/one with the highest number

def saveLastImage():
    #  TODO: Make this more extensible
    allJpegs = glob.glob("/home/$MACHINE_NAME/Pictures/*.jpeg")
    command = "cp /home/$MACHINE_NAME/latest.jpeg /home/$MACHINE_NAME/Pictures/"
    
    if len(allJpegs) == 0:
        # this assumes no other images are in the directory
        print('the list is empty')
        # TODO: os.system is deprecated, you should use the subprocessmodule instead.
        command = command + "1.jpeg"
        os.system(command)
        # this command is not executing   
        time.sleep(3)
        return None   
    lastFileName = allJpegs[0]
    parsedNumer = re.search(r'(?<=.)\d+', lastFileName)
    newNumber = str(int(parsedNumer.group(0)) + 1)
    command = command + newNumber + ".jpeg"
    # TODO: os.system is deprecated, you should use the subprocessmodule instead.
    os.system(command)  

if __name__ == '__main__':
   saveLastImage()
   