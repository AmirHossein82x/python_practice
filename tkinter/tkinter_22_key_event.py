from tkinter import *

#def doSomething(event):
    #print('you pressed: ', event.keysym)   # event.keysym returns which key you clicked
#    label.config(text=event.keysym)

#def out(event):
#   print('you are out of the program, and you pressed: ', event.keysym)

def all(event):
    #print('you enter any key and you pressed: ', event.keysym)
    label.config(text=event.keysym)

window = Tk()

#window.bind("<Return>", doSomething)
#window.bind("<q>", out)

window.bind("<Key>", all) # "<Key>" means any key

label = Label(window, font=('Helvetica', 100), text=None)
label.pack()


window.mainloop()