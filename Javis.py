import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random


engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour==0 and hour<12:
        speak("good morning")
    elif hour==12 and hour<18:
        speak("Goof Afternoon")
    elif hour ==18 and hour<22:
        speak("Good Evening")
    elif hour ==22 and hour<24:
        speak("Good Night")

    speak("I am savita bhabhi how can i help you lode")

def takecommand():
    #its take microphonr input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining.....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
         print("recognition....")
         query=r.recognize_google(audio,language='en-in')
         print(f"User Said:{query}\n")
    except Exception as e:
        print("Say it again gandu.............")
        return "None"

    return query
if __name__ == '__main__':
    wishme()
    while True:
        speak("How can i help u")
        query=takecommand().lower()
        if 'open googel ' in query:
            webbrowser.open('google.com')

        elif 'open yotube'in query:
            webbrowser.open('youtube.com')

        elif 'open facbook' in query:
            webbrowser.open('facbook.com')

        elif'wikipedia' in query:
            speak("Searching Wikipedia..............")
            query.replace('wekipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open music' in query:
            musicpath="C:\\Users\\Lenovo\\Music"
            songs=os.listdir(musicpath)
            song=random.sample(songs,len(songs))
            print(song)
            os.startfile(os.path.join(musicpath,song[1]))