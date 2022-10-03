import PySimpleGUI as sg


contact_information_array = [['Amith', '31 Main St.', '6678989']]
headings = ['Full Name', 'Address', 'Phone Number']

Device1_graph_layout = [
        [sg.Graph(canvas_size=(600, 600), graph_bottom_left= (0,0), graph_top_right= (600, 600), background_color= 'white', key='graph')]
        ]
Device2_graph_layout = [
        [sg.Graph(canvas_size=(600, 600), graph_bottom_left= (0,0), graph_top_right= (600, 600), background_color= 'white', key='graph')]
        ]
Device3_graph_layout = [
        [sg.Graph(canvas_size=(600, 600), graph_bottom_left= (0,0), graph_top_right= (600, 600), background_color= 'white', key='graph')]
        ]
Results_page = [
    [sg.Text("AI HAS SHOWN YOU ARE LYING WITH 100% ACCURACY")],

]

tab_group = [
    [sg.TabGroup(
        [[
          sg.Tab('Device 1 Graph', Device1_graph_layout),
          sg.Tab('Device 2 Graph', Device2_graph_layout),
          sg.Tab('Device 3 Graph', Device3_graph_layout),
          sg.Tab('Results Page', Results_page, title_color='Black', background_color='White')
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
