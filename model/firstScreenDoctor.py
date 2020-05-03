from tkinter import *
import json

def sicknessDataView():
    username_info = username.get()

    with open("config.json", "r") as json_file:
        data = json.load(json_file)
        for user in data['sicknessData']:
            if username_info in user.values():
                Label(screen_doc4, text="").pack()
                Label(screen_doc4, text="Sickness Report :" + str(user["id"]), fg="red", font=("Calibri", 11)).pack()
                Label(screen_doc4, text="Age :" + user["age"]).pack()
                Label(screen_doc4, text="Disease :" + user["disease"]).pack()
                Label(screen_doc4, text="Duration :" + user["duration"]).pack()
                Label(screen_doc4, text="Issued by : Dr." + user["doctor"]).pack()

def sicknessDataViewScreen():
    global screen_doc4
    screen_doc4 = Toplevel(screen_doc2)
    screen_doc4.title("Doctor")
    screen_doc4.geometry("400x400")

    global username
    global username_entry
    username = StringVar()
    Label(screen_doc4, text="Please enter username below").pack()
    Label(screen_doc4, text="").pack()
    Label(screen_doc4, text="Username").pack()
    username_entry = Entry(screen_doc4, textvariable=username)
    username_entry.pack()
    Label(screen_doc4, text="").pack()
    Button(screen_doc4, text="Search", height="1", width="10", command=sicknessDataView).pack()

def sicknessDataSubmit():
    username_info = username.get()
    age_info = age.get()
    disease_info = disease.get()
    duration_info = duration.get()
    result = "fail"
    with open("config.json", 'r') as json_file:
        data = json.load(json_file)
        for user in data["users"]:
            if user["name"] == username_info:
                data['sicknessData'].append({'id':len(data['sicknessData'])+1,'user_id': user['id'],
                    'name': username_info,'age': age_info,'disease': disease_info,
                    'duration': duration_info,
                    'doctor': d_name
                })
                result = "success"
    with open('config.json', 'w') as output_file:
        json.dump(data, output_file)
    if (result == "success"):
        Label(screen_doc3, text="Data Update Successfully", fg="green", font=("Calibri", 11)).pack()
        username_en.delete(0, END)
        age_en.delete(0, END)
        disease_en.delete(0, END)
        duration_en.delete(0, END)
    else:
        Label(screen_doc3, text="Check Username", fg="red", font=("Calibri", 11)).pack()

def sicknessDataSubmitScreen():
    global screen_doc3
    screen_doc3 = Toplevel(screen_doc2)
    screen_doc3.title("Doctor")
    screen_doc3.geometry("400x400")

    global username
    global age
    global disease
    global duration

    global username_en
    global age_en
    global disease_en
    global duration_en

    username = StringVar()
    age = StringVar()
    disease = StringVar()
    duration = StringVar()

    Label(screen_doc3, text="Please enter details below").pack()
    Label(screen_doc3, text="").pack()
    Label(screen_doc3, text="Username").pack()
    username_en=Entry(screen_doc3, textvariable=username)
    username_en.pack()
    Label(screen_doc3, text="Age").pack()
    age_en=Entry(screen_doc3, textvariable=age)
    age_en.pack()
    Label(screen_doc3, text="Disease").pack()
    disease_en=Entry(screen_doc3, textvariable=disease)
    disease_en.pack()
    Label(screen_doc3, text="Duration").pack()
    duration_en=Entry(screen_doc3, textvariable=duration)
    duration_en.pack()
    Label(screen_doc3, text="").pack()
    Button(screen_doc3, text="Submit", height="1", width="10", command=sicknessDataSubmit).pack()

def sicknessData():
    global screen_doc2
    screen_doc2 = Toplevel(screen_doc1)
    screen_doc2.title("Doctor")
    screen_doc2.geometry("300x250")
    Label(screen_doc2, text="").pack()
    Label(screen_doc2, text="Sikness Details", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_doc2, text="").pack()
    Button(screen_doc2, text="Update Data", height="2", width="30", command=sicknessDataSubmitScreen).pack()
    Label(screen_doc2, text="").pack()
    Button(screen_doc2, text="Search Data", height="2", width="30", command=sicknessDataViewScreen).pack()

