import PySimpleGUI as gui
from PIL import Image, ImageTk
import arduino
import matplotlib
matplotlib.use('TKAgg')
import conductExamScreen
import PolygraphExamSetupScreen
import ResultsDisplayScreen
import respirationBelt
import threading
import time
import tts
import graphResults
from statsmodels.stats.weightstats import ztest as ztest
import numpy
import matplotlib.pyplot
from scipy.stats import norm
import statistics
from multiprocessing import Process, Queue
import matplotlib
matplotlib.use("TkAgg")
global window
global examFinished
global examTime
global questionCounter
global newQuestion

global respirationRecordings
global respirationMeasurements
global respirationTimings

global skinConductivityRecordings
global skinConductivityMeasurements
global skinConductivityTimings

global bloodPressureRecordings
global bloodPressureMeasurements
global bloodPressureTimings

global pulseRecordings
global pulseMeasurements
global pulseTimings

global yn
global thread
global readyToStart
global inQuestion
global initialExamEnded
global respirationbyQuestion

global GSRbyQuestion

global questionTimestamps
global zTest1
global zTest2
global zTest3
import pyformulas



class singularRecording:
    def __init__(self, timestamp, measurement, question, yn):
        self.timestamp = timestamp
        self.measurement = measurement
        self.question = question
        self.yn = yn

