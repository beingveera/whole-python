from gtts import gTTS
from  playsound import playsound
ls=input('Enter a string :')
ls=gTTS(ls)
ls.save('veera.mp3')
playsound('veera.mp3')