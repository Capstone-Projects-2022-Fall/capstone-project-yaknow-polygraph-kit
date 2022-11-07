import SingularRecordingsDB
import time

exam_ID =11
question_ID = 0
question = "How old are you?"
response = "y"
timeStamp = time.time()
pulse = "12"
skin_con = 3
respBel = "34"
bp = "43"



#SingularRecordingsDB.add_singularRecord(exam_ID,  question_ID, question, response, timeStamp, pulse, skin_con, respBel, bp, "T")
#SingularRecordingsDB.add_singularRecord(exam_ID,  question_ID, "TEST", response, timeStamp, pulse, skin_con, respBel, bp, "F")
print(SingularRecordingsDB.get_singularRecords()[0])