def make_window():
    # layout is a list of lists
    # the lists corresponds to how many rows there will be on the display

    row0 = [
        [gui.Text('yaKnow - Polygraph Exam Running', size=(25, 1))]
    ]

    row1 = [
        #[gui.Push(), gui.Text(PolygraphExamSetupScreen.global_list_of_questions_selected[0], key='-Text-')]
        [gui.Push(), gui.Text("PolygraphExamSetupScreen.global_list_of_questions_selected[0]", key='-Text-')]
    ]

    row2 = [
        [gui.Text('0', key='-Time-'), gui.Text('Cuff Pressure: ', key='-CuffPressure-')]
    ]
    
    row3 = [
        [gui.Text('                                             ', key='-placeHolder-'), gui.Text('Mean Respiration (N)', key='-MeanRHeader-'), gui.Text('      MeanGSR (S)', key='-MeanGSRHeader-'),  gui.Text('MedianRespiration (N)', key='-MedianRHeader-'), gui.Text('     MedianGSR (S)', key='MedianGSRHeader'), gui.Text('  Blood Pressure (mmHg)', key='-BPHeader-'),  gui.Text('Pulse (BPM)', key='-PHeader-')]
    ]
    
    row4 = [
        [gui.Text('Baseline Question 1                           ', key='-B1placeHolder-'), gui.Text('', key='-B1MeanR-'), gui.Text('', key='-B1MeanGSR-'), gui.Text('', key='-B1MedianR-'), gui.Text('', key='-B1MedianGSR-'),  gui.Text('', key='-B1BP-'), gui.Text('', key='-B1P-')]
    ]
    
    row5 = [
        [gui.Text('Baseline Question 2                           ', key='-B2placeHolder-'), gui.Text('', key='-B2MeanR-'), gui.Text('', key='-B2MeanGSR-'), gui.Text('', key='-B2MedianR-'), gui.Text('', key='-B2MedianGSR-'),  gui.Text('', key='-B2BP-'), gui.Text('', key='-B2P-')]
    ]
    
    row6 = [
        [gui.Text('Baseline Question 3                           ', key='-B3placeHolder-'), gui.Text('', key='-B3MeanR-'), gui.Text('', key='-B3MeanGSR-'), gui.Text('', key='-B3MedianR-'), gui.Text('', key='-B3MedianGSR-'),  gui.Text('', key='-B3BP-'), gui.Text('', key='-B3P-')]
    ]
    
    col3_1 = [
        [gui.Button('Test 1 Respiration', key='-Test1R-', visible=True)],
        [gui.Button('Test 2 Respiration', key='-Test2R-', visible=True)],
        [gui.Button('Test 3 Respiration', key='-Test3R-', visible=True)],
        [gui.Button('Test 4 Respiration', key='-Test4R-', visible=True)],
        [gui.Button('Test 5 Respiration', key='-Test5R-', visible=True)],
        [gui.Button('Test 6 Respiration', key='-Test6R-', visible=True)]
    ]

    col3_2 = [
        [gui.Button('Test 1 GSR', key='-Test1G-', visible=True)],
        [gui.Button('Test 2 GSR', key='-Test2G-', visible=True)],
        [gui.Button('Test 3 GSR', key='-Test3G-', visible=True)],
        [gui.Button('Test 4 GSR', key='-Test4G-', visible=True)],
        [gui.Button('Test 5 GSR', key='-Test5G-', visible=True)],
        [gui.Button('Test 6 GSR', key='-Test6G-', visible=True)]
    ]    
    
    col3_3 = [
        [gui.Text('', key='-Test1MeanR-', visible=True)],
        [gui.Text('', key='-Test2MeanR-', visible=True)],
        [gui.Text('', key='-Test3MeanR-', visible=True)],
        [gui.Text('', key='-Test4MeanR-', visible=True)],
        [gui.Text('', key='-Test5MeanR-', visible=True)],
        [gui.Text('', key='-Test6MeanR-', visible=True)]
    ]
    
    col3_4 = [
        [gui.Text('', key='-Test1MeanG-', visible=True)],
        [gui.Text('', key='-Test2MeanG-', visible=True)],
        [gui.Text('', key='-Test3MeanG-', visible=True)],
        [gui.Text('', key='-Test4MeanG-', visible=True)],
        [gui.Text('', key='-Test5MeanG-', visible=True)],
        [gui.Text('', key='-Test6MeanG-', visible=True)]
    ]
    
    col3_5 = [
        [gui.Text('', key='-Test1MedianR-', visible=True)],
        [gui.Text('', key='-Test2MedianR-', visible=True)],
        [gui.Text('', key='-Test3MedianR-', visible=True)],
        [gui.Text('', key='-Test4MedianR-', visible=True)],
        [gui.Text('', key='-Test5MedianR-', visible=True)],
        [gui.Text('', key='-Test6MedianR-', visible=True)]
    ]
    
    col3_6 = [
        [gui.Text('', key='-Test1MedianG-', visible=True)],
        [gui.Text('', key='-Test2MedianG-', visible=True)],
        [gui.Text('', key='-Test3MedianG-', visible=True)],
        [gui.Text('', key='-Test4MedianG-', visible=True)],
        [gui.Text('', key='-Test5MedianG-', visible=True)],
        [gui.Text('', key='-Test6MedianG-', visible=True)]
    ]
    
    col3_7 = [
        [gui.Text('', key='-Test1BP-', visible=True)],
        [gui.Text('', key='-Test2BP-', visible=True)],
        [gui.Text('', key='-Test3BP-', visible=True)],
        [gui.Text('', key='-Test4BP-', visible=True)],
        [gui.Text('', key='-Test5BP-', visible=True)],
        [gui.Text('', key='-Test6BP-', visible=True)]
    ]

    col3_8 = [
        [gui.Text('', key='-Test1P-', visible=True)],
        [gui.Text('', key='-Test2P-', visible=True)],
        [gui.Text('', key='-Test3P-', visible=True)],
        [gui.Text('', key='-Test4P-', visible=True)],
        [gui.Text('', key='-Test5P-', visible=True)],
        [gui.Text('', key='-Test6P-', visible=True)]
    ]

    row8 = [
        [gui.Button('YES', key='-YES-'), gui.Button('NO', key='-NO-')]
    ]

    row9 = [
        [gui.Push(), gui.Button('Restart', key='-Restart-', visible=False), gui.Button('Cancel Conversion', key='-cancelConversion-'),
         gui.Push()]
    ]

    layout = [
        [gui.Frame(layout=row0, title='', key='row0')],
        [gui.VPush()],
        [gui.Frame(layout=row1, title='', key='row1')],
        [gui.VPush()],
        [gui.Frame(layout=row2, title='', key='row2')],
        [gui.Frame(layout=row3, title='', key='row3', visible=False)],
        [gui.Frame(layout=row4, title='', key='row4', visible=False)],
        [gui.Frame(layout=row5, title='', key='row5', visible=False)],
        [gui.Frame(layout=row6, title='', key='row6', visible=False)],
        [gui.Frame(layout=col3_1, title='', k='col3_1', visible=False), gui.Frame(layout=col3_2, title='', k='col3_2', visible=False), gui.Frame(layout=col3_3, title='', k='col3_3', visible=False), gui.Frame(layout=col3_4, title='', k='col3_4', visible=False), gui.Frame(layout=col3_5, title='', k='col3_5', visible=False), gui.Frame(layout=col3_6, title='', k='col3_6', visible=False), gui.Frame(layout=col3_7, title='', k='col3_7', visible=False), gui.Frame(layout=col3_8, title='', k='col3_8', visible=False)],
        [gui.Push(), gui.Frame(layout=row8, title='', key='row8'), gui.Push()],
        [gui.Push(), gui.Frame(layout=row9, title='', key='row9'), gui.Push()]
    ]
    icon = b'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'

    window = gui.Window('yaKnow - PolyGraph Exam', layout, size=(1000, 900), icon=icon, finalize=True)

    return window


