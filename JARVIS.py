import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def __init__(username ,password):
    driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
    driver.get("https://www.instagram.com/accounts/login/?hl=en")
    time.sleep(3)
    username_textbox = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    password_textbox = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    button = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]')
    button.click()
    time.sleep(5)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mr Ashutosh  I am Jarvis Speed terabyte Memory one zettabyte , how may i help you" ) #you can change your name if you want
    elif hour>=12 and hour<18:
            speak("Good Afternoon Mr Ashutosh  I am Jarvis Speed terabyte Memory one zettabyte , how may i help you")
    else:
        speak("Good Evening Mr Ashutosh  I am Jarvis Speed terabyte Memory one zettabyte , how may i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in') #here we will use google assistant if it failed to recognize
        print(f"user said: {query}\n")
    except exceptions as e:
        
        print("please say it again")
    
        return "None"
    
    return query

    

if __name__== "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("according to wikipedia") 
            print(results)
            speak(results)
        

        elif 'open youtube' in query:
            print("opening youtube")
            speak("opening youtube")
            webbrowser.open('www.youtube.com')

        elif'who made you' in query:
             speak("i am jarvis and i am made by ashutosh mishra sir you can say thanks if you want to say me")

        elif 'open swiggy' in query:
            print("opening swiggy ")
            speak("opening swiggy thanks for using us")
            webbrowser.open('www.swiggy.com')
            
        elif "open google" in query:
            speak("opening google")
            webbrowser.open('www.google.com')
        elif "order food" in query:
            order1=speak("from where you need to order")
            query = takecommand().lower()
            if order1 == 'swiggy':
                speak('ordering food from swiggy thank you sir')
                webbrowser.open('https://www.swiggy.com/mumbai')
            else:
                speak("ordering food from zomato")
                webbrowser.open('https://www.zomato.com/akola?city_id=11434')

        elif "play music" in query:
            speak("playing music")
            music = 'C:\\Users\\ashu\\Desktop\\desktop\\ext\\songs' #directory towards your songs
            songs = os.listdir(music)
            os.startfile(os.path.join(music,songs[5]))
        elif "the time" in query:
            stime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time right now is {stime}")

        elif "quit" in query:
            speak("Thanks for using it Hope you like the experience")
            exit()

        elif " instagram" in query:
            speak("opening instagram stay tuned")
            __init__("","") #here enter your username of instagram and in second the password

        elif " facebook" in query:  
            speak("Opening facebook")
            driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
            driver.get("https://www.facebook.com/")
            time.sleep(3)
            usernametxt = driver.find_element_by_id("email").send_keys("") #enter your facebook username
            passwordtxt = driver.find_element_by_id("pass").send_keys("") #enter your facebook password
            time.sleep(2)
            butt= driver.find_element_by_id("u_0_b")
            butt.click() 
        elif " movie" in query:
             speak("playing your favourite movie ")
             movie = 'C:\\Users\\ashu\\Desktop\\chichore.mkv' #enter the file location of your movie location
             os.startfile(movie)
            
       
        
        
            

    
            
            
        
        
        
        
    
