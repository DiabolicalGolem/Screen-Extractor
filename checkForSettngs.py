import os
from PIL import Image, ImageDraw

#Find Directory path
data = os.path.dirname(__file__)+"\\data"

def checkForSettings():
    #Check for data folder
    os.system("ECHO [97mChecking for data folder[0m")
    if os.path.isdir(data) == False:
        os.system("ECHO [91m    Could not find data folder[0m")

        os.system("MKDIR "+data)
        os.system("ECHO [92m    Created data folder[0m")
    else:
        os.system("ECHO [92m    Found data folder[0m")

    #Check if certain files exist, if not, make it so!
    #Check for sourceImage.png
    os.system("ECHO [97mChecking for sourceImage.png[0m")
    if os.path.isfile(data+"\\sourceImage.png") == False:
        os.system("ECHO [91m    Could not find sourceImage.png[0m")

        img = Image.new("RGB",(100,100),color="blue")
        img.save(data+"\\sourceImage.png")
        os.system("ECHO [92m    Created sourceImage.png[0m")
    else:
        os.system("ECHO [92m    Found sourceImage.png[0m")

    #Check for extractedText.txt
    os.system("ECHO [97mChecking for extractedText.txt[0m")
    if os.path.isfile(data+"\\extractedText.txt") == False:
        os.system("ECHO [91m    Could not find extractedText.txt[0m")

        os.system("ECHO. > "+data+"\\extractedText.txt")
        os.system("ECHO [92m    Created extractedText.txt[0m")
    else:
        os.system("ECHO [92m    Found extractedText.txt[0m")

    #Check for settings.txt
    os.system("ECHO [97mChecking for settings.txt[0m")
    try:
        with open(data+"\\settings.txt") as f:
            os.system("ECHO [92m    There are pre-saved Settings[0m")
    except IOError:
        os.system("ECHO [91m    Could not find settings.txt[0m")
        with open(data+"\\settings.txt","w") as f:
            f.write("doLoop: 0\nloopCount: 1\nsec: 0\nx: 0\ny: 0\nwidth 100\nheight: 100\nraw: 0")
            os.system("ECHO 49[92m    Created settings.txt[0m")