def examCounter():
    while conductExamScreen.examFinished == False:
        if(conductExamScreen.inQuestion == True):
            conductExamScreen.examTime = conductExamScreen.examTime + 1
            conductExamScreen.window['-Time-'].update(examTime)
            if(conductExamScreen.iterated == False):
                conductExamScreen.questionTimestamps.append(examTime)
                conductExamScreen.iterated = True
                #for respirationRecording in conductExamScreen.respirationRecordings:
                #    if respirationRecording.yn == None:
                #        respirationRecording.yn = conductExamScreen.yn
                conductExamScreen.yn = None
                conductExamScreen.newQuestion = PolygraphExamSetupScreen.global_overall_questions[conductExamScreen.questionCounter]
                tts.questionToSpeech(newQuestion, conductExamScreen.questionCounter)
                if (len(PolygraphExamSetupScreen.global_overall_questions) == (questionCounter + 1)):
                    while(len(bloodPressureRecordings) != len(PolygraphExamSetupScreen.global_overall_questions) ):
                        #print("BP SIZE: ", len(bloodPressureRecordings) )
                        #print("Question Size: ", len(PolygraphExamSetupScreen.global_overall_questions))
                        conductExamScreen.examTime = conductExamScreen.examTime + 1
                        conductExamScreen.window['-Time-'].update(examTime)
                        time.sleep(1)
                        continue
                    window.write_event_value('-ENDED-', None)
                else:
                    conductExamScreen.questionCounter = conductExamScreen.questionCounter + 1
                    conductExamScreen.window['-Text-'].update(newQuestion)
            time.sleep(1)
        else:
            print("Pausing")
            conductExamScreen.iterated = False
            time.sleep(1)



def separateByQuestion():
    conductExamScreen.respirationbyQuestion = []
    conductExamScreen.GSRbyQuestion = []
    tempArray = []
    tempQuestion = conductExamScreen.respirationRecordings[0].question
    x = 0
    while(x < len(respirationRecordings)):
        if( (tempQuestion != respirationRecordings[x].question) or (x == (len(respirationRecordings) - 1) ) ):
            if( x == (len(respirationRecordings) - 1) ):
                tempArray.append(respirationRecordings[x].measurement)
            conductExamScreen.respirationbyQuestion.append(tempArray)
            tempArray = []
            tempArray.append(respirationRecordings[x].measurement)
            tempQuestion = respirationRecordings[x].question
            x = x + 1
        else:
            tempArray.append(respirationRecordings[x].measurement)
            x = x + 1

    y = 0
    tempArray = []
    tempQuestion = conductExamScreen.skinConductivityRecordings[0].question
    while (y < len(conductExamScreen.skinConductivityRecordings)):
        if ((tempQuestion != skinConductivityRecordings[y].question) or (y == (len(skinConductivityRecordings) - 1))):
            if (y == (len(skinConductivityRecordings) - 1)):
                tempArray.append(skinConductivityRecordings[y].measurement)
            conductExamScreen.GSRbyQuestion.append(tempArray)
            tempArray = []
            tempArray.append(skinConductivityRecordings[y].measurement)
            tempQuestion = skinConductivityRecordings[y].question
            y = y + 1
        else:
            tempArray.append(skinConductivityRecordings[y].measurement)
            y = y + 1


