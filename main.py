import os
import eel
from engine.features import *
from engine.command import *
from engine.auth import recoganize


def start():

    eel.init('www')

    playAssistantSound()
    @eel.expose
    def init():
        #subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Welcome My Lord, Please Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Recognized Successfully. Hello My Creator Spidey Sir How can I help you today?")
            eel.hideFaceAuthSuccess()
            speak("Spidey At your Service")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Not Recognized. Access Denied. Please Try Again.")
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    
    eel.start('index.html', mode=None, host='localhost', block=True)