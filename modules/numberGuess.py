from clear import clear
from helpModule import Help
from random import randint

def numberGuess():
    number = randint(0,100)
    guessed = False
    guesses = 0
    while not guessed:
        user = input("Guess your number between 0 and 100: ")
        if "help" in user:
            if Help("Number Guess") == 1:
                return 1
        if "q" in user:
            return
        user = int(user)
        guesses += 1
        if user < number:
            print("Higher")
        elif user > number:
            print("Lower")
        elif user == number:
            print("Congratulations! you got it right in {} guesses".format(guesses))
            input("")
            guessed = True
    return


