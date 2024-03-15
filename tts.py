#importing required functions from libraries
from gtts import gTTS
from playsound import playsound
from os import remove

#a function to make the speech file and play it, default language is english
def speak(text,lang='en'):
    speech = gTTS(text=text,lang=lang,slow=False)    #speech object made
    speech.save('speech.mp3')                        #speech object saved (as mp3)
    playsound('speech.mp3')                          #plays the mp3 file
    remove('speech.mp3')                             #deletes the mp3 file, this is to ensure the file is deleted when no longer in use
                                                     #also prevents any overwriting/access to files errors is function is called again

#some examples in different languages (all saying 'Hi')
speak('Hi')                 #english
speak('Salut','fr')         #french
speak('Hola','es')          #spanish
speak('hallo','de')         #german
speak('konnichiwa','ja')    #japanese
