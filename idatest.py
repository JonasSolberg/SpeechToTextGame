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
        emptyText = "You either didn't say anything or you didn't talk loud enough. Could you repeat your answer"
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
        choice21Text1 = "When Jack got home, he ran to his mother to tell her about the magic bean. "
        choice21Text2 = "Mother! He yelled. She walked up to him and asked why he was yelling. "
        choice21Text3 = "I sold the cow mother! Look! He said, showing her the bean. "
        choice21Text4 = "Beans, she said with a confused look. Where is the money, she asked. "
        choice21Text5 = "I sold the cow for these beans mother, they are magical! He said with enthusiasm. "
        choice21Text6 = "You stupid, stupid boy! We needed the money, she said. "
        choice21Text7 = "Jack got angry by hearing this. But mother, they are magical! Just look at them! he said. "
        choice21Text8 = "I do not want to hear it, get them away from me, the mother said. "
        choice21Text9 = "Jack did not like seeing his mother so angry. What should Jack do? Give the beans to the mother or Leave them on the kitchen counter"
        choice21Text10 = "Say Mother to give them to the mother og say Not to put them on the counter"

        choice21Text = choice21Text1 + choice21Text2 + choice21Text3 + choice21Text4 + choice21Text5 + choice21Text6 + choice21Text7 + choice21Text8 + choice21Text9 + choice21Text10

        print(choice21Text)
        speak(choice21Text)

        #RECORD THE USERS CHOICE
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
        answer = text

        # IF JACK GAVE THE BEANS TO THE MOTHER
        if answer == "mother":
            choice21Text11 = "Jack gathers all the beans in one hand and stretches out his hand towards his mother. "
            choice21Text12 = "I do not want to look at those beans anymore! She says. She takes the beans from Jack and throws them out of the window. "
            choice21Text13 = "Jack watches in disbelief. He wants to cry, but not in front of his mother. He runs to his bedroom and stays there the rest of the night. "
            choice21Text14 = "They did not have money for food anyway, so he does not have to go out to get dinner. "
            choice21Text15 = "He falls asleep, thinking about the magic beans. Maybe they were not magic after all…"

            choice21Text = choice21Text11 + choice21Text12 + choice21Text13 + choice21Text14 + choice21Text15

            print(choice21Text)
            speak(choice21Text)

            break

        # IF JACK LEFT THE BEANS ON THE TABLE
        elif answer == "not":
            choice21Text21 = "Jack does not want to argue with his mother anymore. He puts the beans on the dinner table and starts walking towards his room. "
            choice21Text22 = "No! His mother yells. She continues: Since you bought the beans, then you can go out and plant the beans. Maybe we will have beans to eat in a few days. "
            choice21Text23 = "Jack takes the beans and goes out in the garden. After 20 minutes of work, the gardening is done. "
            choice21Text24 = "Jack goes inside, dirty and hungry, but they do not have anything to eat, so he has to go to bed hungry. "
            choice21Text25 = "He falls asleep, thinking about the magic beans. Maybe they were not magic after all… "

            choice21Text = choice21Text21 + choice21Text22 + choice21Text23 + choice21Text24 + choice21Text25

            print(choice21Text)
            speak(choice21Text)

            break

        # CHOICE 1: Did not say a valid answer
        elif not answer == "mother" or answer == "not":
            decisionAnswer = "Your decision was not one of the requested ones, say your decision again"
            speak(decisionAnswer)
            print(decisionAnswer)

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
            answer = text

        # IF THE USER DIDNT SAY ANYTHING OR TALKED LOUD ENOUGH
        elif answer == []:
            emptyText = "You either didn't say anything or you didn't talk loud enough. Could you repeat your answer. Say Mother or say Not"
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
            answer = text

    # CHOICE 2.2: JACK RETURNS WITH THE COW
    elif soldCow == False:
            choice22Text1 = "When Jack gets home, his mother sees him and the cow through the window. Why do you still have the cow, she asked. "
            choice22Text2 = "There was no one at the market who offered me a good deal for her, he said. Well, then you try again tomorrow, his mother said. "
            choice22Text3 = "Jack went to bed that night, thinking what would have happened if he accepted the beans. "

            #THE COW IS GONE
            choice22Text4 = "The next morning Jack wakes up to his mother yelling. NO, Those damn thieves, she shouts. Jack goes outside and sees that the cow is gone and that the gate is broken. "
            choice22Text5 = "Someone stole our cow Jack, his mother said. Jack looks down at the ground. Close to the gate, there is a ripped piece of clothing. "
            choice22Text6 = "The thief must have gotten his pocket stuck in the gate and ruined it. When he gets closer, he can see a small bag with something in it. "
            choice22Text7 = "When he opens it, he sees that there are beans inside of it. Mother, he said, The thief must have lost this when he stole the cow. "
            choice22Text8 = " Beans will not make this better, she yelled. She took the bag and threw it away. Jack could see the beans flying around in the air, landing in the garden. "
            choice22Text9 = "Jack spent the rest of the day looking for berries in the forest so that he and his mother would have something to eat that day. "
            choice22Text10 = "It helped with hunger, but he knew that he could not survive on berries for too long. He went to sleep worried about his mother as well. "

            choice22Text = choice22Text1 + choice22Text2 + choice22Text3 + choice22Text4 + choice22Text5 + choice22Text6 + choice22Text7 + choice22Text8 + choice22Text9 + choice22Text10

            print(choice22Text)
            speak(choice22Text)
            break

#WHEN THE TWO STORIES CATCHES UP TO ONE ANOTHER AFTER JACK GETS HOME AND HAS SLEPT
#CHOICE 3: CLIMB THE BEANSTALK -------------------------------------------------------------------------------------------------
choice3text1 = ""

choice3text = choice3text1

print(choice3text)
speak(choice3text)