from tkinter import *
import hashlib
import json

def close_window():
    screen_reg.destroy()

def register_user():
    username_info = username.get()
    password_info = password.get()
    passwordCheck = str(password_info)
    label = Label(screen_reg,text="")
    if not (any(x.isupper() for x in passwordCheck) and any(x.islower() for x in passwordCheck) and any(
            x.isdigit() for x in passwordCheck)):
        password_entry.delete(0, END)
        label = Label(screen_reg, text="Password should contain any lower letter,upper latter and digit", fg="red",font=("Calibri", 11))
        label.pack()
        label.after(10000, lambda: label.destroy())
    else:
        password_info = hashlib.md5(password_info.encode()).hexdigest()
        with open("config.json",'r') as json_file:
            data = json.load(json_file)
            u_id = len(data['users'])+1
            data['users'].append({
                'id':u_id,
                'name':username_info,
                'password':password_info,
                'category':type,
            })
        with open('config.json','w') as output_file:
            json.dump(data,output_file)

        username_entry.delete(0,END)
        password_entry.delete(0,END)

        Label(screen_reg, text="Registration Success", fg="green",font = ("Calibri",11)).pack()
        Label(screen_reg, text="").pack()
        Button(screen_reg, text="Close", height="1", width="10",command = close_window).pack()

def register(screen,category):
    global screen_reg
    screen_reg= Toplevel(screen)
    screen_reg.title("Register")
    screen_reg.geometry("300x250")
    global username
    global password
    global type
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    type = category
    Label(screen_reg, text="Please enter details below").pack()
    Label(screen_reg, text="").pack()
    Label(screen_reg, text = "Username *").pack()
    username_entry = Entry(screen_reg, textvariable=username)
    username_entry.pack()
    Label(screen_reg, text = "Password *").pack()
    password_entry = Entry(screen_reg, textvariable=password)
    password_entry.pack()
    Label(screen_reg, text="").pack()
    Button(screen_reg, text="Register", height="1", width="10",command = register_user).pack()