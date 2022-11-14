import mysql
from numpy import random
import pandas as pd
import SingularRecordingsDB
import time
from sqlite3 import connect
import database
from sqlalchemy import create_engine



"""while i > 0:
    i -= 1
    counter += 1
    question_ID = counter
    skin_con = skin_con + random.randint(-2, 5)
    pulse = pulse + random.randint(-2, 5)
    bp = bp + random.randint(-2, 5)
    respBel = respBel + random.randint(-2, 5)
    question = f'question part {str(counter)}'
    SingularRecordingsDB.add_singularRecord(exam_ID, question_ID, question, response,
                                            timeStamp, pulse,
                                            skin_con, respBel, bp, "F")
"""

