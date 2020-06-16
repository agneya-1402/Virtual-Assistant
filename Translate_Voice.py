# Voice translate
from googletrans import Translator
import speech_recognition as sr
import pyttsx3
voice=pyttsx3.init()

r=sr.Recognizer()
with sr.Microphone() as source:
       print("Say Something :")
       audio=r.listen(source)
       try:
              text=r.recognize_google(audio)
              print(f"You said :{text}\n")
              print("Translating into russian :")
              translator = Translator(service_urls=["translate.google.com"])
              translation = translator.translate(text, dest="ru")
              voice.say(translation.text)
              voice.runAndWait()
              print(translation.text)

       except:
              print("Sorry couldnt recognize that...!")




