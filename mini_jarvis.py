import streamlit as st
import speech_recognition as sr
import pyttsx3
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    speak(greeting)
    return f"{greeting} I am your assistant. How can I help you?"

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)

    try:
        st.info("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        return query
    except Exception:
        return "Sorry, I didn't catch that. Please try again."

# Streamlit App
st.title("🧠 Mini Jarvis - Voice Assistant")
st.write("Click the button and speak your command.")

if st.button("🎙 Start Listening"):
    wish_text = wishMe()
    st.success(wish_text)
    query1 = takeCommand()
    st.write(f"🗣 You said: {query1}")

    if 'time' in query1:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}"
        speak(response)
        st.success(response)

    elif 'exit' in query1 or 'stop' in query1:
        speak("Goodbye!")
        st.warning("Assistant stopped.")

    else:
        response = "I didn't understand that. Please try again."
        speak(response)
        st.error(response)