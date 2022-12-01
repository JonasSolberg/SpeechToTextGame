#!/use/bin/python

import sys
import os
import cmd
#from playsound import playsound


#Calling the main method
if __name__ == "__main__":
    #main()
    #print("test")

#The game begins
    startGame = input('Would you like to start the game, yes or no?')
    if startGame == 'Yes':
        # print("Begin the game of Jack and the Beanstalk")
        print('Jack takes his cow to the market to sell it and asks the butcher for a trade with magic beans')
        option1 = input('Does Jack want to say yes to the butchers offer or not?')
    else:
        print('Jack is thinking about whether to accept the offer or not')
        exit()  # exit or quit

#The first choice of the game
    if option1 == 'Yes':
        print('Jack gets an offer for the cow and goes home to talks to his mother')
        decision = input('Would you like to accept the offer or not?')
        if decision == 'Accept':
            print('Jack accepts the offer he got for the cow and decides to sell it')
        elif decision == 'Do not accept':
            print('Jack does not accept the offer so he goes to the market')
            decision = input('Do you want to accept to trade the cow for the beans?')
            if decision == 'Accept':
                print('Jack accepts the offer he got for the cow and decides to sell it')
            elif decision == 'Do not accept':
                print('Jack goes to the market to get a better offer for his cow')
                exit()
        else:
            print('This is not a valid option, try again')
            exit()
        next = input('You saw Jack heading towards the market, do you think he should continue to go there or go home')
        if next == 'Continue':
            print('As soon as Jack enters the market, he sees a butcher that might be interested in buying the cow')
            exit()
        elif next == 'Home':
            print('As soon as Jack comes home, he talks with his mother')
            
            
option2 == input('Do you want to throw the beans away or keep them?')
#The second choice of the game
if option2 == 'Throw':
    print('Do you want to keep the beans or throw them out of the window?')
    secondDecision = input('Jack is not happy with the beans so he throws them out, goes to bed and then when he looks out of the window he sees the beanstalk')
    if secondDecision == 'Keep':
        print('Jack wants to keep the beans so he puts them in the kitchen')
    elif secondDecision == 'Throw':
        print('Jack throws the beans out of the window')
        secondDecision = input('Jack keeps the beans')
        if secondDecision == 'Keep':
            print('whatever Jack does after he decides to put the beans in the kitchen')
        elif secondDecision == "Throw":
            print()
            exit()
