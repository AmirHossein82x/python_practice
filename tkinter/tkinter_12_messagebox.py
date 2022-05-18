from tkinter import messagebox

logic = True

while logic:

    if messagebox.askyesno(title="IQ test", message='Are you stupid? '):
        print('I knew it')
        logic = False
        
    else:
        pass

