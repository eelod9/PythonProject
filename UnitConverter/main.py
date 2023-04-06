from tkinter import *



window = Tk()
window.title("My First Gui Program")
#window.minsize(300,200)
window.config(padx=20, pady=20)

label1 = Label(text="is equal to")
label1.grid(row=2, column=0)

label2 = Label(text="Miles")
label2.grid(row=1, column = 2)

label3 = Label(text="Km")
label3.grid(row=2, column= 2)

textbox1 = Entry(width= 10)
textbox1.grid(row = 1, column=1)
def calculateMtoK():
    userinput = textbox1.get()
    kmOutput =float(userinput) * 1.609344
    resultLabel.config(text= kmOutput)


resultLabel = Label(text="0")
resultLabel.grid(row=2, column=1)
button1 = Button(text="Calculate", command = calculateMtoK )
button1.grid(row=3, column=1)
window.mainloop()