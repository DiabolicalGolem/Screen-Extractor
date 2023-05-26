import os
import pyautogui
import time
from pynput.keyboard import Key, Controller
from PIL import Image
from pytesseract import pytesseract

#Find Directory Path
dir = os.path.dirname(__file__)
data = os.path.dirname(__file__)+"\\data"
imagePath = data+"\\sourceImage.png"
pathToTess = data+"\\tesseract\\tesseract.exe"
line = set()
accept = False

#Screenshots a region of the screen
def extract(x,y,width,height):
    oldImageTimeStamp = os.path.getmtime(data+"\\sourceImage.png")

    screenshot = pyautogui.screenshot(region=(x,y,width,height))
    bwShot = screenshot.convert('L')    #Converts screenshot to BW
    bwShot.save(imagePath)  #Saves BW Screenshot

    newImageTimeStamp = os.path.getmtime(data+"\\sourceImage.png")

    if oldImageTimeStamp != newImageTimeStamp:    
        os.system("ECHO [92mSuccessfully [97msaved screen shot to [93msourceImage.png[97m")
    else:
        os.system("ECHO [91mFailed [97mto save screen shot to [93msourceImage.png[97m")

#Sends keystrokes based on extractedText.txt
def autoWrite(txt,loop,sec):
    keyboard = Controller()

    #Loops for lenght specified by the loop variable
    for i in range(loop):
        keyboard.type(str(txt))
        time.sleep(sec)
    
    os.system("ECHO [92mSuccessfully [97mused [93mautoWrite[97m")

#Reads text from sourceImage.png and saves the raw output
def rawRead():
    try:
        img = Image.open(imagePath)
    except IOError:
        os.system("ECHO [91mCould not find [93msourceImage.png[97m")


    pytesseract.tesseract_cmd = pathToTess

    custom_config = r'-l eng --oem 1 --psm 6 -c preserve_interword_spaces=1'
    
    try:
        text = pytesseract.image_to_string(img, config=custom_config)
        os.system("ECHO [92mSuccessfully [97mextracted text from [93msourceImage.png[97m")
    except IOError:
        os.system("ECHO [91mFailed [97mto extract text from [93msourceImage.png[97m")

    return text[:-1]

#Reads text from sourceImage.png and saves the formatted output
def screenRead():
    try:
        img = Image.open(imagePath)
    except IOError:
        os.system("ECHO [91mCould not find [93msourceImage.png[97m")

    pytesseract.tesseract_cmd = pathToTess
    try:
        text = pytesseract.image_to_string(img)
        os.system("ECHO [92mSuccessfully [97mextracted text from [93msourceImage.png[97m")
    except IOError:
        os.system("ECHO [91mFailed [97mto extract text from [93msourceImage.png[97m")

    return text[:-1]

#Settings
def setting():
    global line, accept

    with open(data+"\\settings.txt") as f:
        settingsLines = f.readlines()

    os.system("ECHO [32m                 Settings")
    os.system("ECHO [90mUse \"help\" to see accepted tokens[97m")
    print("[97m".join(settingsLines))

    while True:
        rootQuery = input("[93m>[0m")

        if rootQuery.lower() == "exit":
            break

        if rootQuery.lower() == "help":
            accept = True
            os.system("ECHO [32mAccepted tokens:")
            os.system("ECHO     \"exit\", \"list\", \"help\", \"help vars\", \"cls\"[0m")

        if rootQuery.lower() == "list":
            accept = True
            os.system("ECHO [97m")
            print("".join(settingsLines))

        if rootQuery.lower() == "help vars":
            accept = True
            os.system("ECHO [32mAccepted variables:")
            os.system("ECHO     \"doLoop\", \"loopCount\", \"sec\", \"x\", \"y\", \"height\", \"width\", \"raw\"[0m")

        if rootQuery.lower() == "cls" or rootQuery.lower() == "clear":
            accept = True
            os.system("CLS")
            os.system("ECHO [90mUse \"help\" at any time to get help if you get stuck.[0m")

        if (rootQuery == "doLoop" or rootQuery == "loopCount"
            or rootQuery == "sec" or rootQuery == "x" or rootQuery == "y"
            or rootQuery == "height" or rootQuery == "width"
            or rootQuery == "raw"):
                
            while True:
                accept = False
            
                query = input("[93m"+rootQuery + ">[0m")

                if query.lower() == "back":
                    break

                if query.lower() == "cls" or query.lower() == "clear":
                    accept = True
                
                    os.system("CLS")
                    os.system("ECHO [90mUse \"help\" at any time to get help if you get stuck.[0m")
                    
                if query.lower() == "help":
                    accept = True
                
                    if rootQuery == "doLoop":
                        print(
                            "[32mAccepted inputs:\n    \"1\" (True), \"0\" False\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "loopCount":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only (1-100)\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "sec":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only (0-100)\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "x":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "y":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "height":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only\n    or  \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "width":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "raw":
                        print(
                            "[32mAccepted inputs:\n    \"True\", \"False\"\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                if (rootQuery == "doLoop" or rootQuery
                    == "raw") and (query == "1" or query == "0"):
                    if rootQuery == "doLoop":
                        line = 0
                    if rootQuery == "raw":
                        line = 7
                    accept = True

                if (rootQuery == "loopCount" or rootQuery == "sec" or rootQuery
                    == "x" or rootQuery == "y" or rootQuery == "height"
                    or rootQuery == "width") and query.isdigit():                
                    if (rootQuery == "loopCount") and (int(query) >= 1
                                                    and int(query) <= 100):
                        line = 1
                        accept = True

                    if (rootQuery == "sec" or rootQuery == "x" or rootQuery == "y"
                            or rootQuery == "height"
                            or rootQuery == "width") and (query.isdigit()):
                        accept = True

                        if rootQuery == "sec":
                            line = 2
                        if rootQuery == "x":
                            line = 3
                        if rootQuery == "y":
                            line = 4
                        if rootQuery == "width":
                            line = 5
                        if rootQuery == "height":
                            line = 6
                        
                if accept == False and query != "":
                    os.system("ECHO [91m\"" + query +"\" is not recognized as a valid input![0m")

                if (line != set()) and accept == True:
                    settingsLines[line] = rootQuery + ": " + query + "\n"

                    with open(data+"\\settings.txt", "w") as f:
                        f.write("".join(settingsLines))

                    line = set()

                    os.system("ECHO [32mChanged \"" + rootQuery + "\" to \"" + query + "\"[0m")
                
                accept = False
            
        elif accept == False and rootQuery != "":
            os.system("ECHO [91m\"" + rootQuery +"\" is not recognized as a valid input![0m")