from tkinter import *
import pandas as pd
from password import password
import openpyxl

window = Tk()
window.title("MY PASSWORD MANAGER")
window.minsize(width=700, height=300)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# WEBSITE BOX
website_label = Label(text='Website:', font=("Arial", 12, 'bold'))
website_label.grid(column=0, row=1)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1)

# Email Box
email_label = Label(text="email-address:", font=("Arial", 12, 'bold'))
email_label.grid(column=0, row=2)

email_entry = Entry(width=50)
email_entry.insert(string="youremail@gmail.com", index=0)
email_entry.grid(column=1, row=2)

# Password Box
password_label = Label(text="password:", font=("Arial", 12, 'bold'))
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)


def save_password():
    inputs = {
        "Website Name": website_entry.get(),
        "Password": password_entry.get(),
        "Email Address": email_entry.get()
    }

    fi_le = pd.DataFrame(inputs, index=[0])
    fi_le.to_excel("data.xlsx", 'a')


def generate_password():
    password_entry.insert(END, string=password)


# generate password button
g_pass_button = Button(text="GENERATE", command=generate_password, font=("Arial", 12, 'bold'), width=10)
g_pass_button.grid(column=3, row=3)

# save password button
save_password_button = Button(text="save password", command=save_password, font=("Arial", 12, 'bold'), width=30)
save_password_button.grid(column=1, row=4)

window.mainloop()
