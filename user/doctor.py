from tkinter import *
from authentication.register import register
from authentication.login import login

def reg_form():
    register(screen_doctor,"doctor")

def log_form():
    login(screen_doctor)

def doctor_home(screen):
    global screen_doctor
    screen_doctor = Toplevel(screen)
    screen_doctor.title("Doctor")
    screen_doctor.geometry("300x250")
    Label(screen_doctor, text="").pack()
    Label(screen_doctor,text="Hospital Management", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_doctor, text="").pack()
    Button(screen_doctor, text="Login", height="2", width="30",command = log_form).pack()
    Label(screen_doctor, text="").pack()
    Button(screen_doctor, text="Register", height="2", width="30",command = reg_form).pack()