from tkinter import *
from tkinter import messagebox

def click():

    #messagebox.showinfo()  # it will show an empty messagebox
    #messagebox.showinfo(title='this is an info messagebox', message='you are a person')


    #while True:   # it will repeat the line below
    #    messagebox.showwarning(title='WARNING', message='you have a virus!!!')

      
    #messagebox.showerror(title='ERROR', message='something went wrong') 


   # if messagebox.askokcancel(title='ask ok cancel', message='do you want to do the thing?'): # this line will return True or False
   #     print('you did a thing')
   # else:
   #     print('you canceled a thing! ')


   #if messagebox.askretrycancel(title='ask retry or cancel', message='do you want to retry?'): # this line will return True or False
   #     print('you retried a thing')
   #else:
   #     print('you canceled a thing! ')


   #if messagebox.askyesno(title="ask yes or no", message="do you like cake? "):
   #    print('I like cake too')
   #else:
   #    print("why do you don't like cake? ")


   #answer = messagebox.askquestion(title='question', message='do you like pie?')   # it returns yes or no
   #if answer == "yes":
   #    print('I like pie too')
   #else:
   #     print('why do not you like pie? ')


    answer = messagebox.askyesnocancel(title='yes no cancle', message='do you like to code? ') # it returns True False None

    if answer == True:
        print('you like to code! ')

    elif answer== False:
        print("why? ")
        
    elif answer == None:
        print('you cancled it! ')

        """
        we can change the icon with using icon method
        messagebox.askyesnocancel(title='yes no cancle', message='do you like to code? ', icon= "info")
        kind of icon: 1-> info  2-> warning  3-> error

        """


window = Tk()

button = Button(window,
                command=click,
                text='click me'
                )

button.pack()

window.mainloop()