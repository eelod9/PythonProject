from tkinter import *



window = Tk()
window.title("My First Gui Program")
window.minsize(500,300)
window.config(padx=20, pady=20)




def add(*args):
    total = 0
    for i in args:
        total +=i
    return total

print(add(4,5,6,7))


def calculate(n ,**kwargs):
    print(type(kwargs))
    #for key,value in kwargs.items():
    #    print(key)
    #print(kwargs["add"])
    n+= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3,multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car= Car(make = "Nissan", model = "GT-R")
print(my_car.model)
my_label = Label(text = "Hello", font=("Arial",24,"bold"))
my_label.grid(row= 0, column= 0)
def button_clicked():
    user_input = input.get()
    my_label.config(text = user_input)
    
button = Button(text = "Click Me", command= button_clicked)
button.grid(row=1, column=1)



input = Entry(width= 10)
input.grid(row=2, column=3)

new_button = Button(text="new Button")
new_button.grid(row= 0, column=2)



window.mainloop()