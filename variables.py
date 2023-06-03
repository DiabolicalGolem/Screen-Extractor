import os, platform

#Find OS
operating = platform.system()

#Find and set Directory paths
if operating == "Windows":
    dir = os.getcwd()
    dir_data = dir+"\\data"
    dir_settings = dir_data+"\\settings.txt"
    dir_extractedText = dir_data+"\\extractedText.txt"
    dir_imagePath = dir_data+"\\sourceImage.png"
    dir_pathToTess = dir_data+"\\tesseract\\tesseract.exe"
if operating == "Linux":
    dir = os.getcwd()
    dir_data = os.path.dirname(__file__)+"/data"
    dir_settings = dir_data+"/settings.txt"
    dir_extractedText = dir_data+"/extractedText.txt"
    dir_imagePath = dir_data+"/sourceImage.png"
    dir_pathToTess = dir_data+"/tesseract/tesseract.exe"