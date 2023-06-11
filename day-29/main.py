from tkinter import *
from tkinter import messagebox
import pyperclip
import random
from random import choice, randint, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_letters = [random.choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Pythonic simplification alert
    # Join works on any iterable, e.g. tuples, dictionaries(keys) and lists
    password = "".join(password_list)

    pwd_entry.delete(0, END)
    pwd_entry.insert(0, password)
    pyperclip.copy(pwd_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    user = user_entry.get()
    pwd = pwd_entry.get()

    create_data_entry = website + ', ' + user + ', ' + pwd + '\n'

    if len(website) == 0 or len(user) == 0 or len(pwd) == 0:
        messagebox.showerror(title="Password Manager", message="Please make sure no field is left empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n Email: {user}'
                                                              f'\n Password:{pwd} .\n Is it okay to save?')
        if is_ok:
            with open("data.csv", "a") as data_file:
                data_file.write(create_data_entry)

            pyperclip.copy(pwd_entry.get())

            website_entry.delete(0, END)
            pwd_entry.delete(0, END)
            messagebox.showinfo(title="Passwrd Manager",
                                message="The password for this website and user was successfully "
                                        "saved!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
# Centering the image by putting it in half of width and half of height
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels creation
website_label = Label(text="Website:")
user_label = Label(text="Email/Username:")
pwd_label = Label(text="Password:")

website_label.grid(column=0, row=1)
user_label.grid(column=0, row=2)
pwd_label.grid(column=0, row=3)

# Inputs creation
website_entry = Entry(width=35)
user_entry = Entry(width=35)
pwd_entry = Entry(width=21)

website_entry.grid(column=1, row=1, columnspan=2)
user_entry.grid(column=1, row=2, columnspan=2)
pwd_entry.grid(column=1, row=3)

# Focus cursor on website and pre-fill the email option
website_entry.focus()
user_entry.insert(0, "intz.katerina@gmail.com")

generate_button = Button(text="Generate pass", command=generate_password)
generate_button.grid(column=2, row=3)

save_button = Button(text="Save", command=save, width=33)
save_button.grid(column=1, row=4, columnspan=3)

window.mainloop()
