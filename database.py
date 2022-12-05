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
        # only add if question does not already exist
        mycursor.execute("INSERT IGNORE INTO Question (question) VALUES (%s)", (question,))
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

def search_question_from_database(search_string):
    '''
    This function searches question from database and returns
    True if found or False otherwise.
    :param search_string: string to search from database
    :return: True or False
    '''
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    # list of elements in database
    db_list = get_questions()
    # search string to lower case
    search_string_lower = search_string.lower()
    # search string remove leading and trailing spaces and new lines
    search_string_clean = search_string_lower.strip().replace("\n", "")
    for element in db_list:
        if element == search_string_clean:
            return True
    return False

def select_question_from_database():
    '''
    This function returns all question selected by user input
    :return: question selected by user input
    '''
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    # list of user selections in the form of integers
    user_selections = []

    # get elements in database
    db_list = get_questions()
    # iterator
    i = 0
    # print statement to notify user what's on screen
    print('Elements in database with corresponding number')
    # show user elements in database with corresponding number for user to select
    for element in db_list:
        print(i, element)
        i += 1
    # print statement to prompt user
    print('Enter number associated with question to be selected, press enter with no inputs to stop')
    # exception handler when input is not an integer
    try:
        while True:
            user_selections.append(int(input()))
    # if input is not integer, pass
    except:
        pass

    # the list to be returned consisting of elements specified by user
    ret_list = []
    # append to return list the selection made by user
    for user_input in user_selections:
        ret_list.append(db_list[user_input])

    return ret_list

def add_new_question_to_database(add_string):
    '''
    This function add the new question add_string to the database
    :param add_string: the string to be added to database
    :return: True if add_string is added in database, False otherwise
    '''
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    # add new question to database
    add_question(add_string)
    # check to see if element is in database using search method, true if found, false otherwise
    ret_value = search_question_from_database(add_string)
    return ret_value