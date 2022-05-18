from tkinter import *

def submit():

    username = entry.get()
    print('hello %s'%username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) -1, END)
window = Tk()

entry = Entry(window,
              font=('Arial', 20),
              bg='black',
              fg='#00FF00',
              relief=RAISED,
              border=10,
              borderwidth= 10,
              cursor='cross',
              show='*',
              state='normal',
              )
#entry.insert(0,'password: ') # it takes 2 argument: first: index second: default text

entry.pack(side=LEFT) 

submit_button = Button(window,
                       text='submit',
                       command=submit, 
                       bg='black',
                       fg= '#00FF00',
                       activebackground='black',
                       activeforeground='#00FF00',
                       )

submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text='delete',
                       command=delete,
                       bg='black',
                       fg= '#00FF00',
                       activebackground='black',
                       activeforeground='#00FF00',
                       )
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                       text='backspace',
                       command=backspace,
                       bg='black',
                       fg= '#00FF00',
                       activebackground='black',
                       activeforeground='#00FF00',
                       )
backspace_button.pack(side=RIGHT)

window.mainloop()