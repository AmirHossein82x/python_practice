from tkinter import *
from tkinter import colorchooser

def click():
    #color = colorchooser.askcolor()
    #colorHex = color[1]
    #window.config(bg=colorHex)

    #shorter solution
    window.config(bg=colorchooser.askcolor()[1])
    
window = Tk()
window.geometry("420x420")


button = Button(text='click', command=click)
button.pack()

window.mainloop()