import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import figure

#Blood pressure (Bottom)
#X-Axis = time, Y-Axis = Pressure (mmHG)
#X-Axis = time, Y-Axis = Pulse rate (BPM)
#(Combined data)

#Skin conductivity (Middle)
#X_Axis = time, Y-Axis = Electrical conductance (Electrical Siemens)

#Respiration belt (Top)
#X-Axis = time, Y-Axis = Respiration rate

BPM = [65,67,70,72,80,85,90,95,110,115]
TIME = [1,2,3,4,5,6,7,8,9,10]

SIEMENS = [2, 3, 4, 4.6, 6, 5.3, 4.4, 4, 5, 6.8]

RESPIRATION = [12, 12, 13, 15, 14, 17, 16, 15, 15, 20]

#Figure
def HeartRatePlot(TIME, BPM):
    figure(figsize=(5, 5), dpi=50)
    plt.plot(TIME, BPM, color='red', marker='o')
    plt.title('Beats per minute', fontsize=10)
    plt.xlabel('Time(Minutes)', fontsize=10)
    plt.ylabel('BPM', fontsize=10)
    plt.grid(True)
    return plt.gcf()

def SkinSensor(TIME, SIEMENS):
    figure(figsize=(5, 5), dpi=50)
    plt.plot(TIME, SIEMENS, color='red', marker='o')
    plt.title('Electrical Conductance', fontsize=10)
    plt.xlabel('Time(Minutes)', fontsize=10)
    plt.ylabel('Siemens', fontsize=10)
    plt.grid(True)
    return plt.gcf()

def RespirationBelt(TIME, RESPIRATION):
    figure(figsize=(5, 5), dpi=50)
    plt.plot(TIME, RESPIRATION, color='red', marker='o')
    plt.title('Respiration Rate', fontsize=10)
    plt.xlabel('Time(Minutes)', fontsize=10)
    plt.ylabel('Breaths', fontsize=10)
    plt.grid(True)
    return plt.gcf()

#Canvas
layout_BPM = [
    [sg.Text('Heart Rate Monitor Graph')], [sg.Canvas(size=(1000,1000), key='CANVAS')], [sg.Exit()]
]
layout_GSR = [
    [sg.Text('Skin Conductivity Graph')], [sg.Canvas(size=(1000,1000), key='CANVAS')], [sg.Exit()]
]
layout_Res = [
    [sg.Text('Respiration Rate Graph')], [sg.Canvas(size=(1000,1000), key='CANVAS')], [sg.Exit()]
]

def draw_figure(canvas, figure):
    figure_canvas = FigureCanvasTkAgg(figure, canvas)
    figure_canvas.draw()
    figure_canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
    return figure_canvas

window_BPM = sg.Window("Heart Rate Monitor", layout_BPM, finalize=True, element_justification='center')
window_GSR = sg.Window("Skin Conductivity Monitor", layout_GSR, finalize=True, element_justification='center')
window_Res = sg.Window("Respiration Rate Monitor", layout_Res, finalize=True, element_justification='center')

draw_figure(window_BPM['CANVAS'].TKCanvas, HeartRatePlot(TIME, BPM))
draw_figure(window_GSR['CANVAS'].TKCanvas, SkinSensor(TIME, SIEMENS))
draw_figure(window_Res['CANVAS'].TKCanvas, RespirationBelt(TIME, RESPIRATION))

def main():
    while True:
        event, values = window_BPM.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
    window_BPM.close(), window_GSR.close(), window_Res.close()

if __name__ == '__main__':
    main()