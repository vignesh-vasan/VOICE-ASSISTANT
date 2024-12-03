import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import wolframalpha
import requests
import json
import random
import subprocess
import sys

class VoiceAssistant:
    def __init__(self):
        # Speech recognition setup
        self.recognizer = sr.Recognizer()
        
        # Text-to-speech setup
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speaking rate
        
        # WolframAlpha client for computational queries
        try:
            self.wolframalpha_client = wolframalpha.Client('YOUR_WOLFRAMALPHA_APP_ID')
        except Exception as e:
            print("WolframAlpha setup failed:", e)
            self.wolframalpha_client = None
        
        # Weather API setup (replace with your API key)
        self.weather_api_key = 'YOUR_OPENWEATHERMAP_API_KEY'

    def speak(self, text):
        """Convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Listen to user input via microphone"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)
            
            try:
                command = self.recognizer.recognize_google(audio).lower()
                print("You said:", command)
                return command
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                return ""
            except sr.RequestError:
                print("Could not request results")
                return ""

    def get_weather(self, city):
        """Fetch current weather for a given city"""
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}&units=metric"
        try:
            response = requests.get(base_url)
            data = response.json()
            
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"Temperature in {city} is {temp}°C with {description}"
        except Exception as e:
            return f"Could not fetch weather: {e}"

    def process_command(self, command):
        """Process and respond to voice commands"""
        if 'hello' in command or 'hi' in command:
            responses = [
                "Hello! How can I help you today?", 
                "Hi there! What can I do for you?",
                "Greetings! What would you like assistance with?"
            ]
            self.speak(random.choice(responses))

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")

        elif 'date' in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            self.speak(f"Today's date is {current_date}")

        elif 'wikipedia' in command:
            self.speak("What would you like to search on Wikipedia?")
            search_query = self.listen()
            try:
                result = wikipedia.summary(search_query, sentences=2)
                self.speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                self.speak(f"Multiple results found. Try being more specific. Options include: {e.options[:3]}")
            except Exception as e:
                self.speak(f"Could not fetch Wikipedia information: {e}")

        elif 'weather' in command:
            self.speak("Which city's weather would you like to know?")
            city = self.listen()
            weather_info = self.get_weather(city)
            self.speak(weather_info)

        elif 'open website' in command:
            self.speak("Which website should I open?")
            website = self.listen()
            webbrowser.open(f"https://www.{website}.com")

        elif 'calculate' in command or 'computation' in command:
            self.speak("What calculation would you like me to perform?")
            query = self.listen()
            try:
                if self.wolframalpha_client:
                    res = self.wolframalpha_client.query(query)
                    answer = next(res.results).text
                    self.speak(f"The answer is {answer}")
                else:
                    self.speak("Computational service is not available")
            except Exception as e:
                self.speak(f"Could not perform calculation: {e}")

        elif 'shutdown' in command or 'exit' in command:
            self.speak("Goodbye! Shutting down.")
            sys.exit()

        else:
            self.speak("Sorry, I didn't understand that command.")

    def run(self):
        """Main assistant loop"""
        self.speak("Hello! I'm your voice assistant. How can I help you?")
        
        while True:
            command = self.listen()
            if command:
                self.process_command(command)

def main():
    assistant = VoiceAssistant()
    assistant.run()

if __name__ == "__main__":
    main()