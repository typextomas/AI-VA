AI Voice Assistant

A Python-based AI voice assistant that combines a Large Language Model with text-to-speech and voice conversion technologies to create an interactive conversational experience.

Features
AI-powered conversations using the Groq API
LLM integration with llama-3.1-8b-instant
Text-to-Speech using pyttsx3
Voice conversion using RVC
Modular architecture separating AI processing and voice functionality
Conversation context maintained during the session

Technologies
Python
Groq API
Llama 3.1 8B Instant
pyttsx3
RVC (Retrieval-based Voice Conversion)
Python subprocess and os modules

Project Structure
project/
│
├── brain.py          # AI processing and Groq API integration
├── voice.py          # Text-to-speech functionality
├── main.py           # Main application loop
├── test_brain.py     # Testing
├── rvc/              # RVC voice conversion components
└── README.md

How It Works

The assistant is divided into several components.

1. AI Processing

The brain.py module handles communication with the Groq API.

User messages are added to the conversation history and sent to the language model. The assistant's response is then returned and stored in the conversation history.

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=messages
)
2. Text-to-Speech

The voice.py module converts the AI's text response into speech using pyttsx3.

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
3. Voice Conversion

An experimental voice-conversion pipeline uses RVC to process the generated speech.

The project first generates a .wav file and then runs the RVC inference script to produce the converted voice.

AI response
     ↓
Text-to-Speech
     ↓
tts.wav
     ↓
RVC
     ↓
output.wav
     ↓
Audio playback

Getting Started
Prerequisites
Python 3.x
A Groq API key
The required Python packages
RVC installed and configured if voice conversion is enabled
Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY

Install the required dependencies:

pip install -r requirements.txt

Set your Groq API key as an environment variable:

set GROQ_API_KEY=your_api_key

Never commit your API key to GitHub.

Running the Assistant

Run the main program:

python main.py

Type a message and the assistant will generate an AI response and convert it to speech.

To stop the program:

exit

Architecture

The project uses separate modules for its main responsibilities:

                 ┌───────────────┐
                 │    main.py    │
                 │ User Interface│
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   brain.py    │
                 │   Groq / LLM  │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   voice.py    │
                 │     TTS       │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │      RVC      │
                 │ Voice Convert │
                 └───────────────┘

This structure makes it easier to modify individual components without changing the entire application.

Future Improvements

Possible improvements for future versions include:

Speech-to-text input

Continuous voice interaction

Improved conversation memory

Graphical user interface

Better error handling

Configuration file for model and voice settings

Cross-platform support

More advanced voice customization

Performance optimization


What I Learned

This project has allowed me to explore:

Python application development
Working with external APIs
Integration of Large Language Models
Conversation state management
Text-to-Speech systems
Audio processing
Voice conversion
Modular software architecture
Debugging and integrating multiple technologies

Author

typextomas

This project is continuously being developed and improved.
