# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import gtts
from playsound import playsound
import os

#https://www.thepythoncode.com/article/convert-text-to-speech-in-python
#https://www.geeksforgeeks.org/create-a-voice-recorder-using-python/

print("A five second recording has started")
# Sampling frequency
freq = 44100

# Recording duration
duration = 5

# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
				samplerate=freq, channels=1)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
#write("recording0.wav", freq, recording)

print("The recording has stopped \n We will now say what you said back to you")

# Convert the NumPy array to audio file
wv.write("inputAudio.wav", recording, freq, sampwidth=2)



import speech_recognition as sr
sr.__version__

r = sr.Recognizer()

inputaudio = sr.AudioFile('inputAudio.wav')
with inputaudio as source:
   audio = r.record(source)


type(audio)

tekst = r.recognize_google(audio)

print(tekst)


if tekst == "yes":
    print("you said yes")
else:
    print("you said something else")

tts = gtts.gTTS(tekst, lang="en")
tts.save("outoutAudio.mp3")
playsound("outoutAudio.mp3")

if os.path.exists("inputAudio.wav"):
  os.remove("inputAudio.wav")
  print("input Audio deleted")
else:
  print("The inputAudio.wav does not exist")

if os.path.exists("outoutAudio.mp3"):
  os.remove("outoutAudio.mp3")
  print("output audio deleted")
else:
  print("The outoutAudio.mp3 does not exist")

