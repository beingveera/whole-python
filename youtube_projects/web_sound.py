import speech_recognition as sr 
import webbrowser

sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshold=5000

with sr.Microphone() as sourse:
    print('Speak...')
    audio=r.listen(sourse)
    try:
        text=r.recognize_google(audio)
        print('You Said : {} '.format(text))
        url='https://www.google.co.in/search?q='
        search=url+text
        webbrowser.open(search)
    except:
        print('Can`t Recognize...')