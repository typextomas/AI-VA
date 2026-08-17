from brain import think
from voice import speak

while True:
    text = input("You: ")
    if text.lower() == "exit":
        break

    reply = think(text)
    print("AI:", reply)
    speak(reply)
