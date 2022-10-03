########## testing purposes
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
############ do pytest Main_GUI_Window.py on Terminal

# windowHeader - a string representing the window header
windowHeader = ""
# polygraphExamStartButton - a string representing the start button
polygraphExamStartButton = ""
# obtainIndividualMeasurementsStartButton - a string to obtain individual measurement start button
obtainIndividualMeasurementsStartButton = ""
# userHomeWindowSelection - integer for user home window selection
userHomeWindowSelection = 0
# polygraphExamOptions - a list of string for polygraph exam options
polygraphExamOptions = [""]
# bloodPressureSensorConnected - a boolean representing whether blood pressure sensor is connected or not
bloodPressureSensorConnected = False
# skinConductivitySensorConnected - a boolean representing whether skin conductivity sensor is connected or not
skinConductivitySensorConnected = False
# respirationSensorConnected - a boolean representing whether respiration sensor is connected or  not
respirationSensorConnected = False
# examinerInputProblematicQuestions - a list of string representing problematic questions inputted by examiner
examinerInputProblematicQuestions = [""]
# examinerQuestionsAskedTimestamps - a list of integer representing time question was asked by examiner
examinerQuestionsAskedTimestamps = [0]
# respirationMeasurements - a list of object representing respiration measurements
respirationMeasurements = []
# bloodPressureMeasurements - a list of object representing blood pressure measurements
bloodPressureMeasurements = []
# skinConductivityPressureMeasurements - a list of object representing skin conductivity pressure measurements
skinConductivityPressureMeasurements = []
# current_time - a string representing the current time
current_time  = ""

def displayGraphicalAnalysis():
    '''
    Displays the graphical analysis

    :return: None
    '''

def tensorFlowAnalysis():
    '''
    Analysis of tensor flow

    :return: None
    '''

def determineOutliers():
    '''
    Determine data measurements outliers

    :return: None
    '''

def collectRespirationMeasurements():
    '''
    Collects respiration measurements

    :return: a list of objects representing the respiration measurements
    '''

def collectSkinConductivityMeasurements():
    '''
    Collects skin conductivity measurements

    :return: a list of objects representing the skin conductivity measurements
    '''

def collectBloodPressureMeasurements():
    '''
    Collects blood pressure measurements

    :return: a list of objects representing the blood pressure measurements
    '''

def startSkinConductivitySensorRecording():
    '''
    Starts the skin conductivity sensor recording

    :return: None
    '''

def stopSkinConductivitySensorRecording():
    '''
    Stops the skin conductivity sensor recording

    :return: None
    '''

def startRespirationSensorRecording():
    '''
    Starts the respiration sensor recording

    :return: None
    '''

def stopRespirationSensorRecording():
    '''
    Stops the respiration sensor recording

    :return: None
    '''

def startBloodPressureSensorRecording():
    '''
    Starts the blood pressure sensor recording

    :return: None
    '''

def stopBloodPressureSensorRecording():
    '''
    Stops the blood pressure sensor recording

    :return: None
    '''

def collectExaminerInputQuestions():
    '''
    Collects the examiner input questions from the examinerInputProblematicQuestions[]

    :return: None
    '''

def getTime():
    '''
    Gets the current time and returns the string type version of it. Use datetime module.

    :return: String that represents the current time
    '''

def startPolygraphExam():
    '''
    Starts the polygraph exam

    :return: None
    '''

def checkRespirationSensor():
    '''
    Checks respiration sensor

    :return: True or False from the respirationSensorConnected
    '''

def checkSkinConductivitySensor():
    '''
    Checks skin conductivity sensor

    :return: True or False from the skinConductivitySensorConnected
    '''

def checkBloodPressureSensor():
    '''
    Checks blood pressure sensor

    :return: True or False from the bloodPressureSensorConnected
    '''

def getSelectedExaminationType():
    '''
    Gets selected examination type

    :return: String that represents the selected examination type
    '''

def collectIndividualMeasurementsOption():
    '''
    Collects individual measurement option

    :return: String that represents the individual measurements option
    '''

