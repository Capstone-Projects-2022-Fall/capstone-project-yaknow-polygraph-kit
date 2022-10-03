import PySimpleGUI as sg

#Blood pressure (Bottom)
#X-Axis = time, Y-Axis = Pressure (mmHG)
#X-Axis = time, Y-Axis = Pulse rate (BPM)
#(Combined data)

#Skin conductivity (Middle)
#X_Axis = time, Y-Axis = Electrical conductance

#Respiration belt (Top)
#X-Axis = time, Y-Axis = Respiration rate

def new_window():
    graph_layout = [
        [sg.Graph(canvas_size=(600, 600), graph_bottom_left= (0,0), graph_top_right= (600, 600), background_color= 'white', key='graph')]
        ]

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

def main():
    window = new_window()
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

if __name__ == '__main__':
    main()
