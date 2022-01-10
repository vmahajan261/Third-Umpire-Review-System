import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import numpy as np
import imutils
import threading
import time

stream=cv2.VideoCapture('clip.mp4')
def play(speed):
    print(f"You clicked on play.Speed is {speed}")
        #play video in reverse
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+speed)

    grabbed, frame=stream.read()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image=frame,anchor=tkinter.NW)

        #play forward
def pending(decision):
    # 1. Display decision pending image
    frame=cv2.cvtColor(cv2.imread("pending.jpg"),cv2.COLOR_BGR2RGB)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    #  wait 1 sec 
    time.sleep(2)
    # display decision
    if decision=='out':
        decisionimg='out.png'
    else:
        decisionimg='notout.jpg'
    frame=cv2.cvtColor(cv2.imread(decisionimg),cv2.COLOR_BGR2RGB)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    
def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()

    print("Batsman is out")
def not_out():
    thread=threading.Thread(target=pending,args=("not out",))
    thread.daemon=1
    thread.start()
    print("Batsman is not out")
SET_WIDTH=600
SET_HEIGHT=370

#tkinter gui
window=tkinter.Tk()
window.title("Third Umpire Review System")
cv_img=cv2.cvtColor(cv2.imread('adelaide.jpg'),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window, width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0, ancho=tkinter.NW, image=photo)
canvas.pack()

#buttons to control playback
btn=tkinter.Button(window, text="<<Previous(fast)",width=50, command=partial(play, -25))
btn.pack()
btn=tkinter.Button(window, text="<<Previous(Slow)",width=50, command=partial(play,-2))
btn.pack()
btn=tkinter.Button(window, text="Next(slow)>>",width=50, command=partial(play,2))
btn.pack()
btn=tkinter.Button(window, text="Next(fast)>>",width=50, command=partial(play,25))
btn.pack()

btn=tkinter.Button(window, text="OUT",width=50, command=out)
btn.pack()
btn=tkinter.Button(window, text="NOT OUT",width=50, command=not_out)
btn.pack()
window.mainloop()