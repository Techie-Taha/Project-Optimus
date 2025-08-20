import speech_recognition as sr
import webbrowser
import pyttsx3 # helps to convert text into speech


recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # index 0 makes male voice, index 1 makes female voice


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    pass
    #if "open google" in c.lower():
        #webbrowser.open("https://google.com")
    #elif "open facebook" in c.lower():
        #webbrowser.open("https://facebook.com")
    #elif "open instagram" in c.lower():
        #webbrowser.open("https://instagram.com")
    #elif "open github" in c.lower():
        #webbrowser.open("https://github.com") 
    #elif "open youtube" in c.lower():
        #webbrowser.open("https://youtube.com")


if __name__ == "__main__":
    speak("Initializing Optimus.......")
    while True:
        r = sr.Recognizer() 
        
        print("recognizing....")
        try:
            with sr.Microphone() as source:
               
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "optimus"):
                speak("Yes Chief")
                with sr.Microphone() as source:
                   print("Optimus Activated...")
                   audio = r.listen(source)
                   command = r.recognize_google(audio)


                   processCommand(command)
    
        except Exception as e:
           print("Error; {0}".format(e))
