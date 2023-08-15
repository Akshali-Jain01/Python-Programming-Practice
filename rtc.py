import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import webbrowser
import wikipedia
from  random import *
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# print(speak())

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# speak(" hELLO SJDFHJDSK,SD IFUSD. DIEH FIE")
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    elif hour>=16 and hour<=23:
        speak("Good Evening")
# wishMe()
def takeCommand():
    r = sr.Recognizer() 
    # r is a object that takes input from user in micropohone
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        print(audio)
        print("recogining")
        line = r.recognize_google(audio,language="en-in")
        print(line)
        speak(line)
    return line
        # print(r.recognize_google(audio)) -- speech to text using python

# takeCommand()
if __name__ =="__main__":
    while 1:
        query=takeCommand().lower()
        print(f"user said :{query}")
        speak(f"user said :{query}")
        if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir =f"E:\VR 0.4\Assets\SlimUI"
            songs = os.listdir(music_dir)
            print(songs)
            r = randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[r]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,time is {strtime}")


