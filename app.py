from tkinter import *
from user.admin import admin_code
from user.patient import patient_home

def call_admin():
    admin_code(screen)

def call_patient():
    patient_home(screen)

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Welcome")
    Label(text="Hospital Management", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Admin",height="2",width="30", command=call_admin).pack()
    Label(text="").pack()
    Button(text="Patient", height="2", width="30", command=call_patient).pack()

    screen.mainloop()

main_screen()
