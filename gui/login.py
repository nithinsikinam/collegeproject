from tkinter import *  

root = Tk()  
photo = PhotoImage(file = "icon.ico")
root.iconphoto(False, photo)
# Defining the window size
root.geometry("200x150")
# Fixing the window size
root.resizable()
# Title bar Title
root.title('cms project')
# Title Bar Icon
root.iconbitmap('icon.ico')

root.mainloop()  