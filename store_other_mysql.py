import mysql.connector
from mysql.connector import errorcode
import re
import store_other_mysql

global table_number



def create_table(table_name):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    try:
    # create table called table_name, question with 255 char, response with 255 char, time with 20 digits and 20 decimals, measurement with 20 digits and 20 decimals
        with db.cursor() as mycursor:
            mycursor.execute(f"CREATE TABLE {table_name} (question VARCHAR(255), response VARCHAR(255), time DECIMAL(64, 30), measurement DECIMAL(64, 30))")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print(f'{table_name} table already exists')

    db.commit()
    db.close()

def drop_table(table_name):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    with db.cursor() as mycursor:
        mycursor.execute(f"DROP TABLE {table_name}")
        db.commit()
    db.close()
def show_table(table_to_show):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    '''
    This function shows/prints the contents in table_to_show
    :return: void
    '''
    try:
        with db.cursor() as mycursor:
            mycursor.execute(f"SELECT * FROM {table_to_show}")
            for x in mycursor:
                print(x)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_NO_SUCH_TABLE:
            print(f'{table_to_show} table does not exist')

    db.close()

def show_all_tables():
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    result = None
    with db.cursor() as mycursor:
        mycursor.execute("SHOW TABLES")
        result = mycursor.fetchall()

    for x in result:
        print(x[0])
def desc_table(table_to_desc):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    '''
    This function describes the contents in table_to_desc
    :return: void
    '''
    result = None
    try:
        with db.cursor() as mycursor:
            mycursor.execute(f"DESCRIBE {table_to_desc}")
            result = mycursor.fetchall()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_NO_SUCH_TABLE:
            print(f'{table_to_desc} table does not exist')

    db.close()
    print(result)
def check_table_exist(the_table_to_check):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )
    result = -1
    with db.cursor() as mycursor:
        mycursor.execute("SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'Questions') AND (TABLE_NAME = (%s))", (the_table_to_check,))
        result = mycursor.fetchall()
    db.close()

    # table doesn't exist
    if(result[0][0] == 0):
        return False

    return True


def get_table_id(the_table_to_check):
    match = re.search(r'\d+', the_table_to_check)

    if(match):
        return match.group()
    else:
        return 1

def find_available_id(the_table_to_check):
    new_table_to_check = None
    new_number = 0
    # while table exist, keep searching until table with id doesn't exist
    while check_table_exist(the_table_to_check):
        # get table id
        store_other_mysql.table_number = get_table_id(the_table_to_check)
        # make new table id
        new_number = int(store_other_mysql.table_number) + 1
        # replace table id with new table id
        new_table_to_check = the_table_to_check.replace(store_other_mysql.table_number, str(new_number))
        print(new_table_to_check)
        the_table_to_check = new_table_to_check
        pass

    # if we're here then table does not exist
    # create the table for Respiration
    create_table(the_table_to_check)

    # create the table for BP
    create_table("BP" + str(new_number))

    # create the table for Pulse
    create_table("Pulse" + str(new_number))

    # create the table for GSR
    create_table("GSR" + str(new_number))

    # set the table number
    set_table_number(new_number)



def respiration_insert(respiration_table, question_to_be_inserted, response_to_be_inserted, time_to_be_inserted, measurement_to_be_inserted):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    with db.cursor() as mycursor:
        mycursor.execute(f"INSERT INTO {respiration_table} (question, response, time, measurement) VALUES (%s, %s, {time_to_be_inserted}, {measurement_to_be_inserted})", (question_to_be_inserted, response_to_be_inserted,))
        db.commit()

    db.close()

def BP_insert(bp_table, question_to_be_inserted, response_to_be_inserted, time_to_be_inserted, measurement_to_be_inserted):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    with db.cursor() as mycursor:
        mycursor.execute(f"INSERT INTO {bp_table} (question, response, time, measurement) VALUES (%s, %s, {time_to_be_inserted}, {measurement_to_be_inserted})", (question_to_be_inserted, response_to_be_inserted,))
        db.commit()

    db.close()

def pulse_insert(pulse_table, question_to_be_inserted, response_to_be_inserted, time_to_be_inserted, measurement_to_be_inserted):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    with db.cursor() as mycursor:
        mycursor.execute(f"INSERT INTO {pulse_table} (question, response, time, measurement) VALUES (%s, %s, {time_to_be_inserted}, {measurement_to_be_inserted})", (question_to_be_inserted, response_to_be_inserted,))
        db.commit()

    db.close()

def GSR_insert(gsr_table, question_to_be_inserted, response_to_be_inserted, time_to_be_inserted, measurement_to_be_inserted):
    db = mysql.connector.connect(
        host="173.255.232.150",
        user="cis4398",
        passwd="dNC=IK~9)7",
        database="Questions"
    )

    with db.cursor() as mycursor:
        mycursor.execute(f"INSERT INTO {gsr_table} (question, response, time, measurement) VALUES (%s, %s, {time_to_be_inserted}, {measurement_to_be_inserted})", (question_to_be_inserted, response_to_be_inserted,))
        db.commit()

    db.close()
def get_table_number():
    return table_number

def set_table_number(number_to_be_set):
    store_other_mysql.table_number = number_to_be_set