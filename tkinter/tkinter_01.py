from tkinter import *
window = Tk()
window.geometry('420x420')
window.title('my first GUI program')

icon = PhotoImage(file='small_logo.png')
window.iconphoto(True, icon)
window.config(background='black')

window.mainloop()