import pyttsx3
import speech_recognition as sr
from pyttsx3 import Engine
import random
number = random.randint(1111,9999) #Generate a raandom PIN
n=str(number)
file = open("PIN","r+")
file.write(n)
file.close()
file = open("PIN","r")
PIN = file.read()
file.close()
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
        PINAR = r.recognize_google(audioPIN, language="ar-AR") # speech recognition [speech to text]

    except:
        engine.say("حاول مرة أخرى")


if PINAR == PIN:
    engine.say(u"لقد قمت بأدخال رمز القفل الصحيح  نتمنى لك رحلة ممتعة ")
else:
    engine.say(u"الرمز الذي قمت بإدخاله غير صحيح  ")
engine.runAndWait()


