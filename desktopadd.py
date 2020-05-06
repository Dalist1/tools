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


user = os.popen("w | grep /usr/lib/ | head -n 1 | awk '{print $1;}'").read().rstrip()
homedir = f"/home/{user}"

print("")
name = input("=> Enter the app name: ")
iconname = input("=> Enter Downloaded icon name: ")
imgcmddown = subprocess.run(f"cp {homedir}/Downloads/{iconname} /usr/share/icons/{iconname}", shell=True, capture_output=True, text=True)
imgcmdusr = subprocess.run(f"file /usr/share/icons/{iconname}",shell=True, capture_output=True, text=True)


if imgcmddown.returncode != 0 and imgcmdusr.returncode != 0:
	print("")
	print("Icon with that name was not found under \033[1;91m{homedir}/Downloads/{iconname}\033[1;m nor under \033[1;91m/usr/share/icons/{iconname}\033[1;m... ")
	print("Quitting...")
	sys.exit()
else:
	image = "/usr/share/{iconname}"
	image = image.split("/")[-1]
	image = f'/usr/share/icons/{iconname}'
	print(f"[\033[1;32m+\033[1;m] Icon located at \033[1;32m{image}\033[1;m.")

	execu = input("=> Enter the executable command: ")
	terminal = input("=> Spawn a terminal? (Choose: Yes or No): ")
	while True:
		if terminal == "yes" or terminal == "Yes" or terminal == "YES":
			terminal = "true"
			break
		elif terminal == "no" or terminal =="NO" or terminal == "No":
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
