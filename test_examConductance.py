import unittest
import PolygraphExamSetupScreen
import conductExamScreen
import time
import threading
import random

class examConductanceTest(unittest.TestCase):

    def testLiveGraphing(self):
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

        bpThread = threading.Thread(target=bpCuffThread)
        bpThread.start()

        rThread = threading.Thread(target=respirationThread)
        rThread.start()

        gsrThread = threading.Thread(target=scThread)
        gsrThread.start()

        conductExamScreen.startExam(newWindow)

def bpCuffThread():
    for x in range(9):
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


def scThread():
    while conductExamScreen.examFinished == False:
        if (conductExamScreen.inQuestion == True):
            conductExamScreen.skinConductivityMeasurements.append(random.randrange(20100, 20800))
            conductExamScreen.skinConductivityTimings.append(time.time() - conductExamScreen.startTime)
            conductExamScreen.window.write_event_value('-UPDATED-', None)
            time.sleep(1)



def respirationThread():
    while conductExamScreen.examFinished == False:
        if (conductExamScreen.inQuestion == True):
            conductExamScreen.respirationTimings.append(time.time() - conductExamScreen.startTime)
            conductExamScreen.respirationMeasurements.append(random.random())
            #conductExamScreen.window.write_event_value('-UPDATED-', None)
            time.sleep(1)


if __name__ == '__main__':
    unittest.main()
