import speech_recognition as sr
from newspaper import Article
import nltk

def arama():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Wikipedia'da Ara: ")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio, language='en-en')
        data = data.lower()

    except sr.UnknownValueError:
       print("Ses Algilanamadi")
    
    from nltk.tokenize import word_tokenize
    kelimeler = word_tokenize(data)
    metin = '_'.join(kelimeler)

    link = 'https://en.wikipedia.org/wiki/'+metin

    nltk.download('punkt', quiet=True)
    article = Article(link)
    article.download()
    article.parse()
    article.nlp()
    corpus = article.text

    print(corpus)

