from tkinter import *
import json
import base64
from authentication.register import register
#First screen

def close_window():
    screen_recep2.destroy()

def regPatient():
    register(screen_recep1,"patient")

def personalDataView():
    username_info = username.get()

    with open("config.json", "r") as json_file:
        data = json.load(json_file)
        for user in data['personalData']:
            if username_info in user.values():
                Label(screen_recep4, text="").pack()
                Label(screen_recep4, text="Name :"+username_info).pack()
                Label(screen_recep4, text="NIC :" + base64.b64decode(user["nic"].encode('ascii')).decode('ascii')).pack()
                Label(screen_recep4, text="Date of Birth :" + user["dob"]).pack()
                Label(screen_recep4, text="Gender :" + user["gender"]).pack()
                Label(screen_recep4, text="Phone :" + base64.b64decode(user["phone"].encode('ascii')).decode('ascii')).pack()
                Label(screen_recep4, text="Home Town :" + user["town"]).pack()


def personalDataViewScreen():
    global screen_recep4
    screen_recep4= Toplevel(screen_recep3)
    screen_recep4.title("Receptionist")
    screen_recep4.geometry("400x400")

    global username
    global username_entry
    username = StringVar()
    Label(screen_recep4, text="Please enter username below").pack()
    Label(screen_recep4, text="").pack()
    Label(screen_recep4, text="Username").pack()
    username_entry = Entry(screen_recep4, textvariable=username)
    username_entry.pack()
    Label(screen_recep4, text="").pack()
    Button(screen_recep4, text="Search", height="1", width="10", command=personalDataView).pack()


def personalDataSubmit():
    username_info = username.get()
    dob_info = dob.get()
    gender_info = gender.get()
    phone_info = phone.get()
    phone_info = base64.b64encode(phone_info.encode('ascii')).decode('ascii')
    town_info = town.get()
    nic_info = nic.get()
    nic_info = base64.b64encode(nic_info.encode('ascii')).decode('ascii')
    result = "fail"
    with open("config.json",'r') as json_file:
        data = json.load(json_file)
        for user in data["users"]:
            if user["name"]==username_info:
                data['personalData'].append({
                    'id':user['id'],
                    'name':username_info,
                    'nic':nic_info,
                    'dob':dob_info,
                    'gender':gender_info,
                    'phone':phone_info,
                    'town':town_info
                })
                result = "success"

    with open('config.json','w') as output_file:
        json.dump(data,output_file)
    if(result=="success"):
        Label(screen_recep2, text="Data Update Successfully", fg="green", font=("Calibri", 11)).pack()
        username_entry.delete(0, END)
        nic_entry.delete(0, END)
        dob_entry.delete(0, END)
        gender_entry.delete(0, END)
        town_entry.delete(0, END)
        phone_entry.delete(0, END)
    else:
        Label(screen_recep2, text="Check Username", fg="red", font=("Calibri", 11)).pack()


def personalDataSubmitScreen():
    global screen_recep2
    screen_recep2 = Toplevel(screen_recep3)
    screen_recep2.title("Receptionist")
    screen_recep2.geometry("400x400")

    global username
    global nic
    global dob
    global gender
    global phone
    global town

    global username_entry
    global nic_entry
    global dob_entry
    global gender_entry
    global phone_entry
    global town_entry

    username = StringVar()
    nic = StringVar()
    dob = StringVar()
    gender = StringVar()
    phone = StringVar()
    town = StringVar()

    Label(screen_recep2, text="Please enter details below").pack()
    Label(screen_recep2, text="").pack()
    Label(screen_recep2, text="Username").pack()
    username_entry = Entry(screen_recep2, textvariable=username)
    username_entry.pack()
    Label(screen_recep2, text="NIC").pack()
    nic_entry = Entry(screen_recep2, textvariable=nic)
    nic_entry.pack()
    Label(screen_recep2, text="Date of Birth").pack()
    dob_entry = Entry(screen_recep2, textvariable=dob)
    dob_entry.pack()
    Label(screen_recep2, text="Gender").pack()
    gender_entry = Entry(screen_recep2, textvariable=gender)
    gender_entry.pack()
    Label(screen_recep2, text="Phone Number").pack()
    phone_entry = Entry(screen_recep2, textvariable=phone)
    phone_entry.pack()
    Label(screen_recep2, text="Current City").pack()
    town_entry = Entry(screen_recep2, textvariable=town)
    town_entry.pack()
    Label(screen_recep2, text="").pack()
    Button(screen_recep2, text="Submit", height="1", width="10", command=personalDataSubmit).pack()

def personalDataScreen():
    global screen_recep3
    screen_recep3 = Toplevel(screen_recep1)
    screen_recep3.title("Receptionist")
    screen_recep3.geometry("300x250")
    Label(screen_recep3, text="").pack()
    Label(screen_recep3, text="Personal Details", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_recep3, text="").pack()
    Button(screen_recep3, text="Update Data", height="2", width="30", command=personalDataSubmitScreen).pack()
    Label(screen_recep3, text="").pack()
    Button(screen_recep3, text="Search Data", height="2", width="30",command=personalDataViewScreen).pack()

def firstFormRecep(screen):
    global screen_recep1
    screen_recep1 = Toplevel(screen)
    screen_recep1.title("Receptionist")
    screen_recep1.geometry("300x250")
    Label(screen_recep1, text="").pack()
    Label(screen_recep1,text="Hospital Management", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_recep1, text="").pack()
    Button(screen_recep1, text="Patient Registration", height="2", width="30",command=regPatient).pack()
    Label(screen_recep1, text="").pack()
    Button(screen_recep1, text="Personal Details", height="2", width="30", command=personalDataScreen).pack()


