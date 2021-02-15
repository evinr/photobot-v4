import glob
import re
import os
import subprocess
import time
   
 # read all files to find the last image/one with the highest number

def saveLastImage():
    command = "cp /home/" + os.environ['MACHINE_NAME'] + "/latest.jpeg /home/" + os.environ['MACHINE_NAME'] + "/Pictures/"
    # need to sort on the numbers, not the enitre filename using the key function
    allJpegs = sorted(glob.glob("/home/" + os.environ['MACHINE_NAME'] + "/Pictures/*.jpeg"), key=lambda name: int(name[18:-5]))

    if len(allJpegs) == 0:
        # TODO: os.system is deprecated, you should use the subprocessmodule instead.
        command = command + "1.jpeg"
        os.system(command)
        # this command is not executing   
        time.sleep(3)
        return None 
    print(allJpegs)  
    lastFileName = allJpegs[len(allJpegs)-1]
    print(lastFileName)
    parsedNumer = re.search(r'(?<=.)\d+', lastFileName)
    print(parsedNumer)
    newNumber = str(int(parsedNumer.group(0)) + 1)
    print(newNumber)
    command = command + newNumber + ".jpeg"
    # TODO: os.system is deprecated, you should use the subprocessmodule instead.
    os.system(command)  

if __name__ == '__main__':
   saveLastImage()
   