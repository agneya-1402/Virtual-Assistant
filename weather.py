import pyttsx3
import requests

def weather():
    a = pyttsx3.init()
    # a.say("The current temperature in mumbai is "+ str(weather.temp()))
    # a.say(str(weather.climate()))

    api = "https://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=64587937fbf72cd46ee211b3523abb0a"
    # city="Mumbai"

    # url=api+city
    jsl = requests.get(api).json()

    data = jsl["main"]["temp"]
    data1 = data - 273.15
    print("The temperature in Mumbai is"+str(data1),"*C")
    data2 = jsl["weather"][0]["description"]
    print("It is"+str(data2))
    a.say("The current temperature in mumbai is" + str(data1) + "degrees celcius")
    a.say("It is" + data2)
    a.runAndWait()

