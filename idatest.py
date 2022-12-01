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

introText = introText1 + introText2 + introText3 + introText4 + introText5

print(introText)
speak(introText)


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
    elif not name == []:
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
    elif answer == []:
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
    elif not answer == "yes" or answer == "ready" or answer == "no":
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
    elif answer == "yes" or answer == "Yes" or answer == "ready":
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
        decisionYesText = "Magic beans?! What a bargain, Jack thought. He accepted the offer and ran home to tell his mother about the amazing offer."
        print(decisionYesText)
        speak(decisionYesText)
        soldCow = True
        break

    # CHOICE 1: No
    elif decision == "no":
        decisionNoText1 = "Sorry, but I will not accept the offer’ Jack said. "
        decisionNoText2 = "The butcher said it was okay and wished him good luck at the market. "
        decisionNoText3 = "Jack continued his journey to the market. When he got there, he could see that there were a lot of people there. He would surely be able to sell the cow he thought. "
        decisionNoText4 = "While walking around, Jack sees that there is a booth he has never seen before. He decides to go and take a look. The new booth sells jewels and sage. "
        decisionNoText5 = "He must be a warlock, thought Jack. Jack thought that was very cool, since all the other booths only sell food, ugly clothing and tools. "
        decisionNoText6 = "Hello there young boy, what is your name? Said the salesman. Jack introduced himself. "
        decisionNoText7 = "Well hello Jack, what brings you here today?, the salesman said. I am here to sell my family's cow, Jack told the salesman. "
        decisionNoText8 = "The salesman looked at Jack with enthusiasm. You know, I am in need of a cow, do you think I could buy her, the salesman said. "
        decisionNoText9 = "Jack nodded his head and asked what he could offer. The salesman held out his hand and showed Jack a handful of beans. "
        decisionNoText10 = "They are magic beans, worth quite a lot!, he said. Jack looked at the beans. Another man with magic beans? Maybe they are magical? "
        decisionNoText11 = "Before Jack gave his answer, he asked: How can I know that they are magical? The salesman gave him a big smile before whispering: Because I'm a warlock. "

        decisionNoText = decisionNoText1 + decisionNoText2 + decisionNoText3 + decisionNoText4 + decisionNoText5 + decisionNoText6 + decisionNoText7 + decisionNoText8 + decisionNoText9 + decisionNoText10 + decisionNoText11

        print(decisionNoText)
        speak(decisionNoText)

        decisionNoText12 = "Will Jack accept his offer? Say yes or no"
        print(decisionNoText12)
        speak(decisionNoText12)

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
            decision2TextYes = "But then they must be magic, thought Jack. He accepts the offer and starts the journey home to tell his mother about the magic beans."

            print(decision2TextYes)
            speak(decision2TextYes)

            #Change to true so access the right choice 2
            soldCow = True
            break

        elif decision2 == "no" or decision2 == "No":
            decision2TextNo1 = "Jack returns home with the cow. "
            decision2TextNo2 = "The salesman said it was fine and went back to talking to other customers. When Jack turned around he saw that everyone else had gone home, so now he had no one to sell the cow to. "
            decision2TextNo3 = "He decided to go home and try again the next day. "

            decision2TextNo = decision2TextNo1 + decision2TextNo2 + decision2TextNo3

            print(decision2TextNo)
            speak(decision2TextNo)

            break

        elif not decision2 == "yes" or decision2 == "no":
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

        elif decision2 == []:
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
    elif not decision == "yes" or decision == "no":
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
    elif decision == []:
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
    elif soldCow == False:
        while True:
            choice22Text1 = "Jack gets home and goes to bed. The next day, the cow is gone."
            print(choice22Text1)
            speak(choice22Text1)
            break

#WHEN THE TWO STORIES  CATCHES UP TO ONE ANOTHER
choice2text = "Hello bitches"