from clear import clear



def Help(strIn):
    clear("")
    print("Help")
    print("====\n")
    print("You are currently in " + strIn)
    print("\nhelp) Ask at any time for help")
    print("quit) Quit program")
    print("main) Main menu")
    print("continue) Continue with the program")
    user = input("\nEnter your selection: ")
    if "help" in user:
        Help(strIn)
    if "h" in user:
        Help(strIn)
    if "quit" in user:
        quit()
    if "q" in user:
        quit()
    if "continue" in user:
        return
    if "c" in user:
        return
    if "main" in user:
        return 1
    if "m" in user:
        return 1

