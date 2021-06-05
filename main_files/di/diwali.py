from translate import Translator
from win32com.client import Dispatch
import pyttsx3

def speak(str):
    speak=Dispach('SAPI.SpVoice')
    speak.Speak(str)

trans=Translator(to_lang='English')
translation=trans.translate('good evening manju mosi')
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.say(translation)
engine.runAndWait()

if __name__ == "__main__":
    print('happy diwali')


