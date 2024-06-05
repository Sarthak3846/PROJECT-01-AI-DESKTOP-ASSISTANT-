import speech_recognition as speech
import os 
import pyttsx3
import datetime 
from AppOpener import open
import  wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)

def speak(text):
    engine.say(text)        
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    else:
        speak("Good Evening sir!")

def takeCommand():
    r= speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Interpreting...")
        speak("Interpreting...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Please say that again")
        speak("Please say that again...")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your@gmail.com','password')
    server.sendmail('your@gmail.com',to,content)

while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak("searching in wikipedia..")
        query=query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("Accoding to the information available on wikipedia..")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open instagram' in query:
        webbrowser.open("instagram.com")
    elif "send email to sarthak" in query:
        try:
            speak("what should i say?")
            content = takeCommand()
            to = "sarthaktyagi3846@gmail.com"
            sendEmail(to, content)
            speak("email has been sent successfully")
        except Exception as e:
            print(e)
            speak("sorry i am unable to send this email.")

speak("hello my name is siri")
wish()
takeCommand()