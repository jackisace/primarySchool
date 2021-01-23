from clear import clear
from helpModule import Help
from random import randint

riddles = [["What gets bigger, when you take from it?", "hole"], ["I travel the world, but never leave my corner, what am I?", "stamp"], ["I have holes but I can still hold water, what am I?", "sponge"]]

def riddle():
    clear("")
    riddle = riddles[randint(0,2)]
    tries = 0
    while tries < 5:
        answer = input(riddle[0]+"\n")
        if "quit" in answer:
            quit()
        if "help" in answer:
            if Help("Riddle of the day") == 1:
                return 1
        if answer.lower() == riddle[1].lower():
            print("Well done! that is the right answer!")
            input("")
            return
        else:
            print("Unlucky, try again!\n")
            tries += 1
    print("Unlucky, the answer was {}!".format(riddle[1]))

    

