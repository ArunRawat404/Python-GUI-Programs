from tkinter import *  # it only import classes and constants
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip  # for copy/paste clipboard functions
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # using list comprehension
    password_letters = [(choice(letters)) for _ in range(randint(8, 10))]
    password_symbols = [(choice(symbols)) for _ in range(randint(2, 4))]
    password_numbers = [(choice(numbers)) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_name = website_entry.get()
    email_id = email_entry.get()
    password = password_entry.get()
    # JSON format(javascript object notation)
    new_data = {
        website_name: {
            "email": email_id,
            "password": password,
        }
    }

    # to check if field is empty
    if len(website_name) == 0 or len(email_id) == 0 or len(password) == 0:
        messagebox.showinfo(title="Field empty", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)  # to load data of json file
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)  # to write data in json file
        finally:
            website_entry.delete(0, END)  # will clear the entry filed
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
canvas = Canvas(width=200, heigh=200, )
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=37)
website_entry.grid(column=1, row=1)
website_entry.focus()  # to keep cursor at website_label as default

email_entry = Entry(width=56)
email_entry.grid(column=1, row=2, columnspan=2)
# Add some text to begin with
email_entry.insert(END, string="Your_Username/email")

password_entry = Entry(width=37)
password_entry.grid(column=1, row=3)

# button
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=48, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
