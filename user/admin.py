from tkinter import *
from user.doctor import doctor_home
from user.manager import receptionist_home

def doctor():
    doctor_home(screen_staff)

def receptionist():
    receptionist_home(screen_staff)

#select the category: doctor or receptionist
def staff():
    global screen_staff
    screen_staff = Toplevel(screen_admin)
    screen_staff.title("Staff")
    screen_staff.geometry("300x250")
    Label(screen_staff, text="Select your category", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_staff, text="").pack()
    Button(screen_staff, text="Doctor", height="2", width="30",command = doctor).pack()
    Label(screen_staff, text="").pack()
    Button(screen_staff, text="Receptionist", height="2", width="30",command = receptionist).pack()

def set_code():
    code_info = adminCode.get()
    Label(screen_admin, text="").pack()
    if(code_info=="12345"):
        Label(screen_admin, text="Admin Code is Correct", fg="green", font=("Calibri", 11)).pack()
        staff()
    else:
        Label(screen_admin, text="Code is incorrect,Check Again", fg="red", font=("Calibri", 11)).pack()

#set admin code
def admin_code(screen):
    global screen_admin
    screen_admin = Toplevel(screen)
    screen_admin.title("Admin")
    screen_admin.geometry("300x250")
    global adminCode
    global adminCode_entry

    adminCode = StringVar()
    Label(screen_admin, text="Please enter admin code below", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_admin, text="").pack()
    Label(screen_admin, text="Admin Code").pack()
    adminCode_entry = Entry(screen_admin, textvariable=adminCode)
    adminCode_entry.pack()
    Label(screen_admin, text="").pack()
    Button(screen_admin, text="Submit", height="1", width="10", command=set_code).pack()