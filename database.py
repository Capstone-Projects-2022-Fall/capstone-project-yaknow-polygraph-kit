# lessons with Tech With Tim
# YouTube channel: https://www.youtube.com/c/TechWithTim
import mysql.connector
from mysql.connector import errorcode

def add_question(question):
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
        mycursor.execute("INSERT INTO Question (question) VALUES (%s)", (question,))
        db.commit()

    db. close()

def delete_question(question):
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
            mycursor.execute("DELETE FROM Question Where question = (%s)", (question,))
            db.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLEACCESS_DENIED_ERROR:
            print('This current user do not have privilege to delete from database')
        else:
            raise

    db.close()

def show_questions():
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    '''
    This function shows/prints the contents in Question database in MySQL
    :return: void
    '''
    with db.cursor() as mycursor:
        mycursor.execute("SELECT * FROM Question")
        for x in mycursor:
            print(x[0])

    db.close()
def get_questions():
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    '''
    This function returns the contents in table Question
    :return: questions in tuples
    '''

    questions = []
    with db.cursor() as mycursor:
        mycursor.execute("SELECT * FROM Question")
        questions = mycursor.fetchall()

    # convert list of tuples to just a list
    list_question = [item for t in questions for item in t]
    # change to lowercase
    list_questions_lower = [x.lower() for x in list_question]
    # remove leading and trailing spaces and new lines
    list_questions_clean = [x.strip().replace("\n", "") for x in list_questions_lower]
    db.close()
    return list_questions_clean