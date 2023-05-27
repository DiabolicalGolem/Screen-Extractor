import os
import sys
from pynput import keyboard, mouse
from execute import extract, autoWrite, rawRead, screenRead, setting
from config import config

#Initialize
combo = [
    {keyboard.Key.shift, keyboard.Key.esc},             #Exit program
    {keyboard.Key.alt_l, keyboard.KeyCode(char="n")},   #Set Bounding Box
    {keyboard.Key.alt_l, keyboard.KeyCode(char="m")},   #Extract screen
    {keyboard.Key.alt_l, keyboard.KeyCode(char=",")},   #AutoWrite
    {keyboard.Key.alt_l, keyboard.KeyCode(char=".")},   #Run both
    {keyboard.Key.alt_l, keyboard.Key.f11}              #Settings
]

current = set()

#Find and set Directory path
dir = os.path.dirname(__file__)
data = os.path.dirname(__file__)+"\\data"
os.system("cd "+dir) #Set Path

#Variables for the Bounding box
oldMouse = [0,0]
newMouse = [0,0]

awrite = False
bwrite = False

#Check if certain files exist, if not, make it so!
config()

#Set Extractor variables from settings.txt
with open(data+"\\settings.txt","r") as f:
    settings = f.readlines()
    doLoop = bool(int(settings[0].replace("\n","").split(" ")[1]))
    loopCount = int(settings[1].replace("\n","").split(" ")[1])
    sec = int(settings[2].replace("\n","").split(" ")[1])
    sx = int(settings[3].replace("\n","").split(" ")[1])
    sy = int(settings[4].replace("\n","").split(" ")[1])
    width = int(settings[5].replace("\n","").split(" ")[1])
    height = int(settings[6].replace("\n","").split(" ")[1])
    raw = bool(int(settings[7].replace("\n","").split(" ")[1]))

os.system("cls")
os.system("echo [92m                 Welcome to ScreenExtractor!")
os.system("echo [97mThis program can extract text information from a specified ")
os.system("echo region of your screen and then save it to a [93mfile[97m. ")
os.system("echo [94mSHIFT+ESC [97m= Exit program    [94mALT+N [97m= Set Bounding Box")
os.system("echo [94mALT+M [97m= Extract Screen    [94mALT+, [97m= AutoWrite")
os.system("echo [94mALT+. [97m= Run Both    [94mALT+F11 [97m= Settings")

def on_click(x,y,button,pressed):
    if pressed:
        oldMouse[0] = x
        oldMouse[1] = y
    if not pressed:
        newMouse[0] = x
        newMouse[1] = y
        return False

