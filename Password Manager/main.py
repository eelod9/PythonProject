from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
FONT_NAME = "Times New Roman"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= randint(8,10)
    nr_symbols = randint(2,14)
    nr_numbers = randint(2,4)

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

   
    pw_letters = [choice(letters) for char in range(nr_letters) ]
    pw_symbols = [choice(symbols) for char in range(nr_symbols) ]
    pw_numbers = [choice(numbers) for char in range(nr_numbers) ]
    ''' 
    for char in range(nr_letters):
        pw.append(random.choice(letters))
    for char in range(nr_symbols):
        pw.append(random.choice(symbols))
    for char in range(nr_numbers):
        pw.append(random.choice(numbers))

    ''' 
    pw_list =  pw_letters + pw_symbols + pw_numbers
    shuffle(pw_list)
    #print(pw)


    final = "".join(pw_list)
    password_entry.insert(0,final)
    
    pyperclip.copy(final)
    print(final)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    pw = password_entry.get()
    new_data = {
        website: {
            "email":email,
            "password": pw
        }
    }
    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(title= "Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("./Password Manager/bimil.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("boo no file found")
            with open("./Password Manager/bimil.json", 'w') as file:
                json.dump(new_data,file, indent=4)
        else:
            data.update(new_data)

            with open("./Password Manager/bimil.json", 'w') as file:
                json.dump(data,file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            
#------search function------------------------
def search():
    website = website_entry.get()
    try:
        with open("./Password Manager/bimil.json", 'r') as file:
            filedata = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title= "Error", message="No Data File Found")
    else:
        if website in filedata:
            found_email = filedata[website]["email"]
            found_pw = filedata[website]["password"]
            new_mssg = f"Email: {found_email} \nPassword: {found_pw}"
            messagebox.showinfo(title= website, message=new_mssg)
        else:
            messagebox.showinfo(title= website, message="No details for the website exists")


       
    
    
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./Password Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ella@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text = "Search", width= 13,command = search)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()