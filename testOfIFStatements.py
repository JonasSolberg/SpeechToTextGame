# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import gtts
from playsound import playsound
import os
import speech_recognition as sr
sr.__version__

print("Welcome to the game. Please have your sound turned on")
storyPart1 = "This is a test of a story. please say left or right"
tts = gtts.gTTS(storyPart1, lang="en")
tts.save("storyPart1.mp3")
playsound("storyPart1.mp3")



print("A 2 second recording has started")
# Sampling frequency
freq = 44100

# Recording duration
duration = 2

# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
				samplerate=freq, channels=1)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
#write("recording0.wav", freq, recording)

print("The recording has stopped")

#konverter stemme til tekst

try:
    # Convert the NumPy array to audio file
    wv.write("inputAudio.wav", recording, freq, sampwidth=2)
    r = sr.Recognizer()
    inputaudio = sr.AudioFile('inputAudio.wav')
    with inputaudio as source:
        audio = r.record(source)
    type(audio)
    tekst = r.recognize_google(audio)
    print(tekst)

except:
    print("error with voice to text. Try again. Check if the voice is clear and you have internet connection")
answer1 = 0
try:
    if tekst == "left":
        print("you said left")
        answer1 = 1
    elif tekst == "right":
            print("you said right")
            answer1 = 2
    else:
        print("you said something else\nplease try again")
except:
        print("error with if statement")



if answer1 == 1:
    #left
    storyPart2 ="You said left. Please say go home"
    tts = gtts.gTTS(storyPart2, lang="en")
    tts.save("storyPart1.mp3")
    playsound("storyPart1.mp3")

    freq = 44100
    # Recording duration
    duration = 2
    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
				    samplerate=freq, channels=1)

    # Record audio for the given number of seconds
    sd.wait()
    try:
        # Convert the NumPy array to audio file
        wv.write("inputAudio.wav", recording, freq, sampwidth=2)
        r = sr.Recognizer()
        inputaudio = sr.AudioFile('inputAudio.wav')
        with inputaudio as source:
          audio = r.record(source)
        type(audio)
        tekst = r.recognize_google(audio)
        #print(tekst)

    except:
        print("error with voice to text. Try again. Check if the voice is clear and you have internet connection")
if answer1 == 2:
    #right
    storyPart2 = "You said right. Please say go home"
    tts = gtts.gTTS(storyPart2, lang="en")
    tts.save("storyPart1.mp3")
    playsound("storyPart1.mp3")

    freq = 44100
    # Recording duration
    duration = 2
    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
				    samplerate=freq, channels=1)

    # Record audio for the given number of seconds
    sd.wait()
    try:
        # Convert the NumPy array to audio file
        wv.write("inputAudio.wav", recording, freq, sampwidth=2)
        r = sr.Recognizer()
        inputaudio = sr.AudioFile('inputAudio.wav')
        with inputaudio as source:
          audio = r.record(source)
        type(audio)
        tekst = r.recognize_google(audio)
        #print(tekst)

    except:
        print("error with voice to text. Try again. Check if the voice is clear and you have internet connection")




