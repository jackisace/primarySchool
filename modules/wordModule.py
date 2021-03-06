from clear import clear



def word(line):
    """Word module acts as a thesaurus, is called every time the user inputs a line into the wrkbook module"""

    library = [["building", "structure", "architecture", "home", "house", "hut"], ["animal", "beast", "creature", "pet"]]

    for item in library:
        found = False
        for libraryWord in item:
            if found:
                break
            for lineWord in line.split(" "):
                if found:
                    break
                if libraryWord in lineWord:
                    answer = input("By {}, did you mean any of these? \n{} \ny/n: ".format(lineWord, item))
                    if "y" in answer:
                        library.remove(item)
                        line += " ("
                        for word in item:
                            line += word + " "
                        line = line[:len(line)-1] +  ")"
                        found = True

    return line