def labView():
    username_info = username.get()

    with open("config.json", "r") as json_file:
        data = json.load(json_file)
        for user in data['labData']:
            if username_info in user.values():
                Label(screen_doc7, text="").pack()
                Label(screen_doc7, text="Lab Report :" + user["date"],fg="red",font=("Calibri", 11)).pack()
                Label(screen_doc7, text="Age :" + user["age"]).pack()
                Label(screen_doc7, text="Description :" + user["description"]).pack()
                Label(screen_doc7, text="Issued by : Dr." + user["doctor"]).pack()

def labViewScreen():
    global screen_doc7
    screen_doc7 = Toplevel(screen_doc5)
    screen_doc7.title("Doctor")
    screen_doc7.geometry("400x400")

    global username
    global username_entry
    username = StringVar()
    Label(screen_doc7, text="Please enter username below").pack()
    Label(screen_doc7, text="").pack()
    Label(screen_doc7, text="Username").pack()
    username_entry = Entry(screen_doc7, textvariable=username)
    username_entry.pack()
    Label(screen_doc7, text="").pack()
    Button(screen_doc7, text="Search", height="1", width="10", command=labView).pack()

def labSubmit():
    username_info = username.get()
    age_info = age.get()
    description_info = description.get()
    date_info = date.get()

    result = "fail"
    with open("config.json", 'r') as json_file:
        data = json.load(json_file)
        for user in data["users"]:
            if user["name"] == username_info:
                data['labData'].append({
                    'id': len(data['labData']) + 1,
                    'user_id': user['id'],
                    'name': username_info,
                    'age': age_info,
                    'description': description_info,
                    'date':date_info,
                    'doctor': d_name
                })
                result = "success"
    with open('config.json', 'w') as output_file:
        json.dump(data, output_file)

    if (result == "success"):
        Label(screen_doc6, text="Data Update Successfully", fg="green", font=("Calibri", 11)).pack()
        username_en.delete(0, END)
        age_en.delete(0, END)
        description_en.delete(0, END)
        date_en.delete(0, END)
    else:
        Label(screen_doc6, text="Check Username", fg="red", font=("Calibri", 11)).pack()

def labSubmitScreen():
    global screen_doc6
    screen_doc6 = Toplevel(screen_doc5)
    screen_doc6.title("Doctor")
    screen_doc6.geometry("350x400")
    global username
    global age
    global description
    global date

    global username_en
    global age_en
    global description_en
    global date_en

    username = StringVar()
    age = StringVar()
    description = StringVar()
    date = StringVar()

    Label(screen_doc6, text="Please enter details below").pack()
    Label(screen_doc6, text="").pack()
    Label(screen_doc6, text="Username").pack()
    username_en = Entry(screen_doc6, textvariable=username)
    username_en.pack()
    Label(screen_doc6, text="Age").pack()
    age_en = Entry(screen_doc6, textvariable=age)
    age_en.pack()
    Label(screen_doc6, text="Description").pack()
    description_en = Entry(screen_doc6, textvariable=description)
    description_en.pack()
    Label(screen_doc6, text="Date").pack()
    date_en = Entry(screen_doc6, textvariable=date)
    date_en.pack()
    Label(screen_doc6, text="").pack()
    Button(screen_doc6, text="Submit", height="1", width="10", command=labSubmit).pack()
def lab():
    global screen_doc5
    screen_doc5 = Toplevel(screen_doc1)
    screen_doc5.title("Doctor")
    screen_doc5.geometry("300x250")
    Label(screen_doc5, text="").pack()
    Label(screen_doc5, text="Lab Test Details", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_doc5, text="").pack()
    Button(screen_doc5, text="Update Data", height="2", width="30", command=labSubmitScreen).pack()
    Label(screen_doc5, text="").pack()
    Button(screen_doc5, text="Search Data", height="2", width="30", command=labViewScreen).pack()

def drugView():
    username_info = username.get()

    with open("config.json", "r") as json_file:
        data = json.load(json_file)
        for user in data['drugData']:
            if username_info in user.values():
                Label(screen_doc10, text="").pack()
                Label(screen_doc10, text="Drug Report :" + user["date"], fg="red", font=("Calibri", 11)).pack()
                Label(screen_doc10, text="Age :" + user["age"]).pack()
                Label(screen_doc10, text="Weight :" + user["weight"]).pack()
                Label(screen_doc10, text="Drugs :" + user["drugs"]).pack()
                Label(screen_doc10, text="Issued by : Dr." + user["doctor"]).pack()

