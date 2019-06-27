import random
import pyttsx3
import speech_recognition as sr
from selenium import webdriver

engine = pyttsx3.init()
recog = sr.Recognizer()
mic = sr.Microphone(device_index=1, chunk_size= 512)



resp = ""


while True:

    with mic as source:

        print("Listening...")


        try:
            audio = recog.listen(source)

            recog.adjust_for_ambient_noise(source)
            print("Translating")
            resp = recog.recognize_google(audio)

            print(resp)

        except:
            print("Coudln't understand the mic")