def conductZtest(question):
    '''
    This function will return the z and p values from comparing a problematic question to a baseline
    needs baselineData array/list and ProblematicQuestionData as input
    :return list of (z value, p value), also prints out a statement if we have reasonable evidence to show that someone is lying
    '''
    baselineData1 = respirationbyQuestion[0]
    baselineData2 = respirationbyQuestion[1]
    baselineData3 = respirationbyQuestion[2]
    questionData = respirationbyQuestion[question]
    conductExamScreen.zTest1 = list(ztest(baselineData1, questionData))
    # if zTest1[1] < .05:
    #     print("we reject the null hypothesis, we have reason to believe this data is fairly different... could be lying")
    # else:
    #     print("We do not have reason to believe the data has any major differences")
    conductExamScreen.zTest2 = list(ztest(baselineData2, questionData))
    # if zTest2[1] < .05:
    #     print("we reject the null hypothesis, we have reason to believe this data is fairly different... could be lying")
    # else:
    #     print("We do not have reason to believe the data has any major differences")
    conductExamScreen.zTest3 = list(ztest(baselineData3, questionData))
    # if zTest3[1] < .05:
    #     print("we reject the null hypothesis, we have reason to believe this data is fairly different... could be lying")
    # else:
    #     print("We do not have reason to believe the data has any major differences")
