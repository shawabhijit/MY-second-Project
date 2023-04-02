
from jiya import Ui_Form
from PyQt5 import QtCore, QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.uic import loadUiType
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import cv2
import pyautogui
import requests 
import webbrowser as web
from bs4 import BeautifulSoup
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import pywikihow
from pywikihow import search_wikihow
import randfacts
import pyjokes
import wolframalpha
import sys
import self


engine = pyttsx3. init('sapi5')
voices = engine. getProperty('voices')
engine. setProperty('voice' ,voices[1]. id )

def speak (audio):
    engine. say(audio)
    engine. runAndWait()



#wishings
def wishings(self):
    hour = int(datetime.datetime. now().hour)
    if hour>=0 and hour<12:
        speak ("good morning chief")
    elif hour>=12 and hour<17:
        speak("good afternoon chief")
    elif hour >=17 and hour <21:
        speak("good evening chief")
    else:
        speak("good night chief")

def wakeupcommands(Self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jiya is Sleeping....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source , duration=1)
        audio = r.listen(source)
    try:
        self.query = r.recognize_google(audio, language='en-in')
        print(f"user said:{self.query}\n")
    except:
        Self.query = "none"
    return Self.query

class Mainthread(QThread):

    def __init__(self):
        super(Mainthread,self).__init__()

    def run(self):
        self.task_gui()

    
    
    def takecommend(self):                      
      r = sr. Recognizer()
      with sr. Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        r. adjust_for_ambient_noise(source, duration=1)
        audio = r. listen(source, timeout=60, phrase_time_limit=300)

        try:
          print("recognize....")
          self.query = r. recognize_google(audio, language='en-in')
          print(f"you just said :{self.query}\n")
        except Exception as e:
          print("please tell me again")
          return 'none'
        return self.query

    def news():
      main_url = 'http://Newsapi.org/v2/top-headlines?sources=techcrunch&apikey=d79f1e4f64134ecea0d64f2215a82df8'

      main_page = requests.get(main_url).json()
      articles = main_page["articles"]
      head = []
      day = ["first", "second", "third", "fourth", "five", "six"]
      for ar in articles:
        head.append(ar["title"])
      for i in range (len(day)):
        speak(f"today's {day[i]}news is:{head[i]}")
        print(f"today's {day[i]}news is:{head[i]}")

