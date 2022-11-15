import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import gtts
from playsound import playsound
import os

from modul_TTS import speak

if __name__ == "__main__":
  while True:
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
    speak(introText2)
    speak(introText3)
    speak(introText4)
    speak(introText5)
    name = input()
    introText6 = "Hi, " +name+ "! Good luck!"
    print(introText6)
    speak(introText6)
    break