def on_press(key):
    global settings, doLoop, loopCount, sec, sx, sy, width, height, raw, awrite, bwrite

    #Check if the pressed key is apart of any of the hotkeys
    if key == keyboard.Key.shift:
        current.add(key)
    if key == keyboard.Key.esc:
        current.add(key)
    if key == keyboard.Key.alt_l:
        current.add(key)
    if key == keyboard.KeyCode(char='n'):
        current.add(key)
    if key == keyboard.KeyCode(char='m'):
        current.add(key)
    if key == keyboard.KeyCode(char=','):
        current.add(key)
    if key == keyboard.KeyCode(char='.'):
        current.add(key)
    if key == keyboard.Key.f11:
        current.add(key)

    #SHIFT+ESC (Exit program)
    if current == combo[0]:
        os.system("@echo on")
        exit()
    
    #ALT+N (Set bounding box)
    if current == combo[1]:
        os.system("echo [93mClick and drag to create Bounding Box[97m")

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
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
            width = abs(oldMouse[0]-newMouse[0])
            height = abs(oldMouse[1]-newMouse[1])

            try:
                with open(data+"\\settings.txt","w") as f:
                    f.write("doLoop: 0\nloopCount: 1\nsec: 0\nx: "+str(sx)+"\ny: "+str(sy)+"\nwidth "+str(width)+"\nheight: "+str(height)+"\nraw: 0")
                    os.system("echo [92mSet Bounding Box to: [93m("+str(sx)+","+str(sy)+"), ("+str(sx+width)+","+str(sy+height)+")[97m")
            except IOError:
                os.system("echo [91mCould not set Bounding Box.[97m")
        
        current.clear()
        os.system("echo [32m----------------------End of function----------------------[97m")

    #ALT+M (Extract screen)
    if current == combo[2]:
        extract(sx,sy,width,height)

        #Saves raw, unaltered text to extractedText.txt
        if raw:
            oldTextTimeStamp = os.path.getmtime(data+"\\extractedText.txt")

            with open(data+"\\extractedText.txt", 'w') as f:
                f.write(rawRead())
            
            newTextTimeStamp = os.path.getmtime(data+"\\extractedText.txt")

            if oldTextTimeStamp != newTextTimeStamp:
                os.system("echo [92mSuccessfully [97msaved extracted text to [93mextractedText.txt[97m")
            else:
                os.system("echo [91mFailed [97mto save extracted text to [93mextractedText.txt[97m")

        #Saves formatted text to extractedText.txt
        else:
            oldTextTimeStamp = os.path.getmtime(data+"\\extractedText.txt")

            with open(data+"\\extractedText.txt", 'w') as f:
                f.write(screenRead())
            
            newTextTimeStamp = os.path.getmtime(data+"\\extractedText.txt")
            
            if oldTextTimeStamp != newTextTimeStamp:
                os.system("echo [92mSuccessfully [97msaved extracted text to [93mextractedText.txt[97m")
            else:
                os.system("echo [91mFailed [97mto save extracted text to [93mextractedText.txt[97m")

        os.system("START "+data+"\\extractedText.txt")
        current.clear()
        os.system("echo [32m----------------------End of function----------------------[97m")

    #ALT+, (AutoWrite)
    if current == combo[3]:
        awrite = True
    
    #ALT+. (Run both)
    if current == combo[4]:
        bwrite = True

    #ALT+F11 (Settings)
    if current == combo[5]:
        return False

def on_release(key):
    global awrite, bwrite

    #ALT+,
    if key == keyboard.Key.alt_l and awrite:
        awrite = False
        text = open(data+"\\extractedText.txt","r").read()
        autoWrite(text,loopCount,sec)

        current.clear()
        os.system("echo [32m----------------------End of function----------------------[97m")

    if key == keyboard.Key.alt_l and bwrite:
        bwrite = False
        
        for i in range(loopCount):
            extract(sx,sy,width,height)

            if raw:
                oldTextTimeStamp = os.path.getmtime(data+"\\extractedText.txt")

                with open(data+"\\extractedText.txt", 'w') as f:
                    f.write(rawRead())
                
                newTextTimeStamp = os.path.getmtime(data+"\\extractedText.txt")

                if oldTextTimeStamp != newTextTimeStamp:
                    os.system("echo [92mSuccessfully [97msaved extracted text to [93mextractedText.txt[97m")
                else:
                    os.system("echo [91mFailed [97mto save extracted text to [93mextractedText.txt[97m")

            #Saves formatted text to extractedText.txt
            else:
                oldTextTimeStamp = os.path.getmtime(data+"\\extractedText.txt")

                with open(data+"\\extractedText.txt", 'w') as f:
                    f.write(screenRead())
                
                newTextTimeStamp = os.path.getmtime(data+"\\extractedText.txt")
                
                if oldTextTimeStamp != newTextTimeStamp:
                    os.system("echo [92mSuccessfully [97msaved extracted text to [93mextractedText.txt[97m")
                else:
                    os.system("echo [91mFailed [97mto save extracted text to [93mextractedText.txt[97m")
            
            text = open(data+"\\extractedText.txt","r").read()
            autoWrite(text,1,sec)

        os.system("echo [32m----------------------End of function----------------------[97m")

    if current != set():
        if key == keyboard.Key.alt_l:
            current.remove(key)
        if key == keyboard.KeyCode(char='n'):
            current.remove(key)
        if key == keyboard.KeyCode(char='m'):
            current.remove(key)
        if key == keyboard.KeyCode(char=','):
            current.remove(key)
        if key == keyboard.KeyCode(char='.'):
            current.remove(key)
        if key == keyboard.Key.f11:
            current.remove(key)

os.system("echo [32m-----------------------Program ready-----------------------[97m")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    if not listener.running:
        setting()
        os.system("echo [32m----------------------End of function----------------------[97m")
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)