# return conductExamScreen.zTest1,conductExamScreen.zTest2,zTest3
def showRespirationProbabilityDistribution(question):
    # mean1 = statistics.mean(cityA)
    # sd1 = statistics.stdev(cityA)
    #
    # mean2 = statistics.mean(cityB)
    # sd2 = statistics.stdev(cityB)
    #
    # # plt.plot(cityA, norm.pdf(cityA, mean1, sd1), 'r')
    # #
    #
    #
    #
    # graph0.plot(cityB, norm.pdf(cityB, mean2, sd2), 'g', marker='*')
    # plt.show()
    for measurement in respirationbyQuestion[question]:
        print(measurement)
    conductExamScreen.respirationbyQuestion[question].sort()
    conductExamScreen.respirationbyQuestion[0].sort()
    conductExamScreen.respirationbyQuestion[1].sort()
    conductExamScreen.respirationbyQuestion[2].sort()

    # # subplot x and y axis
    # ax = fig.add_subplot(111)
    # ax.spines['top'].set_color('none')
    # ax.spines['bottom'].set_color('none')
    # ax.spines['left'].set_color('none')
    # ax.spines['right'].set_color('none')
    # ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)
    # ax.set_xlabel('respiration')
    # ax.set_ylabel('probability')

    #   fig, (graph0, graph1, graph2, ax) = matplotlib.pyplot.subplots(nrows=4, ncols=1, sharex=False)
    fig, (graph0, graph1, graph2) = matplotlib.pyplot.subplots(nrows=3, ncols=1, sharex=False)

    # baseline1question
    meanBaseline1 = statistics.mean(conductExamScreen.respirationbyQuestion[0])

    standardDeviationBaseline1 = statistics.stdev(conductExamScreen.respirationbyQuestion[0])
    #   graph0.plot(conductExamScreen.respirationbyQuestion[0], norm.pdf(respirationbyQuestion[0], meanBaseline1, standardDeviationBaseline1), 'r',marker='o')
    # baseline2question
    meanBaseline2 = statistics.mean(conductExamScreen.respirationbyQuestion[1])
    standardDeviationBaseline2 = statistics.stdev(conductExamScreen.respirationbyQuestion[1])
    #  graph1.plot(conductExamScreen.respirationbyQuestion[1], norm.pdf(respirationbyQuestion[1], meanBaseline2, standardDeviationBaseline2), 'r', marker='o')
    # baseline3question
    meanBaseline3 = statistics.mean(conductExamScreen.respirationbyQuestion[2])
    standardDeviationBaseline3 = statistics.stdev(conductExamScreen.respirationbyQuestion[2])
    #   graph2.plot(conductExamScreen.respirationbyQuestion[2], norm.pdf(respirationbyQuestion[2], meanBaseline3, standardDeviationBaseline3), 'r', marker='o')
    # Test
    meanTest = statistics.mean(conductExamScreen.respirationbyQuestion[question])
    standardDeviationTest = statistics.stdev(conductExamScreen.respirationbyQuestion[question])
    # plotting
    graph0.plot(conductExamScreen.respirationbyQuestion[question],
                norm.pdf(respirationbyQuestion[question], meanTest, standardDeviationTest), 'g', marker='*')
    graph0.plot(conductExamScreen.respirationbyQuestion[0],
                norm.pdf(respirationbyQuestion[0], meanBaseline1, standardDeviationBaseline1), 'r', marker='o')
    graph1.plot(conductExamScreen.respirationbyQuestion[question],
                norm.pdf(respirationbyQuestion[question], meanTest, standardDeviationTest), 'g', marker='*')
    graph1.plot(conductExamScreen.respirationbyQuestion[1],
                norm.pdf(respirationbyQuestion[1], meanBaseline2, standardDeviationBaseline2), 'r', marker='o')
    graph2.plot(conductExamScreen.respirationbyQuestion[question],
                norm.pdf(respirationbyQuestion[question], meanTest, standardDeviationTest), 'g', marker='*')
    graph2.plot(conductExamScreen.respirationbyQuestion[2],
                norm.pdf(respirationbyQuestion[2], meanBaseline3, standardDeviationBaseline3), 'r', marker='o')
    # Subplot Titles
    #     graph0[0, 0].title.set_text("Normal Distribution 1")
    #     graph0[0, 1].title.set_text("Normal Distribution 2")
    #     graph0[0, 2].title.set_text("Normal Distribution 3")

    conductZtest(question)
    graph0.text(0.5, 0.25, 'Ztest: results(%s)' % conductExamScreen.zTest1, horizontalalignment='center',
                verticalalignment='center',
                transform=graph0.transAxes)
    graph1.text(0.5, 0.25, 'Ztest: results(%s)' % conductExamScreen.zTest2, horizontalalignment='center',
                verticalalignment='center',
                transform=graph1.transAxes)
    graph2.text(0.5, 0.25, 'Ztest: results(%s)' % conductExamScreen.zTest3, horizontalalignment='center',
                verticalalignment='center',
                transform=graph2.transAxes)
    matplotlib.pyplot.show()

