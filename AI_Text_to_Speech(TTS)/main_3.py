from langdetect import detect
import speech_recognition as sr

r1 = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Now")
    audio = r1.listen()

print(detect(audio))