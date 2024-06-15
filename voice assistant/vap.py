import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser

# Initialize the recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            return text.lower()

        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"Error occurred: {e}")
            return ""

# Main loop for interaction
while True:
    speak("How can I help you?")
    command = listen()

    if "hello" in command:
        speak("Hello there!")
    elif "what's the time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "what's the date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today is {today}")
    elif "weather" in command:
        city = "New York"  # Change this to the desired city
        api_key = "YOUR_WEATHER_API_KEY"  # Replace with your actual API key
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        response = requests.get(weather_url)
        if response.status_code == 200:
            weather_data = response.json()
            description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            speak(f"The weather in {city} is {description}. The temperature is {temperature} Kelvin.")
        else:
            speak("Sorry, I couldn't fetch the weather information.")
    elif "search" in command:
        speak("What do you want to search for?")
        search_query = listen()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
    elif "stop" in command:
        speak("Goodbye!")
    break