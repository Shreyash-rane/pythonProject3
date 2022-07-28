import datetime
import pyttsx3

engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")

engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def entry():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("Good Morning Sir. You are on a morning shift.")
    if time>=12 and time <15:
        speak("Good Afternoon Sir .You are on mid shift.")
    if time>=15 and time<20:
        speak("Good Evening Sir. You are late for mid shift.")
    if time>=20 and time<=24:
        speak("You are doing night shift. Drink Your Coffee.")

    speak("Anything else u want to ask.I can't be able to answer because for that code is incomplete ... Sorry.")
entry()
