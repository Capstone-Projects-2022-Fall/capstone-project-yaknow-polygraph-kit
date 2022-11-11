import PySimpleGUI as gui
import UserLogin
import homescreen
import mysql.connector
from mysql.connector import Error

password = ''
confirmPassword = ''

def new_user_login():
    layout = [
            [gui.Text('First name:'), gui.InputText(key='-FIRSTNAME-')],
            [gui.Text('Last name:'), gui.InputText(key='-LASTNAME-')],
            [gui.Text('Email:'), gui.InputText(key='-EMAIL-')],
            [gui.Text('Password:'), gui.InputText(key='-PASSWORD-', password_char='*', do_not_clear=False)],
            [gui.Text('Confirm Password:'), gui.InputText(key='-CONFIRMPASSWORD-', password_char='*', do_not_clear=False)],
            [gui.Button('Ok'), gui.Button('Cancel')]
    ]

    window = gui.Window('Create account', layout)

    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == 'Cancel':
            break
        else:
            if event == "Ok":
                password = values['-PASSWORD-']
                confirmPassword = values['-CONFIRMPASSWORD-']

                if password == confirmPassword:
                    name = values['-FIRSTNAME-'] + " " + values['-LASTNAME-']
                    email = values['-EMAIL-']
                    password = values['-PASSWORD-']

                    insert_user(name, email, password)
                elif password != confirmPassword:
                    gui.popup("Please retype password. Passwords to not match", font=16)
                    continue
        window.close()

def existing_user():
    layout = [
            [gui.Text('Email:'), gui.InputText(key='-EMAIL-')],
            [gui.Text('Password:'), gui.InputText(key='-PASS-', password_char='*', do_not_clear=False)],
            [gui.Button('Ok'), gui.Button('Cancel')]
    ]

    window = gui.Window('Login', layout)

    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == 'Cancel':
            break
        else:
            email = values['-EMAIL-']
            password = values['-PASSWORD-']
            get_user(email, password)

        window.close()

def decision():
    layout = [
        [gui.Button('Returning User'), gui.Button('New User')],
        [gui.Button('Cancel')]
    ]
    window = gui.Window('Welcome To Polygraph Test Kit!', layout)
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == 'Cancel':
            break
        else:
            if event == 'New User':
                new_user_login()
            else:
                existing_user()

def insert_user(name, email, password):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    with db.cursor() as mycursor:
        # only add if question does not already exist
        mycursor.execute("INSERT INTO users.user (name, email, password) VALUES (%s, %s, %s)",
                         (name, email, password))
        db.commit()
        print("User Added")
    db.close()

def get_user(email, password):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    with db.cursor() as mycursor:
        mycursor.execute("SELECT email, password FROM users.user WHERE email=" + email + " password=" + password)
        db.commit()
        print("User Selected")


if __name__ == "__main__":
    decision()
