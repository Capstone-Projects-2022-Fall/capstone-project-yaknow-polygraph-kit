import mysql

db = mysql.connector.connect(
    host="173.255.232.150",
    user="cis4398",
    passwd="dNC=IK~9)7",
    database="Recordings"
)

mycursor = db.execute()
mycursor.execute("CREATE TABLE `SingularRecording` (`question` TEXT,`response` CHAR,`timestamp` DATETIME,`pulse` DECIMAL,`skin_conductivity` DECIMAL,`respiration_belt` DECIMAL,`blood_pressure` DECIMAL")

class SingluarRecording:
    def __init__(self, timestamp, question, response, skin_conductivity, respiration_belt, blood_pressure, pulse):
        self.timestamp = timestamp
        self.question = question
        self.response = response
        self.skin_conductivity = skin_conductivity
        self.respiration_belt = respiration_belt
        self.blood_pressure = blood_pressure
        self.pulse = pulse