import PySimpleGUI as sg
from gtts import gTTS
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
# try to remove the temp files. You'll likely be left with 1 to clean up


def questionToSpeech(question, counter):
    mixer.init()
    tts = gTTS(text=question, lang='en', slow=False)
    tts.save('speech{}.mp3'.format(counter % 2))
    # playback the speech
    mixer.music.load('speech{}.mp3'.format(counter % 2))
    mixer.music.play()
    #time.sleep(2)
    mixer.stop()
    #try:
    #    os.remove('speech{}.mp3'.format(counter % 2))
    #    print("Removed")
    #except Exception as e:
    #    print(e)
    #    pass

