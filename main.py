# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import gtts
from playsound import playsound



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



# Convert the NumPy array to audio file
wv.write("harvard.wav", recording, freq, sampwidth=2)



import speech_recognition as sr
sr.__version__

r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
   audio = r.record(source)

type(audio)

tekst = r.recognize_google(audio)

print(tekst)


if tekst == "yes":
    print("Confirm")
else:
    print("noe annet")

tts = gtts.gTTS(tekst, lang="en")
tts.save("hola.mp3")
playsound("hola.mp3")