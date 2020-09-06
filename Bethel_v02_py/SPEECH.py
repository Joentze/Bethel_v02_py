
import pyttsx3 as voice

def say(stringToSpeak):
    engine = voice.init()
    engine.say(stringToSpeak)
    engine.runAndWait()
