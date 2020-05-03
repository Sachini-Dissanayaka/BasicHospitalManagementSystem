from tkinter import *
from authentication.register import register
from authentication.login import login

def reg_form():
    register(screen_recep,"receptionist")

def log_form():
    login(screen_recep)

#home page: Login and registration
def receptionist_home(screen):
    global screen_recep
    screen_recep = Toplevel(screen)
    screen_recep.title("Receptionist")
    screen_recep.geometry("300x250")
    Label(screen_recep, text="").pack()
    Label(screen_recep,text="Hospital Management", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_recep, text="").pack()
    Button(screen_recep, text="Login", height="2", width="30",command = log_form).pack()
    Label(screen_recep, text="").pack()
    Button(screen_recep, text="Register", height="2", width="30",command = reg_form).pack()