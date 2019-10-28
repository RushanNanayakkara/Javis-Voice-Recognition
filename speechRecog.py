import speech_recognition as sr
import pyttsx3

__sampleRate = 48000

__chunkSize = 2048


r = sr.Recognizer()
engine = pyttsx3.init()

while 1:
    with sr.Microphone(sample_rate=__sampleRate,chunk_size=__chunkSize) as src:
        print("Speek anything")
        r.adjust_for_ambient_noise(src)
        audio = r.listen(src)
        try:
            text = r.recognize_google(audio)
            print(text)
            if(text=="Jarvis"):
                engine.say("Hello Rushan")
                engine.runAndWait()
        except Exception as e:
            print(e)