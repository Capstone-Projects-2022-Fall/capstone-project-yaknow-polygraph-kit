# lessons with Tech With Tim
# YouTube channel: https://www.youtube.com/c/TechWithTim
import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    host="173.255.232.150",
    user="cis4398",
    passwd="dNC=IK~9)7",
    database="Questions"
)

def add_question(question):
    '''
    This function adds question into the centralized database using MySQL
    :param question: The user input for question to be added
    :return: void
    '''
    with db.cursor() as mycursor:
        mycursor.execute("INSERT INTO Question (question) VALUES (%s)", (question,))
        db.commit()

def delete_question(question):
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

def show_questions():
    '''
    This function shows/prints the contents in Question database in MySQL
    :return: void
    '''
    with db.cursor() as mycursor:
        mycursor.execute("SELECT * FROM Question")
        for x in mycursor:
            print(x[0])

show_questions()