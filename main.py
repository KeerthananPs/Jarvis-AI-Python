import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import shutil
import sys


print("""

╱╱╭╮
╱╱┃┃
╱╱┃┣━━┳━┳╮╭┳┳━━╮
╭╮┃┃╭╮┃╭┫╰╯┣┫━━┫
┃╰╯┃╭╮┃┃╰╮╭┫┣━━┃
╰━━┻╯╰┻╯╱╰╯╰┻━━╯
v1.04
by Keerthanan
Virtual Assistant
""")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("how should i help you")

def takeCommand():
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-uk')
        print(f"You Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again....")
        return "None"
    return query

if __name__ == '__main__':
    speak("Iam Jarvis Made bY keerthanan")
    speak("recognizing your os")
    if sys.platform == 'win32':
        speak("You are USING Windows")
    elif sys.platform == mac:
        speak("You are using mac os")
    else:
        speak("you are using linux")

    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('http://google.com')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {strTime}")

        elif 'browser' in query:
            firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefox_path)

        elif 'open minecraft' in query:
            minecraft_path = "C:\\Users\\User\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(minecraft_path)

        elif 'open mail' in query:
            webbrowser.open('https://www.gmail.com/')

        elif 'open code' in query:
            code_path = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Enterprise\\Common7\\IDE\\devenv.exe"
            os.startfile(code_path)

        elif 'open powerpoint' in query:
            powrpnt_path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(powrpnt_path)

        elif 'storage' in query:
            total, used, free = shutil.disk_usage("C:/")

            speak("Storage in Local Disk C")

            store = ("Total: %d Gigs" % (total // (2 ** 30)))
            store2 = ("Used: %d Gigs" % (used // (2 ** 30)))
            store3 = ("Free: %d Gigs" % (free // (2 ** 30)))

            speak(store)
            speak(store2)
            speak(store3)

