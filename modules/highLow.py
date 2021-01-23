from clear import clear
from helpModule import Help
from random import randint

def highLow():
    """Higher or Lower game module"""
    score = 0
    while True:
        number = randint(0,100)
        nextNumber = randint(0,100)
        clear("")
        print("quit) quit to main menu\n")
        answer = input("The number is {}, will the next one be higher or lower?: ".format(number))
        if "q" in answer:
            return
        if "help" in answer:
            if Help("Higher or Lower") == 1:
                return 1
            continue
        elif "h" in answer:
            if number < nextNumber:
                score += 1
                if score == 3:
                    print("Well done, you have won!")
                else:
                    print("Well done! you have got {} in a row, get 3 to win".format(score))
            else:
                score = 0
                print("Unlucky, keep trying!")
        elif "l" in answer:
            if number > nextNumber:
                score += 1
                if score == 3:
                    print("Well done, you have won!")
                else:
                    print("Well done! you have got {} in a row, get 3 to win".format(score))
            else:
                score = 0
                print("Unlucky, keep trying!")
        input("Press Enter to continue")
        if score == 3:
            return

        



