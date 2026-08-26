import pyttsx3  # For text-to-speech
import speech_recognition as sr  # For speech recognition
import requests  # For making HTTP requests
import webbrowser  # For opening URLs
import tkinter as tk  # For GUI

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get weather
def get_weather(city):
    api_key = "YOUR_WEATHER_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    weather = data["weather"][0]["description"]
    speak(f"The weather in {city} is {weather}")

# Function to open URL
def open_url(url):
    webbrowser.open(url)

# Function to process voice commands
def process_command(command):
    if "weather" in command:
        city = command.split("weather in ")[-1]
        get_weather(city)
    elif "play" in command:
        query = command.split("play ")[-1]
        url = f"https://www.youtube.com/results?search_query={query}"
        open_url(url)

# Function to handle microphone input
def listen_microphone():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        process_command(command)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
    except sr.RequestError:
        print("Sorry, I couldn't reach Google Speech Recognition service.")

# Function to handle GUI input
def process_gui_input():
    command = entry.get()
    process_command(command)

# Create GUI window
window = tk.Tk()
window.title("Jarvis")
window.geometry("400x200")

# Create GUI components
label = tk.Label(window, text="Type a command or click the microphone icon to speak:")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

button = tk.Button(window, text="Speak", command=listen_microphone)
button.pack()

window.mainloop()
