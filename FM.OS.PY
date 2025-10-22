#PASS WORD = 710


import os
import sys
import time
import psutil
import pyttsx3
import winsound
import datetime
import platform
import subprocess
import playsound
import webbrowser
from tqdm import tqdm
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)

PACKAGE = ['psutil' , 'pyttsx3' , 'playsound' , 'tqdm' , 'colorama']
subprocess.check_call([sys.executable, "-m", "pip", "install"] + PACKAGE)
print("Packages installed.")
os.system("cls")

pass_word = input("                                                  Pass Word>> ")
if pass_word == "710":
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
else:
    print(f"{Fore.RED}                                                 Wrong Pass_Word!")
    time.sleep(1)
    sys.exit()

steps = 100
print("                                                     Loading")
for _ in tqdm(range(steps), bar_format="{l_bar}{bar}|"):
    time.sleep(0.01)
print("                                               Loading is complete.\n")
os.system("cls")

print("    ▄████████   ▄▄▄▄███▄▄▄▄  ")
print("   ███    ███ ▄██▀▀▀███▀▀▀██▄")
print("   ███    █▀  ███   ███   ███")
print("  ▄███▄▄▄     ███   ███   ███")
print(" ▀▀███▀▀▀     ███   ███   ███")
print("   ███        ███   ███   ███")
print("   ███        ███   ███   ███")
print("   ███         ▀█   ███   █▀ ")

print("Welcome To FM.OS [Version 2.0]\nType 'Help' For A List Of Commands.\n")

