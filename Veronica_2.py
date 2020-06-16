# Veronica 2.0

from googletrans import Translator
import DesktopApps
import CricketLiveScore
import speech_recognition as sr
import pyttsx3
import WhatsApp_msg
import WebDriver
import datetime
import random
import wikipedia
import Mail
import Wifi
import Time
import weather
import News


voice = pyttsx3.init()
hr=int(datetime.datetime.now().hour)
if hr>=0 and hr<12:
       voice.say("Good morning Sir")
       voice.runAndWait()
       print("Good Morning Sir")
elif hr>=12 and hr<16:
       voice.say("good afternoon sir")
       voice.runAndWait()
       print("Good Afternoon Sir")
elif hr>=16 and hr<21:
       voice.say("Good Evening Sir")
       voice.runAndWait()
       print("Good Evening Sir")


r = sr.Recognizer()
with sr.Microphone() as source:
       print("Listening....")
       audio=r.listen(source)
       try:
              text = r.recognize_google(audio)
              print(f"You said :{text}\n")
              if "weather" in text.lower():
                     weather.weather()
              elif "good morning" in text.lower():
                     Time.time()
                     Time.date()
                     Time.day()
                     weather.weather()
                     print("Todays Headlines")
                     voice.say("todays headlines")
                     voice.runAndWait()
                     News.news()
                     print("Have a Wonderful Day")
                     voice.say("Have a wonderful day")
                     voice.runAndWait()
              elif "translate" and "russian" in text.lower():
                     translator = Translator(service_urls=["translate.google.com"])
                     translation1 = translator.translate(text, dest="ru")
                     print(f"Translated into Russian :{translation1.text}\n")
                     voice.say("Sorry i cannot speak russian")
                     voice.runAndWait()

              elif "whatsapp" in text.lower():
                     voice.say("Enter receivers number")
                     voice.runAndWait()
                     WhatsApp_msg.msg()
                     print("Scan QR code with your phone")
                     voice.say("Scan QR code with your phone")
                     voice.say("message will be sent soon")
                     voice.runAndWait()

              elif "cricket" in text.lower():
                     CricketLiveScore.livescore()

              elif "open cmd" in text.lower():
                     DesktopApps.cmd()
                     print("Opening CMD")
                     voice.say("opening cmd")
                     voice.runAndWait()
              elif "open calculator" in text.lower():
                     print("Opening Calculator")
                     voice.say("opening calulator")
                     voice.runAndWait()
                     DesktopApps.calculator()
              elif "open spark ar" in text.lower():
                     print("Opening Spark AR")
                     voice.say("opening spark ar")
                     voice.runAndWait()
                     DesktopApps.spark_AR()
              elif "open task manager" in text.lower():
                     print("Opening Task Manager")
                     voice.say("opening tast manager")
                     voice.runAndWait()
                     DesktopApps.task_manager()
              elif "open control panel" in text.lower():
                     print("Opening Conrol Panel")
                     voice.say("opening control")
                     voice.runAndWait()
                     DesktopApps.control_panel()

              elif "youtube" in text.lower():
                     voice.say("opening youtube")
                     voice.runAndWait()
                     WebDriver.youtube()
              elif "twitter" in text.lower():
                     voice.say("opening twitter")
                     voice.runAndWait()
                     WebDriver.twitter()
              elif "facebook" in text.lower():
                     voice.say("opening facebook")
                     voice.runAndWait()
                     WebDriver.facebook()
              elif "open mail" in text.lower():
                     voice.say("opening mail")
                     voice.runAndWait()
                     WebDriver.gmail()
              elif "amazon" in text.lower():
                     voice.say("opening amazon")
                     voice.runAndWait()
                     WebDriver.amazon()
              elif "google" in text.lower():
                     voice.say("opening google")
                     voice.runAndWait()
                     WebDriver.google()
              elif "photos" in text.lower():
                     voice.say("opening google photos")
                     voice.runAndWait()
                     WebDriver.photos()

              elif "time" in text.lower():
                     x=datetime.datetime.now()
                     voice.say(x)
                     voice.runAndWait()
              elif "news" in text.lower():
                     News.news()

              elif "introduce" in text.lower():
                     voice.say("Hey i am veronica your virtual assistant \n How may i help you")
                     voice.runAndWait()

              elif "joke" in text.lower():
                     a = "When i see lover's names carved on a tree,i dont think its sweet,\nI just think its surprising how many people bring a knife on a date"
                     b = "My old aunts would come and tease me at weddings,: Well Veronica you think you will be next ?\n We have settled this quickly once i started doing the same to them at funerals"
                     c = "Dentist : This will hurt a little \n Patient : Ok \n Dentist : I have been  having an affair with your wife for a while now"
                     d = "I dreamed I was forced to eat a giant marshmallow.\n When i woke up,my pillow was gone"
                     list1 = [a, b, c, d]
                     x = (random.choice(list1))
                     print(x)
                     voice.say(x)
                     voice.runAndWait()
              elif "song" in  text.lower():
                     voice.say("Opening spotify")
                     voice.runAndWait()
                     WebDriver.spotify()

              elif "wikipedia" in text.lower():
                     voice.say("Searching Wikipedia")
                     text=text.replace("wikipedia", "")
                     results=wikipedia.summary(text,sentences=2)
                     voice.say(results)
                     print(results)
                     voice.runAndWait()

              elif "mail" in text.lower():
                     Mail.mail()

              elif "on" and "wifi" in text.lower():
                     Wifi.on()
              elif "off" or "of" and "wifi" in text.lower():
                     Wifi.off()

              else:
                     voice.say("Error")
                     voice.runAndWait()
                     print("Error")

       except:
              print("Sorry couldnt get that")
              voice.say("Sorry couldnt get that")
              voice.runAndWait()


