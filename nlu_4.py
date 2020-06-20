
import os 
import time 
import playsound
import speech_recognition as sr 
from gtts import gTTS

import speech_recognition as sr
from newspaper import Article
import nltk

import nlu_5

def speak(text):
    tts= gTTS(text=text, lang="tr") 
    filename= "voice.mp3" 
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio,language="tr-tr")
            print(said)
        
        except Exception as e:
            print("Exeception : "+ str(e))
            

    return said
    

text = get_audio()

if "arama" in text:
    speak("vikipediya açılıyor ")
    print("yalnızca ingilizce aratabilirsin")
    
    nlu_5.arama()

if "Merhaba" in text:
    speak("merhaba efendim")
