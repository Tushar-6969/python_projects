
# module to import 
import time
import os
import pyttsx3  # for text to voice 
import speech_recognition as sr # for voice to text
import webbrowser
import datetime
import pyjokes
import requests


def sptext():
     recognizer=sr.Recognizer() # functiom call
     with sr.Microphone() as source:  # listen trhough mic 
           print("listening......")
           recognizer.adjust_for_ambient_noise(source)  # cleaning noise 
           audio=recognizer.listen(source)    # actual listemn 


# now we handle the case when anyone no speak 
           try:
                print("recognizing")
                data=recognizer.recognize_google(audio)
                print(data)
                return data
                
           except sr.UnknownValueError:
                print(" not understand ")     

               
def speech_totxt(x):
      engine=pyttsx3.init()   # for calling fun from module 
        
# get property is used to  make chnge int o speech and allow some custom change and set proprty allows to set thes change s
      voices=engine.getProperty('voices')
      engine.setProperty('voice',voices[0].id)    # 0 for men voice and 1 for woman voice 

# for speed of speech      
      rate=engine.getProperty('rate')
      engine.setProperty('rate',120)
      engine.say(x)
      engine.runAndWait()

if __name__=='__main__':
     
     speech_totxt("hii i am jarvis i am here to help you sir ")
     while True:
            
            
            data1=sptext()

            if "your name" in data1:
                  name=" my name is jarvis iam here to help you "
                  speech_totxt(name)
            elif "old are you" in data1: 
                  age="2.5 minute"
                  speech_totxt(age)
            elif "time" in data1:
                  time=datetime.datetime.now().strftime("%I%M%p")
            #   print(time)
                  speech_totxt(time) 
            elif "open youtube" in data1:
                  webbrowser.open("https://www.youtube.com/")   
            elif "search" in data1:
                  speech_totxt("What do you want to search for?")
                  search_query =sptext()
                  if search_query:
                        url = f"https://www.google.com/search?q={search_query}"
                        webbrowser.open(url)
            elif "joke" in data1:
                  joke1=pyjokes.get_joke(language="en", category="neutral")
                  print(joke1)
                  speech_totxt(joke1)

            elif 'play song' in data1:
                  add=r"C:\Users\Tushar\Music"
                  listeonsong=os.listdir(add)
                  os.startfile(os.path.join(add,listeonsong[0]))    
            elif 'exit' in data1:
                  speech_totxt(" thank for having me ")
                  break     
            time.sleep(5)
