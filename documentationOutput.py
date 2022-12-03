import homescreen
import PolygraphExamSetupScreen
import conductExamScreen
import respirationBelt
import arduino
import bloodPressureDevice
import graphResults


documentationFile = open("documentationOutput.txt", "a")

helpHomescreen = (str(help(homescreen)))
documentationFile.write(helpHomescreen)
helpPolygraphExamSetupScreen = (str(help(PolygraphExamSetupScreen)))
documentationFile.write(helpPolygraphExamSetupScreen)
helpConductExamScreen = (str(help(conductExamScreen)))
documentationFile.write(helpConductExamScreen)
helpRespirationBelt = (str(help(respirationBelt)))
documentationFile.write(helpRespirationBelt)
helpArduino = (str(help(arduino)))
documentationFile.write(helpArduino)
helpBloodPressure = (str(help(bloodPressureDevice)))
documentationFile.write(helpBloodPressure)
helpGraphResults = (str(help(graphResults)))
documentationFile.write(helpGraphResults)
documentationFile.close()
