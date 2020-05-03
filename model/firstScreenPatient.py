from tkinter import *
import json
import base64

def drugReport():
    global screen_p5
    screen_p5 = Toplevel(screen_p1)
    screen_p5.title("Patient")
    screen_p5.geometry("300x250")
    Label(screen_p5, text="").pack()
    Label(screen_p5, text="Drug Details", font=("Calibri", 13)).pack()
    with open("config.json", "r") as json_file:
        data = json.load(json_file)
        for user in data['drugData']:
            if user["name"]==u_name and user["user_id"]==u_id:
                Label(screen_p5, text="").pack()
                Label(screen_p5, text="Drug Report :" + user["date"], fg="red", font=("Calibri", 11)).pack()
                Label(screen_p5, text="Age :" + user["age"]).pack()
                Label(screen_p5, text="Weight :" + user["weight"]).pack()
                Label(screen_p5, text="Drugs :" + user["drugs"]).pack()
                Label(screen_p5, text="Issued by :Dr." + user["doctor"]).pack()

def sickReport():
    global screen_p4
    screen_p4 = Toplevel(screen_p1)
    screen_p4.title("Patient")
    screen_p4.geometry("300x250")
    Label(screen_p4, text="").pack()
    Label(screen_p4, text="Sickness Details", font=("Calibri", 13)).pack()
    with open("config.json", "r") as json_file:
        data = json.load(json_file)
        for user in data['sicknessData']:
            if user["name"]==u_name and user["user_id"]==u_id:
                Label(screen_p4, text="").pack()
                Label(screen_p4, text="Sickness Report :" + str(user["id"]), fg="red", font=("Calibri", 11)).pack()
                Label(screen_p4, text="Age :" + user["age"]).pack()
                Label(screen_p4, text="Disease :" + user["disease"]).pack()
                Label(screen_p4, text="Duration :" + user["duration"]).pack()
                Label(screen_p4, text="Issued by :Dr." + user["doctor"]).pack()

def labReport():
    global screen_p3
    screen_p3 = Toplevel(screen_p1)
    screen_p3.title("Patient")
    screen_p3.geometry("300x250")
    Label(screen_p3, text="").pack()
    Label(screen_p3, text="Lab Reports", font=("Calibri", 13)).pack()
    with open("config.json", "r") as json_file:
        data = json.load(json_file)
        for user in data['labData']:
            if user["name"]==u_name and user["user_id"]==u_id:
                Label(screen_p3, text="").pack()
                Label(screen_p3, text="Lab Report :" + user["date"], fg="red", font=("Calibri", 11)).pack()
                Label(screen_p3, text="Age :" + user["age"]).pack()
                Label(screen_p3, text="Description :" + user["description"]).pack()
                Label(screen_p3, text="Issued by :Dr." + user["doctor"]).pack()

def personalData():
    global screen_p2
    screen_p2 = Toplevel(screen_p1)
    screen_p2.title("Patient")
    screen_p2.geometry("300x250")
    Label(screen_p2, text="").pack()
    Label(screen_p2, text="My Information", font=("Calibri", 13)).pack()
    with open("config.json", "r") as json_file:
        data = json.load(json_file)
        for user in data['personalData']:
            if u_name in user.values() and u_id in user.values():
                Label(screen_p2, text="").pack()
                Label(screen_p2, text="Name :" + u_name).pack()
                Label(screen_p2,
                      text="NIC :" + base64.b64decode(user["nic"].encode('ascii')).decode('ascii')).pack()
                Label(screen_p2, text="Date of Birth :" + user["dob"]).pack()
                Label(screen_p2, text="Gender :" + user["gender"]).pack()
                Label(screen_p2,
                      text="Phone :" + base64.b64decode(user["phone"].encode('ascii')).decode('ascii')).pack()
                Label(screen_p2, text="Home Town :" + user["town"]).pack()

def firstFormPatient(id,name,screen):
    global screen_p1
    screen_p1 = Toplevel(screen)
    screen_p1.title("Patient")
    screen_p1.geometry("300x250")

    global u_id
    global u_name

    u_id = id
    u_name = name

    Label(screen_p1, text="").pack()
    Label(screen_p1, text="Hospital Management", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_p1, text="").pack()
    Button(screen_p1, text="Personal Details", height="2", width="30", command=personalData).pack()
    Label(screen_p1, text="").pack()
    Button(screen_p1, text="Lab Reports", height="2", width="30", command=labReport).pack()
    Label(screen_p1, text="").pack()
    Button(screen_p1, text="Sickness Details", height="2", width="30", command=sickReport).pack()
    Label(screen_p1, text="").pack()
    Button(screen_p1, text="Drug Details", height="2", width="30", command=drugReport).pack()