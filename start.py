import os, sys
import variables

os.system(f"cd {variables.dir}")

os.system("title Screen-Extractor && mode con: cols=60 lines=30 && echo Working on compiling program. This may take a while...")

#Check for .venv
os.system("echo [97mChecking for .venv[0m")
if not os.path.isdir(".venv"):
    os.system("echo [91m    Could not find .venv[0m")

    try:
        os.system(f"{sys.executable} -m venv .venv")
    except:
        os.system("echo [91m    Could not create .venv[0m")
        input("Please fix and then restart program")

if variables.operating == "Windows":
    os.system(f"{variables.dir}\\.venv\\Scripts\\python main.py")
elif variables.operating == "Linux":
    os.system(f"{variables.dir}/.venv/bin/python main.py")