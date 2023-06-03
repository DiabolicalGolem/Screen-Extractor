import sys
from config import *

#Check if certain files exist, if not, make it so!
try:
    sys.argv[1] == '-n'
except IndexError or IOError or NameError:
    config()

import os, subprocess, keyboard, mouse
from settings import *
from execute import *

#Import Variables
import variables

print(variables.dir)
os.system(f"cd {variables.dir}") #Set Path

#Set Extractor variables from settings.txt
with open(variables.dir_settings,"r") as f:
    settings = f.readlines()
    doLoop = bool(int(settings[0].replace("\n","").split(" ")[1]))
    loopCount = int(settings[1].replace("\n","").split(" ")[1])
    sec = int(settings[2].replace("\n","").split(" ")[1])
    sx = int(settings[3].replace("\n","").split(" ")[1])
    sy = int(settings[4].replace("\n","").split(" ")[1])
    width = int(settings[5].replace("\n","").split(" ")[1])
    height = int(settings[6].replace("\n","").split(" ")[1])
    raw = bool(int(settings[7].replace("\n","").split(" ")[1]))

try:
    subprocess.check_output(["clear"], stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError:
    subprocess.run(["cls"], shell=True )

os.system("echo [92m                 Welcome to ScreenExtractor!")
os.system("echo [97mThis program can extract text information from a specified ")
os.system("echo region of your screen and then save it to a [93mfile[97m. ")
os.system("echo [94mSHIFT+ESC [97m= Exit program    [94mALT+N [97m= Set Bounding Box")
os.system("echo [94mALT+M [97m= Extract Screen    [94mALT+, [97m= AutoWrite")
os.system("echo [94mALT+. [97m= Run Both    [94mALT+F11 [97m= Settings")

#Variables for the Bounding box
oldMouse = [0,0]
newMouse = [0,0]

##Put Bounding logic here?
def on_click(x,y,button,pressed):
    if pressed:
        oldMouse[0] = x
        oldMouse[1] = y
    if not pressed:
        newMouse[0] = x
        newMouse[1] = y
        return False

#Hotkey Variables
bool_boundingBox = False
bool_extract = False
bool_autoWrite = False
bool_runBoth = False
bool_settings = False

#Hotkey Logic
#ALT+N (Set bounding box)
def funct_boundingBox():
    global sx, sy, width, height
    
    os.system("echo [93mClick and drag to create Bounding Box[97m")

    mouse.wait(button='left',target_types='down')
    oldMouse = mouse.get_position()
    mouse.wait(button='left',target_types='up')
    newMouse = mouse.get_position()

    #Check against mouse x's
    if oldMouse[0] < newMouse[0]:
        if oldMouse[1] < newMouse[1]:
            sx = oldMouse[0]
            sy = oldMouse[1]
        else:
            sx = oldMouse[0]
            sy = newMouse[1]
    else:
        if oldMouse[1] < newMouse[1]:
            sx = newMouse[0]
            sy = oldMouse[1]
        else:
            sx = newMouse[0]
            sy = newMouse[1]
    
    #Find width and height
    width = abs(oldMouse[0]-newMouse[0])
    height = abs(oldMouse[1]-newMouse[1])

    try:
        with open(variables.dir_settings,'w') as f:
            f.write(f"doLoop: 0\nloopCount: 1\nsec: 0\nx: {str(sx)}\ny: {str(sy)}\nwidth {str(width)}\nheight: {str(height)}\nraw: 0")
            os.system(f"echo [92mSet Bounding Box to: [93m({str(sx)},{str(sy)}), ({str(sx+width)},{str(sy+height)})[97m")
    except IOError:
        os.system("echo [91mCould not set Bounding Box.[97m")
    
    os.system("echo [32m----------------------End of function----------------------[97m")

#ALT+M (Extract screen)
def funct_extract():
    extract(sx,sy,width,height)

    #Saves raw, unaltered text to extractedText.txt
    try:
        if raw:
            oldTextTimeStamp = os.path.getmtime(variables.dir_extractedText)

            with open(variables.dir_extractedText, 'w') as f:
                f.write(rawRead())

            newTextTimeStamp = os.path.getmtime(variables.dir_extractedText)

            if oldTextTimeStamp != newTextTimeStamp:
                os.system("echo [92mSuccessfully [97msaved extracted text to [93mextractedText.txt[97m")
            else:
                os.system("echo [91mFailed [97mto save extracted text to [93mextractedText.txt[97m")
        
        #Saves formatted text to extractedText.txt
        else:
            oldTextTimeStamp = os.path.getmtime(variables.dir_extractedText)

            with open(variables.dir_extractedText,'w') as f:
                f.write(screenRead())
            
            newTextTimeStamp = os.path.getmtime(variables.dir_extractedText)

            if oldTextTimeStamp != newTextTimeStamp:
                os.system("echo [92mSuccessfully [97msaved extracted text to [93mextractedText.txt[97m")
            else:
                os.system("echo [91mFailed [97mto save extracted text to [93mextractedText.txt[97m")
        
        os.system(f"start {variables.dir_extractedText}")
    except:
        os.system("echo [91mFailed to execute properly. Make sure Tesseract is installed!")
    
    os.system("echo [32m----------------------End of function----------------------[97m")

#ALT+, (AutoWrite)
def funct_autoWrite():
    text = open(variables.dir_extractedText,'r').read()

    if text != "":
        autoWrite(text,loopCount,sec)
    else:
        os.system("echo [93mextractedText.txt[97m is [91mempty[97m")
    
    if loopCount == 1:
        os.system("echo [97m     Looped 1 time")
    else:
        os.system(f"echo [97m     Looped {loopCount} times")

    os.system("echo [32m----------------------End of function----------------------[97m")

#ALT+. (Run both)
def funct_runBoth():
    for i in range(loopCount):
        extract(sx,sy,width,height)

        if raw:
            oldTextTimeStamp = os.path.getmtime(variables.dir_extractedText)

            with open(variables.dir_extractedText, 'w') as f:
                f.write(rawRead())
            
            newTextTimeStamp = os.path.getmtime(variables.dir_extractedText)

            if oldTextTimeStamp != newTextTimeStamp:
                os.system("echo [92mSuccessfully [97msaved extracted text to [93mextractedText.txt[97m")
            else:
                os.system("echo [91mFailed [97mto save extracted text to [93mextractedText.txt[97m")
                break
        else:
            oldTextTimeStamp = os.path.getmtime(variables.dir_extractedText)

            with open(variables.dir_extractedText, 'w') as f:
                f.write(screenRead())
            
            newTextTimeStamp = os.path.getmtime(variables.dir_extractedText)
            
            if oldTextTimeStamp != newTextTimeStamp:
                os.system("echo [92mSuccessfully [97msaved extracted text to [93mextractedText.txt[97m")
            else:
                os.system("echo [91mFailed [97mto save extracted text to [93mextractedText.txt[97m")
                break
        
        text = open(variables.dir_extractedText,"r").read()

        if text != "":
            autoWrite(text,loopCount,sec)
        else:
            os.system("[93mextractedText.txt[97m is [91mempty[97m")
            break
    
    if loopCount == 1:
        os.system("echo [97m     Looped 1 time")
    else:
        os.system(f"echo [97m     Looped {loopCount} times")

    os.system("echo [32m----------------------End of function----------------------[97m")

#ALT+F11 (Settings)
def funct_setting():
    setting()
    os.system("echo [32m----------------------End of function----------------------[97m")
    os.system(f"{sys.executable} {sys.argv[0]} -n")

os.system("echo [32m-----------------------Program ready-----------------------[97m")

#Main Loop
while True:
    keyboard.add_hotkey('alt+n', funct_boundingBox)
    keyboard.add_hotkey('alt+m', funct_extract)
    keyboard.add_hotkey('alt+comma', funct_autoWrite)
    keyboard.add_hotkey('alt+period', funct_runBoth)
    keyboard.add_hotkey('alt+f11', funct_setting)

    keyboard.wait('shift+esc')
    exit()