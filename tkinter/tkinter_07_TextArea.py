from tkinter import *

def submit():

    input = text.get('1.0', END)  # "1.0" is index if we change it to "2.0" it doesn't print line 1
    print(input)

window = Tk()

text = Text(window,
            bg='light yellow',
            font=('Ink free', 25),
            height=8,
            width=20,
            padx=20,  # it will put distance from the boarder
            pady=20,  # it will put distance from the boarder
            fg='purple'
            )  
text.pack()

button = Button(window, command=submit, text="submit")

button.pack()

window.mainloop()