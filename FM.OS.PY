#Windows dependent

import os
import sys
import time
import psutil
import socket
import pyttsx3
import winsound
import datetime
import webbrowser
from urllib.parse import quote
from tqdm import tqdm
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)


os.system("title FM . OS")


os.system("pip install colorama tqdm pyttsx3 psutil")
os.system("cls")


steps = 100
print("                                                     Loading")
for _ in tqdm(range(steps), bar_format="{l_bar}{bar}|"):
	time.sleep(0.01)
print("                                               Loading is complete.\n")
os.system("cls")


print("   ▄████████    ▄▄▄▄███▄▄▄▄  ")
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
			print(f"""
{Fore.LIGHTGREEN_EX}List of available commands:

help      - Show this list of commands
shutdown  - Exit the program
clear     - Clear the terminal screen
cls       - Clear the terminal screen
calc      - Perform simple calculations
time      - Display the current date and time
date      - Display the current date and time
ls        - List files and directories in the current folder
dir       - List files and directories in the current folder
ls2       - List all files and folders in the current folder
dir2      - List all files and folders in the current folder
openf     - Open a file by specifying its name
addf      - Add a new file with content
pcontentf - Update content of an existing file
renamef   - Rename an existing file
readf     - Read and display the content of a text file
removef   - Delete an existing file
tasklist  - Display running processes
taskkill  - Terminate a process by PID
sysinfo   - Show system information
battery   - Show battery status
wifi      - Checking WiFi connection status
wifia     - Show a list of nearby Wi-Fi networks
wifip     - Show the passwords of the WiFi networks we are connected to
game      - Running web games
sound     - Convert text to sound
title     - Change OS title
echo      - Print a custom message
print     - Print a custom message
color     - Change text and background colors
search    - Ability to search in Google browser
os        - Show FM.OS operating system specifications
star      - Vote for the app on GitHub{Style.RESET_ALL}
""")

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

		case "ls" | "dir":
			ls = os.listdir()
			for item in ls:
				print(f"{Fore.YELLOW}{item}{Style.RESET_ALL}")

		case "ls2" | "dir2":
			os.system("tree /f")

		case "openf":
			files = os.listdir()
			filer = input("Enter the name of the file to Run>> ")
			if filer in files:
				os.system(f"{filer}")
			else:
				winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
				print(f"{Fore.RED}Invalid File Name.{Style.RESET_ALL}")

		case "addf":
			filen = input("Add New File Name (with extension)>> ").strip().lower()
			content = input("Enter content for the file>> ")
			with open(filen, 'w', encoding='utf-8') as f:
				f.write(content)
			print(f"{Fore.GREEN}Success! File '{filen}' created and content written.{Style.RESET_ALL}")

		case "pcontentf":
			filem = input("Enter file name to update content>> ").strip().lower()
			if os.path.exists(filem):
				content = input("Enter NEW content>> ")
				with open(filem, 'w', encoding='utf-8') as f:
					f.write(content)
				print(f"{Fore.GREEN}File '{filem}' content updated successfully.{Style.RESET_ALL}")
			else:
				winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
				print(f"{Fore.RED}File '{filem}' does not exist.{Style.RESET_ALL}")

		case "renamef":
			old_name = input("Enter the current name of the file>> ").strip().lower()
			if os.path.exists(old_name):
				new_name = input("Enter the new name for the file>> ").strip().lower()
				os.rename(old_name, new_name)
				print(f"{Fore.GREEN}Success! File '{old_name}' has been renamed to '{new_name}'.{Style.RESET_ALL}")
			else:
				winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
				print(f"{Fore.RED}Error: Source file '{old_name}' not found. Cannot rename.{Style.RESET_ALL}")

		case "readf":
			filear = input("Enter the name of the file to read>> ").strip().lower()
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

		case "tasklist":
			for proc in psutil.process_iter(["pid" , "name"]):
				print(f"{Fore.YELLOW}{proc.info}{Style.RESET_ALL}")

		case "taskkill":
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
			mem = psutil.virtual_memory()
			disk = psutil.disk_usage('/')
			print("System Info: ")
			os.system("wmic cpu get name")
			os.system("systeminfo")
			print(f"""
RAM Total: {mem.total / (1024 ** 3):.2f} GB
RAM Used: {mem.used / (1024 ** 3):.2f} GB ({mem.percent}%)
RAM Available: {mem.available / (1024 ** 3):.2f} GB
Disk Total: {disk.total / (1024 ** 3):.2f} GB
Disk Used: {disk.used / (1024 ** 3):.2f} GB ({disk.percent}%)
Disk Free: {disk.free / (1024 ** 3):.2f} GB
Swap Memory Usage Percentage: {psutil.swap_memory().percent}%
CPU Usage: {psutil.cpu_percent()}%
CPU Cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count()} logical
CPU Frequency: {psutil.cpu_freq().current:.2f} MHz
				""")

		case "battery":
			battery = psutil.sensors_battery()
			print(f"{Fore.LIGHTGREEN_EX}Battery: {battery.percent}% - {'Charging' if battery.power_plugged else 'Not Charging'}{Style.RESET_ALL}")

		case "wifi":
			winsound.Beep(1000 , 500)
			print(Fore.GREEN)
			os.system("netsh wlan show interfaces")
			hostname = socket.gethostname()
			ip = socket.gethostbyname(hostname)
			print(f"    IP Address: {ip}")
			print(Style.RESET_ALL)

		case "wifia":
			winsound.Beep(1000 , 500)
			print(Fore.GREEN)
			os.system("netsh wlan show network")
			print(Style.RESET_ALL)

		case "wifip":
			WiFi_Name = input("WiFi Name>> ").strip().lower()
			wifi_password = (f' netsh wlan show profile name = "{WiFi_Name}" key=clear | findstr "Key Content" ')
			print(Fore.LIGHTMAGENTA_EX)
			os.system(wifi_password)
			print(Style.RESET_ALL)

		case "game":
			print(f"{Fore.LIGHTBLUE_EX}list games : deadshot | shilter | sloperun | slingdrift | pong | sonic | pacmac")
			game = input(f"Select the game>> {Style.RESET_ALL}")
			game = game.lower().strip()
			if game == "deadshot":
				webbrowser.open("https://deadshot.io/")
			elif game == "shilter":
				webbrowser.open("http://slither.io/")
			elif game == "sloperun":
				webbrowser.open("https://slopegame.io/")
			elif game == "slingdrift":
				webbrowser.open("https://slingdrift.com/")
			elif game == "pong":
				webbrowser.open("https://freepong.org/")
			elif game == "sonic":
				webbrowser.open("https://freesonic.org/")
			elif game == "pacman":
				webbrowser.open("https://www.google.com/logos/2010/pacman10-i.html")
			else:
				winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
				print(f"{Fore.RED}game not found!{Style.RESET_ALL}")

		case "sound":
			sinput = input("text to audio>>")
			sound1 = pyttsx3.init()
			sound1.setProperty("rate" , 140)
			sound1.say(sinput)
			sound1.runAndWait()

		case "title":
			newt = input("new title>> ")
			os.system(f"title {newt}")

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
				os.system("cls")
			else:
				winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
				print(f"Invalid color! Try again.")
				continue
			winsound.Beep(1000, 500)
			print(colort + colorb + "Color updated!")
			os.system("cls")

		case "search":
			search = input("SEARCH>> ")
			if "http" in search.lower():
   				fs = search
			else:
				fs =  "https://www.google.com/search?q=" + quote(search)
			webbrowser.open(fs)

		case "os":            
			print(f"""{Fore.LIGHTBLUE_EX}The name of the operating system : FM.OS
Operating system version : 2.0
Developer name : SHAYAN-FM{Style.RESET_ALL}""")
			
		case "star":
			github = "https://github.com/SHAYAN-FM/FM.OS.PY.git"
			webbrowser.open(github)

		case "":
			pass

		case _:
			print(f"{Fore.LIGHTBLACK_EX}Command Not Found: {command}{Style.RESET_ALL}")
