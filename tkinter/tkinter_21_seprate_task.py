from tkinter import *
from tkinter import ttk

window= Tk()

notebook = ttk.Notebook(window)   # widget that manage a collection of window
tab1 = Frame(notebook)   # new frame for tab1
tab2 = Frame(notebook)   # new frame for tab2
notebook.add(tab1, text='tab1')
notebook.add(tab2, text='tab2')
notebook.pack(expand=True, fill='both')    # it will expand the size of the window if we want to make window bigger
                                           # fill will be help the expand to perform well


Label(tab1, text='Hello this is tab1', width=50, height=25).pack()
Label(tab2, text='Hello this is tab2', width=50, height=25).pack()

window.mainloop()