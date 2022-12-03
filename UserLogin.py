import PySimpleGUI as gui
import homescreen
import mysql.connector

password = ''
confirmPassword = ''

def new_user_login():
    layout = [
        [gui.Text('First name:', justification="left"), gui.InputText(key='-FIRSTNAME-', justification="left")],
        [gui.Text('Last name:', justification="left"), gui.InputText(key='-LASTNAME-', justification="left")],
        [gui.Text('Email:', justification="left"), gui.InputText(key='-EMAIL-', justification="left")],
        [gui.Text('Password:', justification="left")],
        [gui.InputText(key='PASSWORD', password_char='*', do_not_clear=False, justification="left")],
        [gui.Text('Confirm Password:', justification="left")],
        [gui.InputText(key='-CONFIRMPASSWORD-', password_char='*', do_not_clear=False, justification="left")],
        [gui.Button('Ok'), gui.Button('Cancel')]
    ]

    window = gui.Window('Create account', layout, size=(400, 200))

    while True:
        event, values = window.read()
        if event == 'Cancel' or event == gui.WIN_CLOSED:
            window.close()
            break
        else:
            if event == "Ok":
                password = values['PASSWORD']
                confirmPassword = values['-CONFIRMPASSWORD-']

                if password == confirmPassword:
                    name = values['-FIRSTNAME-'] + " " + values['-LASTNAME-']
                    email = values['-EMAIL-']

                    if get_user(email, password):
                        gui.popup("The User Already Exists. Try Logging In Via Returning User option Maybe?")
                    else:
                        insert_user(name, email, password)
                        homescreen.main()

                elif password != confirmPassword:
                    gui.popup("Please retype password. Passwords to not match", font=16)
                    continue
        #window.close()

def existing_user():
    layout = [
        [gui.Text('Email:'), gui.InputText(key='-EMAIL-')],
        [gui.Text('Password:'), gui.InputText(key='PASSWORD', password_char='*', do_not_clear=False)],
        [gui.Button('Ok'), gui.Button('Cancel')]
    ]

    window = gui.Window('Login', layout)

    while True:
        event, values = window.read()
        if event == 'Cancel' or event == gui.WIN_CLOSED:
            window.close()
            break
        else:
            email = values['-EMAIL-']
            password = values['PASSWORD']
            if (get_user(email, password)):
                homescreen.main()
            else:
                gui.popup("The User Does Not Exist. Try Again Maybe?")

        #window.close()

def decision():
    layout = [
        [gui.Text("Welcome To Polygraph Test Kit!")],
        [gui.Button('New User')],
        [gui.Button('Returning User')],
        [gui.Button('Cancel')]
    ]
    window = gui.Window('Welcome To Polygraph Test Kit!', layout, size=(300, 150))
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
    email_list = []
    password_list = []
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    with db.cursor() as mycursor:
        mycursor.execute("SELECT email, password FROM users.user")
        result = list(mycursor.fetchall())

    for x in result:
        email_list.append(x[0])

    for x in result:
        password_list.append(x[1])

    return email in email_list and password in password_list

if __name__ == "__main__":
    decision()
