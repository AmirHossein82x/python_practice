from tkinter import *
window = Tk()
photo = PhotoImage(file='small_logo.png')
Label = Label(window,
              text='Hello World',
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='black', 
              relief=RAISED, 
              bd=10, 
              padx=20, 
              pady=20, 
              image=photo,
              compound='top')


Label.pack() # it place the text in the top
#Label.place(x = 0, y=100) # it place the text where ever we want


window.mainloop()