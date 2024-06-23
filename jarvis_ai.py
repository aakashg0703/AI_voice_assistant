import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyaudio

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 5:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("I am jarvis. How may I help you?")


def takeCommand():
    # It takes voice input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        # print(e)
        print("Please say that again!")
        return "None"
    return query


if __name__ == '__main__':

    speak("Hello")
    wishme()
    while True:
        query = takeCommand().lower()
        # Logic for executing task based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipdeia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak( strTime)
        elif "open word" in query:
            wordpath = "C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE"
            os.startfile(wordpath)
        elif "stop" in query:
            exit()
        elif "band ho ja" in query:
            exit()
        elif "exit" in query:
            exit()
