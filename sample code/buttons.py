from tkinter import *
from tkinter.ttk import *

# Set the canvas
canv = Tk()
canv.geometry('200x150')

#Create style object
sto = Style()

#configure style
sto.configure('W.TButton', font= ('Arial', 10, 'underline'),
foreground='Green')

#Button with style
btns = Button(canv, text='Welcome !',
      style='W.TButton',
      command=canv.destroy)
btns.grid(row=0, column=1, padx=50)

#Button without style
btnns = Button(canv, text='Click to Start !', command=None)
btnns.grid(row = 1, column = 1, pady = 10, padx = 50)

canv.mainloop()