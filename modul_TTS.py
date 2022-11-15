# forsøk på å lage en modul av TTS slik at koden blir mer ryddig

# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import gtts
from playsound import playsound
import os

def speak(tekst):
  tts = gtts.gTTS(tekst, lang="en")
  tts.save("module_test.mp3")
  playsound("module_test.mp3")


def rec():
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
  # write("recording0.wav", freq, recording)

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
  finally: print("Error in Module")

  name = tekst

