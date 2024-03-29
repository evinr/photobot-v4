# Displays an image fullwidth and wil probably require a restart if a remote session or multiple monitors

# Shoutouts
#  https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
# https://stackoverflow.com/questions/53638972/displaying-an-image-full-screen-in-python
# 
import os
import sys 
import tkinter
import time
import psutil
from PIL import Image, ImageTk
# from file import function

def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()    
    root.bind("<Key>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    
    # display fullscreen width
    new_width  = w
    new_height = int(new_width * h / w) 
    pilImage = pilImage.resize((new_width,new_height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    canvas.create_image(w/2,h/2,image=image)
    root.mainloop()

def removeImage():
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill() 

def showLatestImage():
    removeImage()
    image = Image.open("/home/" + os.environ['MACHINE_NAME'] + "/latest.jpeg")
    # root = tkinter.Tk()
    # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    # new_width  = w
    # need to take account for the menu bar at the top, otherwise two windows open
    # new_height = int(0.95*(new_width * h / w))
    # image = image.resize((new_width,new_height))
    # hardcoding to minimize BS
    image = image.resize((800,480))
    image.show()

if __name__ == '__main__':
    showLatestImage()
    time.sleep(3)
    removeImage()
