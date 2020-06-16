import pywhatkit
def msg():
    number=int(input("Enter number :"))
    pywhatkit.sendwhatmsg(number, "Test-1", 17, 44)
