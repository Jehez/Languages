#importing required functions from libraries
from gtts import gTTS
from playsound import playsound
from os import remove

#a function to make the speech file and play it, default language is english
def speak(s,l='en'):
    speech = gTTS(text=s,lang=l,slow=False)     #speech object made
    speech.save('speech.mp3')                   #speech object saved (as mp3)
    playsound('speech.mp3')                     #plays the mp3 file
    remove('speech.mp3')                        #deletes the mp3 file, this is to save space and ensure there is no overwriting on files

#some examples in different languages (all saying 'Hi')

speak('Hi')                 #english
speak('Salut','fr')         #french
speak('Hola','es')          #spanish
speak('hallo','de')         #german
speak('konnichiwa','ja')    #japanese