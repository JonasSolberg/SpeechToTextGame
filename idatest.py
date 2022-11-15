import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import gtts
from playsound import playsound
import os
import speech_recognition as sr
sr.__version__
from modul_TTS import speak

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

#CODE FOR RECORDING TO STRING

#Sampling frequency
freq = 44100

# Recording duration
duration = 3

# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
				samplerate=freq, channels=1)
print("Recording has started")

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
#write("recording0.wav", freq, recording)

print("The recording has stopped")

#konverter stemme til tekst

# Convert the NumPy array to audio file
wv.write("inputAudio.wav", recording, freq, sampwidth=2)
r = sr.Recognizer()
inputaudio = sr.AudioFile('inputAudio.wav')
with inputaudio as source:
    audio = r.record(source)

type(audio)
name = r.recognize_google(audio)
#print(name)

#name = input(name)

introText6 = "Hi, " + name + "! Are you ready to play?"

print(introText6)
speak(introText6)

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
answer = r.recognize_google(audio)

#Ready to play: User says no
if answer == "no":
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
    answer = r.recognize_google(audio)

    print(answer)

#Ready to play: User says yes or is now ready
if answer == "yes" or answer == "ready":
    choice = ["accept", "refuse"]
    choice1text = "Great! Lets start!"
    speak(choice1text)
    choice1input = input()

else:
    "Okei, the game quits now"
    quit()
