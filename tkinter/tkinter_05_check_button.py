from tkinter import *

window = Tk()

photo = PhotoImage(file="small_logo.png")
#x = IntVar() # if we use this , we should use 1 and 0 in the onvalue and offvalue
#x = BooleanVar() # if we use this , we should use True and False in the onvalue and offvalue
x = StringVar() # if we use this , we should use "YES" and "NO" in the onvalue and offvalue

def display():

    if (x.get() == "YES"):   # base on x we should change the condition
        print('you agree')
    else:
        print("you don't agree")

check_button = Checkbutton(window,
                           text='I agree to something',
                           variable=x,
                           onvalue="YES",
                           offvalue="NO",
                           command=display,
                           font=('Arial', 10),
                           fg="#00FF00",
                           bg="black",
                           activebackground="black",
                           activeforeground="#00FF00",
                           padx=10,
                           pady=10,
                           image=photo,
                           compound="left"
                           )

check_button.pack()

window.mainloop()
