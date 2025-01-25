import keyboard
import speech_recognition as sr
import pyttsx3
import getpass
import webbrowser
import time
import pyautogui

def gm_home():
    images_to_click = [
    "img/gmail/gm_home.png"
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

def gm_compose():
    images_to_click = [
    "img/gmail/gm_compose.png"
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
            

def gm_to(email):
    images_to_click = [
    "img/gmail/gm_to.png"
    ]
    time.sleep(5)
    for image in images_to_click:
        try:
            image_location = pyautogui.locateCenterOnScreen(image,confidence=0.9)

            if image_location:
                pyautogui.click(image_location)
                print(f"Clicked on {image}")
                pyautogui.typewrite(email)
                keyboard.press_and_release('enter')
                break 
            else:
                pyautogui.click(x=1215, y=473)
                pyautogui.typewrite(email)
                keyboard.press_and_release('enter')
                
        except pyautogui.ImageNotFoundException as e:
            print(f"Error:",e)



def gm_subject(text):
    images_to_click = [
    "img/gmail/gm_subject.png"
    ]
    time.sleep(5)
    for image in images_to_click:
        try:
            image_location = pyautogui.locateCenterOnScreen(image,confidence=0.9)

            if image_location:
                pyautogui.click(image_location)
                print(f"Clicked on {image}")
                pyautogui.typewrite(text)
                keyboard.press_and_release('enter')
                message_1()
                break 
        except pyautogui.ImageNotFoundException as e:
            print(f"Error:",e)



def gm_send():
    images_to_click = [
    "img/gmail/gm_send.png"
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

def message_1():
    keyboard.press_and_release('tab')
    pyautogui.typewrite("This is a empty message")

def main(to, subject, message):
    webbrowser.open_new("https://gmail.com")
    time.sleep(6)
    gm_compose()
    time.sleep(4)
    gm_to(to)
    time.sleep(3)
    gm_subject(subject)
    time.sleep(4)
    gm_send()

    