import os
import urllib.request


def internet(ping="https://google.com"):
    try:
        urllib.request.urlopen(ping)
        return True
    except:
        return False
    
def run():
    if internet():
        pip_upgrade = 'python.exe -m pip install pip --upgrade'

        modules =' numpy scipy sounddevice speechrecognition pynput keyboard wikipedia pyjokes pyttsx3 pyautogui pymsgbox winshell pyfiglet'

        print("upgrading pip")
        os.system(pip_upgrade)
        print("Installing Required Modules")
        os.system(f'python.exe -m pip install {modules}')
        
        

        