def startExam(window1):

    conductExamScreen.justRespirationRate = []

    conductExamScreen.questionTimestamps = []

    conductExamScreen.respirationbyQuestion = []

    conductExamScreen.GSRbyQuestion = []

    conductExamScreen.window = window1

    conductExamScreen.initialExamEnded = False

    conductExamScreen.liveGraph, (conductExamScreen.respirationLiveGraph, conductExamScreen.gsrLiveGraph, conductExamScreen.bpLiveGraph, conductExamScreen.pulseLiveGraph) = matplotlib.pyplot.subplots(nrows=4, ncols=1, sharex=True)
    matplotlib.pyplot.subplots_adjust(bottom=0.25)

    conductExamScreen.liveGraphInArray = numpy.zeros((1, 1)) #Prepares numpy array to hold snapshot of live graphing data
    conductExamScreen.liveGraphScreen = pyformulas.screen(conductExamScreen.liveGraphInArray, 'Live Readings') #Creates a numpy canvas compatible with numpy graph created above
    conductExamScreen.liveGraphingWidth, conductExamScreen.liveGraphingHeight = conductExamScreen.liveGraph.canvas.get_width_height()  # Gets the width and height of the numpy canas used for live graphing

    print("Live Graphing Width: ", conductExamScreen.liveGraphingWidth)
    print("Live Graphing Height: ", conductExamScreen.liveGraphingHeight)

    thread = threading.Thread(target=conductExamScreen.examCounter)
    thread.start()
    while True:
        #event, values = PolygraphExamSetupScreen.window.read()
        event, values = conductExamScreen.window.read()
        # if user clicks Start Examination button go to next page
        if event in (gui.WIN_CLOSED, 'EXIT'):
            break
        elif event == '-YES-':
            conductExamScreen.yn = True
        elif event == '-NO-':
            conductExamScreen.yn = False
        elif event == '-ENDED-':
            separateByQuestion()
            conductExamScreen.examFinished = True
            conductExamScreen.window['row3'].update(visible=True)
            conductExamScreen.window['row4'].update(visible=True)
            conductExamScreen.window['row5'].update(visible=True)
            conductExamScreen.window['row6'].update(visible=True)
            conductExamScreen.window['col3_1'].update(visible=True)
            conductExamScreen.window['col3_2'].update(visible=True)
            conductExamScreen.window['col3_3'].update(visible=True)
            conductExamScreen.window['col3_4'].update(visible=True)
            conductExamScreen.window['col3_5'].update(visible=True)
            conductExamScreen.window['col3_6'].update(visible=True)
            conductExamScreen.window['col3_7'].update(visible=True)
            conductExamScreen.window['col3_8'].update(visible=True)

            conductExamScreen.window['-B1MeanR-'].update(round(statistics.mean(respirationbyQuestion[0]), 3))
            conductExamScreen.window['-B2MeanR-'].update(round(statistics.mean(respirationbyQuestion[1]), 3))
            conductExamScreen.window['-B3MeanR-'].update(round(statistics.mean(respirationbyQuestion[2]), 3))
            conductExamScreen.window['-Test1MeanR-'].update(round(statistics.mean(respirationbyQuestion[3]), 3))
            conductExamScreen.window['-Test2MeanR-'].update(round(statistics.mean(respirationbyQuestion[4]), 3))
            conductExamScreen.window['-Test3MeanR-'].update(round(statistics.mean(respirationbyQuestion[5]), 3))
            conductExamScreen.window['-Test4MeanR-'].update(round(statistics.mean(respirationbyQuestion[6]), 3))
            conductExamScreen.window['-Test5MeanR-'].update(round(statistics.mean(respirationbyQuestion[7]), 3))
            conductExamScreen.window['-Test6MeanR-'].update(round(statistics.mean(respirationbyQuestion[8]), 3))

            conductExamScreen.window['-B1MeanGSR-'].update("                        " + str(round(statistics.mean(GSRbyQuestion[0]), 3)))
            conductExamScreen.window['-B2MeanGSR-'].update("                        " + str(round(statistics.mean(GSRbyQuestion[1]), 3)))
            conductExamScreen.window['-B3MeanGSR-'].update("                        " + str(round(statistics.mean(GSRbyQuestion[2]), 3)))
            conductExamScreen.window['-Test1MeanG-'].update("                    " + str(round(statistics.mean(GSRbyQuestion[3]), 3)))
            conductExamScreen.window['-Test2MeanG-'].update("                    " + str(round(statistics.mean(GSRbyQuestion[4]), 3)))
            conductExamScreen.window['-Test3MeanG-'].update("                    " + str(round(statistics.mean(GSRbyQuestion[5]), 3)))
            conductExamScreen.window['-Test4MeanG-'].update("                    " + str(round(statistics.mean(GSRbyQuestion[6]), 3)))
            conductExamScreen.window['-Test5MeanG-'].update("                    " + str(round(statistics.mean(GSRbyQuestion[7]), 3)))
            conductExamScreen.window['-Test6MeanG-'].update("                    " + str(round(statistics.mean(GSRbyQuestion[6]), 3)))

            conductExamScreen.window['-B1MedianR-'].update("                     " + str(round(numpy.median(respirationbyQuestion[0]), 3)))
            conductExamScreen.window['-B2MedianR-'].update("                      " + str(round(numpy.median(respirationbyQuestion[1]), 3)))
            conductExamScreen.window['-B3MedianR-'].update("                     " + str(round(numpy.median(respirationbyQuestion[2]), 3)))
            conductExamScreen.window['-Test1MedianR-'].update("                   " + str(round(numpy.median(respirationbyQuestion[3]), 3)))
            conductExamScreen.window['-Test2MedianR-'].update("                   " + str(round(numpy.median(respirationbyQuestion[4]), 3)))
            conductExamScreen.window['-Test3MedianR-'].update("                   " + str(round(numpy.median(respirationbyQuestion[5]), 3)))
            conductExamScreen.window['-Test4MedianR-'].update("                   " + str(round(numpy.median(respirationbyQuestion[6]), 3)))
            conductExamScreen.window['-Test5MedianR-'].update("                   " + str(round(numpy.median(respirationbyQuestion[7]), 3)))
            conductExamScreen.window['-Test6MedianR-'].update("                   " + str(round(numpy.median(respirationbyQuestion[8]), 3)))

            conductExamScreen.window['-B1MedianGSR-'].update("                       " + str(round(numpy.median(GSRbyQuestion[0]), 3)))
            conductExamScreen.window['-B2MedianGSR-'].update("                       " + str(round(numpy.median(GSRbyQuestion[1]), 3)))
            conductExamScreen.window['-B3MedianGSR-'].update("                        " + str(round(numpy.median(GSRbyQuestion[2]), 3)))
            conductExamScreen.window['-Test1MedianG-'].update("                   " + str(round(numpy.median(GSRbyQuestion[3]), 3)))
            conductExamScreen.window['-Test2MedianG-'].update("                   " + str(round(numpy.median(GSRbyQuestion[4]), 3)))
            conductExamScreen.window['-Test3MedianG-'].update("                   " + str(round(numpy.median(GSRbyQuestion[5]), 3)))
            conductExamScreen.window['-Test4MedianG-'].update("                   " + str(round(numpy.median(GSRbyQuestion[6]), 3)))
            conductExamScreen.window['-Test5MedianG-'].update("                   " + str(round(numpy.median(GSRbyQuestion[7]), 3)))
            conductExamScreen.window['-Test6MedianG-'].update("                   " + str(round(numpy.median(GSRbyQuestion[8]), 3)))

            conductExamScreen.window['-B1BP-'].update("                 " + str(round(bloodPressureRecordings[0].measurement, 3)))
            conductExamScreen.window['-B2BP-'].update("                 " + str(round(bloodPressureRecordings[1].measurement, 3)))
            conductExamScreen.window['-B3BP-'].update("                 " + str(round(bloodPressureRecordings[2].measurement, 3)))
            conductExamScreen.window['-Test1BP-'].update("              " + str(round(bloodPressureRecordings[3].measurement, 3)))
            conductExamScreen.window['-Test2BP-'].update("              " + str(round(bloodPressureRecordings[4].measurement, 3)))
            conductExamScreen.window['-Test3BP-'].update("              " + str(round(bloodPressureRecordings[5].measurement, 3)))
            conductExamScreen.window['-Test4BP-'].update("              " + str(round(bloodPressureRecordings[6].measurement, 3)))
            conductExamScreen.window['-Test5BP-'].update("              " + str(round(bloodPressureRecordings[7].measurement, 3)))
            conductExamScreen.window['-Test6BP-'].update("              " + str(round(bloodPressureRecordings[8].measurement, 3)))

            conductExamScreen.window['-B1P-'].update("                  " + str(round(pulseRecordings[0].measurement, 3)))
            conductExamScreen.window['-B2P-'].update("                 " + str(round(pulseRecordings[1].measurement, 3)))
            conductExamScreen.window['-B3P-'].update("                 " + str(round(pulseRecordings[2].measurement, 3)))
            conductExamScreen.window['-Test1P-'].update("               " + str(round(pulseRecordings[3].measurement, 3)))
            conductExamScreen.window['-Test2P-'].update("               " + str(round(pulseRecordings[4].measurement, 3)))
            conductExamScreen.window['-Test3P-'].update("               " + str(round(pulseRecordings[5].measurement, 3)))
            conductExamScreen.window['-Test4P-'].update("               " + str(round(pulseRecordings[6].measurement, 3)))
            conductExamScreen.window['-Test5P-'].update("               " + str(round(pulseRecordings[7].measurement, 3)))
            conductExamScreen.window['-Test6P-'].update("               " + str(round(pulseRecordings[8].measurement, 3)))

            conductExamScreen.window['-Restart-'].update(visible=True)
            graphResults.createGraphs()
            graphResults.slider_position.on_changed(graphResults.update)
            graphResults.plt.show(block=True)

        elif event == '-Test1R-':
            showRespirationProbabilityDistribution(3)
        elif event == '-Test2R-':
            showRespirationProbabilityDistribution(4)
        elif event == '-Test3R-':
            showRespirationProbabilityDistribution(5)
        elif event == '-Test4R-':
            showRespirationProbabilityDistribution(6)
        elif event == '-Test5R-':
            showRespirationProbabilityDistribution(7)
        elif event == '-Test6R-':
            showRespirationProbabilityDistribution(8)
        elif event == '-UPDATED-':
            updateTime = time.time() - conductExamScreen.startTime
            conductExamScreen.respirationLiveGraph.axis(xmin=updateTime - 20, xmax=updateTime + 20)
            conductExamScreen.respirationLiveGraph.axis(ymin=-3, ymax=3)
            conductExamScreen.respirationLiveGraph.plot(conductExamScreen.respirationTimings, conductExamScreen.respirationMeasurements, c='black')

            conductExamScreen.gsrLiveGraph.axis(xmin=updateTime - 20, xmax=updateTime + 20)
            conductExamScreen.gsrLiveGraph.axis(ymin=-3, ymax=3)
            conductExamScreen.gsrLiveGraph.plot(conductExamScreen.skinConductivityTimings, conductExamScreen.skinConductivityMeasurements, c='black')

            conductExamScreen.bpLiveGraph.axis(xmin=updateTime - 20, xmax=updateTime + 20)
            conductExamScreen.bpLiveGraph.axis(ymin=-3, ymax=3)
            conductExamScreen.bpLiveGraph.plot(conductExamScreen.bloodPressureTimings, conductExamScreen.bloodPressureMeasurements,c='black')

            conductExamScreen.pulseLiveGraph.axis(xmin=updateTime - 20, xmax=updateTime + 20)
            conductExamScreen.pulseLiveGraph.axis(ymin=-3, ymax=3)
            conductExamScreen.pulseLiveGraph.plot(conductExamScreen.pulseTimings, conductExamScreen.pulseMeasurements, c='black')

            conductExamScreen.liveGraph.canvas.draw() #Creates the new numpy live graphing snapshot

            liveGraphingSnapshot = numpy.array(list(conductExamScreen.liveGraph.canvas.tostring_rgb()), 'uint8') #Gets a snapshot of the new live graphing as unsigned integers
            liveGraphingSnapshot = liveGraphingSnapshot.reshape(conductExamScreen.liveGraphingHeight, conductExamScreen.liveGraphingWidth, 3) #Reformats the above snapshot into arrays needed to update numpy canvas 3 unsigned ints in each of 480 arrays, each inside 640 arrays

            conductExamScreen.liveGraphScreen.update(liveGraphingSnapshot) #updates the numpy canvas

          #  newWindow = homescreen.make_window()
          #   conductExamScreen.window.close()
          #  # PolygraphExamSetupScreen.window = newWindow
          #   homescreen.main()

