import conductExamScreen
import datetime
import random
import PolygraphExamSetupScreen
import matplotlib

conductExamScreen.respirationRecordings = []
conductExamScreen.skinConductivityRecordings = []
conductExamScreen.bloodPressureRecordings = []
conductExamScreen.pulseRecordings = []
examStartTime = datetime.datetime.now()
questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
questionIterator = 0
currentQuestion = questions[questionIterator]
bpMeasurements = []
bpMeasurements.append(random.random())
pulseMeasurements = []
pulseMeasurements.append(random.random())
currentTime = (datetime.datetime.now() - examStartTime).total_seconds()
tempMeasurement = conductExamScreen.singularRecording(currentTime, bpMeasurements, currentQuestion, None)
conductExamScreen.bloodPressureRecordings.append(tempMeasurement)
tempMeasurement = conductExamScreen.singularRecording(currentTime, pulseMeasurements, currentQuestion, None)
conductExamScreen.pulseRecordings.append(tempMeasurement)

for x in range(27):
    respirationMeasurements = []
    bpMeasurements = []
    pulseMeasurements = []
    currentTime = (datetime.datetime.now() - examStartTime).total_seconds()
    if (((x % 3) == 0) and (x != 0)):
        bpMeasurements.append(random.random())
        pulseMeasurements.append(random.random())
        tempMeasurement = conductExamScreen.singularRecording(currentTime, bpMeasurements, currentQuestion, None)
        conductExamScreen.bloodPressureRecordings.append(tempMeasurement)
        tempMeasurement = conductExamScreen.singularRecording(currentTime, pulseMeasurements, currentQuestion, None)
        conductExamScreen.pulseRecordings.append(tempMeasurement)
        questionIterator = questionIterator + 1
        currentQuestion = questions[questionIterator]
    respirationMeasurements.append(random.random())
    tempMeasurement = conductExamScreen.singularRecording(currentTime, respirationMeasurements, currentQuestion, None)
    conductExamScreen.respirationRecordings.append(tempMeasurement)
    scMeasurements = random.random()
    tempMeasurement = conductExamScreen.singularRecording(currentTime, scMeasurements, currentQuestion, None)
    conductExamScreen.skinConductivityRecordings.append(tempMeasurement)


conductExamScreen.questionCounter = 8
PolygraphExamSetupScreen.global_overall_questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
conductExamScreen.iterated = False
conductExamScreen.examTime = 0
conductExamScreen.examFinished = False
conductExamScreen.inQuestion = True
newWindow = conductExamScreen.make_window()
conductExamScreen.startExam(newWindow)