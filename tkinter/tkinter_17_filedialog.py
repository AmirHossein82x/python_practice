from tkinter import *
from tkinter import filedialog

def openfile():

    file_path = filedialog.askopenfilename(initialdir="D:\\python_exesize",
                                           title='open file',
                                           filetypes=(('text files',"*.txt"), ('all files','*.*'))
                                           ) 
                                           
    #print(file_path)
    file = open(file_path, "r")
    print(file.read())
    file.close()

window = Tk()

button = Button(window, text='open', command=openfile)

button.pack()

window.mainloop()