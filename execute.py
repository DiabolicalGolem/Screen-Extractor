import os
import subprocess
import platform
import pyautogui
import time
from pynput.keyboard import Key, Controller
from PIL import Image
from pytesseract import pytesseract

#Find OS
operating = platform.system()

#Find Directory Path
if operating == "Windows":
    dir = os.getcwd()
    dir_data = dir+"\\data"
    dir_settings = dir_data+"\\settings.txt"
    dir_imagePath = dir_data+"\\sourceImage.png"
    dir_pathToTess = dir_data+"\\tesseract\\tesseract.exe"
elif operating == "Linux":
    dir = os.getcwd()
    dir_data = os.getcwd()+"/data"
    dir_settings = dir_data+"/settings.txt"
    dir_imagePath = dir_data+"/sourceImage.png"
    dir_pathToTess = dir_data+"/tesseract/tesseract.exe"


#Settings Variables
line = set()
accept = False

#Screenshots a region of the screen
def extract(x,y,width,height):
    oldImageTimeStamp = os.path.getmtime(dir_imagePath)

    screenshot = pyautogui.screenshot(region=(x,y,width,height))
    bwShot = screenshot.convert('L')    #Converts screenshot to BW
    bwShot.save(dir_imagePath)  #Saves BW Screenshot

    newImageTimeStamp = os.path.getmtime(dir_imagePath)

    if oldImageTimeStamp != newImageTimeStamp:    
        os.system("echo [92mSuccessfully [97msaved screen shot to [93msourceImage.png[97m")
    else:
        os.system("echo [91mFailed [97mto save screen shot to [93msourceImage.png[97m")

#Sends keystrokes based on extractedText.txt
def autoWrite(txt,loop,sec):
    keyboard = Controller()

    #Loops for lenght specified by the loop variable
    for i in range(loop):
        keyboard.type(str(txt))
        time.sleep(sec)
    
    os.system("echo [92mSuccessfully [97mused [93mautoWrite[97m")

#Reads text from sourceImage.png and saves the raw output
def rawRead():
    try:
        img = Image.open(dir_imagePath)
    except IOError:
        os.system("echo [91mCould not find [93msourceImage.png[97m")


    pytesseract.tesseract_cmd = dir_pathToTess

    custom_config = r'-l eng --oem 1 --psm 6 -c preserve_interword_spaces=1'
    
    try:
        text = pytesseract.image_to_string(img, config=custom_config)
        os.system("echo [92mSuccessfully [97mextracted text from [93msourceImage.png[97m")
    except IOError:
        os.system("echo [91mFailed [97mto extract text from [93msourceImage.png[97m")
        raise Exception

    return text[:-1]


#Reads text from sourceImage.png and saves the formatted output
def screenRead():
    try:
        img = Image.open(dir_imagePath)
    except IOError:
        os.system("echo [91mCould not find [93msourceImage.png[97m")

    pytesseract.tesseract_cmd = dir_pathToTess
    try:
        text = pytesseract.image_to_string(img)
        os.system("echo [92mSuccessfully [97mextracted text from [93msourceImage.png[97m")
    except IOError:
        text = ""
        os.system("echo [91mFailed [97mto extract text from [93msourceImage.png[97m")
        
    return text[:-1]


#Settings
def setting():
    global line, accept

    with open(dir_settings) as f:
        settingsLines = f.readlines()

    os.system("echo [32m                 Settings")
    os.system("echo [90mUse \"help\" to see accepted tokens[97m")
    print("".join(settingsLines))

    while True:
        rootQuery = input("[93m>[0m")

        if rootQuery.lower() == "exit":
            break

        if rootQuery.lower() == "help":
            accept = True
            os.system("echo [32mAccepted tokens:")
            os.system("echo     \"exit\", \"list\", \"help\", \"help vars\", \"cls\"[0m")

        if rootQuery.lower() == "list":
            accept = True
            os.system("echo [97m")
            print("".join(settingsLines))

        if rootQuery.lower() == "help vars":
            accept = True
            os.system("echo [32mAccepted variables:")
            os.system("echo     \"doLoop\", \"loopCount\", \"sec\", \"x\", \"y\", \"height\", \"width\", \"raw\"[0m")

        if rootQuery.lower() == "cls" or rootQuery.lower() == "clear":
            accept = True
            os.system("CLS")
            os.system("echo [90mUse \"help\" at any time to get help if you get stuck.[0m")

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
                    os.system("echo [90mUse \"help\" at any time to get help if you get stuck.[0m")
                    
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
                    os.system("echo [91m\"" + query +"\" is not recognized as a valid input![0m")

                if (line != set()) and accept == True:
                    settingsLines[line] = rootQuery + ": " + query + "\n"

                    with open(dir_settings, "w") as f:
                        f.write("".join(settingsLines))

                    line = set()

                    os.system("echo [32mChanged \"" + rootQuery + "\" to \"" + query + "\"[0m")
                
                accept = False
            
        elif accept == False and rootQuery != "":
            os.system("echo [91m\"" + rootQuery +"\" is not recognized as a valid input![0m")