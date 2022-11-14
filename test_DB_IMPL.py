from numpy import random

import SingularRecordingsDB
import time
import database

exam_ID = SingularRecordingsDB.getLastExamNumber().pop() +1
question_ID = 0
question = "Initial Test Question"
response = "n"
timeStamp = time.time()
pulse = 70
skin_con = 3
respBel = 34
bp = 111

i = 5
counter = 0
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

#SingularRecordingsDB.delete_singularRecord(1)
#var =  SingularRecordingsDB.getLastExamNumber().pop() +1
#print(var)
#SingularRecordingsDB.add_singularRecord(exam_ID, question_ID, question, response, timeStamp, pulse, skin_con, respBel,  bp, "T")
#SingularRecordingsDB.add_singularRecord(exam_ID,  question_ID, "TEST", response, timeStamp, pulse, skin_con, respBel, bp, "F")
SingularRecordingsDB.delete_singularRecord(0)
SingularRecordingsDB.delete_singularRecord(1)
SingularRecordingsDB.delete_singularRecord(2)
SingularRecordingsDB.delete_singularRecord(3)
SingularRecordingsDB.delete_singularRecord(4)
SingularRecordingsDB.delete_singularRecord(5)
SingularRecordingsDB.delete_singularRecord(6)

#SingularRecordingsDB.delete_singularRecord('12')
# print(SingularRecordingsDB.get_singularRecords()[0])