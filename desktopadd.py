#!/usr/bin/env python3

import os 
import subprocess
import sys
import platform

#Run this as root!

if platform.system() != 'Linux':
	print("Please use Linux!")
	sys.exit()

if os.getuid() != 0:
	print ("[\033[1;91m !! \033[1;m] Start the script as root! ")
	print("[\033[1;91m !! \033[1;m] Use > '\033[1;32msudo\033[1;m' and try again.")
	sys.exit()


print("\nBefore starting, please download an Icon for the app (\033[1;36mRecommended\033[1;m: https://flaticon.com)")
name = input("\n=> Enter a name for the App: ")
iconpath = input("=> Enter Downloaded icon's full path: ")
iconname = iconpath.rsplit("/")[-1]
imgcmddown = subprocess.run(f"cp {iconpath} /usr/share/icons/{iconname}", shell=True, capture_output=True, text=True)

if imgcmddown.returncode != 0:
	print(f"\nIcon was not found under \033[1;34m{iconpath}\033[1;m\n\033[1;39mQuitting...\033[1;m\n")
	sys.exit(1)
elif not ".svg" or ".png" in iconname:
	print("\nPlease download a svg or png icon and try again\n\033[1;39mQuitting...\033[1;m\n")
	sys.exit(1)


image = f'/usr/share/icons/{iconname}'
print(f"[\033[1;32m+\033[1;m] Icon located at \033[1;32m{image}\033[1;m.")

execu = input("=> Enter the executable command: ")
terminal = input("=> Spawn a terminal? (y/n): ")
while True:
	if terminal == "Y" or terminal == "y":
		terminal = "true"
		break
	elif terminal == "N" or terminal == "n":
		terminal = "false"
		break
	else:
		print("[\033[1;91m!\033[1;m] Please enter a valid option!")
		continue

desktop = f"[Desktop Entry]\nVersion=1.0\nName={name}\nComment=Waves\nExec={execu}\nIcon={image}\nTerminal={terminal}\nType=Application\nCategories=Utility;Application;"

with open(f"/usr/share/applications/{name}.desktop", "w+") as e:
	e.write(desktop)

print("")
print(f"[\033[1;32m+\033[1;m] Created Desktop App at \033[1;32m/usr/share/applications/{name}.desktop\033[1;m.")

