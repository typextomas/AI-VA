from brain import think
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    text = input("You: ")
    if text.lower() == "exit":
        break

    reply = think(text)
    print("Assistant:", reply)
    speak(reply)
