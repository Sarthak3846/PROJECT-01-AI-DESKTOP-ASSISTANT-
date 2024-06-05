import speech_recognition as speech
import os 
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)

def speak(text):
    engine.say(text)        
    engine.runAndWait()

speak("hello")
