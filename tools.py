#!/usr/bin/env python3

import os 
import sys
import time
from time import sleep

if os.getuid() != 0:
	print ("/_\\ Sorry,this script requires sudo privledges, run as root! ")
	print("Use > 'sudo -i' and run the script again.")
	sys.exit()

#*******************************************Open & Read**************************************************
def editzsh():
		s = open("/root/.zshrc").read()
		s = s.replace("plugins=(git)", "plugins=(git zsh-autosuggestions zsh-syntax-highlighting)")
		f = open("/root/.zshrc", 'w')
		f.write(s)
		f.close()

def line():
	print("\033[1;91m--------------------------------\033[1;m")

def editlang():
	s = open("/etc/apt/apt.conf.d/00aptitude").read()
	s = s.replace("Acquire::Languages \"none\";", "")
	f = open("/etc/apt/apt.conf.d/00aptitude", 'w')
	f.write(s)
	f.close()
	l = open("/etc/apt/apt.conf.d/00aptitude", "a+")
	l.write("Acquire::Languages \"none\";")
	l.close()

def editram():
	s = open("/etc/fstab").read()
	s = s.replace("tmpfs /tmp tmpfs mode=1777,nosuid,nodev 0 0", "")
	f = open("/etc/fstab", 'w')
	f.write(s)
	f.close()
	l = open("/etc/fstab", "a+")
	l.write("tmpfs /tmp tmpfs mode=1777,nosuid,nodev 0 0")
	l.close()

#*******************************************Clean*******************************************************


def clear():
	os.system("clear")
def leaving():
	print("")
	print(" [\033[1;32m ok \033[1;m] Removing temporary files")
	sleep(1.5)
	print("")
	os.system("rm -rf /tmp*")
	print("")
	print(" [\033[1;32m ok \033[1;m] Cleaning the system")
	print("")
	sleep(1.5)
	os.system("apt-get -y clean && apt-get -y autoremove && apt-get -y autoclean")
	print("")
	print(" [\033[1;91m ++ \033[1;m]\033[1;32m Created by \033[1;m\033[1;36mDalist\033[1;m")
	sleep(1.5)
	print("")

def done():
	print("")
	print("\033[1;32m ✔ Done!\033[1;m")



#*************************************************Program*****************************************************
tools = True
options = True

while options == True:
	clear()
	print("")
	print("\033[1;32m+ Items to choose: \033[1;m ")
	print("")
	print("")
	print("1) Install Oh-My-Zsh")
	print("----------------------------")
	print("2) Install Chrome, Steam, Sublime-Text(3207), Stacer, Gnome-Tweaks ")
	print("----------------------------")
	print("3) Speed up & optimize tweaks")
	print("----------------------------")
	print("4) Install IRC Client (WeeChat)")
	print("----------------------------")
	print("5) Customize the OS ")
	print("----------------------------")
	print("6) EXIT ")
	print("")
	option = input("➜  Choose an item: ")



	while tools == True:
		if option == "1":
			clear()
			line()
			print(" === > Downloading & Installing Oh-My-Zsh")
			line()
			cmda1 = os.system("apt-get -y update")
			cmda2 = os.system("apt-get install -y git wget")
			cmda3 = os.system("apt -y install zsh")
			cmda4 = os.system("chsh -s /usr/bin/zsh root")
			cmda5 = os.system("wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh")
			cmda6 = os.system("cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc source ~/.zshrc")
			cmda7 = os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")
			cmda8= os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")
			editzsh()
			print("")
			done()


		elif option == "2":
			clear()
			line()
			print(" === > Downloading Chrome... ")
			line()
			cmdb1 = os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
			line()
			print(" === > Installing Chrome... ")
			line()
			cmdb2 = os.system("dpkg -i google-chrome-stable_current_amd64.deb")
			cmdb5 = os.system("rm -rf google-chrome-stable_current_amd64.deb")
			line()
			print(" === > Installing Steam... ")
			line()
			cmdb3 = os.system("apt-get install -y steam:i386")
			line()
			print(" === > Installing Sublime-Text... ")
			line()
			cmdb6 = os.system("snap install sublime-text --classic")
			line()
			print(" === > Downloading Stacer... ")
			line()
			cmdb7 = os.system("wget https://datapacket.dl.sourceforge.net/project/stacer/v1.1.0/stacer_1.1.0_amd64.deb")
			line()
			print(" === > Installing Stacer... ")
			line()
			cmdb8 = os.system("dpkg -i stacer_1.1.0_amd64.deb")
			cmdb9 = os.system("rm -rf stacer_1.1.0_amd64.deb")
			line()
			print(" === > Installing Gnome-Tweaks...")
			line()
			cmdb10 = os.system("apt install gnome-tweaks -y")
			line()
			print(" === > Updating and upgrading... ")
			line()
			cmdb9 = os.system("apt-get -y update && apt-get -y upgrade")
			print("")
			done()


		elif option == "3":
			clear()
			line()
			print(" === > Optimizing swappiness: ")
			line()
			cmdc1 = os.system("sysctl vm.swappiness=10")
			line()
			print(" === > Installing Preload... ")
			line()
			cmdc2 = os.system("apt-get install -y preload")
			line()
			print(" === > Cleaning...")
			line()
			cmbc3 = os.system("apt-get -y clean && apt-get -y autoremove && apt-get -y autoclean")
			editlang()
			line()
			print(" === > Moving /tmp folder to RAM to speed up Ubuntu... ")
			line()
			editram()
			done()

		elif option == "4":
			clear()
			line()
			print(" === > Downloading WeeChat...")
			line()
			cmdd1 = os.system("sh -c \'echo \"deb https://weechat.org/ubuntu $(lsb_release -cs) main\" >> /etc/apt/sources.list.d/weechat.list\'")
			cmdd2 = os.system("apt-key adv --keyserver keys.gnupg.net --recv-keys 11E9DE8848F2B65222AA75B8D1820DB22A11534E")
			cmdd3 = os.system("apt-get -y update")
			line()
			print(" === > Installing WeeChat...")
			line()
			cmdd4 = os.system("apt-get install -y weechat")
			print("")
			done()

		elif option == "5":
			clear()
			line()
			print(" === > Removing Ubuntu-dock...")
			line()
			cmde1 = os.system("apt remove -y gnome-shell-extension-ubuntu-dock")
			line()
			print(" === > Disabling hot corners...")
			line()
			cmde2 = os.system("gsettings set org.gnome.shell enable-hot-corners false")
			print(" === > Deleting Firefox...")
			cmde4 = os.system("	apt-get -y remove firefox")
			cmde5 = os.system(" apt-get -y --purge autoremove firefox")
			cmde6 = os.system("rm -rf ~/.mozilla")
			done()


		elif option == "6":
			leaving()
			exit()

		else:
			print("")
			print("\033[1;91m[ ✖ ] Wrong command\033[1;m")
			sleep(2)
			os.system("clear")
			break


		print("")
		option2 = input("> Do you want to choose another action ? Press (y) for YES and (n) for NO: ")
		if option2 == "y":
			break
			options = True
		if option2 == "n":
			leaving()
			tools = False
			options = False
