import pyttsx3
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""


def jarvis():
    speak("Hello! I'm Jarvis. How can I assist you today?")

    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hi there!")
        elif "goodbye" in query:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm sorry, I don't have the capability to respond to that.")


if __name__ == '__main__':
    jarvis()
