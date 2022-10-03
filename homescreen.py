# import
import PySimpleGUI as sg


# function to create specific window
def make_window():
    welcomeText = "Welcome To yaKnow PolyGraph Test. yaKnow strives to provide leading support in conducting Polygraph Tests to all of our users and provide in-depth insight with our leading software technologies"

    # layouts are nested list. Layouts create the UI (texts, button).
    layout = [
        [sg.Text(welcomeText)],
        [sg.Text('Please enter your Name, Age, Phone')],
        [sg.Text('First Name', size=(15, 1)), sg.InputText()],
        [sg.Text('Last Name', size=(15, 1)), sg.InputText()],
        [sg.Text('Age', size=(15, 1)), sg.InputText()],
        [sg.Text('Phone', size=(15, 1)), sg.InputText()],
        [sg.Button('Submit'), sg.Button('Clear'), sg.Button('Exit')]
    ]

    # Window
    window = sg.Window('yaKnow - PolyGraph Exam Home Screen', layout, size=(1000, 900))
    return window


def main():
    # sets the theme, background color and creates a window
    sg.theme('Dark Amber')
    sg.theme_background_color('#000000')
    window = make_window()

    # handles the user and prints the value to the terminal
    event, values = window.read()
    print(event, values[0], values[1], values[2], values[3])


if __name__ == '__main__':
    main()
