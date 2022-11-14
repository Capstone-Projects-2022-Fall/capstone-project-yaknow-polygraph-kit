# lessons with Tech With Tim
# YouTube channel: https://www.youtube.com/c/TechWithTim
import mysql.connector
from mysql.connector import errorcode


def add_singularRecord(examID, questionID, question, response, time_stamp, pulse, skin_Con, respiration, bp, label):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    '''
    This function adds question into the centralized database using MySQL
    :param question: The user input for question to be added
    :return: void
    '''
    with db.cursor() as mycursor:
        # mycursor.execute("INSERT INTO SingularRecording(exmaID, questionID, question, response, timeStamp, pulse,  skin_conductivity, respiration_belt, blood_pressure) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s), ())
        mycursor.execute(
            "INSERT INTO SingularRecording (exmaID, questionID, question, response, tsStamp , pulse, skin_conductivity, respiration_belt, blood_pressure, ML_Prediction ,ML_Accuracy, actual_ans) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)",
            (examID, questionID, question, response, time_stamp, pulse, skin_Con, respiration, bp, "null", "null",
             label,))

        db.commit()

    db.close()


def delete_singularRecord(examID):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    '''
    This function delete question from the centralized database.
    Only user with admin rights can delete question from the database.
    Error is handled when user do not have right privileges to delete.
    Program will not crash as a result of error.
    :param question: The user input for question to be deleted
    :return: void
    '''
    try:
        with db.cursor() as mycursor:
            mycursor.execute("DELETE FROM SingularRecording Where exmaID = (%s)", (examID,))
            db.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLEACCESS_DENIED_ERROR:
            print('This current user do not have privilege to delete from database')
        else:
            raise

    db.close()


def show_singularRecords():
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    '''
    This function shows/prints the contents in SingularRecording database in MySQL
    :return: void
    '''
    with db.cursor() as mycursor:
        mycursor.execute("SELECT * FROM SingularRecording")
        for x in mycursor:
            print(x[0])

    db.close()


def get_singularRecords():
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    '''
    This function returns the contents in table SingularRecording
    :return: questions in tuples
    '''

    questions = []
    with db.cursor() as mycursor:
        mycursor.execute("SELECT * FROM SingularRecording")
        questions = mycursor.fetchall()

    # convert list of tuples to just a list
    list_singularRecord = [item for t in questions for item in t]
    # change to lowercase
    #list_singularRecords_lower = [x.lower() for x in list_singularRecord]
    # remove leading and trailing spaces and new lines
    #list_singularRecords_clean = [x.strip().replace("\n", "") for x in list_singularRecords_lower]
    db.close()
    #return list_singularRecords_clean
    return list_singularRecord


def getLastExamNumber():
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    '''
    This function returns the contents in table SingularRecording
    :return: questions in tuples
    '''

    questions = []
    with db.cursor() as mycursor:
        mycursor.execute("SELECT exmaID FROM SingularRecording ORDER BY exmaID DESC LIMIT 1")
        questions = mycursor.fetchall()

    # convert list of tuples to just a list
    list_singularRecord = [item for t in questions for item in t]
    # change to lowercase
    #list_singularRecords_lower = [x.lower() for x in list_singularRecord]
    # remove leading and trailing spaces and new lines
    #list_singularRecords_clean = [x.strip().replace("\n", "") for x in list_singularRecords_lower]
    db.close()
    #return list_singularRecords_clean
    return list_singularRecord


'''def uploadableSingularRecording(self, examID, questionID, question, response, timestamp, pulse, skin_Con, respiration,
                                bp):
    self.examID = examID
    self.questionID = questionID
    self.question = question
    self.response = response
    self.timestamp = timestamp
    self.pulse = pulse
    self.skin_Con = skin_Con
    self.respiration = respiration
    self.bp = bp'''