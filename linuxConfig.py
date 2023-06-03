import os
from PIL import Image, ImageDraw

def linuxConfig():
    #Find Directory path
    data = os.path.dirname(__file__)+"/data"
    
    #Check for libraries
    os.system("echo [97mInstalling required libraries[0m")

    if os.system("pip install -r requirements.txt") == 0:
        os.system("echo [92m    Successfully installed required libraries[0m")
    else:
        os.system("echo [91m    Was not able to install required libraries")
        os.system("echo     Make sure you have \"requirements.txt\" and that \"pip\" is installed and then restart this program[0m")
        os.system("pause >nul")
        exit()

    #Check for data folder
    os.system("echo [97mChecking for data folder[0m")
    if os.path.isdir(data) == False:
        os.system("echo [91m    Could not find data folder[0m")

        os.system("mkdir "+data)
        os.system("echo [92m    Created data folder[0m")
    else:
        os.system("echo [92m    Found data folder[0m")

    #Check if certain files exist, if not, make it so!
    #Check for sourceImage.png
    os.system("echo [97mChecking for sourceImage.png[0m")
    if os.path.isfile(data+"/sourceImage.png") == False:
        os.system("echo [91m    Could not find sourceImage.png[0m")

        img = Image.new("RGB",(100,100),color="blue")
        img.save(data+"/sourceImage.png")
        os.system("echo [92m    Created sourceImage.png[0m")
    else:
        os.system("echo [92m    Found sourceImage.png[0m")

    #Check for extractedText.txt
    os.system("echo [97mChecking for extractedText.txt[0m")
    if os.path.isfile(data+"/extractedText.txt") == False:
        os.system("echo [91m    Could not find extractedText.txt[0m")

        os.system("echo >nul > "+data+"/extractedText.txt")
        if os.path.isfile(data+"/extractedText.txt") == False:
            os.system("echo [91m    Was unable to create extractedText.txt[0m")
        else:
            os.system("echo [92m    Created extractedText.txt[0m")
    else:
        os.system("echo [92m    Found extractedText.txt[0m")

    #Check for settings.txt
    os.system("echo [97mChecking for settings.txt[0m")
    try:
        with open(data+"/settings.txt") as f:
            os.system("echo [92m    There are pre-saved Settings[0m")
    except IOError:
        os.system("echo [91m    Could not find settings.txt[0m")
        with open(data+"/settings.txt","w") as f:
            f.write("doLoop: 0\nloopCount: 1\nsec: 0\nx: 0\ny: 0\nwidth 100\nheight: 100\nraw: 0")
            os.system("echo [92m    Created settings.txt[0m")