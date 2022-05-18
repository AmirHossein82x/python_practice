from tkinter import *
from tkinter import filedialog

def save():

    file = filedialog.asksaveasfile(initialdir="D:\\python_exesize",
                                    defaultextension=".txt",
                                    filetypes = [
                                           ("text file", ".txt"),
                                           ("HTML file", ".html"),
                                           ("all file", ".*")
                                        ]
                                                 )

    if file is None:   # if we change our mind to save, it will prevent to see error
        return 
        
    # if we don't use write method the file will save empty
    fileText = str(text.get('1.0', END))
    #fileText = input('enter text: ') we can use this way too
    file.write(fileText)
    file.close()

window = Tk()

text = Text(window,
            font=("comic sans", 20),
            width=20,
            height=8,
            padx=4,
            pady=4,
            bg="#f7ffde",
            fg="blue"
            )

text.pack()

button = Button(window,text="save",
                command=save,
                bg="#f7ffde"
                )
button.pack()

window.mainloop()