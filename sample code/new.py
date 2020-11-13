from tkinter import *  
from PIL import ImageTk, Image   

root = Tk()  

root.iconbitmap('D:\collegeproject\gui\image\icon.ico')
# Defining the window size
root.geometry("200x150")
# Fixing the window size
root.resizable()
# Title bar Title
root.title('cms project')
# Title Bar Icon

img = ImageTk.PhotoImage(Image.open('D:\collegeproject\gui\image\Team48.png'))
panel = Label(root, image = img)
panel.pack()



root.mainloop()  