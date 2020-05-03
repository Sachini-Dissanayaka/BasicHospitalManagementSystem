from tkinter import *
from authentication.login import login

def log_form():
    login(screen_patient)

def patient_home(screen):
    global screen_patient
    screen_patient = Toplevel(screen)
    screen_patient.title("Patient")
    screen_patient.geometry("300x250")
    Label(screen_patient, text="").pack()
    Label(screen_patient,text="Hospital Management", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_patient, text="").pack()
    Button(screen_patient, text="Login", height="2", width="30",command = log_form).pack()
    Label(screen_patient, text="").pack()