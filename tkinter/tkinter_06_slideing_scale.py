from tkinter import *

def submit():
    print('the temprature is: %s degree C' %(scale.get()))
window = Tk()

hot_image = PhotoImage(file='fire.png')
hot_label = Label(window,
                  image=hot_image)
hot_label.pack()

scale = Scale(window,
              from_=100, to=0,
              length=600,
              orient=VERTICAL,  # we can also use HORIZONTAL
              font=("Consolas", 20),
              tickinterval=10,  # adds numeric indicators for value
              showvalue=0,      # it hides current value
              resolution=5,     # it will set the increasment of slider 
              troughcolor='#69EAFF', # it will set the color 
              fg="#FF1C00",          # it will set the number's color
              bg="black",              
              )

scale.set(50) # it will set default number of scale
scale.set(((scale['from']-scale['to'])/2) + scale['to']) # it is just like above line but in different way 

scale.pack()

cold_image = PhotoImage(file='snow.png')
cold_label = Label(window,
                  image=cold_image,
                  )
                  
cold_label.pack()

button = Button(window,
                text="submit",
                command=submit,
                )
button.pack()

window.mainloop()