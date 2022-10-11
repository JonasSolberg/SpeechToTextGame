# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import gtts
from playsound import playsound
import os

#fuck off
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

print("The recording has stopped \nWe will now say what you said back to you")

try:
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

except:
    print("error with voice to text. Try again. Check if the voice is clear and you have internet connection")

try:
    if tekst == "yes":
        print("you said yes")
    else:
        print("you said something else")
except:
        print("error with if statement")

try:
    tts = gtts.gTTS(tekst, lang="en")
    tts.save("outputAudio.mp3")
    playsound("outputAudio.mp3")
except:
    print("Error with output of audio")

if os.path.exists("inputAudio.wav"):
  os.remove("inputAudio.wav")
  print("input Audio deleted")
else:
  print("The inputAudio.wav does not exist")

if os.path.exists("outputAudio.mp3"):
  os.remove("outputAudio.mp3")
  print("output audio deleted")
else:
  print("The outputAudio.mp3 does not exist")

