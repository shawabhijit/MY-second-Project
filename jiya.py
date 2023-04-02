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
import self
from pywikihow import search_wikihow
import randfacts
import pyjokes
import wolframalpha
import sys



engine = pyttsx3. init('sapi5')
voices = engine. getProperty('voices')
engine. setProperty('voice' ,voices[1]. id )
engine.setProperty('rate', 170)

def speak (audio):
    engine. say(audio)
    engine. runAndWait()

def time(self):
  strtime = datetime.datetime.now().strftime("%H:%M:%S")
  print(f"now the time is:  {strtime}")
  speak(f"now {strtime}")

#wishings
def wishings(Self):
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
        speak("i did not understand what you said ,  please tell me again !")
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
    result = wolfRamAlpha(Final)
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
    try:
      if horeal == datetime.datetime.now().hour:
        if mireal == datetime.datetime.now().minute:
          print("alarm is running")
          music_dir = "B:\\music"
          songs = os.listdir(music_dir)
          os.startfile(os.path.join(music_dir, songs[0]))

        elif mireal<datetime.datetime.now().minute:
          break
    except Exception as e:
      "none"

def closeapps():
  if "youtube"in self.query:
    os.system("taskkill /im"+str(self.query))
  elif "facebook"in self.query:
    os.system("taskkill /im"+str(self.query))
  elif "instagram"in self.query:
    os.system("taskkill /im"+str(self.query))
  elif "flipkart"in self.query:
    os.system("taskkill /im"+str(self.query))






