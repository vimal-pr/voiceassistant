import pyttsx3
import urllib.request
import os
import time
import pyautogui
import pymsgbox
import keyboard as kb 
import webbrowser
from urllib import request
import json
import winshell
import subprocess

def internet(ping="https://google.com"):
    try:
        urllib.request.urlopen(ping)
        return True
    except:
        return False
    
def speak(text, voice_index=1, rate=160, volume=100.0):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.say(text)
    engine.runAndWait()

def open_notepad():
    os.system('start notepad')

def clear():
    os.system('cls')

def type_data(data):
    os.system('open notepad')
    time.sleep(2)
    pyautogui.typewrite(data)
    x=input("Enter the file name: ")
    kb.press_and_release('ctrl+s')
    pyautogui.typewrite(x)
    kb.press('enter')

def open_google():
    speak("Opening google")
    webbrowser.open_new("https://google.com")

def open_youtube():
    speak("opening youtube")
    webbrowser.open_new("https://youtube.com")

def exit():
    speak("Thankyou for using me")

def news():
    try:
        jsonObj = request.urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
        data = json.load(jsonObj)
        i = 1
        speak('here are some top news from the times of india')
        print('''=============== TIMES OF INDIA ============'''+ '\n')
        for item in data['articles']:
            print(str(i) + '. ' + item['title'] + '\n')
            print(item['description'] + '\n')
            speak(str(i) + '. ' + item['title'] + '\n')
            i += 1
    except Exception as e:
        print(str(e))


def empty_recyclebin():
    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
    speak("Recycle Bin Recycled")
def restart():
    subprocess.call(["shutdown", "/r"])

def logout(sec=10):
    speak(f"Logging of in {sec} seconds")
    time.sleep(sec)
    subprocess.call(["shutdown","/l"])

