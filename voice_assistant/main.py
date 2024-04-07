import pyttsx3
import speech_recognition as sr 
import webbrowser 
import datetime
import pyjokes
import time

def sptext():
    # All of the magic in SpeechRecognition happens with the Recognizer class
    recognizer = sr.Recognizer()
    while True:
    # Access microphone 
        with sr.Microphone() as source: 
            print("Listening...")
            # In order to cancel the noise of the source 
            recognizer.adjust_for_ambient_noise(source)
            # get the audio from the source 
            audio = recognizer.listen(source)
            try:
                print("recognizing...")
                # get the text from the audio 
                data = recognizer.recognize_google(audio)
                print(data)
                return data
            except sr.UnknownValueError:
                print("Not understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    if sptext().lower() == "hey alexa":
        speechtx("I am listening")

        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is Alexa!"
                speechtx(name)
            elif "old are you" in data1:
                age = "i am 2 years old"
                speechtx(age)
            elif "time now" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                print(time)
                speechtx(time)
            elif "youtube" in data1:
                speechtx("Opening youtube")
                webbrowser.open("https://www.youtube.com/")
            elif "google" in data1:
                speechtx("opening Google")
                webbrowser.open("https://www.google.com/")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke("en","all")
                speechtx(joke_1)
            elif "exit" in data1:
                speechtx("thank you!")
                break
            time.sleep(8)
# sptext()
# speechtx(sptext())