if __name__ == "__main__":
    #wishings()

    while True:
        permission = wakeupcommands(self).lower()
        if "wake up"in permission:
          speak("Now me to introduce my self, i am  jiya, A artificial narrow inteligence project, and i am here to assist you of your systemas a best icon,  importing all references of hurm interface,   systems now fully operational")
          time(self)
          wishings(self)
          speak(f"hallo chief, now i am abel to take your commands")
        
        
        
                 
        while True:
    
                    self.query = takecommend(self)
                    if 'time' in self.query:
                       strtime = datetime.datetime.now().strftime("%H:%M:%S")
                       print(strtime)
                       speak(f"chief the time is {strtime}")
                    elif 'date'in self.query:
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

                    elif "search"in self.query or "search on Chrome"in self.query:
                      speak("what should i search chief")
                      search = takecommend(self).lower()
                      chrompath = ('C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s')
                      webbrowser.get(chrompath).open_new_tab(search+'.com')
                    
                    
                    elif 'launch youTube'in self.query:
                        speak("chief , what should i search on youtube")
                        am = takecommend(self).lower()
                        webbrowser.open(f"{am}")
                        speak("opening youtube chief")
                    elif "close youtube"in self.query:
                      speak("ok chief, closing youtube")
                      closeapps()

                    
                    elif 'launch Facebook'in self.query:
                       webbrowser.open("www.facebook.com")
                       speak("opening facebook chief")
                    elif "close Facebook"in self.query:
                      speak("ok chief, closing facebook")
                      closeapps()
                    
                    elif 'open Gmail'in self.query:
                       webbrowser.open("www.gmail.com")
                       speak("opening gmail chief")
                    
                    elif 'launch instagram'in self.query:
                       webbrowser.open("www.instagram.com")
                       speak("opening instagram chief")
                    elif "close instagram"in self.query:
                      speak("ok chief, closing instagram")
                      closeapps()
                    
                    elif 'launch flipkart'in self.query:
                       webbrowser.open("www.flipkart.com")
                       speak("opening flipkart chief")
                    elif "close flipkart"in self.query:
                      speak("ok chief, closing flipkart")
                      closeapps()
                    
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
                         speak("as per my program, i can do operate all system on your laptop, example, fierfox, youtube, google, cmd, datetime, news and excetra")
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
                       news()
                    
                    elif 'hello'in self.query:
                      speak("hello chief, i am online, tell me what can i do for you")
                    
                    elif 'how are you'in self.query:
                      speak("i am fine chief, how you are")
                    
                    elif 'i am also fine'in self.query or "also fine"in self.query:
                         speak("that's osm, i wish always you have a good health chief")

                    elif "what is your name"in self.query:
                      speak("my name is, jiya")
                      speak(" who are you? ")
                    elif "my name is abhijit" in self.query or "Abhijeet"in self.query:
                      speak("wellcome,  told me how can i help you")
                    
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
                           how = takecommend(self)
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
                      my_location()
                    
                    elif "where is"in self.query:
                      place = self.query.replace("where is ", "")
                      place = place.replace("jiya" , "")
                      googlemaps(place)
                    
                    elif "random joke" in self.query:
                      speak("yes, chief")
                      mm = (pyjokes.get_joke())
                      speak(f"that is your joke, {mm}")
                      print(f"that is your joke:{mm}")
                    
                    
                    elif "calculate"in self.query:
                      
                      self.query = self.query.replace("calculate", "")
                      self.query = self.query.replace("jiya", "")
                      calc(self.query)
                    
                    elif "alarm"in self.query:
                      speak("chief please tell me the time to set alarm set")
                      tt = takecommend(self)
                      tt = tt.replace("set alarm to", "")
                      tt = tt.replace(".","")
                      tt = tt.upper()
                      alarm(tt)
                    
                    elif "open"in self.query:
                      self.query = self.query.replace("open", "")
                      self.query = self.query.replace("jiya", "")
                      pyautogui.press("super")
                      pyautogui.typewrite(self.query)
                      pyautogui.sleep(2)
                      pyautogui.press("enter")
                      speak(f"sure chief, opening{self.query} application")
                    
                    
                    elif "shutdown"in self.query or "down"in self.query or "please sutdown"in self.query:
                      speak("chief, if you reyaly want to shutdown")
                      while True:
                        shut = takecommend(self)
                        if "yes"in shut or "Yes"in shut:
                            speak("ok chief, your system was closed")
                            os.system("shutdown /s /t 5")
                        else:
                           'none'

                    elif "restart"in self.query or "ressart"in self.query or "can you restart my laptop"in self.query:
                      speak("yes chief,  i can")
                      speak("chief, if you reyaly want to restart")
                      while True:
                        shut = takecommend(self)
                        if "yes"in shut or "Yes"in shut:
                            speak("ok chief, your system was restarting")
                            os.system("shutdown /r /t 5")
                        else:
                           'none'
                    
                    elif "minimize"in self.query or "minimise"in self.query:
                      speak("ok chief, minimizeing")
                      pyautogui.hotkey('win', 'd')

                    elif "maximize"in self.query or "maximise"in self.query:
                      speak("ok chief, maximizeing")
                      pyautogui.hotkey('win', 'd')


                    elif 'should you tell me something'in self.query :
                          speak("sorry chief , for let wishing")
                          webbrowser.open("https://in.images.search.yahoo.com/yhs/search;_ylt=Awrx5krfebBjB24AvxznHgx.;_ylu=Y29sbwMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=happy+new+year+pic+2023&type=fc_ADDA49F0A8D_s58_g_e_d041522_n9998_c24&param1=7&param2=eJwti8EKgzAMQH8lRwWpaa3a4mfsNMRDp50rra2ow7GvX4SRy3svyeymvhtud44ohZZ9MURyrbUivFYoeS0EyUgirgO3EsmWcc5UyxSnNNtEzUXCtyFa0teFYMqaIWSni1M6d4gHcGTYAYVGdvBpZA5mXYM97cO7o6yrllUNZP51LKGA4LyF2Y4%2B5TC%2BtrTYkqNieA3s5mk293%2F5AYfkOog%3D&hsimp=yhs-2461&hspart=fc&ei=UTF-8&fr=yhs-fc-2461#id=3&iurl=https%3A%2F%2Fbrofurnaces.com%2Fwp-content%2Fuploads%2F2022%2F12%2Fhappy-new-year-2023.jpg&action=click")
                          speak("HAPPY NEW YEAR CHIEF")
                          print("HAPPY NEW YEAR CHIEF")
                          speak("have a great first of this year")
                    elif 'thank you' in self.query:
                          speak("it's my pleasure chief")
                    elif 'close this'in self.query:
                          speak("closing chief")
                          import closeapp
                          st = [self.query[5:]]
                          closeapp.close(st[0])
                    elif 'by the way, you are late' in self.query:
                          speak("that's not my fault")
                    elif 'what' or 'what do you mean' in self.query:
                          print("___________sorry : sorry : sorry : sorry__________")
                    
                    elif "good night" in self.query:
                          speak("good night chief , have a sweet dream")
                              
                    elif "exit"in self.query or "good by"in self.query or "goodbye"in self.query:
                      speak("ok chief, i wish have a good day for you")
                      sys.exit()
                      
                    


                      

                    
                      
                    

    






              
            
              


              

                 
                










                





            







         

    







