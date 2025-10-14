#PASS WORD = 710


import os
import sys
import time
import psutil
import datetime
import platform
import subprocess
import playsound
from tqdm import tqdm
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)

pass_word = input("                                                  Pass Word>> ")
if pass_word == "710":
    pass
else:
    print("                                                 Wrong Pass_Word!")
    time.sleep(1.5)
    sys.exit()

steps = 100
print("                                                     Loading")
for _ in tqdm(range(steps), bar_format="{l_bar}{bar}|"):
    time.sleep(0.015)
print("                                               Loading is complete.\n")

print("Welcome To FM.OS [Version 1.0]\nType 'Help' For A List Of Commands.\n")

while True:
    user_input = input(">>> ")
    command = user_input.strip().lower()

    match command:
        case "help":
            print("\nList of available commands:\n")
            print("help      - Show this list of commands")
            print("shutdown  - Exit the program")
            print("clear     - Clear the terminal screen")
            print("cls       - Clear the terminal screen")
            print("calc      - Perform simple calculations")
            print("time      - Display the current date and time")
            print("date      - Display the current date and time")
            print("ls        - List files and directories in the current folder")
            print("dit       - List files and directories in the current folder")
            print("gci       - List files and directories in the current folder")
            print("openf     - Open a file by specifying its name")
            print("addf      - Add a new file with content")
            print("pcontentf - Update content of an existing file")
            print("renamef   - Rename an existing file")
            print("readf     - Read and display the content of a text file")
            print("removef   - Delete an existing file")
            print("plays     - Play a song by specifying its name")
            print("task      - Display running processes")
            print("pidkill    - Terminate a process by PID")
            print("sysinfo   - Show system information")
            print("wifi      - Checking WiFi connection status")
            print("wifia     - Show a list of nearby Wi-Fi networks")
            print("echo      - Print a custom message")
            print("print     - Print a custom message")
            print("color     - Change text and background colors")
            print("os        - Show FM.OS operating system specifications")

        case "shutdown":
            print("Shutting Down FM.OS...")
            time.sleep(1.5)
            sys.exit()

        case "clear" | "cls":
            os.system("cls")
        
        case "calc":
            calc = input("CalC>> ")
            result = eval(calc)
            print(f"Result : {result}")

        case "time" | "date":
            print(f"Present time: {datetime.datetime.now()}")

        case "ls" | "dir" | "gci":
            ls = os.listdir()
            for item in ls:
                print(item)

        case "openf":
            files = os.listdir()
            filer = input("Enter the name of the file to Run>> ")
            if filer in files:
                os.system(f"{filer}")
            else:
                print("Invalid File Name.")

        case "addf":
            filen = input("Add New File Name (with extension)>> ")
            content = input("Enter content for the file>> ")
            with open(filen, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Success! File '{filen}' created and content written.")

        case "pcontentf":
            filem = input("Enter file name to update content>> ")
            if os.path.exists(filem):
                content = input("Enter NEW content>> ")
                with open(filem, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"File '{filem}' content updated successfully.")
            else:
                print(f"File '{filem}' does not exist.")

        case "renamef":
            old_name = input("Enter the current name of the file>> ")
            if os.path.exists(old_name):
                new_name = input("Enter the new name for the file>> ")
                os.rename(old_name, new_name)
                print(f"Success! File '{old_name}' has been renamed to '{new_name}'.")
            else:
                print(f"Error: Source file '{old_name}' not found. Cannot rename.")

    
        case "readf":
            filear = input("Enter the name of the file to read>> ")
            if os.path.exists(filear):
                with open(filear, 'r', encoding='utf-8') as f:
                    print(f.read())
            else:
                print(f"Error: File '{filear}' does not exist.")

        case "removef":
            filetd = input("Enter file name to delete>> ")
            if os.path.exists(filetd):
                os.remove(filetd)
                print(f"Success: File '{filetd}' has been deleted.")
            else:
                print(f"File {filetd} does not exist.")
        
        case "plays":
            song_name = input("Song_name>> ")
            if os.path.exists(song_name):
                playsound(song_name, block=False)
                print(f"Playing '{song_name}' in background.")
            else:
                print(f"File '{song_name}' not found.")


        case "task":
            for proc in psutil.process_iter(['pid', 'name']):
                print(proc.info)

        case "pidkill":
            pidtk = input("PIDtk>> ")
            if pidtk.isdigit():
                p = psutil.Process(int(pidtk))
                p.terminate()
                print(f"Process {pidtk} closed.")
            else:
                print(f"{pidtk} does not exist")

        case "sysinfo":
            print("System Info:")
            print(f"OS: {platform.system()} {platform.release()}")
            print(f"Total Memory (RAM): {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
            print(f"Used Memory (RAM): {psutil.virtual_memory().used / (1024 ** 3):.2f} GB")
            print(f"Memory Usage Percentage (RAM): {psutil.virtual_memory().percent}%")
            print(f"Total Swap Memory: {psutil.swap_memory().total / (1024 ** 3):.2f} GB")
            print(f"Used Swap Memory: {psutil.swap_memory().used / (1024 ** 3):.2f} GB")
            print(f"Swap Memory Usage Percentage: {psutil.swap_memory().percent}%")

        case "wifi":
            output = subprocess.check_output("netsh wlan show interfaces", shell = True , text = True)
            if "SSID" in output:
                print(output)
            else:
                print("Not connected to any Wi-Fi network.")

        case "wifia":
            wifia = subprocess.check_output(['netsh', 'wlan', 'show', 'network']).decode('utf-8')
            print("Scan Wi-Fi:\n")
            print(wifia)

        case "echo" | "print":
            ep = input("ep>> ")
            print(ep)

        case "color":
            colort = Fore.RESET
            colorb = Back.RESET
            print("\nAvailable colors:\nText Colors: red , green , blue , reset\nBackground Colors: bg_red , bg_green , bg_blue , reset\n")
            color = input("color>> ").strip().lower()
            if color == "red":
                colort = Fore.RED
            elif color == "green":
                colort = Fore.GREEN
            elif color == "blue":
                colort = Fore.BLUE
            elif color == "bg_red":
                colorb = Back.RED
            elif color == "bg_green":
                colorb = Back.GREEN
            elif color == "bg_blue":
                colorb = Back.BLUE
            elif color == "reset":
                colort = Fore.RESET
                colorb = Back.RESET
                print(Style.RESET_ALL + "Colors have been reset!")
            else:
                print("Invalid command! Try again.")
                continue
            print(colort + colorb + "Color updated!\n")

        case "os":
            print("The name of the operating system : FM.OS")
            print("Operating system version : 1.0")
            print("Operating system manufacturer name : SHAYAN-FM")

        case "":
            pass

        case _:
            print(f"Command Not Found: {command}\n")

