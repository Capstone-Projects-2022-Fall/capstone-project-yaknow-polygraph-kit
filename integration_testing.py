import pyautogui
import os
import time
import unittest

import database


def integration_testing():
    # Test Case 1
    # start the homescreen module
    os.system('python3 homescreen.py &')
    # wait 9 seconds, give some time for screen to load
    time.sleep(9)
    cpeb = pyautogui.locateCenterOnScreen('conduct_polygraph_exam_button.png')
    # conditional statement to see if conduct polygraph exam button exists on screen,
    # if not return False, break out of function
    if cpeb == None:
        return False

    # move the mouse to cpeb
    pyautogui.moveTo(cpeb.x / 2, cpeb.y / 2)

    # click conduct polygraph exam button
    pyautogui.click()

    # Test Case 2
    # should be in polygraph exam setup page
    time.sleep(9)
    af = pyautogui.locateCenterOnScreen('add_functionality.png')
    if af == None:
        return False
    pyautogui.moveTo(af.x / 2, af.y / 2)
    pyautogui.click()
    pyautogui.typewrite('hello world?')

    # locate the add button
    add_button = pyautogui.locateCenterOnScreen('add_to_database_button.png')
    if add_button == None:
        return False
    pyautogui.moveTo(add_button.x / 2, add_button.y /2)
    pyautogui.click()

    # locate the search functionality input box
    search_input_box = pyautogui.locateCenterOnScreen('search_functionality.png')
    if search_input_box == None:
        return False
    pyautogui.moveTo(search_input_box.x / 2, search_input_box.y / 2)
    pyautogui.click()
    pyautogui.typewrite('hello world?')

    # Test Case 4 (testing select functionality)
    # locate select functionality and select a question
    select_mode = pyautogui.locateCenterOnScreen('select_mode.png')
    if select_mode == None:
        return False
    pyautogui.moveTo(select_mode.x / 2, select_mode.y / 2)
    pyautogui.click()
    time.sleep(3)

    # Test Case 3
    # locate the start examination button
    start_examination_button = pyautogui.locateCenterOnScreen('start_examination_button.png')
    if start_examination_button == None:
        return False
    pyautogui.moveTo(start_examination_button.x / 2, start_examination_button.y / 2)
    pyautogui.click()

    # wait 9 seconds, give some time for screen to load
    time.sleep(3)
    # locate the first question 'hello world?' on conduct exam screen page
    hello_world = pyautogui.locateCenterOnScreen('hello_world.png')
    if hello_world == None:
        return False
    pyautogui.moveTo(hello_world.x / 2, hello_world.y / 2)

    # delete 'hello world?' from database for future test use
    database.delete_question('hello world?')

    # locate the close button
    close_button = pyautogui.locateCenterOnScreen('close.png')
    if close_button == None:
        return False
    pyautogui.moveTo(close_button.x / 2, close_button.y / 2)
    pyautogui.click()

    # start the conductExamScreenEndTest module
    os.system('Python3 conductExamScreenEndTest.py &')
    # wait for 9 seconds, give some time for module to load
    time.sleep(9)

    # Test Case 5
    # locate the graph
    data_collected = pyautogui.locateCenterOnScreen('data_collected.png')
    if data_collected == None:
        return False
    pyautogui.moveTo(data_collected.x / 2, data_collected.y / 2)
    time.sleep(3)

    # locate the respiration button
    respiration_button = pyautogui.locateCenterOnScreen('respiration_button.png')
    if respiration_button == None:
        return False
    pyautogui.moveTo(respiration_button.x / 2, respiration_button.y /2)
    time.sleep(3)

    # locate the gsr button
    gsr_button = pyautogui.locateCenterOnScreen('gsr_button.png')
    if gsr_button == None:
        return False
    pyautogui.moveTo(gsr_button.x / 2, gsr_button.y / 2)
    time.sleep(3)

    # locate the cuff pressure
    cuff_pressure = pyautogui.locateCenterOnScreen('cuff_pressure.png')
    if cuff_pressure == None:
        return False
    pyautogui.moveTo(cuff_pressure.x / 2, cuff_pressure.y / 2)
    pyautogui.click()
    time.sleep(3)

    # go into full screen mode
    pyautogui.keyDown('fn')
    pyautogui.press('F')

    time.sleep(4)
    # Test Case 6
    # locate the restart button
    restart_button = pyautogui.locateCenterOnScreen('restart_button.png')
    if restart_button == None:
        return False
    pyautogui.moveTo(restart_button.x / 2, restart_button.y / 2)
    pyautogui.click()
    time.sleep(15)

    return True

class IntegrationTests(unittest.TestCase):

    def test_integration_testing(self):
        # if True return then we've reached the end
        self.assertTrue(integration_testing())
        #integration_testing()

if __name__ == '__main__':
    unittest.main()