while True:
    user_input = input(">>> ")
    command = user_input.strip().lower()

    match command:
        case "help":
            print(f"\n{Fore.GREEN}List of available commands:\n")
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
            print("pidkill   - Terminate a process by PID")
            print("sysinfo   - Show system information")
            print("wifi      - Checking WiFi connection status")
            print("wifia     - Show a list of nearby Wi-Fi networks")
            print("echo      - Print a custom message")
            print("print     - Print a custom message")
            print("color     - Change text and background colors")
            print("star      - Vote for the app on GitHub")
            print(f"os        - Show FM.OS operating system specifications{Style.RESET_ALL}")

        case "shutdown":
            sound = pyttsx3.init()
            sound.setProperty("rate" , 200)
            sound.say("shut down")
            time.sleep(0)
            sound.runAndWait()
            print(f"{Fore.LIGHTMAGENTA_EX}Shutting Down FM.OS...")
            time.sleep(0.5)
            sys.exit()

        case "clear" | "cls":
            winsound.Beep(2000,250)
            os.system("cls")
        
        case "calc":
            calc = input("CalC>> ")
            result = eval(calc)
            print(f"{Fore.LIGHTRED_EX}Result : {result}{Style.RESET_ALL}")

        case "time" | "date":
            print(f"{Fore.YELLOW}Present time: {datetime.datetime.now()}{Style.RESET_ALL}")

        case "ls" | "dir" | "gci":
            ls = os.listdir()
            for item in ls:
                print(f"{Fore.YELLOW}{item}{Style.RESET_ALL}")

        case "openf":
            files = os.listdir()
            filer = input("Enter the name of the file to Run>> ")
            if filer in files:
                os.system(f"{filer}")
            else:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
                print(f"{Fore.RED}Invalid File Name.{Style.RESET_ALL}")

        case "addf":
            filen = input("Add New File Name (with extension)>> ")
            content = input("Enter content for the file>> ")
            with open(filen, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"{Fore.GREEN}Success! File '{filen}' created and content written.{Style.RESET_ALL}")

        case "pcontentf":
            filem = input("Enter file name to update content>> ")
            if os.path.exists(filem):
                content = input("Enter NEW content>> ")
                with open(filem, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"{Fore.GREEN}File '{filem}' content updated successfully.{Style.RESET_ALL}")
            else:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
                print(f"{Fore.RED}File '{filem}' does not exist.{Style.RESET_ALL}")

        case "renamef":
            old_name = input("Enter the current name of the file>> ")
            if os.path.exists(old_name):
                new_name = input("Enter the new name for the file>> ")
                os.rename(old_name, new_name)
                print(f"{Fore.GREEN}Success! File '{old_name}' has been renamed to '{new_name}'.{Style.RESET_ALL}")
            else:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
                print(f"{Fore.RED}Error: Source file '{old_name}' not found. Cannot rename.{Style.RESET_ALL}")

    
        case "readf":
            filear = input("Enter the name of the file to read>> ")
            if os.path.exists(filear):
                with open(filear, 'r', encoding='utf-8') as f:
                    print(f.read())
            else:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
                print(f"{Fore.RED}Error: File '{filear}' does not exist.{Style.RESET_ALL}")

        case "removef":
            filetd = input("Enter file name to delete>> ")
            if os.path.exists(filetd):
                os.remove(filetd)
                print(f"{Fore.GREEN}Success: File '{filetd}' has been deleted.{Style.RESET_ALL}")
            else:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
                print(f"{Fore.RED}File {filetd} does not exist.{Style.RESET_ALL}")
        
        case "plays":
            song_name = input("Song_name>> ")
            if os.path.exists(song_name):
                playsound(song_name, block=False)
                print(f"Playing '{song_name}' in background.")
            else:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
                print(f"{Fore.RED}File '{song_name}' not found.{Style.RESET_ALL}")


        case "task":
            for proc in psutil.process_iter(['pid' , 'name']):
                print(f"{Fore.YELLOW}{proc.info}{Style.RESET_ALL}")

        case "pidkill":
            pidtk = input("PIDtk>> ")
            if pidtk.isdigit():
                p = psutil.Process(int(pidtk))
                p.terminate()
                winsound.Beep(1000, 500)
                print(f"{Fore.GREEN}Process {pidtk} closed.{Style.RESET_ALL}")
            else:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
                print(f"{Fore.RED}{pidtk} does not exist{Style.RESET_ALL}")

        case "sysinfo":
            print(f"{Back.LIGHTBLACK_EX}System Info:")
            print(f"OS: {platform.system()} {platform.release()}")
            print(f"Total Memory (RAM): {psutil.virtual_memory().total / (1024 ** 3):.2f}GB")
            print(f"Used Memory (RAM): {psutil.virtual_memory().used / (1024 ** 3):.2f} GB")
            print(f"Memory Usage Percentage (RAM): {psutil.virtual_memory().percent}%")
            print(f"Total Swap Memory: {psutil.swap_memory().total / (1024 ** 3):.2f} GB")
            print(f"Used Swap Memory: {psutil.swap_memory().used / (1024 ** 3):.2f} GB")
            print(f"Swap Memory Usage Percentage: {psutil.swap_memory().percent}%{Style.RESET_ALL}")

        case "wifi":
            winsound.Beep(1000, 500)
            output = subprocess.check_output("netsh wlan show interfaces", shell = True , text = True)
            if "SSID" in output:
                print(f"{Fore.GREEN}{output}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}You are not connected to any WiFi.{Style.RESET_ALL}")

        case "wifia":
            winsound.Beep(1000, 500)
            wifia = subprocess.check_output(['netsh', 'wlan', 'show', 'network']).decode('utf-8')
            print("Scan Wi-Fi:\n")
            print(f"{Fore.GREEN}{wifia}{Style.RESET_ALL}")

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
                winsound.Beep(1000, 500)
                print(Style.RESET_ALL + "Colors have been reset!")
            else:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
                print(f"Invalid command! Try again.")
                continue
            winsound.Beep(1000, 500)
            print(colort + colorb + "Color updated!")

        case "os":
            print(f"{Fore.BLUE}The name of the operating system : FM.OS")
            print("Operating system version : 2.0")
            print(f"Operating system manufacturer name : SHAYAN-FM{Style.RESET_ALL}")

        case "star":
            url = "https://github.com/SHAYAN-FM/FM.OS.PY.git"
            webbrowser.open(url)

        case "":
            pass

        case _:
            print(f"{Fore.LIGHTBLACK_EX}Command Not Found: {command}{Style.RESET_ALL}")
