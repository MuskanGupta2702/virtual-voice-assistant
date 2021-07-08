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
import sys
import time
import calendar

from bs4 import BeautifulSoup

# GUI

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

from PyQt5.uic import loadUiType
from voiceAssistant import Ui_Form

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

d = { 'shreya':'manjuchashreya2711@gmail.com','muskan':"muskan80525@gmail.com",
"hrishita":"hrishitakumar@gmail.com",'teacher':'kumkum@saxena.ind.in','sir':'kkkarun@yahoo.com','rashid':'md.r.a.n.786@gmail.com',
'daddy':'kamlesh.gupta@alembic.co.in','bharati':'bharatipanigrahi9901@gmail.com','saima':'saimarshk@gmail.com','ankit':'Ankit04092000.ap@gmail.com',
'dhiraj':'lalwanidheeraj1234@gmail.com'}

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
    # self.speak("Jinu Jinu Jinu. Kya huukuum hai mere aaaka ?")


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    f = open("password.txt")
    password = f.read()
    server.login('your_mail_id',password)
    server.sendmail('your_mail_id',to,content)
    server.close()   
    f.close()

def note(query):
    date = datetime.datetime.now().strftime('%I:%M:%S %p')
    file_name = str(date).replace(":","-") + " note.txt"
    with open(file_name, "w") as f:
        f.write(query)
    subprocess.Popen(["notepad.exe", file_name])

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.taskExecution()

    def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()

    def takeCommand(self):
        # It takes microphone input from user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return self.query

    def taskExecution(self):
        wishMe()
        while True:
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on self.query
            if 'wikipedia' in self.query:
                self.speak("Searching Wikipedia...")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query,sentences=2)
                self.speak("According to Wikipedia")
                print(results)
                self.speak(results)
                print("\n")

            elif 'open youtube' in self.query:
                self.speak('I am opening youtube')
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                self.speak('I am opening google')
                webbrowser.open("google.com")

            elif 'open vs code' in self.query:
                self.speak('ok sir, I am opening VS code editor')
                code_path = "C:\\Users\\Muskan Gupta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)

            elif "word" in self.query:
                self.speak('ok sir, I am opening Microsoft word')
                code_path = "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE"
                os.startfile(code_path)

            elif "excel" in self.query:
                self.speak('ok sir, I am opening Microsoft Excel')
                code_path = "C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE"
                os.startfile(code_path)

            elif 'what' in self.query:
                print('''
               1. I can tell you the time.
               2. I can tell you the temperature.
               3. I can work as a calculator.
               4. I can make a note for you in notepad.
               5. I can open various websites like google, stackoverflow, YouTube, etc.
               6. I can open various desktop applications like Microsoft word, excel, VS code editor.
               7. I can change Background of your Desktop that is wallpaper.
               8. Can tell location of any place by opening Google maps.
               9. I can send emails on your behalf.
               10.Can play Music in YouTube.
               11.Can entertain you by telling Jokes.
               12.Can pause or sleep for some time.
               13.Stop the work when said.  ''')
                self.speak('''
               1. I can tell you the time.
               2. I can tell you the temperature.
               3. I can work as a calculator.
               4. I can make a note for you in notepad.
               5. I can open various websites like google, stackoverflow, YouTube, etc.
               6. I can open various desktop applications like Microsoft word, excel, VS code editor.
               7. I can change Background of your Desktop that is wallpaper.
               8. Can tell location of any place by opening Google maps.
               9. I can send emails on your behalf.
               10.Can play Music in YouTube.
               11.Can entertain you by telling Jokes.
               12.Can pause or sleep for some time.
               13.Stop the work when said.  ''')
            
            elif 'calendar' in self.query:
                year = 2021
                month = 5
                print(calendar.month(year,month))

            elif "note" in self.query or "remember this" in self.query:
                    self.speak("What would you like me to write down?")
                    note_text = self.takeCommand()
                    note(note_text)
                    self.speak("I have made a note of that.")

            elif 'open stack overflow' in self.query:
                self.speak('ok sir, I am opening stack over flow')
                webbrowser.open("stackoverflow.com")

            elif "change background" in self.query or "change wallpaper" in self.query:
                    img = "C:\\Users\\Muskan Gupta\\Desktop\\Background"
                    list_img = os.listdir(img)
                    imgChoice = random.choice(list_img)
                    randomImg = os.path.join(img, imgChoice)
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                    print("Background changed successfully")
                    self.speak("Background changed successfully")

            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime('%I:%M:%S %p')
                print(strTime)
                self.speak(f"Sir, the time is {strTime}")
                print("\n")

            elif "where is" in self.query:
                    ind = self.query.lower().split().index("is")
                    location = self.query.split()[ind + 1:]
                    url = "https://www.google.com/maps/place/" + "".join(location)
                    self.speak = "This is where " + str(location) + " is."
                    webbrowser.open(url)

            elif 'joke' in self.query:
                self.speak('Joke for you')
                joke = pyjokes.get_joke()
                print(joke,'\n')
                self.speak(joke) 

            elif 'send email' in self.query:
                try:
                    self.query = self.query.replace("send email to ","")
                    to = d[self.query]               
                    self.speak('What should I write in email?')
                    content = self.takeCommand()
                    # to = "manjuchashreya@gmail.com"
                    # to = "kkkarun@yahoo.com"
                    # to = "hrishitakumar@gmail.com"
                    # to = "muskan80525@gmail.com" 
                    # to = "kumkum@saxena.ind.in"                

                    sendEmail(to,content)
                    print('Email has been sent!')
                    self.speak('Email has been sent!')
                except Exception as e:
                    print(e)
                    self.speak("Sorry my friend. I am not able to send this email.")

            elif 'do my assignment' in self.query:
                print('Sorry. Its your work so do it on your own!')
                self.speak('Sorry. Its your work so do it on your own!')

            elif 'temperature' in self.query or 'weather' in self.query:
                url = f"https://www.google.com/search?q={self.query}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                print(temp)
                speak(temp)
                # res = app.self.query(self.query)
                # print(next(res.results).text)
                # self.speak(next(res.results).text)
            
            elif 'calculator' in self.query:
                self.speak('What should I calculate?')
                self.query = self.takeCommand().lower()
                try:
                    app = wolframalpha.Client("GGQ2W7-WP9QJQT7HA")
                except Exception as e:
                    print(e)
                    print("See your Net Connection")
                res = app.query(self.query)
                print(f"Answer is {next(res.results).text}")
                self.speak(f"Answer is {next(res.results).text}")

            elif 'thank you' in self.query:
                self.speak('Most Welcome')

            elif 'stop the work' in self.query or 'bye' in self.query:
                self.speak('ok i am stoping the work')
                exit()

            elif 'play music in youtube' in self.query:
                self.speak('Which song should i play?')
                self.query = self.takeCommand().lower()
                song = self.query.replace('play','')
                self.speak('playing' + song)
                pywhatkit.playonyt(song)

            elif "don't listen" in self.query or "stop listening" in self.query or "do not listen" in self.query:
                self.speak("for how many seconds do you want me to sleep")
                try:
                    a = int(self.takeCommand().lower())
                    time.sleep(a)
                    self.speak(f"{str(a)} seconds completed. Now you can ask me anything")
                except Exception as e:
                    print(e)
                    self.speak("Please give numberic value only")


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self) #To display the GUI
        self.ui.pushButton1.clicked.connect(self.startTask)
        # self.ui.pushButton1.clicked.connect(self.showTime)
        self.ui.pushButton2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("background.gif")
        self.ui.background.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time=QTime.currentTime() 
        current_date=QDate.currentDate() 
        label_time=current_time.toString('hh:mm:ss') 
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        while True:
            QApplication.processEvents()
            dt = datetime.datetime.now()
            self.ui.textBrowser.setText('Date:- %s-%s-%s' % (dt.day, dt.month, dt.year))
            self.ui.textBrowser_2.setText('Time:- %s:%s:%s' % (dt.hour,dt.minute,dt.second))
    
startExecution = MainThread()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    jarvis=Main()
    jarvis.show()
    exit(app.exec_())
   
