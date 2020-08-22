import pyttsx3
import speech_recognition as sr
from pyttsx3 import Engine
ar_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_arSA_NaayfM'
engine: Engine = pyttsx3.init()
engine.setProperty("rate", 190)
engine.setProperty('voice', ar_voice_id)  # To set a speaker language into Arabic language
engine.say(u"مَرحبًا بِك    فضلًا قُم بِإدخال رمز القُفل ") # Speech synthesis [text to speech]
engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    audioPIN = r.listen(source)
    try:
        PINAR = r.recognize_google(audioPIN, language="ar-AR") #speech recognition [speech to text]
        print(PINAR)
    except:
        print("حاول مرة أخرى")