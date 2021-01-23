from helpModule import Help
from spellModule import spell
from wordModule import word
from clear import clear



def workbook():
    """Workbook module, the projects main word processing function. Makes use of wordModule and spellModule. 
    Calculations are carried out within this module"""
    historyFile = open("history.txt", "r")
    history = historyFile.read()
    historyFile.close
    msg = ""
    while True:
        clear(msg)
        msg = ""
        print("history: \n" + history)
        print("Workbook")
        print("========")
        try:
            ui = input("\nEnter calculations (ie. 7*3) or just write notes :)\n\n")
        except IndexError:
            continue
        if "quit" == ui:
            return
        if "q" == ui:
            return
        if "h" == ui:
            if Help("Workbook") == 1:
                return
            continue
        if "help" == ui:
            if Help("Workbook") == 1:
                return
            continue
        isCalc = True
        for char in ui:
            if char.isalpha():
                isCalc = False
        if isCalc:
            if "+" in ui:
                a = float(ui.split("+")[0])
                b = float(ui.split("+")[1])
                c = a+b
                st = "{}+{}={}\n".format(a, b, c)
                st = st.replace(".0", "")
                history += st
                print(st)
            elif "-" in ui:
                a = float(ui.split("-")[0])
                b = float(ui.split("-")[1])
                c = a-b
                st = "{}-{}={}\n".format(a, b, c)
                st = st.replace(".0", "")
                history += st
                print(st)
            elif "*" in ui:
                a = float(ui.split("*")[0])
                b = float(ui.split("*")[1])
                c = a*b
                st = "{}*{}={}\n".format(a, b, c)
                st = st.replace(".0", "")
                history += st
                print(st)
            elif "/" in ui:
                a = float(ui.split("/")[0])
                b = float(ui.split("/")[1])
                c = a/b
                st = "{}/{}={}\n".format(a, b, c)
                st = st.replace(".0", "")
                history += st
                print(st)
        else:
            ui = spell(ui)
            ui = word(ui)
            history += ui + "\n"

        historyLines = history.count("\n")
        while historyLines > 19:
            found = history.find("\n", 2)
            history = history[found:]
            historyLines = history.count("\n")

        historyFile = open("history.txt", "w")
        historyFile.write(history)
        historyFile.close
            



