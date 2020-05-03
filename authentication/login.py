import hashlib
from model.firstScreenReceptionist import *
from model.firstScreenDoctor import *
from model.firstScreenPatient import *

def login_user():
    username_info = username.get()
    password_info = password.get()
    password_info = hashlib.md5(password_info.encode()).hexdigest()
    result = "fail"
    with open("config.json", "r") as json_file:
        data = json.load(json_file)
        for user in data['users']:
            if username_info in user.values() and password_info in user.values():
                current_user = user
                Label(screen_log, text=username_info+", login is successful!", fg="green", font=("Calibri", 11)).pack()
                result = "success"
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    if(result=="fail"):
        Label(screen_log, text=username_info + ", login is failed!", fg="red", font=("Calibri", 11)).pack()
    else:
        if current_user["category"]=="receptionist":
            firstFormRecep(screen_log)
        elif current_user["category"]=="doctor":
            firstFormDoc(current_user["name"],screen_log)
        elif current_user["category"]== "patient":
            firstFormPatient(current_user["id"],current_user["name"],screen_log)

def login(screen):
    global screen_log
    screen_log = Toplevel(screen)
    screen_log.title("Login")
    screen_log.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen_log, text="Please enter details below").pack()
    Label(screen_log, text="").pack()
    Label(screen_log, text="Username *").pack()
    username_entry = Entry(screen_log, textvariable=username)
    username_entry.pack()
    Label(screen_log, text="Password *").pack()
    password_entry = Entry(screen_log, textvariable=password)
    password_entry.pack()
    Label(screen_log, text="").pack()
    Button(screen_log, text="Login", height="1", width="10", command=login_user).pack()