#location
    def my_location():
       op = "https://www.google.co.in//maps//place//Keshiakole,+Bankura,+West+Bengal+722155//@23.2442056,87.0752747,16z//data=!4m5!3m4!1s0x39f7a5e9143c4897:0x73685c37d57a7417!8m2!3d23.2449878!4d87.0803526"
  
       speak("checking chief")
       web.open(op)
       ip_add = requests.get("https://api.ipify.org").text
       url = "https://get.geojs.io/v1/ip/geo/"+ip_add +".json"
       geo_q = requests.get(url)
       geo_d = geo_q. json()
       state = geo_d["city"]
       country = geo_d['country']
       speak(f"chief, you are now in {state , country}.")

    def googlemaps(place):
       url_place = "https://www.google.com/maps/place/" + str(place)
       geolocator = Nominatim(user_agent= "myGeocoder")
       location = geolocator.geocode(place, addressdetails= True)
       target_latlon = location.latitude , location.longitude
       web.open(url_place)
       location = location.raw['address']
       target = {'city' : location.get('city', ''),'state' : location.get('state', ''),
            'country' : location.get('country','')}
       current_loca = geocoder.ip('me')
       current_lotlon = current_loca.latlng
       distance = str(great_circle(current_lotlon,target_latlon))
  
       distance = (distance,2)
       speak(target)
       speak(f"chief, {place} is {distance} kilometre away from your location .")


    def wolfRamAlpha(query):
      apikey = ("R5TAL3-99EJ2JR8AY")
      requester = wolframalpha.Client(apikey)
      requested = requester.query(query)

      try:
        answer = next(requested.results).text
        return answer
      except:
         speak("the value is not answerable")

    def calc(query):
      Term = str(query)
      Term = Term.replace("jiya", "")
      Term = Term.replace("plus","+")
      Term = Term.replace("minus","-")
      Term = Term.replace("multiply","*")
      Term = Term.replace("divide","/")

      Final = str(Term)
      try:
         result = wolframalpha(Final)
         print(f"your result is {result}")
         speak(f"your result is {result}")
      except:
         speak("the value is not answerable")

    def alarm(timing):
      altime = str(datetime.datetime.now().strptime(timing, "%I:%M %p"))
      altime = altime[11:-3]
      print(altime)
      horeal = altime[:2]
      horeal = int(horeal)
      mireal = altime[3:5]
      mireal = int(mireal)
      print(f"done chief, alarm is set for{timing}")
      while True:
         if horeal == datetime.datetime.now().hour:
            if mireal == datetime.datetime.now().minute:
               print("alarm is running")
        # mixer.init()
        # mixer.music.load("C:\\Users\\abhij\\B:\JIYA by abhi\\iron_man_suits_up.mp3")
        # mixer.music.play 
            elif mireal<datetime.datetime.now().minute:
             break

    def closeapps():
       if "youtube"in self.query:
        os.system("TASKKILL /F /im msedge.exe")
       elif "facebook"in self.query:
        os.system("TASKKILL /F /im msedge.exe")
       elif "instagram"in self.query:
        os.system("TASKKILL /F /im msedge.exe")
       elif "flipkart"in self.query:
        os.system("TASKKILL /F /im msedge.exe")
  
    def task_gui(self):
        speak("i am jiya chief")
        parmission = wakeupcommands(self).lower()
        if "wake up"in parmission:
          wishings(self)
          speak(f"hallo chief, i am now online, tell me how can i help you")
        
    #if __name__ == "__main__":         
        while True:
    
                    self.query = self.takecommend()
                    if 'time' in self.query:
                       strtime = datetime.datetime.now().strftime("%H:%M:%S")
                       print(strtime)
                       speak(f"chief the time is {strtime}")
                    elif 'date' in self.query:
                       strdate = datetime.datetime.now().strftime("%D")
                       print(strdate)
                       speak(f"chief the date is {strdate}")
                    elif"open Firefox"in self.query:
                      npath = ("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
                      os.startfile(npath)
                      speak("opening firefox application chief")
                
                    elif 'open command prompt' in self.query:
                      os.system("start cmd")
                      speak("opening command prompt application chief")
        
        
                    elif 'Wikipedia' in self.query:
                      speak('search in wikipedia...')
                      self.query = self.query.replace('accarding to Wikipedia', "")
                      self.query = self.query.replace("who is", "")
                      Results = wikipedia.summary(self.query, sentences= 2)
                      speak("according to wikipedia...")
                      speak(Results)
                      print(Results)
                    elif 'open google' in self.query:
                       webbrowser.open("www.google.com")
                       speak("opening google chif")
                    
                    
                    elif 'open youtube'in self.query:
                        speak("chief , what should i search on youtube")
                        am = self.takecommend().lower()
                        webbrowser.open(f"{am}")
                        speak("opening youtube chief")
                    elif "close youtube"in self.query:
                      speak("ok chief, closing youtube")
                      self.closeapps()
                    
                    elif 'open facebook'in self.query:
                       webbrowser.open("www.facebook.com")
                       speak("opening facebook chief")
                    elif "close facebook"in self.query:
                      speak("ok chief, closing facebook")
                      self.closeapps()
                    
                    elif 'open gmail'in self.query:
                       webbrowser.open("www.gmail.com")
                       speak("opening gmail chief")
                    
                    elif 'open instagram'in self.query:
                       webbrowser.open("www.instagram.com")
                       speak("opening instagram chief")
                    elif "close instagram"in self.query:
                      speak("ok chief, closing instagram")
                      self.closeapps()
                    
                    elif 'open flipkart'in self.query:
                       webbrowser.open("www.flipkart.com")
                       speak("opening flipkart chief")
                    elif "close flipkart"in self.query:
                      speak("ok chief, closing flipkart")
                      self.closeapps()
                    
                    elif 'play'in self.query:
                       speak("sure chief , i can")
                       self.query = self.query.replace('can you', "")
                       self.query = self.query.replace('play', "")
                       speak('playing' + self.query)
                       pywhatkit.playonyt(self.query)
                    
                    elif"magic sentences" in self.query:
                        speak("yes chief, for your pleasure")
                    
                    elif "what can you do for me" in self.query:
                         speak("nice question chief")
                         speak("as per my program, i can do operate all system on you laptop, example, fierfox, youtube, google, cmd, datetime, news and excetra")
                         print("as per my program, i can do operate all system on you laptop, example, fierfox, youtube, google, cmd, datetime ")
                    
                    elif "cool" in self.query or "nice" in self.query or "awsome"in self.query or "thank you"in self.query:
                        speak("it's my pleasure chief!")
              
            
                    elif 'open camera'in self.query :
                       speak("opening camera chief")
                       cap = cv2.VideoCapture(0)
                       while True:
                          ret, img = cap.read()
                          cv2. imshow('webcame', img)
                          k = cv2.waitKey(50)
                          if k==27:
                            break
                          cap.release()
                          cv2. destroyAllWindows()
                    elif 'switch the window'in self.query:
                         pyautogui.keyUp("alt")
                         speak("switching the window chief")
                         pyautogui.keyDown("alt")
                         pyautogui.press("tab")
                    elif "tell me today's news"in self.query.lower():
                       speak("please wait chief, feteching the latest news")
                       self.news()
                    elif 'hello'in self.query:
                      speak("hello chief, i am online, tell me what can i do for you")
                    elif "how are you"in self.query:
                       speak("i am fine chief,  how you are!")
                    elif 'i am also fine'in self.query:
                         speak("that's osm, i wish always you have a good health chief")
                    
                    elif "temperature"in self.query:
                      search = "temperature in west bengal"
                      url = f"https://www.google.com/search?q={search}"
                      r = requests.get(url)
                      data = BeautifulSoup(r.text, "html.parser")
                      temp = data.find("div", class_="BNeawe").text
                      speak(f"current{search} is {temp}")
                    elif "activate how to do mode"in self.query:
                        speak("how to do mode is activated")
                        while True:
                           speak("please tell me what you want to know")
                           how = self.takecommend()
                           try:
                             if "exit"in how or "close"in how:
                               speak("okey chief, how to do mode is closed")
                               break
                             else:
                                max_results = 1
                                how_to = search_wikihow(how, max_results)
                                assert len(how_to)==1
                                how_to[0].print()
                                speak(how_to[0]. summary)
                           except:
                               speak("sorry chief, i am note able to find this")
                    elif "facts"in self.query:
                       a= randfacts.get_fact()
                       b= randfacts.get_fact()
                       c= randfacts.get_fact()
                       d= randfacts.get_fact()
                       x= a,b,c,d
                       facts = ("one", "two", "three","four")
                       for i in range (len(facts)):
                          print(f"fact number{facts[i]}:",x[i])
                          speak(f"fact number{facts[i]},{x[i]}")
                    elif 'track my location'in self.query:
                         self.my_location()
                    
                    elif "where is"in self.query:
                      place = self.query.replace("where is ", "")
                      place = place.replace("jiya" , "")
                      self.googlemaps(place)
                    
                    elif "random joke" in self.query:
                      speak(pyjokes.get_joke())
                      print(pyjokes.get_joke())
                    
                    elif "can you calculate"in self.query:
                      
                      self.query = self.query.replace("calculate", "")
                      self.query = self.query.replace("jiya", "")
                      self.calc(self.query)
                    
                    elif "alarm"in self.query:
                      speak("chief please tell me the time to set alarm set")
                      tt = self.takecommend()
                      tt = tt.replace("set alarm to", "")
                      tt = tt.replace(".","")
                      tt = tt.upper()
                      self.alarm(tt)
                    elif "open"in self.query:
                      self.query = self.query.replace("open", "")
                      self.query = self.query.replace("jiya", "")
                      pyautogui.press("super")
                      pyautogui.typewrite(self.query)
                      pyautogui.sleep(2)
                      pyautogui.press("enter")
                      speak(f"sure chief, opening{self.query} application")
                      

    # if __name__ == "__main__":
startFunction = Mainthread()


class gui_Start(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)

  def steartFunc(self):
    self.ui.movies = QtGui.QMovie("Code_Template.gif")
    self.ui.label_2.setMovie(self.ui.movies)
    self.ui.movies.start()

    self.ui.movies = QtGui.QMovie("Earth_Template.gif")
    self.ui.label_3.setMovie(self.ui.movies)
    self.ui.movies.start()

    self.ui.movie = QtGui.QMovie("SAUCY LOUDPACK Loading______.jpg")
    self.ui.label_4.setMovie(self.ui.movies)
    self.ui.movie.start()

    self.ui.movie = QtGui.QMovie("Health_Template.gif")
    self.ui.label_5.setMovie(self.ui.movies)
    self.ui.movie.start()

    self.ui.movie = QtGui.QMovie("Aqua.gif")
    self.ui.label_6.setMovie(self.ui.movies)
    self.ui.movie.start()

    startFunction.start()

gui_app = QApplication(sys.argv)
gui_jiya = gui_Start()
gui_jiya.show()
exit(gui_app.exec_())












