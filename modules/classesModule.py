from clear import clear
from helpModule import Help

allClasses = ["Art", "Science", "Maths", "English", "History", "Drama", "Music", "PE", "Cooking", "IT"]

def undoChanges(undoClasses):
    """ Used for undoing the changes this session"""
    classesFile = open("classes.txt", "w")
    for eachClass in undoClasses:
            classesFile.write(eachClass)
            classesFile.write("\n")
    classesFile.close()
    return undoClasses

def acceptChanges(currentClasses):
    """used to accept the changes this session"""
    classesFile = open("classes.txt", "w")
    for eachClass in currentClasses:
            classesFile.write(eachClass)
            classesFile.write("\n")
    classesFile.close()




def classes():
    """Classes module, for students to see and update the day's classes"""
    classesFile = open("classes.txt", "r")
    currentClasses = classesFile.read().split("\n")
    undoClasses = []
    for eachClass in currentClasses:
        undoClasses.append(eachClass)
    classesFile.close()
    classesFile = None
    while True:
        clear("")
        print("Classes")
        print("=======")
        print("\n\nYour classes for today are: \n")
        for i in range(1,5):
            print("{}) {}".format(i, currentClasses[i-1]))
        print("\nupdate) update your classes")
        print("accept) accept changes")
        print("delete) delete changes")
        print("quit) main menu")
        try:
            user = input("\n")[0]
        except IndexError:
            continue
        if "h" in user:
            if Help("Classes") == 1:
                return
        if "a" in user:
            acceptChanges(currentClasses)
            continue
        if "d" in user:
            currentClasses = undoChanges(undoClasses)
            continue
        if "q" in user:
            return
        if "u" in user:
            print("Classes")
            print("=======")
            print("\n\nYour classes for today are: ")
            i = 0
            clear("")

            for i in range(1,5):
                print("{}) {}".format(i, currentClasses[i-1]))
            userA = input("\nplease select which one you need to update: \n\n") 

            if userA == "q":
                return
            if userA == "quit":
                return
            if userA == "h":
                if Help("Classes") == 1:
                    return
            if userA == "help":
                if Help("Classes") == 1:
                    return
            userA = int(userA) - 1

            j = 0
            clear("")
            for eachAllclass in allClasses:
                if j < len(allClasses) - 1:
                    j += 1
                    print("{}) {}".format(j, eachAllclass))
            userB = input("please select which one you need to update to: ")

            if userB == "q":
                return
            if userB == "quit":
                return
            if userB == "h":
                if Help("Classes") == 1:
                    return
            if userB == "help":
                if Help("Classes") == 1:
                    return
            userB = int(userB) - 1

            currentClasses[userA] = allClasses[userB]






