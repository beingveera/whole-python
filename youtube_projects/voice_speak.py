from gtts import gTTS
from playsound import playsound
def sound(text):
    tts=gTTS(text)
    tts.save('voice.mp3')
sound('lokesh sharma....')

def read(filename):
    playsound(filename)

read("C:\\Users\\techno\\voice.mp3")



