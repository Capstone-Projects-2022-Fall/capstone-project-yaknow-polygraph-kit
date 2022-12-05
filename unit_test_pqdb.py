import unittest
import database

class TestProblematicQuestionDatabase(unittest.TestCase):

    def test_search_question_from_database(self):
        message = 'question was not found in database'
        # should return True if ' is the sky blue? \n' is found in database after sanitizing it
        self.assertTrue(database.search_question_from_database(' is the sky blue? \n'), message)

    def test_select_question_from_database(self):
        # the pre_defined_list is the expected result of running the select_question_from_database function
        # with the user input being 41 for 'is your name riley', 33 for 'is your favorite color purple?',
        # and 5 for 'are you happy?'
        pre_defined_list = ['is your name riley?', 'is your favorite color purple?', 'are you happy?']
        # should return Equality according to the pre_defined_list and pre-defined user input [41, 33, 5]
        self.assertEqual(pre_defined_list, database.select_question_from_database(), 'pre_defined_list is not equal to list returned from function')

    def test_add_new_question_to_database(self):
        # should return True if 'something unique 123?' was added and found in database
        self.assertTrue(database.add_new_question_to_database('something unique 123?'))
        print('before')
        print(database.get_questions())
        # delete the string 'something unique 123?' for future test to work as intended, which is to add that
        # string to the database and check if found (True) in database
        database.delete_question('something unique 123?')
        print('after')
        print(database.get_questions())