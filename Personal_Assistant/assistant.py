import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import speech_recognition as sr
import tempfile
import os
import webbrowser
import keyboard 
import wikipedia
import datetime
import pyjokes
import ctypes
from core import banner
import mod_installer
from pynput.keyboard import Listener, Key as k
from core.assistant_functions import *n
from core.youtube_functions import *
from core.whatsapp_functions import *
from core.gmail_functions import main


class VoiceAssistant:

    def __init__(self):
        self.fs = 44100  
        self.audio_data = []
        self.stream = sd.InputStream(callback=self.audio_callback,
                                     samplerate=self.fs, channels=1, dtype='float32')
        
    def audio_callback(self, indata, frames, time, status):
        self.audio_data.extend(indata[:, 0])
    
    def process_recording(self):
        try:
            audio_int16 = np.int16(np.array(self.audio_data) * 32767)
            tmpfile = tempfile.mktemp(suffix='.wav')
            write(tmpfile, self.fs, audio_int16)
            recognizer = sr.Recognizer()
            with sr.AudioFile(tmpfile) as source:
                audio_recorded = recognizer.record(source)
                print("Recognizing...")
                query = recognizer.recognize_google(audio_recorded)
                print(f"Recognized query: {query}")
                self.handle_command(query.lower())
        except Exception as e:
            print(f"Could not process audio: {e}")
        finally:
            os.remove(tmpfile)

    def handle_command(self, query):
        query = query.lower()
        
        if 'hello' in query or 'hi' in query:
            speak("Hello! How can I help you?")
            print("Hello! How can I help you?")

        elif 'open youtube' in query:
            yt_open()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'shutdown in' in query:
            query=query.replace('shutdown','')
            query=query.replace('in','')
            query=query.replace('seconds','')
            os.system(f'shutdown /s /t {int(query)}')
            
        elif 'open' in query and ('chrome' in query or 'vscode' in query or 'notepad' in query):
            query = query.replace('open', 'start')
            os.system(query)

        elif 'open file' in query or 'open file explorer' in query:
            keyboard.press_and_release("win+E")
            
        elif 'next song in youtube' in query:
            next_video()
            
        elif 'open youtube history' in query:
            webbrowser.open_new("https://www.youtube.com/feed/history")

        elif 'search' in query and 'in youtube' in query:
            query = query.replace("search", "").replace("in youtube", "")
            yt_search(query)
            
        elif 'open gmail' in query:
            webbrowser.open_new("https://gmail.com")
            
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
            
        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S") 
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
        elif 'joke' in query or 'tell me a joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'write a note' in query or 'create a text file' in query:
            os.system('start notepad')
            
        elif 'search' in query:
            query=query.replace('search','')
            webbrowser.open_new(query) 
            
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
            
        elif "will you be my gf" in query or "will you be my bf" in query: 
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand")
            
        elif 'send a mail' in query or 'send mail' in query:
            main
            
        else:
            speak(f"I'm sorry, I didn't understand the command: {query}")

    def block_space_key(self):
        keyboard.block_key('space')

    def unblock_space_key(self):
        keyboard.unblock_key('space')
      
    def run(self):
        self.block_space_key()
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
        self.unblock_space_key()

    def on_press(self, key1):
        if key1 == k.space and not self.stream.active:
            self.audio_data.clear()
            self.stream.start()
            print("Recording started...")

    def on_release(self, key):
        if key == k.space and self.stream.active:
            self.stream.stop()
            print("Recording stopped.")
            self.process_recording()

if __name__ == "__main__":
    while True:
        if internet():
            print("Internet connection is Available")
            clear()
            print("Installing all required modules/packages")
            time.sleep(1)
            clear()
            mod_installer.run()
            time.sleep(2)
            clear()
            banner.banner("V-ASSISTANT")
            print("Assistant Starts press and release the Space Bar while speaking")
            va = VoiceAssistant()
            va.run()
        else:
            print("Internet Connection is required")
