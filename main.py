# ----Standard Libraries----#
import os
import time
import socket
import webbrowser

#----Audio and Speech----#
import speech_recognition as sr  # Speech-to-text
from gtts import gTTS            # Google Text-to-Speech
import pygame                    # To play TTS audio

#----AI Logic & Helpers----#
from qa import questions         # Predefined FAQs
from gpt import load_model       # Load GPT model


# Load the GPT4All model once
model = load_model()


# Initialize speech recognizer
recognizer = sr.Recognizer()



#----Internet connectivity----
def has_internet():
        socket.create_connection(("1.1.1.1", 53), timeout=3)
        print("✅ Internet connected 🔌")
        return True
    


# ----------------- SPEAK FUNCTION ------------------
def speak(text):
    """
    Converts the input text to speech using gTTS, plays it using pygame, and removes the temp file.
    """
    tts = gTTS(text)
    tts.save('save.mp3')  # Save the generated speech audio

    pygame.mixer.init()
    pygame.mixer.music.load("save.mp3")
    pygame.mixer.music.play()

    # Wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    # Clean up the temp file and audio player
    pygame.mixer.quit()
    os.remove("save.mp3")



# ----------------- MAIN LOGIC FUNCTION ------------------
def main(d):
    d = d.lower().strip()

    for faq in questions:
        if all(keyword in d for keyword in faq["keywords"]):
            speak(faq["response"])
            # Special case: Open website if user is asking to apply online
            if "apply online" in faq["response"].lower():
                webbrowser.open("https://dcrustadmission.org/")
            return
    
  
    # ❌ No keyword match – fallback to GPT4All
    with model.chat_session():
        ai_response = model.generate(d, max_tokens=100)
        print("GPT⚡:", ai_response)
        speak(ai_response)



# ----------------- PROGRAM STARTS HERE ------------------
if __name__ == "__main__":
    speak("AI Chatbot initializing")  # Intro message
    has_internet()

    while True:
        try:
            # ------------ PHASE 1: WAKE-UP WORD ------------
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
                speak("What you want to ask for")  # Prompt user
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)  # Listen briefly for a trigger word
                word = recognizer.recognize_google(audio)  # Convert to text
                print(f'You said: {word}')


            # ------------ PHASE 2: USER COMMANDS AFTER TRIGGER ------------
            if word.lower() == "tiny":  # Trigger word to activate bot
                speak("At your service, sir")
                print("🎙️")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    command_audio = recognizer.listen(source, timeout=2, phrase_time_limit=10)  # Listen to user query
                    command = recognizer.recognize_google(command_audio)
                    print(f"You said: {command.lower()}")
                    main(command)  # Process command

        except Exception as e:
            print(f"Error: {e}")

        