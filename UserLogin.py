import PySimpleGUI as gui
import UserLogin
import homescreen
import mysql.connector
from mysql.connector import errorcode

password = ''
confirmPassword = ''

def new_user_login():
    layout = [
            [gui.Text('First name:'), gui.InputText(key='-firstname-')],
            [gui.Text('Last name:'), gui.InputText(key='-lastname-')],
            [gui.Text('Email:'), gui.InputText(key='-EMAIL-')],
            [gui.Text('Password:'), gui.InputText(key='-PASS-', password_char='*', do_not_clear=False)],
            [gui.Text('Confirm Password:'), gui.InputText(key='-CONFIRMPASS-', password_char='*', do_not_clear=False)],
            [gui.Button('Ok'), gui.Button('Cancel')]
    ]

    window = gui.Window('Create account', layout)

    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == 'Cancel':
            break
        else:
            if event == "Ok":
                password = values['-PASS-']
                confirmPassword = values['-CONFIRMPASS-']
                if password == confirmPassword:
                    break
                elif password != confirmPassword:
                    gui.popup("Error", font=16)
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
            if event == "Ok":
                password = values['-PASS-']
                if password == '''SQLPASSWORD''':
                    break
                elif password != '''SQLPASSWORD''':
                    gui.popup("Incorrect password", font=16)
                    continue
        window.close()
