
library = ["humans", "building", "structure", "architecture", "home", "house", "hut", "animal", "beast", "creature", "pet"]
vowels = "aeiou"

def spell(line):


    for lineWord in line.split(" "):
        if lineWord in library:
            continue
        for libraryWord in library:
            if lineWord == libraryWord:
                continue
            if libraryWord[0] == lineWord[0]:
                accuracy = 0
                for lineLetter in lineWord:
                    if lineLetter in libraryWord: 
                        accuracy += 1

                if accuracy > len(libraryWord)/2:
                    print("by {}, did you mean {}?".format(lineWord, libraryWord))
                    answer = input("y/n: ")
                    if "y" in answer:
                        line = line.replace(lineWord, libraryWord)

    return line
                        
                    



