import variables, os

#Settings
def setting():
    global line, accept

    with open(variables.dir_settings) as f:
        settingsLines = f.readlines()

    os.system("echo [32m                 Settings")
    os.system("echo [90mUse \"help\" to see accepted tokens[97m")
    print("".join(settingsLines))

    while True:
        rootQuery = input("[93m>[0m")

        if rootQuery.lower() == "exit":
            break

        if rootQuery.lower() == "help":
            accept = True
            os.system("echo [32mAccepted tokens:")
            os.system("echo     \"exit\", \"list\", \"help\", \"help vars\", \"cls\"[0m")

        if rootQuery.lower() == "list":
            accept = True
            os.system("echo [97m")
            print("".join(settingsLines))

        if rootQuery.lower() == "help vars":
            accept = True
            os.system("echo [32mAccepted variables:")
            os.system("echo     \"doLoop\", \"loopCount\", \"sec\", \"x\", \"y\", \"height\", \"width\", \"raw\"[0m")

        if rootQuery.lower() == "cls" or rootQuery.lower() == "clear":
            accept = True
            os.system("CLS")
            os.system("echo [90mUse \"help\" at any time to get help if you get stuck.[0m")

        if (rootQuery == "doLoop" or rootQuery == "loopCount"
            or rootQuery == "sec" or rootQuery == "x" or rootQuery == "y"
            or rootQuery == "height" or rootQuery == "width"
            or rootQuery == "raw"):
                
            while True:
                accept = False
            
                query = input(f"[93m{rootQuery}>[0m")

                if query.lower() == "back":
                    break

                if query.lower() == "cls" or query.lower() == "clear":
                    accept = True
                
                    os.system("cls")
                    os.system("echo [90mUse \"help\" at any time to get help if you get stuck.[0m")
                    
                if query.lower() == "help":
                    accept = True
                
                    if rootQuery == "doLoop":
                        print(
                            "[32mAccepted inputs:\n    \"1\" (True), \"0\" False\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "loopCount":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only (1-100)\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "sec":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only (0-100)\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "x":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "y":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "height":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only\n    or  \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "width":
                        print(
                            "[32mAccepted inputs:\n    Accepts integers only\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                    if rootQuery == "raw":
                        print(
                            "[32mAccepted inputs:\n    \"True\", \"False\"\n    or \"back\" to go back and \"cls\" to clear screen.[0m"
                        )

                if (rootQuery == "doLoop" or rootQuery
                    == "raw") and (query == "1" or query == "0"):
                    if rootQuery == "doLoop":
                        line = 0
                    if rootQuery == "raw":
                        line = 7
                    accept = True

                if (rootQuery == "loopCount" or rootQuery == "sec" or rootQuery
                    == "x" or rootQuery == "y" or rootQuery == "height"
                    or rootQuery == "width") and query.isdigit():                
                    if (rootQuery == "loopCount") and (int(query) >= 1
                                                    and int(query) <= 100):
                        line = 1
                        accept = True

                    if (rootQuery == "sec" or rootQuery == "x" or rootQuery == "y"
                            or rootQuery == "height"
                            or rootQuery == "width") and (query.isdigit()):
                        accept = True

                        if rootQuery == "sec":
                            line = 2
                        if rootQuery == "x":
                            line = 3
                        if rootQuery == "y":
                            line = 4
                        if rootQuery == "width":
                            line = 5
                        if rootQuery == "height":
                            line = 6
                        
                if accept == False and query != "":
                    os.system("echo [91m\"" + query +"\" is not recognized as a valid input![0m")

                if (line != set()) and accept == True:
                    settingsLines[line] = rootQuery + ": " + query + "\n"

                    with open(variables.dir_settings, "w") as f:
                        f.write("".join(settingsLines))

                    line = set()

                    os.system("echo [32mChanged \"" + rootQuery + "\" to \"" + query + "\"[0m")
                
                accept = False
            
        elif accept == False and rootQuery != "":
            os.system("echo [91m\"" + rootQuery +"\" is not recognized as a valid input![0m")