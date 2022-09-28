# import
import PySimpleGUI as sg
from PIL import Image, ImageTk

# function to create specific window
def make_window():

    header = ['yaKnow - Polygraph Exam Startup']

    #Checkmark Image Source: https://toppng.com/uploads/preview/check-mark-png-11553206004impjy81rdu.png
    checkmarkImage = Image.open("transparentCheck.png")

    # X Image Source: https://www.pngfind.com/pngs/m/42-423721_green-check-red-x-png-red-x-transparent.png
    xImage = Image.open("transparentX.png")
    xImage = xImage.resize((50,50), Image.Resampling.LANCZOS)
    #xImage = ImageTk.PhotoImage(image=xImage)

    menu = ['', ['Control Question Technique', 'Guilty Knowledge Test']]

    # layout is a list of lists
    # the lists corresponds to how many rows there will be on the display

    row0 = [
        [sg.Text('yaKnow - Polygraph Exam Startup', size=(25,1))]
    ]

    row1 = [
        [sg.ButtonMenu('Select Examination Type', menu, k='-EXAMINATIONTYPE-'), sg.Text('Blood Pressure Sensor'), sg.Text('Skin Conductivity Sensor'), sg.Text('Respiration Sensor')]
    ]

    row2 = [
        [sg.Text('                                              '), sg.Image(size=(50, 50), key='theImage1'), sg.Text('                     '), sg.Image(size=(50, 50), key='theImage2'), sg.Text('                 '), sg.Image(size=(50, 50), key='theImage3')]

    ]

    row3 = [
        [sg.Text('Enter up to 5 "problematic questions" separated by a new line:')]
    ]

    row4 = [
        [sg.Multiline(key='-PROBLEMATICQUESTIONS-', s=(40, 5)), sg.Button('Start Examination')]
    ]

    layout = [
        [sg.Frame(layout=row0, title='', key='row0')],
        [sg.Frame(layout=row1, title='', key='row1')],
        [sg.Frame(layout=row2, title='', key='row2')],
        [sg.Frame(layout=row3, title='', key='row3')],
        [sg.Frame(layout=row4, title='', key='row4')]
        #[sg.Button('Ok')]

    ]

    # Window
    window = sg.Window('yaKnow - PolyGraph Exam Startup', layout, size=(1000, 900), finalize=True)

    xImage = ImageTk.PhotoImage(image=xImage)

    window['theImage1'].update(data=xImage)

    window['theImage2'].update(data=xImage)

    window['theImage3'].update(data=xImage)

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
        #print(event, values)
        # if user clicks Start Examination button go to next page
        if(sg.WIN_CLOSED):
            print("Bye")
        elif event in ('Start Examination'):
            window['row0'].update(visible=False)
            window['row1'].update(visible=False)
            window['row2'].update(visible=False)
            window['row3'].update(visible=False)
            window['row4'].update(visible=False)
        elif event == '-EXAMINATIONTYPE-':
            if values['-EXAMINATIONTYPE-'] == 'Control Question Technique':
                window['-EXAMINATIONTYPE-'].update(button_text="Control Question Technique")
                examination_type = values['-EXAMINATIONTYPE-']
                window.refresh()
            elif values['-EXAMINATIONTYPE-'] == 'Guilty Knowledge Test':
                window['-EXAMINATIONTYPE-'].update(button_text="Guilty Knowledge Test")
                problematic_questions = values['-PROBLEMATICQUESTIONS-']
                list_of_questions = str(problematic_questions).split('\n')
                window.refresh()

    # list_of_questions stores all the problematic questions entered by the user
    # the purpose of list_of_questions is to be able to grab the questions individually


    # only grab the first 5 questions, x starts at 0, increments automatically, and does not include 5
    #for x in range(5):
    #    print(list_of_questions[x])

    #print(examination_type)

    #close
    #window.close()

if __name__ == '__main__':
    main()
