import datetime
import pyttsx3
voice=pyttsx3.init()
i=datetime.datetime.now()
def time():
    y = i.strftime("%I")
    z = i.strftime("%M")
    x = i.strftime("%p")
    time1 = (str(y) + str(z) + str(x))
    print("The time is "+str(time1))
    voice.say("The time is")
    voice.say(time1)
    voice.runAndWait()
def month():
    x=i.strftime("%B")
    print("The Month is "+str(x))
    voice.say("The month is")
    voice.say(x)
    voice.runAndWait()
def year():
    x=i.strftime("%Y")
    print("The year is "+str(x))
    voice.say("The year is")
    voice.say(x)
    voice.runAndWait()
def date():
    x=i.strftime("%d")
    y=i.strftime("%B")
    print("Todays date is "+str(x)+" "+str(y))
    voice.say("todays date is")
    voice.say(x)
    voice.say(y)
    voice.runAndWait()
def day():
    x=i.strftime("%A")
    print("The day is "+str(x))
    voice.say("The day is"+str(x))
    voice.runAndWait()

