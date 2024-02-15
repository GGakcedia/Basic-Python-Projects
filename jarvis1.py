import speech_recognition as sr
from os import system as comment

r = sr.Recognizer()
with sr.Microphone() as source:
    comment("cls") or comment("clear")
    print("Say something!")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio,language="tr")
    print("You said: " + text )
    
    text = text.lower
except sr.UnknownValueError:
    print("Google speech recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google speech recognition service; {e}")
