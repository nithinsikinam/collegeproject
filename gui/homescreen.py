from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
import os

root = Tk()  

root.iconbitmap('D:\college project\gui\image\icon.ico')
# Defining the window size
screenw= root.winfo_screenwidth()
screenh=root.winfo_screenheight()
root.geometry("%dx%d" %(screenw,screenh) )
# Fixing the window size
root.resizable()
# Title bar Title
root.title('cms project')

global idw
global framew
global frameh

if (screenw==1920):
    idw=420
    framew=500
    frameh=1020
elif (screenw==1600):
    idw=400
    framew=400  
    frameh=900


#--------------------------------------------------------------------------------------------------------
#frames
frameL = Frame(root,borderwidth=10, relief="groove",width=framew,height=650,bg="#133c55")
frameL.grid(row=0,column=1)
frameL.pack_propagate(0)

framem = Frame(root,borderwidth=10, relief="groove",width=framew,height=650,bg="#133c55")
framem.grid(row=0,column=2)
framem.pack_propagate(0)

framer = Frame(root,borderwidth=10, relief="groove",width=framew,height=650,bg="#133c55")
framer.grid(row=0,column=3)
framer.pack_propagate(0)


frame1 = Frame(root,borderwidth=0, relief="groove",width=idw,height=frameh,bg="grey")
frame1.grid(row=0,column=0)
frame1.pack_propagate(0)




#--------------------------------------------------------------------------------------------------------
dashbFont = font.Font(family='Helvetica', size=60, weight='bold')
dashb = Label(frameL, text="dashboard", fg="White",bg="#133c55")
dashb['font']=dashbFont
dashb.pack()


libFont = font.Font(family='Helvetica', size=60, weight='bold')
lib = Label(framem, text="library", fg="White",bg="#133c55")
lib['font']=libFont
lib.pack()


classvFont = font.Font(family='Helvetica', size=60, weight='bold')
classv = Label(framer, text="classes", fg="White",bg="#133c55")
classv['font']=classvFont
classv.pack()

img = ImageTk.PhotoImage(Image.open("D:\college project\gui\image\ok.png"))
panel = Label(frame1, image = img)
panel.pack()


print(str(root.winfo_screenwidth()))

root.mainloop()