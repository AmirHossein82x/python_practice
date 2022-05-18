from tkinter import *

foods = ['pizza', 'hamburger', 'hotdog']

def order():

    if (x.get() == 0):
        print('you ordered a pizza!')

    elif (x.get() == 1):
        print('you ordered a hamburger!')

    elif (x.get() == 2):
        print('you ordered a hotdog!')

    else:
        print('what?')

window = Tk()

pizza_image = PhotoImage(file='pizza.png')
hamburger_image = PhotoImage(file='hamburger.png')
hotdog_image = PhotoImage(file='hotdog.png')

images = [pizza_image, hamburger_image, hotdog_image]


x = IntVar()

for index in range(len(foods)):
    radio_button = Radiobutton(window,
                               text=foods[index],
                               variable=x,  # groups radio_buttons together if they share the same variable 
                               value=index, # assigns each radio_button a different value
                               padx=20,     # it will add spaces before text
                               font= ('impact', 50),      
                               image=images[index],
                               compound=LEFT,
                               indicatoron=0, # it will eliminate circle indicator
                               width=400,      # it will set width of radio buttons
                               command=order,
                              )  
                                   
    radio_button.pack(anchor=W) # anchor function will give them discipline


window.mainloop()