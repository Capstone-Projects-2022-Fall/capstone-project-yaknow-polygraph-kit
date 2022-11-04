import unittest
import conductExamScreen
import datetime
import time
import random

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def testQuestionSeparation(self):
        conductExamScreen.respirationRecordings = []
        examStartTime = datetime.datetime.now()
        questions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        questionIterator = 0
        measurements = []
        currentQuestion = questions[questionIterator]
        for x in range(27):
            if( ( (x % 3) == 0 ) and (x != 0) ):
                questionIterator = questionIterator + 1
                currentQuestion = questions[questionIterator]
            currentTime = (datetime.datetime.now() - examStartTime).total_seconds()
            measurements.append(random.random())
            tempMeasurement = conductExamScreen.singularRecording(currentTime, measurements, currentQuestion, None)
            conductExamScreen.respirationRecordings.append(tempMeasurement)
            measurements = []

        conductExamScreen.separateByQuestion()
        self.assertEqual(len(conductExamScreen.respirationRecordings), 27)
        self.assertEqual(len(conductExamScreen.respirationbyQuestion), 9)
        for y in range(9):
            assert (len(conductExamScreen.respirationbyQuestion[y]) == 3)


if __name__ == '__main__':
    unittest.main()
