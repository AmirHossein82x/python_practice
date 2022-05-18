from tkinter import *
window = Tk()
frame = Frame(window, bg='pink', bd=5, relief=RAISED,)
frame.pack()
button = Button(frame, text="W", font=("Consolas",25), width=3).pack(side='top')
button = Button(frame, text="A", font=("Consolas",25), width=3).pack(side="left")
button = Button(frame, text="S", font=("Consolas",25), width=3).pack(side='left')
button = Button(frame, text="D", font=("Consolas",25), width=3).pack(side='left')

window.mainloop()