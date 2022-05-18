from tkinter import *

def submit():

        #item = list_box.get(list_box.curselection()) # we use this when selectmode is not set to MULTIPLE
        #print('you have ordered %s:'%item)

        foods = []
        for index in list_box.curselection():  # it's a tuple which contains index
            foods.insert(index, list_box.get(index))

        print('you have ordered:')

        for food in foods:
            print(food)

def add():

    list_box.insert(list_box.size(), entry_box.get())
    list_box.config(height=list_box.size())
    entry_box.delete(0, END)  # it will delete what you wrote in the entry_box

def delete():
    for index in reversed(list_box.curselection()):  # if we don't use reversed ---> delete button don't perform well
        list_box.delete(index)
    #list_box.delete(list_box.curselection())   # we use this when selectmode is not set to MULTIPLE
    list_box.config(height=list_box.size())
    
window = Tk()

list_box = Listbox(window,
                   bg="#f7ffde",
                   font=("Constantia", 35),
                   width=12,
                   selectmode=MULTIPLE, # it allows you to choose more than 1 item
                   )
list_box.pack()

list_box.insert(1, 'pizza')
list_box.insert(2, 'pasta')
list_box.insert(3, 'garlic bread')
list_box.insert(4, 'soup')
list_box.insert(5, 'salad')

list_box.config(height=list_box.size()) # it adjusts the size of the listbox exatly base on number of items

entry_box = Entry(window)

entry_box.pack()

submit_button = Button(window,
                       text='submit',
                       command=submit,
                       bg="#f7ffde",
                       fg="blue"
                       )
submit_button.pack()

add_button = Button(window,
                    text='add',
                    command=add,
                    bg="#f7ffde",
                    fg="green"
                    )
add_button.pack()

delete_button = Button(window,
                    text='delete',
                    command=delete,
                    bg="#f7ffde",
                    fg='red'
                    )

delete_button.pack()

window.mainloop()