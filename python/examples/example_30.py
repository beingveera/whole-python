import pyttsx3
import  os 
import speech_recognition as sr
import wikipedia
import  smtplib
import webbrowser
import  datetime


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good morning Friend')
    elif hour >=12 and hour<=18:
        speak('Afternoon')
    else:
        speak('Good Evening ')
    speak('Dear sir ')

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listing to You......')
        #r.pause_threshold=1
        audio=r.listen(source)
        print("Recogning Your Voice .....")
        query=r.recognize_google(audio,language='en-in')
        print(query)
        return query

def send_mail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mail','password')
    server.sendmail('yourmail@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishme()

    while True:
        tech=take_command()

        if 'wikipedia' in tech:
            speak('Searching Wikipedia...')
            query=tech.replace('wikipedia','')
            results=wikipedia.summary(tech,sentences=2)
            speak("According to Wikipedia ")
            print(results)
            speak(results)
        elif 'open notepad' in tech:
            npath='C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)

        elif 'open youtube' in tech:
            webbrowser.open('youtube.com')
        
        elif 'open google' in tech:
            webbrowser.open('google.com')
        
        elif 'open github ' in tech:
            webbrowser.open('github.com/techno-veera')
        
        elif 'open vs code' in tech:
            vpath='C:\\Users\\techno\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
            os.startfile(vpath)
        
        elif 'open dev ' in tech:
            dpath='C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe'
            os.startfile(dpath)
        
        elif 'the time ' in tech:
            strtime=datetime.datetime.now().strftime(' %H : %M : %S ')
            speak(strtime)
        
        elif 'email to veera' in tech:
            try:
                speak('What should i send in the mail')
                content=take_command()
                to="veera@gmail.com"
                send_mail(to,content)
                speak('Email has sent to veera...')
            except Exception as e:
                print(e)
                speak('Not Able...')