import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import gtts
from playsound import playsound
import os
import speech_recognition as sr
sr.__version__
from modul_TTS import speak

def rec():
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
