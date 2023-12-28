import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import datetime
import wolframalpha
import os
import sys
import tkinter
engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('L47KRX-J2X67V5A79')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('SAARA : ' + audio)
    engine.say(audio)
    engine.runAndWait()




def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()



        
