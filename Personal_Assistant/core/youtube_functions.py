import keyboard
import webbrowser
import pyttsx3

def speak(data):
    engine=pyttsx3.init()
    engine.say(data)
    engine.runAndWait()

def reload():
    keyboard.press_and_release('F5')
    
def yt_history():
    webbrowser.open_new("https://www.youtube.com/feed/history")

def yt_search(query):
    print(f"Searching for '{query}' on YouTube...")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def yt_open():
    speak("Openning Youtube")
    webbrowser.open_new("https://youtube.com")

def next_video():
    keyboard.press_and_release('shift+N')
    