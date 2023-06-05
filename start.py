import os, sys
import variables

#Check for .venv
os.system("echo [97mChecking for .venv[0m")
if not os.path.isdir(".venv"):
    os.system("echo [91m    Could not find .venv[0m")

    try:
        os.system(f"{sys.executable} -m venv .venv")
    except:
        os.system("echo [91m    Could not create .venv[0m")
        input("Please fix and then restart program")
else:
    os.system("[92m    Found .venv folder[0m")

if variables.operating == "Windows":
    os.system(f"{variables.dir}\\.venv\\Scripts\\python main.py")
elif variables.operating == "Linux":
    os.system(f"{variables.dir}/.venv/bin/python main.py")
