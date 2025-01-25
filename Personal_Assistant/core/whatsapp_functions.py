import keyboard
import speech_recognition as sr
import pyttsx3
import getpass
import webbrowser
from core.assistant_functions import *
import os
import time
import pyautogui


def gm_home():
    images_to_click = [
    "img/whatsapp/gm_home.png"
    ]
    time.sleep(5)
    for image in images_to_click:
        try:
            image_location = pyautogui.locateCenterOnScreen(image,confidence=0.9)
            if image_location:
                pyautogui.click(image_location)
                print(f"Clicked on {image}")
                break 
        except pyautogui.ImageNotFoundException as e:
            print(f"Error:",e)


def open_web_whatsapp():
    if internet():
        webbrowser.urlopen("https://web.whatsapp.com")
        

def wp_new_chat():
    images_to_click = [
    "img/whatsapp/new_chat.png"
    ]
    time.sleep(5)
    for image in images_to_click:
        try:
            image_location = pyautogui.locateCenterOnScreen(image,confidence=0.9)
            if image_location:
                pyautogui.click(image_location)
                print(f"Clicked on {image}")
                break 
        except pyautogui.ImageNotFoundException as e:
            print(f"Error:",e)

