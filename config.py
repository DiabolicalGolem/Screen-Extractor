import platform
import os
from PIL import Image, ImageDraw
from windowsConfig import windowsConfig
from linuxConfig import linuxConfig

def config():
    #Check OS
    os.system("echo [97mChecking OS[0")
    operating = platform.system()

    os.system("echo [92m    Running on [1m"+operating+"[0m")
    
    #Configure for respective systems
    if operating == "Windows":
        windowsConfig()
    elif operating == "Linux":
        linuxConfig()