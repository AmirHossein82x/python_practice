from tkinter import *

def openfile():
    print('File has been opened!')

def savefile():
    print('File has been saved!')

def copy():
    print('you copied this file!')

def cut():
    print('you cutted this file! ')

def paste():
    print('you pasted this file!')

window = Tk()

openimage = PhotoImage(file="pizza.png")
saveimage = PhotoImage(file="fire.png")
exitimage = PhotoImage(file="hamburger.png")

menubar = Menu(window)
window.config(menu=menubar)


fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 10))   # tearoff=0 will remove "-----"
menubar.add_cascade(label='file', menu=fileMenu)
fileMenu.add_command(label='Open', command=openfile, image=openimage, compound='left')
fileMenu.add_command(label='Save', command=savefile, image=saveimage, compound='left')
fileMenu.add_separator()  # it will add ----- in the menu bar
fileMenu.add_command(label='Exit', command=quit, image=exitimage, compound='left')



editmenu = Menu(menubar, tearoff=0, font=("MV Boli", 10))
menubar.add_cascade(label='edit', menu=editmenu)
editmenu.add_command(label='cut', command=cut)
editmenu.add_command(label='copy', command=copy)
editmenu.add_command(label='paste', command=paste)

window.mainloop()