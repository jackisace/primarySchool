from clear import clear
from helpModule import Help
from random import randint

operators = ["+", "-"]

def mathsTest():
    """Maths test module"""
    
    correct = 0

    for i in range(0,10):
        operator = randint(0,1)
        operator = operators[operator]
        answer = -1
        if operator == "+":
            a = randint(0,10)
            b = randint(0,10)
            answer = a+b
        if operator == "-":
            while answer < 0:
                a = randint(0,10)
                b = randint(0,10)
                answer = a-b
            
        print("\nquit) to quit to main menu\n")
        valid = False
        while not valid:
            user = input("What is {}{}{}?: ".format(a,operator,b))
            if "help" in user:
                if Help("Maths Test") == 1:
                    return
            if "h" in user:
                if Help("Maths Test") == 1:
                    return
            if "quit" in user:
                return
            if "q" in user:
                return
            try:
                user = int(user)
                valid = True
            except ValueError:
                valid = False
        if user == answer:
            clear("Well done!")
            correct += 1
        else:
            clear("Unlucky! The answer was {}".format(answer))


    if correct == 5 and correct == 6:
        input("\n\nYou got {}/10, well done!".format(correct))
    elif correct == 7 and correct == 8:
        input("\n\nYou got {}/10, really well done!".format(correct))
    elif correct == 9:
        input("\n\nYou got {}/10, Great work!".format(correct))
    elif correct == 10:
        input("\n\nYou got {}/10, Amazing!!".format(correct))
    else:
        input("\n\nYou got {}/10 ".format(correct))



    


