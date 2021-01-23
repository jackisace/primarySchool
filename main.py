import sys
sys.path.insert(1, 'modules')

from clear import clear
from helpModule import Help
from workbookModule import workbook
from gamesModule import games
from classesModule import classes
from mathsTest import mathsTest


def main():
    msg = ""
    while True:
        clear(msg)
        msg = ""
        print("Main Menu")
        print("=========")
        print("\n1) Workbook")
        print("2) Todays Classes")
        print("3) Maths Test")
        print("4) Games")
        inputting = True
        while inputting:
            try:
                ui = input("\nEnter your selection:\n\n").lower()[0]
                inputting = False
            except IndexError:
                clear(msg)
                print("Main Menu")
                print("=========")
                print("\n1) Workbook")
                print("2) Todays Classes")
                print("3) Maths Test")
                print("4) Games\n")
                print("You didn't input anything last time, lets try again :)")
                continue

        if "q" in ui:
            
            quit()
        elif "h" in ui:
            Help("Main Menu")
        elif "1" in ui:
            workbook()
        elif "2" in ui:
            classes()
        elif "3" in ui:
            mathsTest()
        elif "4" in ui:
            games()        
        else:
            msg = "I'm sorry, that selection doesn't match any of the options. Press Enter to continue:"
            continue

if __name__ == "__main__":
    main()

