# import
import PySimpleGUI as gui


# function to create specific window
def make_window():
    welcomeText = "Welcome To yaKnow PolyGraph Test"

    # layouts are nested list. Layouts create the UI (texts, button).
    row0 = [
        [gui.Push(), gui.Text(welcomeText), gui.Push()]
    ]

    row1 = [
        [gui.Push(), gui.Button('Conduct Polygraph Exam'), gui.Button('Obtain Individual Sensor Measurements'),
         gui.Push()]
    ]
    layout = [
        [gui.Push(), gui.Frame(layout=row0, title='', key='row0'), gui.Push()],
        [gui.VPush()],
        [gui.Push(), gui.Frame(layout=row1, title='', key='row1'), gui.Push()],
        [gui.VPush()],
    ]

    # Window
    # window = gui.Window('yaKnow - PolyGraph Examination Kit', layout).Finalize
    # window.maximize()
    window = gui.Window('Window Title', layout, resizable=True, finalize=True)
    window.Maximize()
    return window


def main():
    # sets the theme, background color and creates a window
    gui.theme('Dark Amber')
    gui.theme_background_color('#000000')
    window = make_window()

    while True:
        event, values = window.read()

        # if user clicks Start Examination button go to next page
        if event in (gui.WIN_CLOSED, 'EXIT'):
            break
        elif event in 'Conduct Polygraph Exam' or event in 'Obtain Individual Sensor Measurements':
            window['row0'].update(visible=False)
            window['row1'].update(visible=False)


if __name__ == '__main__':
    main()
