import PySimpleGUI as sg



def new_window_graph():
    # graph_layout = [
    #     [sg.Graph(canvas_size=(600, 600), graph_bottom_left= (0,0), graph_top_right= (600, 600), background_color= 'white', key='graph')]
    #     ]

    TOP = 600
    MIDDLE = TOP * 1/3
    BOTTOM = TOP * 2/3

    window = sg.Window('Graph test', graph_layout, finalize=True)

    graph = window['graph']

    BPM = [65,67,70,72,80,85,90,95,110,115,130]

    graph.draw_line((0, MIDDLE), (600, MIDDLE), color='black')
    graph.draw_line((0, BOTTOM), (600, BOTTOM), color='black')

    graph.draw_line((0,0), (100, 100), color= 'black')

    return window

contact_information_array = [['Amith', '31 Main St.', '6678989']]
headings = ['Full Name', 'Address', 'Phone Number']

instructions_layout = [
    [sg.Text("Enter contact information in the 'New Contact' tab and view all contacts in the 'Contacts Tab'.")]
]

form_layout = [
    [sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
    [sg.Text("Enter address:"), sg.Input(key='-ADDRESS-', do_not_clear=True, size=(20, 1))],
    [sg.Text("Enter phone number:"), sg.Input(key='-PHONE_NUMBER-', do_not_clear=True, size=(20, 1))],
    [sg.Button('Submit Contact Information')]
]

table_layout = [
    [sg.Table(values=contact_information_array, headings=headings, max_col_width=35,
              auto_size_columns=True,
              display_row_numbers=True,
              justification='right',
              num_rows=10,
              key='-TABLE-',
              row_height=35,
              tooltip='Contacts Table')]
]
graph_layout = [
        [sg.Graph(canvas_size=(600, 600), graph_bottom_left= (0,0), graph_top_right= (600, 600), background_color= 'white', key='graph')]
        ]

tab_group = [
    [sg.TabGroup(
        [[sg.Tab('Instructions', instructions_layout, title_color='Red', background_color='Green',
                 tooltip='Instructions', element_justification='right'),

          sg.Tab('Enter Contact Information', form_layout, title_color='Blue', background_color='Yellow'),

          sg.Tab('All Contacts', table_layout, title_color='Black', background_color='Pink',
                 tooltip='See all your contacts'),
          sg.Tab('Device Graph', graph_layout)
          ]],

        tab_location='centertop',
        title_color='Red', tab_background_color='Purple', selected_title_color='Green',
        selected_background_color='Gray', border_width=5), sg.Button('Exit')
    ]
]

# Define Window
window = sg.Window("Tabs", tab_group)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Submit Contact Information":
        contact_information_array.append([values['-NAME-'], values['-ADDRESS-'], values['-PHONE_NUMBER-']])
        window['-TABLE-'].update(values=contact_information_array)
window.close()
