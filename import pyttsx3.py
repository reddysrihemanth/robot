import pyttsx3
import speech_recognition as  sr
import datetime
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voice  = engine.getProperty('voices')
#print(voice[1].id)
engine.setProperty('voice', voice[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOODMORNING")

    elif hour>=12 and hour<18:
        speak(" GOOD AFTERNOON")

    else:
        speak("GOOD EVENING")

    speak ("I am Jarvis Sir. Please tell me how may i help you")

def takeCommand():
    #it takes the micro input to from the user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google_cloud(audio, language="en-in")
        print(f"User  said:  (query)\n")

    except Exception as e:
        #print(e):
        print("say the again please.....") 
        return    "NONE"
    return query




    
if __name__  == "_main_":
    wishMe()
    while True:
       query = takeCommand().lower()

       if 'wikipedia' in query:
           speak('searching wikipedia.....')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
           
        
           