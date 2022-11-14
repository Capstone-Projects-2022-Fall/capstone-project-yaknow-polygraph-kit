# import PySimpleGUI as sg
# from time import sleep
# import logging
# import datetime
#
# import PolygraphExamSetupScreen
# import IndividualDeviceScreen
#
# import math
# import numpy as np
#
# import time
#
# from scipy.signal import find_peaks
# from gdx import gdx
#
#
#
#
# sg.theme('Dark Blue 3')
#
#
# '''
#     This function shows how to create a custom window with a custom progress bar and then
#     how to update the bar to indicate progress is being made
# '''
#
#
#
# def manually_updated_meter_test():
#     # layout the form
#     layout = [[sg.Text('This meter is manually updated 4 times')],
#               [sg.ProgressBar(max_value=10, orientation='h', size=(20, 20), key='progress')]]
#
#     # create the form`
#     # must finalize since not running an event loop
#     window = sg.Window('Custom Progress Meter', layout, finalize=True)
#
#     # Get the element to make updating easier
#     progress_bar = window['progress']
#     connected = False
#     # theAPIs = gdx()
#     # connected = False
#     # while connected == False:
#     #     devicesFound = theAPIs.open_ble('GDX-BP 141014A2')
#     #     #        devicesFound = theAPIs.open_usb()
#     #     if devicesFound == True:
#     #         connected = True
#     #
#     # theAPIs.select_sensors([1, 7])
#     # theAPIs.start(100)
#     #
#     correctPressure = False
#     while correctPressure == False:
#         measurements = theAPIs.read()
#         print(measurements)
#         # -------------------- Your Program Code --------------------
#         # Spot #1 to indicate progress
#         if measurements[0] > 15:
#             print("you made it to 10 percent")
#             progress_bar.update_bar(1)         # show 10% complete
#             # sleep(2)
#
#
#         if measurements[0] > 30:
#             print("you made it to 20 percent")
#             progress_bar.update_bar(2)         # show 20% complete
#
#             # sleep(2)
#         if measurements[0] > 45:
#             print("you made it to 30 percent")
#             progress_bar.update_bar(3)         # show 30% complete
#             # sleep(2)
#
#         if measurements[0] > 60:
#             print("you made it to 40 percent")
#             progress_bar.update_bar(4)         # show 40% complete
#             # sleep(2)
#         if measurements[0] > 75:
#             print("you made it to 50 percent")
#             progress_bar.update_bar(5)         # show 50% complete
#             # sleep(2)
#
#         if measurements[0] > 90:
#             print("you made it to 60 percent")
#             progress_bar.update_bar(6)         # show 60% complete
#             # sleep(2)
#         if measurements[0] > 105:
#             print("you made it to 70 percent")
#             progress_bar.update_bar(7)         # show 70% complete
#             # sleep(2)
#         if measurements[0] > 120:
#             print("you made it to 80 percent")
#             progress_bar.update_bar(8)         # show 80% complete
#             # sleep(2)
#         if measurements[0] > 135:
#             print("you made it to 90 percent")
#             progress_bar.update_bar(9)         # show 90% complete
#             # sleep(2)
#
#         if measurements[0] > 150:
#             print("you made it to 100 percent")
#             progress_bar.update_bar(10)         # show 100% complete
#             sleep(3)
#             correctPressure = True
#             window.close()
#
#
# theAPIs = gdx()
# connected = False
# while connected == False:
#     devicesFound = theAPIs.open_ble('GDX-BP 141014A2')
#     #        devicesFound = theAPIs.open_usb()
#     if devicesFound == True:
#         connected = True
#
# theAPIs.select_sensors([1, 7])
# theAPIs.start(100)
#
#
# manually_updated_meter_test()
# #custom_meter_example()
#


