from logging import exception
from bs4 import BeautifulSoup
import pyttsx3
import requests 
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import pywhatkit 
import time
import wikipedia
from googlesearch import search
import smtplib
import pyautogui
import pyjokes
import subprocess
import numpy as np
import cv2
import face_recognition


alarms = {
  0:[14,15,"i"],
  1:[9,21,"i"]  
  }

functions_list = ["playsound('mmusic2.mp3')","playsound('mmusic1.mp3')"]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        print("Good Morning.")
        speak("Good Morning.")
        print(f" it's {tt}")  
        speak(f" it's {tt}")

    elif hour>=12 and hour<18:
        print("Good Afternoon.")
        speak("Good Afternoon.")
        print(f" it's {tt}")  
        speak(f" it's {tt}")

    else:
        print("Good Evening.")
        speak("Good Evening.")
        print(f" it's {tt}")  
        speak(f" it's {tt}")
        
    print("welcome back sir ,  all functions of edith   are on , you can grab a cup of tea")
    speak("welcome back sir ,  all functions of edith  are on  , you can grab a cup of tea")
           

def face_unlock():
    video_capture = cv2.VideoCapture(0)
    obama_image = face_recognition.load_image_file("WIN_20210602_11_59_44_Pro.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    known_face_encodings = [
        obama_face_encoding
    ]
    known_face_names = [
        "vishnu"
    ]
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    i = 0
    while i <=80:
        ret , frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                face_names.append(name)

        process_this_frame = not process_this_frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if i ==60:
            if "vishnu" not in face_names:
                print("no you are not vishnu sir")
                speak("no you are not vishnu sir , i can't give access of me to you")
                time.sleep(1)
                return "n"
            else:
                video_capture.release()
                cv2.destroyAllWindows()
                return "y"     
        i+=1
    video_capture.release()
    cv2.destroyAllWindows()
    return "y"

def takeCommand():
    i = 0 
    #It takes microphone input from the user and returns string output
    while i == 0:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            alaram(alarms)
            r.pause_threshold = 1
            audio = r.listen(source)
            
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            i+=1

        except Exception as e:
            # print(e)
            continue      
    if i > 0:        
        return query.lower()
def takeCommandm():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...text")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...text")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  
    except Exception as e:
        return "hello"              
    return query       
      
def send_email(email,message):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chityala.vishnu.ramu@gmail.com', 'vishnu1234')
    server.sendmail('chityala.vishnu.ramu@gmail.com', email, message)
    server.close()
def alaram(alarms):
    i = 0
    while i < len(alarms):
      current_hour = datetime.datetime.now().hour
      current_min = datetime.datetime.now().minute
      if current_hour == alarms[i][0]:
        if current_min == alarms[i][1]:
          if "i" ==  alarms[i][2]:
            os.startfile("D:\my_playlist\Machayenge 3 - Emiway Bantai.mp3")
            alarms[i] = [current_hour,current_min,"n"]
            i+=1
            return "w"
      else:
        i+=1

contacts = {"aakash":"+919825111444","kaveri":"+919687000333","papa":"+919898510127","uncle":"+919825759759","mom":"+916353255682","tulsi":"+919510756465","brother":"+919603816010"}
emails = {"aakash":"aakash.chityala@gmail.com","papa":"ramuvchityala@gmail.com","uncle":"Mohan@siliconinfovision.com","brother":"pavankandagatla26@gmail.com"}


def sleep():
    zl = 0
    while zl == 0  :
        vpermission = takeCommand()
        alaram(alarms)
        if vpermission in "wake up" :
            task_execution()

