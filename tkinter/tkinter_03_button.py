from tkinter import *

window = Tk()

photo = PhotoImage(file='small_logo.png')

count = 0
def click():
    global count
    print('you click the button')
    count += 1
    print(count)

button = Button(window, 
                text= 'click me',
                command=click, 
                font=('Comic Sans',30),
                fg="#00FF00",
                bg="black", 
                activeforeground="#00FF00", # this option and the downer option will help when
                activebackground="black",   # you click the button the color doesn't change!
                #state=DISABLED,            # if we use this function we can not click any more
                image=photo, 
                compound='bottom'           # if we don't use this fucntion the text doen not show
                )                

button.pack()     # if we don't use this function the button doesn't appear
window.mainloop()