import os 


def getHoleCount():

    loopBoolean = True
    holeCount = ""

    while loopBoolean:
        print("How many holes are you playing today?\n")

        holeCount = input("9 or 18 ")

        if holeCount == "9" or holeCount == "18":
            loopBoolean = False
            break
        
        os.system("clear")

    return int(holeCount)
