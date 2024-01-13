import tkinter
import cv2
import PIL.Image ,PIL.ImageTk
from functools import partial   #for 'command' to take arguments in action button
import threading
import imutils  #for resizing image
import time

stream = cv2.VideoCapture("runout1.mp4")    #c2.videocapture captures the video

def play(speed):
    print(f"You clicked on play.Speed is {speed}")

    #play the video in reverse mode
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)

    grabbed,frame=stream.read()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image=frame,anchor=tkinter.NW)



def pending(decision):
    frame=cv2.cvtColor(cv2.imread("decision_pending.jpeg"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    time.sleep(1.5)

    if decision == "out":
        decisionImg="out.webp"
    else:
        decisionImg="not_out.jpeg"

    frame=cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)


def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("Player is out")

def not_out():
    thread=threading.Thread(target=pending,args=("not out",))
    thread.daemon=1
    thread.start()
    print("Player is not-out")

#height and width of the main screen
SET_WIDTH= 650
SET_HEIGHT = 368 

#GUI
window = tkinter.Tk()
window.title("Third Umpire")
cv_img=cv2.cvtColor(cv2.imread("welcome.webp"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)  #image will be inside the canvas (height and width = set width and height of the GUI)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,anchor=tkinter.NW,image=photo) #position of the image 0,0 coordinate and NW direction
canvas.pack()


#Buttons to control playback

btn=tkinter.Button(window,text="<< Previous (Fast)",width=50,command=partial(play,-25))
btn.pack()

btn=tkinter.Button(window,text="<< Previous (Slow)",width=50,command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text="Next (Slow) >>",width=50,command=partial(play,1))
btn.pack()

btn=tkinter.Button(window,text="Next (Fast) >>",width=50,command=partial(play,25)) #command execute the given funtion ,
btn.pack()

btn=tkinter.Button(window,text="Give Out",width=50,command=out)
btn.pack()

btn=tkinter.Button(window,text="Give Not Out",width=50,command=not_out)
btn.pack()

window.mainloop()