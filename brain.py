from groq import Groq

client = Groq()

messages = [
    {
        "role": "system",
        "content": "You are a sarcastic cute AI voice assistant. Speak naturally and clearly."
    }
]

def think(user_input):
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # VERY good model
        messages=messages
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    return reply
