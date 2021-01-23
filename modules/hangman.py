from clear import clear
from helpModule import Help
import random

def hangman():
    """Hangman game module"""
    
    words = ["blaze", "skate", "eagle", "chill"]
    word = words[random.randint(0,3)]

    playing = True
    guesses = 0
    wrongGuesses = 0
    hidden = []
    guessedLetters = []

    hanger = ["""







    """,
    """







    =================""",
    """
          ||               
          ||               
          ||               
          ||               
          ||               
          ||               
          ||               
    =================""", 
    """
          =======         
          ||              
          ||              
          ||              
          ||              
          ||              
          ||              
    =================""", 
    """
          =======         
          ||              
          ||              
          ||              
          ||              
         /||              
        //||              
    =================""", 
    """
          =======         
          ||              
          ||              
          ||              
          ||              
         /||\             
        //||\\\\          
    =================""", 
    """
          =======         
          ||//            
          ||/             
          ||              
          ||              
         /||\             
        //||\\\\          
    =================""", 
    """
          =======         
          ||//  |         
          ||/             
          ||              
          ||              
         /||\             
        //||\\\\        
    =================""", 
                          
    """
          =======         
          ||//  |         
          ||/   O         
          ||  --:--       
          ||    n         
         /||\  / \        
        //||\\\\          
    =================""",]

    for letter in word:
        hidden.append("-")

    while playing:
        print(hanger[wrongGuesses])
        if wrongGuesses == 8:
            print("Unlucky, the word was " + word + " better luck next time!")
            input("")
            playing = False
            continue
        display = "Display: "
        hiddenStr = ""
        for letter in hidden:
            hiddenStr += letter
        print(display + hiddenStr)
        if hiddenStr in word:
            print("Congratulations, you have won! The word was {} and it took {} guesses".format(word, guesses))
            input("")
            playing = False
            continue

        valid = False
        while not valid:
            repeat = False
            guess = input("Enter letter to guess: ")
            if "help" in guess:
                if Help("Hangman") == 1:
                    return 1
            guess = guess[0]
            
            for letter in guessedLetters:
                if guess is letter:
                    repeat = True
                    print("You already tried that letter, try again :)")
            if not repeat:
                valid = True
        guessedLetters.append(guess)

        i = 0
        correct = False
        for letter in word:
            if guess in letter:
                hidden[i] = guess
                correct = True
            i += 1
        if not correct:
            wrongGuesses += 1
        guesses += 1

