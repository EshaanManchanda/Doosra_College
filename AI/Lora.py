import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour>=12:
        speak("Good morning sir ")
    elif hour<=12 and hour>-18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening")
    speak("good evening sir  . Please Tell me how may help you ")


def takequery():
    # it takes microphone input and string output
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("listing......")
        r.pause_threshold=1
        audio = r.listen(source,timeout=5,phrase_time_limit=20)

    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language="en-in")
        print(f'User said : {query} \n')
    except Exception as e:
        print(e)
        print("somthing wrong...say again...")
        return "None"
    return query
if __name__ == "__main__":
    speak("hello sir i am ready for your help")
    wishme()
    while  True:
        Quit=["stop","quit","ruck jao"]
        query=takequery().lower()
        if 'wikipedia'in query:
            speak("Searching....")
            print("Searching....")
            query=query.replace("wikipedia"," ")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak("According to wikipedia..")
            speak(result)
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
        elif 'open google'in query:
            webbrowser.open("google.com")
        elif 'play english song' in query:
            music_dir = 'E:\\music\\0010English song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play punjabi song' in query:
            music_dir = 'E:\\music\\004 Punjabi song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play hindi song' in query:
            music_dir = 'E:\\music\\007 HINDI DJ'
            songs = os.listdir(music_dir)
            # print(songs)
            # hindi=str(random.choice(songs))
            # print(hindi)
            os.startfile(os.path.join(music_dir, songs[0]))
        # elif Quit in query:
        #     quit()

        else:
            quit()