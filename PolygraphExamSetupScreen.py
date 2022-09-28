# import
import PySimpleGUI as sg

# function to create specific window
def make_window():
    menu = ['', ['Control Question Technique', 'Guilty Knowledge Test']]

    # layout is a list of lists
    # the lists corresponds to how many rows there will be on the display
    layout = [
        [sg.ButtonMenu('Select Examination Type', menu, k='-EXAMINATIONTYPE-')],
        [sg.Text('Enter up to 5 "problematic questions" separated by a new line:')],
        [sg.Multiline(key='-PROBLEMATICQUESTIONS-', s=(40, 5))],
        [sg.Button('Start Examination')],
        [sg.Button('Ok')],
    ]

    # Window
    window = sg.Window('yaKnow - PolyGraph Exam Startup', layout, size=(1000, 900))
    return window

def main():
    # set theme to dark amber
    sg.theme('Dark Amber')

    # set background color to black
    sg.theme_background_color('#000000')

    # make window
    window = make_window()

    # event loop / handling
    # window read returns a tuple (event and value)
    while True:
        event, values = window.read()
        print(event, values)
        # if user closes window or hit Start Examination button go to next page
        if event in (sg.WIN_CLOSED, 'Start Examination'):
            break
        elif event == '-EXAMINATIONTYPE-':
            if values['-EXAMINATIONTYPE-'] == 'Control Question Technique':
                window['-EXAMINATIONTYPE-'].update(button_text="Control Question Technique")
                window.refresh()
            elif values['-EXAMINATIONTYPE-'] == 'Guilty Knowledge Test':
                window['-EXAMINATIONTYPE-'].update(button_text="Guilty Knowledge Test")
                window.refresh()


    examination_type = values['-EXAMINATIONTYPE-']
    problematic_questions = values['-PROBLEMATICQUESTIONS-']


    # list_of_questions stores all the problematic questions entered by the user
    # the purpose of list_of_questions is to be able to grab the questions individually
    list_of_questions = str(problematic_questions).split('\n')

    # only grab the first 5 questions, x starts at 0, increments automatically, and does not include 5
    #for x in range(5):
    #    print(list_of_questions[x])

    print(examination_type)

    # close
    window.close()

if __name__ == '__main__':
    main()
