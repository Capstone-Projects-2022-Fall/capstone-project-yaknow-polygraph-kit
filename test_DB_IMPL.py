import testUpdateSingularRecording
import time

exam_ID = 9
question_ID = 0
question = "How old are you?"
response = "y"
timeStamp = time.time()
pulse = "12"
skin_con = 3
respBel = "34"
bp = "43"

testUpdateSingularRecording.add_singularRecord(exam_ID,  question_ID, question, response, timeStamp, pulse, skin_con, respBel, bp, "T")