def drugViewScreen():
    global screen_doc10
    screen_doc10 = Toplevel(screen_doc8)
    screen_doc10.title("Doctor")
    screen_doc10.geometry("400x400")

    global username
    global username_entry
    username = StringVar()
    Label(screen_doc10, text="Please enter username below").pack()
    Label(screen_doc10, text="").pack()
    Label(screen_doc10, text="Username").pack()
    username_entry = Entry(screen_doc10, textvariable=username)
    username_entry.pack()
    Label(screen_doc10, text="").pack()
    Button(screen_doc10, text="Search", height="1", width="10", command=drugView).pack()

def drugSubmit():
    username_info = username.get()
    age_info = age.get()
    weight_info = weight.get()
    drug_info = drugs.get()
    date_info = date.get()

    result = "fail"
    with open("config.json", 'r') as json_file:
        data = json.load(json_file)
        for user in data["users"]:
            if user["name"] == username_info:
                data['drugData'].append({
                    'id': len(data['drugData']) + 1,
                    'user_id': user['id'],
                    'name': username_info,
                    'age': age_info,
                    'weight': weight_info,
                    'drugs': drug_info,
                    'date': date_info,
                    'doctor': d_name
                })
                result = "success"
    with open('config.json', 'w') as output_file:
        json.dump(data, output_file)
    if (result == "success"):
        Label(screen_doc9, text="Data Update Successfully", fg="green", font=("Calibri", 11)).pack()
        username_en.delete(0, END)
        age_en.delete(0, END)
        weight_en.delete(0, END)
        drugs_en.delete(0, END)
        date_en.delete(0, END)
    else:
        Label(screen_doc9, text="Check Username", fg="red", font=("Calibri", 11)).pack()

def drugSubmitScreen():
    global screen_doc9
    screen_doc9 = Toplevel(screen_doc8)
    screen_doc9.title("Doctor")
    screen_doc9.geometry("350x400")

    global username
    global age
    global weight
    global drugs
    global date

    global username_en
    global age_en
    global weight_en
    global drugs_en
    global date_en

    username = StringVar()
    age = StringVar()
    weight = StringVar()
    drugs = StringVar()
    date = StringVar()

    Label(screen_doc9, text="Please enter drug details").pack()
    Label(screen_doc9, text="").pack()
    Label(screen_doc9, text="Username").pack()
    username_en = Entry(screen_doc9, textvariable=username)
    username_en.pack()
    Label(screen_doc9, text="Age").pack()
    age_en = Entry(screen_doc9, textvariable=age)
    age_en.pack()
    Label(screen_doc9, text="Weight").pack()
    weight_en = Entry(screen_doc9, textvariable=weight)
    weight_en.pack()
    Label(screen_doc9, text="Drugs").pack()
    drugs_en = Entry(screen_doc9, textvariable=drugs)
    drugs_en.pack()
    Label(screen_doc9, text="Date").pack()
    date_en = Entry(screen_doc9, textvariable=date)
    date_en.pack()
    Label(screen_doc9, text="").pack()
    Button(screen_doc9, text="Submit", height="1", width="10", command=drugSubmit).pack()
def drug():
    global screen_doc8
    screen_doc8 = Toplevel(screen_doc1)
    screen_doc8.title("Doctor")
    screen_doc8.geometry("300x250")
    Label(screen_doc8, text="").pack()
    Label(screen_doc8, text="Drug Details", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_doc8, text="").pack()
    Button(screen_doc8, text="Update Data", height="2", width="30", command=drugSubmitScreen).pack()
    Label(screen_doc8, text="").pack()
    Button(screen_doc8, text="Search Data", height="2", width="30", command=drugViewScreen).pack()

def firstFormDoc(name,screen):
    global screen_doc1
    global d_name
    d_name = name
    screen_doc1 = Toplevel(screen)
    screen_doc1.title("Doctor")
    screen_doc1.geometry("300x250")
    Label(screen_doc1, text="").pack()
    Label(screen_doc1,text="Hospital Management", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen_doc1, text="").pack()
    Button(screen_doc1, text="Sikness Data", height="2", width="30",command=sicknessData).pack()
    Label(screen_doc1, text="").pack()
    Button(screen_doc1, text="Lab Test Details", height="2", width="30", command=lab).pack()
    Label(screen_doc1, text="").pack()
    Button(screen_doc1, text="Drug Details", height="2", width="30", command=drug).pack()