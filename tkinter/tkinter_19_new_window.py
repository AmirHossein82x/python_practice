from tkinter import *

def create_window():
    # this 2 ways have some diffetents 
    #new_window = Toplevel()
    new_window = Tk()
    old_window.destroy()   # this will close out old_window

old_window = Tk()
Button(old_window, text='create new window', command=create_window).pack()
old_window.mainloop()