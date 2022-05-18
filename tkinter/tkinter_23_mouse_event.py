from tkinter import *

def dosomething1(event):

    # str(event.x) returns position x where you clicked
    # str(event.y) returns position y where you clicked

    print('you clicked on left mouse key on the position (%s , %s)' %(str(event.x), str(event.y)))

def dosomething2(event):
    print('you clicked on scroll key on the mouse')

def dosomething3(event):
    print('you clicked on right mouse key')

window = Tk()

#window.bind("<Button-1>", dosomething1)   # "<Button-1>" is left mouse click

window.bind("<Button-2>", dosomething2)   # "<Button-2>" is right scroll wheel

window.bind("<Button-3>", dosomething3)   # "<Button-2>" is right right wheel

#window.bind("<ButtonRelease>", dosomething1)   

#window.bind("<Enter>", dosomething1)   #"<Enter>" will perform dosomethitg1 where you put the mouse for the first time

#window.bind("<Leave>", dosomething1)   #"<Leave>" will perform dosomethitg1 where you put out the mouse for the first time

window.bind("<Motion>", dosomething1)   #"<Motion>" will perform dosomething1 whenever you move the mouse



window.mainloop()
