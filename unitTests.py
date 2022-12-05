import unittest
import homescreen
import PySimpleGUI as gui
import time
import threading
import unitTests
import PolygraphExamSetupScreen
import conductExamScreen
import datetime
import random
import os
import signal

global testWindow

class MyTestCase(unittest.TestCase):
    #homescreen module tests
    def test_homescreen_main(self):
        homescreen.window = None
        homescreenTest = threading.Thread(target=unitTests.homescreenTestThread, daemon=True)
        homescreenTest.start()
        homescreen.main()


    def test_homscreen_make_window(self):
        unitTests.testWindow = homescreen.make_window()
        self.assertEqual(isinstance(unitTests.testWindow, gui.Window), True)  # add assertion here

    #PolygraphExamSetupScreen module tests

    def test_PolygraphExamSetupScreen_startExam(self):
        window = PolygraphExamSetupScreen.make_window()
        polygraphExamTest = threading.Thread(target=unitTests.polygraphExamTestThread, daemon=True)
        polygraphExamTest.start()
        PolygraphExamSetupScreen.startExam(window)

    def test_PolygraphExamSetupScreen_make_window(self):
        testWindow = PolygraphExamSetupScreen.make_window()
        self.assertEqual(isinstance(testWindow, gui.Window), True)

    #conductExamScreen module tests

    def test_conductExamScreen_startExam(self):
        conductExamScreen.examFinished = True
        window = conductExamScreen.make_window()
        conductExamScreenTest = threading.Thread(target=unitTests.conductExamScreenTestThread, daemon=True)
        conductExamScreenTest.start()
        conductExamScreen.startExam(window)

    def test_conductExamScreen_make_window(self):
        testWindow = conductExamScreen.make_window()
        self.assertEqual(isinstance(testWindow, gui.Window), True)

    def test_conductExamScreen_separateByQuestion(self):
        conductExamScreen.respirationRecordings = []
        conductExamScreen.skinConductivityRecordings = []
        examStartTime = datetime.datetime.now()
        questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        questionIterator = 0
        measurements = []
        currentQuestion = questions[questionIterator]
        for x in range(27):
            if (((x % 3) == 0) and (x != 0)):
                questionIterator = questionIterator + 1
                currentQuestion = questions[questionIterator]
            currentTime = (datetime.datetime.now() - examStartTime).total_seconds()
            measurements.append(random.random())
            tempMeasurement = conductExamScreen.singularRecording(currentTime, measurements, currentQuestion, None)
            conductExamScreen.respirationRecordings.append(tempMeasurement)
            conductExamScreen.skinConductivityRecordings.append(tempMeasurement)
            measurements = []

        conductExamScreen.separateByQuestion()
        self.assertEqual(len(conductExamScreen.respirationRecordings), 27)
        self.assertEqual(len(conductExamScreen.respirationbyQuestion), 9)
        for y in range(9):
            assert (len(conductExamScreen.respirationbyQuestion[y]) == 3)

    '''def test_conductExamScreen_examCount(self):
        PolygraphExamSetupScreen.global_overall_questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

        conductExamScreen.respirationMeasurements = []
        conductExamScreen.respirationTimings = []

        conductExamScreen.skinConductivityMeasurements = []
        conductExamScreen.skinConductivityTimings = []

        conductExamScreen.bloodPressureMeasurements = []
        conductExamScreen.bloodPressureTimings = []
        conductExamScreen.bloodPressureRecordings = []

        conductExamScreen.pulseMeasurements = []
        conductExamScreen.pulseTimings = []

        conductExamScreen.yn = None

        conductExamScreen.questionCounter = 0

        conductExamScreen.examFinished = False

        conductExamScreen.examTime = 1

        conductExamScreen.newQuestion = PolygraphExamSetupScreen.global_overall_questions[0]

        conductExamScreen.inQuestion = False

        conductExamScreen.iterated = False

        PolygraphExamSetupScreen.examStarted = True
        newWindow = conductExamScreen.make_window()
        conductExamScreen.window = newWindow

        conductExamScreen.respirationTimings = []
        conductExamScreen.respirationRecordings = []

        conductExamScreen.startTime = time.time()

        bpThread = threading.Thread(target=unitTests.bpCuffThread)
        bpThread.start()

        rThread = threading.Thread(target=unitTests.respirationThread)
        rThread.start()

        gsrThread = threading.Thread(target=unitTests.scThread)
        gsrThread.start()

        conductExamScreen.startExam(newWindow)'''

    def test_conductExamScreen_conductZtestSkinConductivity(self):
        conductExamScreen.GSRbyQuestion = []
        gsrMeasurement = 202000
        for y in range (4):
            tempMeasurements = []
            for x in range(4):
                gsrMeasurement  = gsrMeasurement + 1
                tempMeasurements.append(gsrMeasurement)
            conductExamScreen.GSRbyQuestion.append(tempMeasurements)
        conductExamScreen.conductZtestSkinConductivity(3)
        self.assertEqual(conductExamScreen.zTest1SkinConductivity[0], -13.145341380123986)
        self.assertEqual(conductExamScreen.zTest1SkinConductivity[1], 1.8098685839954278e-39)
        self.assertEqual(conductExamScreen.zTest2SkinConductivity[0], -8.763560920082657)
        self.assertEqual(conductExamScreen.zTest2SkinConductivity[1], 1.891775991421363e-18)
        self.assertEqual(conductExamScreen.zTest3SkinConductivity[0], -4.381780460041329)
        self.assertEqual(conductExamScreen.zTest3SkinConductivity[1], 1.1771339097614998e-05)

    def test_conductExamScreen_conductZtestRespiration(self):
        conductExamScreen.respirationbyQuestion = []
        respirationMeasurement = 0
        for y in range(4):
            tempMeasurements = []
            for x in range(4):
                respirationMeasurement = respirationMeasurement + 1
                tempMeasurements.append(respirationMeasurement)
            conductExamScreen.respirationbyQuestion.append(tempMeasurements)
        conductExamScreen.conductZtestRespiration(3)
        self.assertEqual(conductExamScreen.zTest1Respiration[0], -13.145341380123986)
        self.assertEqual(conductExamScreen.zTest1Respiration[1], 1.8098685839954278e-39)
        self.assertEqual(conductExamScreen.zTest2Respiration[0], -8.763560920082657)
        self.assertEqual(conductExamScreen.zTest2Respiration[1], 1.891775991421363e-18)
        self.assertEqual(conductExamScreen.zTest3Respiration[0], -4.381780460041329)
        self.assertEqual(conductExamScreen.zTest3Respiration[1], 1.1771339097614998e-05)

    '''def test_conductExamScreen_showRespirationProbabilityDistribution(self):
        conductExamScreen.respirationbyQuestion = []
        respirationMeasurement = 0
        for y in range(4):
            tempMeasurements = []
            for x in range(4):
                respirationMeasurement = respirationMeasurement + 1
                tempMeasurements.append(respirationMeasurement)
            conductExamScreen.respirationbyQuestion.append(tempMeasurements)
        conductExamScreen.showRespirationProbabilityDistribution(3)
        matplotlib.pyplot.close('all')'''

    '''def test_conductExamScreen_uploadToDatabase(self):
        conductExamScreen.pulseMeasurements = []
        conductExamScreen.bloodPressureRecordings= []
        conductExamScreen.respirationRecordings = []
        conductExamScreen.skinConductivityRecordings = []
        examStartTime = datetime.datetime.now()
        questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        questionIterator = 0
        measurements = []
        currentQuestion = questions[questionIterator]
        for x in range(27):
            if (((x % 3) == 0) and (x != 0)):
                questionIterator = questionIterator + 1
                currentQuestion = questions[questionIterator]
            currentTime = (datetime.datetime.now() - examStartTime).total_seconds()
            measurements.append(random.random())
            tempMeasurement = conductExamScreen.singularRecording(currentTime, measurements, currentQuestion, None)
            conductExamScreen.respirationRecordings.append(tempMeasurement)
            conductExamScreen.skinConductivityRecordings.append(tempMeasurement)
            conductExamScreen.bloodPressureRecordings.append(tempMeasurement)
            conductExamScreen.skinConductivityRecordings.append(tempMeasurement)
            measurements = []'''

    def test_conductExamScreen_getNumOfMeasurements(self):
        conductExamScreen.pulseRecordings = []
        conductExamScreen.bloodPressureRecordings= []
        conductExamScreen.respirationRecordings = []
        conductExamScreen.skinConductivityRecordings = []
        examStartTime = datetime.datetime.now()
        questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        questionIterator = 0
        measurements = []
        currentQuestion = questions[questionIterator]
        for x in range(27):
            if (((x % 3) == 0) and (x != 0)):
                questionIterator = questionIterator + 1
                currentQuestion = questions[questionIterator]
            currentTime = (datetime.datetime.now() - examStartTime).total_seconds()
            measurements.append(random.random())
            tempMeasurement = conductExamScreen.singularRecording(currentTime, measurements, currentQuestion, None)
            conductExamScreen.respirationRecordings.append(tempMeasurement)
            conductExamScreen.skinConductivityRecordings.append(tempMeasurement)
            conductExamScreen.bloodPressureRecordings.append(tempMeasurement)
            conductExamScreen.pulseRecordings.append(tempMeasurement)
            measurements = []
        theMax = conductExamScreen.getNumOfMeasurements()
        self.assertEqual(theMax,27)

    #arduino module

    def test_respirationBelt_connectGSRSensor(self):
        conductExamScreen.examFinished = False

        conductExamScreen.respirationMeasurements = []
        conductExamScreen.respirationTimings = []

        conductExamScreen.skinConductivityMeasurements = []
        conductExamScreen.skinConductivityTimings = []

        conductExamScreen.bloodPressureMeasurements = []
        conductExamScreen.bloodPressureTimings = []
        conductExamScreen.bloodPressureRecordings = []

        conductExamScreen.pulseMeasurements = []
        conductExamScreen.pulseTimings = []

        conductExamScreen.startTime = time.time()

        bpThread = threading.Thread(target=unitTests.bpCuffThread)
        bpThread.start()

        rThread = threading.Thread(target=unitTests.respirationThread)
        rThread.start()

        gsrThread = threading.Thread(target=unitTests.scThread)
        gsrThread.start()

        bpThread.join()
        self.assertEqual(len(conductExamScreen.skinConductivityMeasurements), 12)

        # respirationBelt module

    def test_respirationBelt_connectRespirationBelt(self):
        conductExamScreen.examFinished = False

        conductExamScreen.respirationMeasurements = []
        conductExamScreen.respirationTimings = []

        conductExamScreen.skinConductivityMeasurements = []
        conductExamScreen.skinConductivityTimings = []

        conductExamScreen.bloodPressureMeasurements = []
        conductExamScreen.bloodPressureTimings = []
        conductExamScreen.bloodPressureRecordings = []

        conductExamScreen.pulseMeasurements = []
        conductExamScreen.pulseTimings = []

        conductExamScreen.startTime = time.time()

        bpThread = threading.Thread(target=unitTests.bpCuffThread)
        bpThread.start()

        rThread = threading.Thread(target=unitTests.respirationThread)
        rThread.start()

        gsrThread = threading.Thread(target=unitTests.scThread)
        gsrThread.start()

        bpThread.join()
        self.assertEqual(len(conductExamScreen.respirationMeasurements), 12)

    #bloodPressureDevice module

    def test_respirationBelt_connectBloodPressureDevice(self):
        conductExamScreen.examFinished = False

        conductExamScreen.respirationMeasurements = []
        conductExamScreen.respirationTimings = []

        conductExamScreen.skinConductivityMeasurements = []
        conductExamScreen.skinConductivityTimings = []

        conductExamScreen.bloodPressureMeasurements = []
        conductExamScreen.bloodPressureTimings = []
        conductExamScreen.bloodPressureRecordings = []

        conductExamScreen.pulseMeasurements = []
        conductExamScreen.pulseTimings = []

        conductExamScreen.startTime = time.time()

        bpThread = threading.Thread(target=unitTests.bpCuffThread)
        bpThread.start()

        rThread = threading.Thread(target=unitTests.respirationThread)
        rThread.start()

        gsrThread = threading.Thread(target=unitTests.scThread)
        gsrThread.start()

        bpThread.join()
        self.assertEqual(len(conductExamScreen.bloodPressureMeasurements), 3)
        #os.kill(os.getpid(), signal.SIGTERM)





