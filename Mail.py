#
import ezgmail
import speech_recognition as sr
import pyttsx3

def mail():
    voice1 = pyttsx3.init()
    r = sr.Recognizer()
    voice1.say("Sorry you will have to enter the email address manually")
    voice1.say("Enter recipant")
    voice1.runAndWait()
    recipant = input("Enter recipant :")
    with sr.Microphone() as source1:
        print("Enter Email Subject :")
        voice1.say("Enter Email Subject")
        voice1.runAndWait()
        audio1 = r.listen(source1)
        try:
            text1 = r.recognize_google(audio1)
            print(f"Subject :{text1}\n")
            subject = text1
            with sr.Microphone() as source2:
                print("Compose Email :")
                voice1.say('compose mail')
                voice1.runAndWait()
                audio2 = r.listen(source2)
                try:
                    text2 = r.recognize_google(audio2)
                    print(f"Text :{text2}\n")
                    text0 = text2

                    ezgmail.send(recipant, subject, text0)


                except:
                    print("Error")
                    voice1.say("error")
                    voice1.runAndWait()
        except:
            print("Error")
            voice1.say("error")
            voice1.runAndWait()