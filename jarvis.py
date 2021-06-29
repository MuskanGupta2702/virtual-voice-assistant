# Virtual Voice Assistance
import pyttsx3 #py text to speech version 3
import speech_recognition as sr # to recognize audio and convert to text for further processing
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import smtplib # email
import pywhatkit #youtube music
import pyjokes #jokes
import wolframalpha
import requests
import subprocess
import random
import ctypes
import winshell

from bs4 import BeautifulSoup

try:
    app = wolframalpha.Client("GGQ2W7-WP9QJQT7HA")
except Exception as e:
    print(e)
    print("See your Net Connection")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',170)

d = {'shreya':'manjuchashreya2711@gmail.com','muskan':"muskan80525@gmail.com","hrishita":"hrishitakumar@gmail.com"}
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")
    
    print("I am Jarvis Sir. Please tell me how may I help you?")
    speak("I am Jarvis Sir. Please tell me how may I help you?")
    # speak("Jinu Jinu Jinu. Kya huukuum hai mere aaaka ?")

def takeCommand():
    # It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    f = open("password.txt")
    password = f.read()
    server.login('muskan80525@gmail.com',password)
    server.sendmail('muskan80525@gmail.com',to,content)
    server.close()   
    f.close()

def note(query):
    date = datetime.datetime.now().strftime('%I:%M:%S %p')
    file_name = str(date) + " note.txt"
    with open(file_name, "w") as f:
        f.write(query)
    subprocess.Popen(["notepad.exe", file_name])

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            print("\n")

        elif 'open youtube' in query:
            speak('I am opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('I am opening google')
            webbrowser.open("google.com")

        elif 'open vs code' in query:
            speak('ok sir, I am opening VS code editor')
            code_path = "C:\\Users\\Muskan Gupta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "word" in query:
            speak('ok sir, I am opening Microsoft word')
            code_path = "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE"
            os.startfile(code_path)

        elif "excel" in query:
            speak('ok sir, I am opening Microsoft Excel')
            code_path = "C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE"
            os.startfile(code_path)

        
        elif "note" in query or "remember this" in query:
                speak("What would you like me to write down?")
                note_text = takeCommand()
                note(note_text)
                speak = "I have made a note of that."

        elif 'open stack overflow' in query:
            speak('ok sir, I am opening stack over flow')
            webbrowser.open("stackoverflow.com")

        elif "change background" in query or "change wallpaper" in query:
                img = "C:\\Users\\Muskan Gupta\\Desktop\\Background"
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                print("Background changed successfully")
                speak("Background changed successfully")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M:%S %p')
            print(strTime)
            speak(f"Sir, the time is {strTime}")
            print("\n")

        elif "where is" in query:
                ind = query.lower().split().index("is")
                location = query.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = "This is where " + str(location) + " is."
                webbrowser.open(url)

        # elif 'play music' in query:
        #     music_dir = ""
        #     songs = os.listdir(music_dir)
        #     print(songs,"\n")
        #     os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play music in youtube' in query:
            speak('Which song should i play?')
            query = takeCommand().lower()
            song = query.replace('play','')
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif 'joke' in query:
            speak('Joke for you')
            joke = pyjokes.get_joke()
            print(joke,'\n')
            speak(joke) 

        elif 'send email' in query:
            try:
                query = query.replace("send email to ","")
                to = d[query]               
                speak('What should I write in email?')
                content = takeCommand()
                # to = "manjuchashreya@gmail.com"
                # to = "kkkarun@yahoo.com"
                # to = "hrishitakumar@gmail.com"
                # to = "muskan80525@gmail.com" 
                # to = "kumkum@saxena.ind.in"                

                sendEmail(to,content)
                print('Email has been sent!')
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email.")

        elif 'do my assignment' in query:
            print('Sorry. Its your work so do it on your own!')
            speak('Sorry. Its your work so do it on your own!')

        elif 'temperature' in query or 'weather' in query:
            res = app.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)
        
        elif 'calculator' in query:
            speak('What should I calculate?')
            query = takeCommand().lower()
            res = app.query(query)
            print(f"Answer is {next(res.results).text}")
            speak(f"Answer is {next(res.results).text}")


        elif 'thank you' in query:
            speak('Most Welcome')

        elif 'stop the work' in query or 'bye' in query:
            speak('ok i am stoping the work')
            exit()

        # else:
        #     speak('No match pattern. I will search in google. So Please say again')
        #     query = takeCommand().lower()
        #     url = f"https://www.google.com/search?q={query}"
        #     r = requests.get(url)
        #     data = BeautifulSoup(r.text,"html.parser")
        #     temp = data.find("div",class_="BNeawe").text
        #     print(temp)
        #     speak(temp)

