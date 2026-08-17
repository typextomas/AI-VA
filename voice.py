import os
import pyttsx3
import subprocess

TTS_OUTPUT = "tts.wav"
RVC_OUTPUT = "output.wav"

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, TTS_OUTPUT)
    engine.runAndWait()

def run_rvc():
    command = [
        "python", "rvc/infer.py",
        "--model", "Sinder_2",
        "--input", TTS_OUTPUT,
        "--output", RVC_OUTPUT
    ]
    subprocess.run(command)

def speak_with_rvc(text):
    text_to_speech(text)
    run_rvc()
    os.system(f"start {RVC_OUTPUT}")
