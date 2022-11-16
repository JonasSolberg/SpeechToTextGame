#ALL IMPORTS------------------------------------------------------------------------------------------------------------
import sys

import sounddevice as sd
import speech_recognition
from scipy.io.wavfile import write
import wavio as wv
import gtts
from playsound import playsound
import os
import speech_recognition as sr
sr.__version__
from modul_TTS import speak

#INTRO PART ONE --------------------------------------------------------------------------------------------------------
introText1 = "Welcome to our game!"
introText2 = "In this game you will be playing as Jack, a poor farmers boy living with his mother."
introText3 = "As you play as Jack, you will encounter challenges that you have to take smart choices"
introText4 = "You will be given choices where you have to speak. Remember to only say the one word we tell you to"
introText5 = "We would like to know who is playing our game, could you tell us your name?"
print(introText1)
print(introText2)
print(introText3)
print(introText4)
print(introText5)
speak(introText1)
# speak(introText2)
# speak(introText3)
# speak(introText4)
speak(introText5)


#CODE FOR RECORDING NAME ------------------------------------------------------------------------------------------------
freq = 44100
duration = 3
recording = sd.rec(int(duration * freq),
                           samplerate=freq, channels=1)
print("Recording has started")
sd.wait()
print("The recording has stopped")
wv.write("inputAudio.wav", recording, freq, sampwidth=2)
r = sr.Recognizer()
inputaudio = sr.AudioFile('inputAudio.wav')
with inputaudio as source:
            audio = r.record(source)
type(audio)
text = r.recognize_google(audio, language='en-IN', show_all=True)
name = text

#IF USER DOES NOT SAY ANYTHING
while True:
    if name == []:
            repeatName = "You either didnt say anything or you didn't talk loud enough. Could you please repeat your name"
            print(repeatName)
            speak(repeatName)

            freq = 44100
            duration = 3
            recording = sd.rec(int(duration * freq),
                               samplerate=freq, channels=1)
            print("Recording has started")
            sd.wait()
            print("The recording has stopped")
            wv.write("inputAudio.wav", recording, freq, sampwidth=2)
            r = sr.Recognizer()
            inputaudio = sr.AudioFile('inputAudio.wav')
            with inputaudio as source:
                audio = r.record(source)
            type(audio)
            #FALSE ON THIS, OTHERWISE THE NEXT PART WILL FAIL
            text = r.recognize_google(audio, language='en-IN', show_all=False)

            name = text

    #NAME SAID, INTRO CONTINUES
    if not name == []:
        #ADD + FALSE ON THIS, OTHERWISE THE NEXT PART WILL FAIL
        text = r.recognize_google(audio, language='en-IN', show_all=False)
        name = text

        introText6 = "Hi, " + name + "! Are you ready to play? Say yes or no"
        print(introText6)
        speak(introText6)
        break

#RECODRING FOR ARE YOU READY
freq = 44100
duration = 3
recording = sd.rec(int(duration * freq),
                           samplerate=freq, channels=1)
print("Recording has started")
sd.wait()
print("The recording has stopped")
wv.write("inputAudio.wav", recording, freq, sampwidth=2)
r = sr.Recognizer()
inputaudio = sr.AudioFile('inputAudio.wav')
with inputaudio as source:
            audio = r.record(source)
type(audio)
text = r.recognize_google(audio, language='en-IN', show_all=True)

#TURNS TEXT TO ANSWER
answer = text
print(answer)

#ARE USER READY TO PLAY?------------------------------------------------------------------------------------------------
while True:
    # READY TO PLAY: User says no
    #Maybe add if user wants to quit
    if answer == "no" or answer == "No":
        noText = "Okei, say ready whenever you are ready."
        speak(noText)

        #RECORDING FOR READY IF ANSWER WAS NO
        freq = 44100
        duration = 3
        recording = sd.rec(int(duration * freq),
                               samplerate=freq, channels=1)
        print("Recording has started")
        sd.wait()
        print("The recording has stopped")
        wv.write("inputAudio.wav", recording, freq, sampwidth=2)
        r = sr.Recognizer()
        inputaudio = sr.AudioFile('inputAudio.wav')
        with inputaudio as source:
                audio = r.record(source)
        type(audio)
        text = r.recognize_google(audio)

        answer = text
        print(answer)

    # READY TO PLAY: User says nothing
    if answer == []:
        emptyText = "You either didnt say anything or you didn't talk loud enough. Could you repeat your answer"
        print(emptyText)
        speak(emptyText)

        freq = 44100
        duration = 3
        recording = sd.rec(int(duration * freq),
                           samplerate=freq, channels=1)
        print("Recording has started")
        sd.wait()
        print("The recording has stopped")
        wv.write("inputAudio.wav", recording, freq, sampwidth=2)
        r = sr.Recognizer()
        inputaudio = sr.AudioFile('inputAudio.wav')
        with inputaudio as source:
            audio = r.record(source)
        type(audio)
        text = r.recognize_google(audio)

        answer = text
        print(answer)

    #READY TO PLAY: User says something else
    if not answer == "yes" or answer == "ready" or answer == "no":
        invalidAnswer = "You did not say one of the requested answers"
        invalidAnswer2 = "Say Yes or No"
        speak(invalidAnswer)
        print(invalidAnswer)
        speak(invalidAnswer2)
        print(invalidAnswer2)

        freq = 44100
        duration = 3
        recording = sd.rec(int(duration * freq),
                           samplerate=freq, channels=1)
        print("Recording has started")
        sd.wait()
        print("The recording has stopped")
        wv.write("inputAudio.wav", recording, freq, sampwidth=2)
        r = sr.Recognizer()
        inputaudio = sr.AudioFile('inputAudio.wav')
        with inputaudio as source:
            audio = r.record(source)
        type(audio)
        text = r.recognize_google(audio)

        answer = text
        print(answer)

    #READY TO PLAY: User says yes or is now ready
    if answer == "yes" or answer == "ready":
        choice1text = "Great! Lets start!"
        print(choice1text)
        speak(choice1text)
        break

#CHOICE 1: SELL COW OR GO TO MARKED------------------------------------------------------------------------------------------------
ida=1