from json import JSONDecodeError
from pathlib import Path
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json


# ------- Password Generator ----------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for i in range(nr_letters)]

    password_list += [random.choice(symbols) for j in range(nr_symbols)]

    password_list += [random.choice(numbers) for k in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # for char in password_list:
    #   password += char


# -------
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            search_keyword = website
    except (FileNotFoundError, JSONDecodeError):
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if search_keyword in data:
            email = data[search_keyword]["email"]
            password = data[search_keyword]["password"]
            messagebox.showinfo(title=search_keyword,
                                message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")

window = Tk()

window.title("Password manager")

window.config(padx=50, pady=50)

# timer_label = Label(text="Timer", font=("Arial", 20, "bold"))
# timer_label.grid(column=1, row=0)
# timer_label.config(padx=20, pady=5)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_entry = Label(text='Password:')
password_entry.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text='Search', width=15, command=find_password)
search_button.grid(row=1, column=2, columnspan=2)

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "jagadeesh@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text='Generate Password', width=15, command=generate_password)
generate_password_button.grid(row=3, column=2)




def button_clicked():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    if len(email) == 0 or len(password) == 0:
        print('entered')
        messagebox.showerror("Oops", "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)
            else:
               # updating old data with new data
               data.update(new_data)
               with open("data.json", "w") as data_file:
                   # Saving updated data
                   json.dump(data, data_file, indent=4)
            finally:
               website_entry.delete(0, END)
               password_entry.delete(0, END)












add_button = Button(text='Add', command=button_clicked, width=30)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
