import os
import variables

os.system("@echo off && title Screen-Extractor && mode con: cols=60 lines=30 && echo Working on compiling program. This may take a while...")

if variables.operating == "Windows":
    os.system(f"{variables.dir}\\.venv\\Scripts\\python main.py")
elif variables.operating == "Linux":
    os.system(f"{variables.dir}/.venv/bin/python main.py")
