import pyttsx3
import speech_recognition as sr
from pyttsx3 import Engine
import random
number = random.randint(1111,9999) #Generate a raandom PIN
n=str(number)
file = open("PIN2","w")
file.write(n)
file.close()
file = open("PIN2","r")
PINen = file.read(4)
file.close()
engine: Engine = pyttsx3.init()
engine.setProperty("rate", 190)
engine.say("Welcome ,        please Enter the PIN") # Speech synthesis [text to speech]
engine.runAndWait()
r = sr.Recognizer()
with sr.Microphone() as source:
    audioPINENG = r.listen(source)
    try:
        PIN = r.recognize_google(audioPINENG)


    except:
        engine.say("Error..TRY AGAIN ")

if PIN == PINen:
    engine.say("You entered the right PIN, we wish to you have  pleasant trip.")   # speech recognition [speech to text]
else:
    engine.say("The PIN you entered is incorrect")
engine.runAndWait()