if __name__ == '__main__':
    unittest.main()

def homescreenTestThread():
    time.sleep(2)
    while(homescreen.window == None):
        continue
        time.sleep(1)
    homescreen.window.write_event_value(gui.WIN_CLOSED, None)

def polygraphExamTestThread():
    time.sleep(2)
    while(PolygraphExamSetupScreen.window == None):
        continue
        time.sleep(1)
    PolygraphExamSetupScreen.window.write_event_value(gui.WIN_CLOSED, None)

def conductExamScreenTestThread():
    time.sleep(2)
    while (conductExamScreen.window == None):
        continue
        time.sleep(1)
    conductExamScreen.window.write_event_value(gui.WIN_CLOSED, None)

def bpCuffThread():
    for x in range(3):
        conductExamScreen.inQuestion = True
        print("In Question")
        time.sleep(4)
        conductExamScreen.bloodPressureMeasurements.append(random.randrange(70,150))
        conductExamScreen.bloodPressureTimings.append(time.time() - conductExamScreen.startTime)
        conductExamScreen.pulseMeasurements.append(random.randrange(40, 130))
        conductExamScreen.pulseTimings.append(time.time() - conductExamScreen.startTime)
        #conductExamScreen.window.write_event_value('-UPDATED-', None)
        conductExamScreen.bloodPressureRecordings.append(1)
        conductExamScreen.inQuestion = False
        time.sleep(2)
    conductExamScreen.examFinished = True


def scThread():
    while conductExamScreen.examFinished == False:
        if (conductExamScreen.inQuestion == True):
            conductExamScreen.skinConductivityMeasurements.append(random.randrange(20100, 20800))
            conductExamScreen.skinConductivityTimings.append(time.time() - conductExamScreen.startTime)
            #conductExamScreen.window.write_event_value('-UPDATED-', None)
            time.sleep(1)



def respirationThread():
    while conductExamScreen.examFinished == False:
        if (conductExamScreen.inQuestion == True):
            conductExamScreen.respirationTimings.append(time.time() - conductExamScreen.startTime)
            conductExamScreen.respirationMeasurements.append(random.random())
            print("ADDED: ", len(conductExamScreen.respirationMeasurements))
            #conductExamScreen.window.write_event_value('-UPDATED-', None)
            time.sleep(1)