import speech_recognition as sr
from webbrowser import *
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)  
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)
    print("You said: ", text)
    text=text.lower()
    if text=="open youtube":
        open("www.youtube.com")
    elif text=="open gpt":
        open("www.chatgpt.com")
    elif text=="open google":
        open("www.google.com")
    elif text=="open game":
        open("https://smashkarts.io/")
