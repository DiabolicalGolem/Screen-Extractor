import os
import pyautogui
import time
import keyboard
from PIL import Image
from pytesseract import pytesseract
import variables

#Settings Variables
line = set()
accept = False

#Screenshots a region of the screen
def extract(x,y,width,height):
    oldImageTimeStamp = os.path.getmtime(variables.dir_imagePath)

    screenshot = pyautogui.screenshot(region=(x,y,width,height))
    bwShot = screenshot.convert('L')    #Converts screenshot to BW
    bwShot.save(variables.dir_imagePath)  #Saves BW Screenshot

    newImageTimeStamp = os.path.getmtime(variables.dir_imagePath)

    if oldImageTimeStamp != newImageTimeStamp:    
        os.system("echo [92mSuccessfully [97msaved screen shot to [93msourceImage.png[97m")
    else:
        os.system("echo [91mFailed [97mto save screen shot to [93msourceImage.png[97m")

#Sends keystrokes based on extractedText.txt
def autoWrite(txt,loop,sec):
    #Loops for lenght specified by the loop variable
    for i in range(loop):
        keyboard.write(txt,sec,restore_state_after=True)
    
    os.system("echo [92mSuccessfully [97mused [93mautoWrite[97m")

#Reads text from sourceImage.png and saves the raw output
def rawRead():
    try:
        img = Image.open(variables.dir_imagePath)
    except IOError:
        os.system("echo [91mCould not find [93msourceImage.png[97m")


    pytesseract.tesseract_cmd = variables.dir_pathToTess

    custom_config = r'-l eng --oem 1 --psm 6 -c preserve_interword_spaces=1'
    
    try:
        text = pytesseract.image_to_string(img, config=custom_config)
        os.system("echo [92mSuccessfully [97mextracted text from [93msourceImage.png[97m")
    except IOError:
        os.system("echo [91mFailed [97mto extract text from [93msourceImage.png[97m")
        os.system("echo [91mMake sure you have \"Tesseract OCR\" installed![97m")
        raise Exception

    return text[:-1]

#Reads text from sourceImage.png and saves the formatted output
def screenRead():
    try:
        img = Image.open(variables.dir_imagePath)
    except IOError:
        os.system("echo [91mCould not find [93msourceImage.png[97m")

    pytesseract.tesseract_cmd = variables.dir_pathToTess
    try:
        text = pytesseract.image_to_string(img)
        os.system("echo [92mSuccessfully [97mextracted text from [93msourceImage.png[97m")
    except IOError:
        text = ""
        os.system("echo [91mFailed [97mto extract text from [93msourceImage.png[97m")
        
    return text[:-1]