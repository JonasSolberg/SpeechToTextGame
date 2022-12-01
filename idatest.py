# ALL IMPORTS------------------------------------------------------------------------------------------------------------
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

# INTRO PART ONE --------------------------------------------------------------------------------------------------------
introText1 = "Welcome to our game!"
introText2 = "In this game you will be playing as Jack, a poor farmer's boy living with his mother."
introText3 = "As you play as Jack, you will encounter different challenges where you have to make smart choices."
introText4 = "You will be given choices where you have to speak. Remember to only say the one of the two words we tell you to say."
introText5 = "But before you can start, we would like to know who is playing our game! Could you tell us your name please?"
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

# CODE FOR RECORDING NAME ------------------------------------------------------------------------------------------------
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

# IF USER DOES NOT SAY ANYTHING
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
        # FALSE ON THIS, OTHERWISE THE NEXT PART WILL FAIL
        text = r.recognize_google(audio, language='en-IN', show_all=False)

        name = text

    # NAME SAID, INTRO CONTINUES
    if not name == []:
        # ADD + FALSE ON THIS, OTHERWISE THE NEXT PART WILL FAIL
        text = r.recognize_google(audio, language='en-IN', show_all=False)
        name = text

        introText6 = "Hi, " + name + "! Are you ready to play? Say yes or no"
        print(introText6)
        speak(introText6)
        break

# RECODRING FOR ARE YOU READY
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
text = r.recognize_google(audio, language='en-IN', show_all=False)

# TURNS TEXT TO ANSWER
answer = text
print(answer)

# ARE USER READY TO PLAY?------------------------------------------------------------------------------------------------
while True:
    # READY TO PLAY: User says no
    # Maybe add if user wants to quit
    if answer == "no" or answer == "No":
        noText = "Okei, say ready whenever you are ready."
        speak(noText)

        # RECORDING FOR READY IF ANSWER WAS NO
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

    # READY TO PLAY: User says something else
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

    # READY TO PLAY: User says yes or is now ready
    if answer == "yes" or answer == "Yes" or answer == "ready":
        choice1text = "Great! Lets start!"
        print(choice1text)
        speak(choice1text)
        break

# CHOICE 1: SELL COW OR GO TO MARKED------------------------------------------------------------------------------------------------

#Boolean which determines what happens in CHOICE2
soldCow = False

while True:
    # CHOICE 1: Story
    choice1Text1 = "Once upon a time, there was a boy. His name was Jack. "
    choice1Text2 = "Jack lived with his mother far out in the countryside. His mother would say that Jack was good-natured, but a bit lazy. "
    choice1Text3 = "Jack and his mother were quite poor, and one day there was no money left to buy food. "
    choice1Text4 = "Jack’s mother then told him to take the cow to the market and sell it, but only for a good price. "
    choice1Text5 = "On the way there Jack meets the butcher. He asked where Jack was taking the cow. "
    choice1Text6 = "I'm taking the cow to the market. My mother told me to sell it, Jack said. "
    choice1Text7 = "What a nice cow. You know what? If you sell the cow to me, I will pay you with these five magic beans, the butcher said. "
    choice1Text8 = "Jack looks at the beans. He kinda thinks they look like regular beans, but when he looks closely, he can see that they sparkle! "

    choice1Text9 = "Will Jack accept this offer? Say Yes or No."

    choice1Text = choice1Text1 + choice1Text2 + choice1Text3 + choice1Text4 + choice1Text5 + choice1Text6 + choice1Text7 + choice1Text8 + choice1Text9
    print(choice1Text)

    speak(choice1Text)

    # RECORD THE ANSWER
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
    text = r.recognize_google(audio, language='en-IN', show_all=False)
    decision = text

    # CHOICE 1: Yes
    if decision == "yes":
        decisionYesText = "Jack accepts the offer he got for the cow and decides to sell it"
        print(decisionYesText)
        speak(decisionYesText)
        soldCow = True
        break

    # CHOICE 1: No
    elif decision == "no":
        decisionNoText = "Jack does not accept the offer so he goes to the market"
        print(decisionNoText)
        speak(decisionNoText)

        decisionNoText2 = "He gets a new offer for the cow, again with beans, does he accept?"

        # RECORD THE ANSWER
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
        text = r.recognize_google(audio, language='en-IN', show_all=False)
        decision2 = text

        # CHOICE 1.5: AT THE MARKED ------------------------------------------------------------------------------------------------
        if decision2 == "yes" or decision2 == "Yes":
            decision2Text = "Jack accepts the offer he got for the cow and decides to sell it"
            print(decision2Text)
            speak(decision2Text)
            # Add more to line up with the rest of the story
            soldCow = True
            break

        if decision2 == "no" or decision2 == "No":
            decision2Text2 = "Jack returns home with the cow"
            print(decision2Text2)
            speak(decision2Text2)
            # Add more to line up with the rest of the story
            break

        if not decision2 == "yes" or decision2 == "no":
            invalidDecision = "Your decision was not one of the requested ones, say your decision again"
            speak(invalidDecision)
            print(invalidDecision)

            # NEW RECORDING
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
            text = r.recognize_google(audio, language='en-IN', show_all=False)
            decision2 = text

        if decision2 == []:
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
            text = r.recognize_google(audio, language='en-IN', show_all=False)
            decision2 = r.recognize_google(audio)

    # CHOICE 1: Did not say a valid answer
    if not decision == "yes" or decision == "no":
        invalidDecision = "Your decision was not one of the requested ones, say your decision again"
        speak(invalidDecision)
        print(invalidDecision)

        # NEW RECORDING
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
        text = r.recognize_google(audio, language='en-IN', show_all=False)
        decision = text

    # CHOICE 1: Did not say anything
    if decision == []:
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
        text = r.recognize_google(audio, language='en-IN', show_all=False)
        decision = text

# CHOICE 2: JACK IS HOME ------------------------------------------------------------------------------------------------
while True:
    # CHOICE 2.1: ONLY GOING TO HAPPEN IF JACK SOLD THE COW
    if soldCow == True:
        while True:
            choice21Text1 = "Jack gets home. He shows his mother the beans. She is angry"
            print(choice21Text1)
            speak(choice21Text1)
            break

    # CHOICE 2.2: JACK RETURNS WITH THE COW
    if soldCow == False:
        while True:
            choice22Text1 = "Jack gets home and goes to bed. The next day, the cow is gone."
            print(choice22Text1)
            speak(choice22Text1)
            break

#WHEN THE STORIES CATCHES UP TO ONE ANOTHER
choice2text = "Hello bitches"