def task_execution():
    verify = face_unlock()

    if verify == "y":
        alaram(alarms)
        wishMe()
        loop = 0
        while loop == 0 :

            alaram(alarms)
            query = takeCommand()

            if 'open youtube' in query:
                webbrowser.open("www.youtube.com")

            elif 'open google' in query:
                webbrowser.open("www.google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("www.stackoverflow.com") 

            elif 'play my song' in query or "play my playlist" in query:
                n = random.randint(0,3)
                my_music = "D:\my_playlist"
                songs = os.listdir(my_music) 
                os.startfile(os.path.join(my_music,songs[n]))

            elif "play song" in query :
                try:
                    speak("which song do you want to play")
                    print("which song do you want to play")
                    song_name = takeCommand()
                    result =  search(song_name)
                    webbrowser.open(result[0])
                except Exception as e :
                    print("sorry sir i can't find your song!!")
                    speak("sorry sir i can't find your song!!")

            elif "what is"in query and "your creator"not in query or "who is" in query and "your creator" not in query : 
                if "time now" not in query:#problem   
                    answer = wikipedia.summary(query,2) 
                    print(f"{answer}")
                    speak(f"{answer}")
            
            elif "tell me something about" in query:
                question = " "
                for i in query.split() :
                    if  i not in "tell me something about":
                        question+=question + i
                result = wikipedia.summary(query,2)
                print(result)
                speak(result)          

            elif "message" in query:
                speak("please speak name of contact")
                name = takeCommand().lower()
                if name not in contacts.keys():
                    print("thier is no such contact")
                    speak('thier no such contact')
                else:
                    speak("what is your message")
                    print("what is your message")
                    message = takeCommandm()
                    number = contacts[name]
                    pywhatkit.sendwhatmsg_instantly(number,message,10)

            elif "send email" in query :
                speak("what is name of email contact")
                print("what is name of email  :")
                name = takeCommand().lower() 
                if name not in emails.keys():
                    speak("there is no such email contact")
                    print("there is no such email contact")
                else:
                    speak("what is your message")
                    print("what is your message :")
                    message = takeCommand()
                    send_email(emails[name],message)

            elif "you can sleep" in query :
                print("sir have a nice day , i wish your day will be good without me ")
                speak("sir have a nice day , i wish your day will be good without me ")
                sleep()

            elif "close google" in query:#incomplete
                print("okay sir closing google")    
                speak("okay sir closing google")
                os.system("TASKKILL /F / im chrome.exe")    

  
            elif "how are you" in  query:
                print("i am fine sir")
                speak("i am fine sir")

            elif "what are you doing" in query:
                print("just thinking what can i do for you")
                speak("just thinking what can i do for you")

            elif "time now" in query: 
                tt = time.strftime("%I:%M %p")
                print(f"current time is {tt}")
                speak(f"current time is {tt}")

            elif "tell me your name" in query :
                print("my name is edith , i am an small ai , fullform  ,even dead i am the hero")                  
                speak("my name is edith , i am an small ai , fullform  ,even dead i am the hero")
        
            elif "how is weather" in query or "weather forecast" in query :
                search = "tempratue in surat"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser") 
                temp = data.find("div",class_="BNeawe").text 
                speak(f"current {search} is {temp}")

            elif "volume up" in query :
                pyautogui.press("volumeup")

            elif "volume down" in query:
                pyautogui.press("volumedown")

            elif "mute sound" in query:
                pyautogui.press("volumemute")

            elif "unmute sound" in query:
                pyautogui.press("volumeunmute")

            elif "make me laugh" in query or "make me laugh please" in query :
                print("there is one joke for you sir")
                speak("there is one joke for you sir")
                print(pyjokes.get_joke())
                speak(pyjokes.get_joke())
            
            elif "what should i do" in query:
                print("sir you should do your study without wasting time")
                speak("sir you should do your study without wasting time")

            elif "your creator" in query:
                print("sir my creator is vishnu and aakash")
                speak("sir my creator is vishnu and aakash")

            elif "which company owns you" in query:
                print("silicon infovision private limited owns me")
                speak("silicon infovision private limited owns me")

            elif "what can you do" in query :
                print("i can do various of task like , telling a joke , creating an alaram , giving every information which is possible")
                speak("i can do various of task like , telling a joke , creating an alaram , giving every information which is possible")

            elif "sing a song" in query :
                webbrowser.open_new_tab("https://www.youtube.com/watch?v=nLnp0tpZ0ok")

            elif "open wikipedia of" in query:
                result = wikipedia.summary(query, sentences=2) 
                print(result)
                speak(result)
            elif "what is your name" in query :
                print("my name is jarvis")    
task_execution()