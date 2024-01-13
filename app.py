import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip

window = tk.Tk()
window.title('Password Generator')
window.geometry("700x500")
window.configure(bg='white', padx=100, pady=50)



alphanumeric_letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I',
                         'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
                           's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


file_path = '/Users/sylwestersojka/Documents/VS_reposittory/Password_generator/data.txt'



# ---------- Saving to file -------------------#

def save_user_input_to_file(file_path=file_path):

    user_website = entry_website.get()
    user_email = entry_credentials.get()
    user_password = entry_password.get()

    print(len(user_password))


    if len(user_email) == 0 or len(user_password) == 0:
        messagebox.showerror(title="Empty fields detected", message="Please do not leave any of the field blank")

    else:


        output_string = f"{user_website} | {user_email} | {user_password}"

        is_ok = messagebox.askokcancel(title=user_website, message=f"Is Email: {user_email} \n and Password: {user_password}\n Correct to proceed?")

        if is_ok:
            with open(file_path, 'a') as file:
                file.write(output_string + "\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)

def generate_password():

    password = []
    
    password_letters = [choice(alphanumeric_letters) for _ in range(randint(6, 8))]
    password_symbols = [choice(special_characters) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password = password_letters + password_numbers + password_symbols
    shuffle(password)
    
    new_pass = ''.join(password)

    pyperclip.copy(new_pass)
    entry_password.insert(0, new_pass)

  

    



# ---------- GUI delcaration -------------------#
canvas=tk.Canvas(window, width=200, height=200, bg='white')
canvas.grid(padx=50, pady=20 ,column=1, row=0)

canv_h = 200
canv_w = 200
logo_h = 153
logo_w = 179

x_coords = (canv_w - logo_w) // 2
y_coords = (canv_h - logo_h) // 2

logo = PhotoImage(file='logo.png')
canvas.create_image(x_coords, y_coords, anchor='nw', image=logo)

label_website = Label(text="Website:" , bg='white', fg='black')
label_website.grid(column=0, row=1)


label_credentials = Label(text="Email/Username:" , bg='white', fg='black')
label_credentials.grid(column=0, row=2, sticky='e')

label_password = Label(text="Password:" , bg='white', fg='black')
label_password.grid(column=0, row=3)

entry_website = Entry(width=30, fg='black', bg='white')
entry_website.grid(column=1, row=1, columnspan=2, pady=1)
entry_website.focus()

entry_credentials = Entry(width=30, fg='black', bg='white')
entry_credentials.grid(column=1, row=2, columnspan=2, pady=1)
entry_credentials.insert(0, "1404_pornosiara@gmail.com")

entry_password = Entry(width=13, fg='black', bg='white', show="*")
entry_password.grid(column=1, row=3)

button_generate_password = Button(text="Generate Password", fg='black', width=12, command=generate_password)
button_generate_password.grid(column=2, row=3, sticky='w')

button_add_user = Button(text="Add", width=28, fg='black', bg='white', command=save_user_input_to_file)
button_add_user.grid(column=1, row=4, columnspan=2, pady=1)



window.mainloop()