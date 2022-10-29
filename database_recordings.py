import mysql
import mysql.connector

db = mysql.connector.connect(
    host="173.255.232.150",
    user="cis4398",
    passwd="dNC=IK~9)7",
    database="SingularRecording"
)

mycursor = db.execute()
mycursor.execute("CREATE TABLE `SingularRecording` (`exmaID` DECIMAL,`questionID` DECIMAL,`question` TEXT,`response` CHAR,`timestamp` DATETIME,`pulse` DECIMAL,`skin_conductivity` DECIMAL,`respiration_belt` DECIMAL,`blood_pressure` DECIMAL")

""""
CREATE TABLE `Questions`.`SingularRecording` (
  `exmaID` INT NOT NULL,
  `questionID` INT NOT NULL,
  `question` VARCHAR(255) NULL,
  `response` VARCHAR(255) NULL DEFAULT 'no response',
  `timestamp` DATETIME NOT NULL,
  `pulse` VARCHAR(255) NULL,
  `skin_conductivity` INT NULL,
  `respiration_belt` VARCHAR(45) NULL,
  `blood_pressure` VARCHAR(45) NULL,
  UNIQUE INDEX `timestamp_UNIQUE` (`timestamp` ASC));
"""""




class SingluarRecording:
    def __init__(self, timestamp, question, response, skin_conductivity, respiration_belt, blood_pressure, pulse):
        self.timestamp = timestamp
        self.question = question
        self.response = response
        self.skin_conductivity = skin_conductivity
        self.respiration_belt = respiration_belt
        self.blood_pressure = blood_pressure
        self.pulse = pulse