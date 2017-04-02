# python
# Note：this example require Pyaudio because it uses the Microphone class
import speech_recognition as sr
import pyaudio

# obtain audio from the microphone

r = sr.Recognizer()
with sr.Microphone(device_index=2,sample_rate=44100) as source:
    print("Say something!")
    audio = r.listen(source)
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
