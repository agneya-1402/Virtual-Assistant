import requests
from bs4 import  BeautifulSoup
import pyttsx3

voice=pyttsx3.init()
url="https://www.cricbuzz.com/cricket-match/live-scores"

def livescore():
    page=requests.get(url)
    soup=BeautifulSoup(page.content,"html.parser")
    score=soup.find_all("whatever tag is present for the score")
    score1=(score[0].get_text())
    voice.say(score1)
    voice.runAndWait()