#!/usr/bin/env python3

import os 
import sys
from time import sleep
try:

	import py7zr

except:

	os.system("apt install python3-pip -y; pip3 install py7zr;")
	import py7zr


while True:


	if os.getuid() != 0:
		print ("/_\\ Sorry,this script requires sudo privledges, run as root! ")
		print("Use > 'sudo su' and run the script again.")
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
		print("")
		print(" [\033[1;32m ok \033[1;m] Cleaning the system")
		print("")
		os.system("apt-get -y clean && apt-get -y autoremove && apt-get -y autoclean")
		print("")
		print(" [\033[1;91m ++ \033[1;m]\033[1;32m Created by \033[1;m\033[1;36mDalist\033[1;m")
		sleep(1.5)
		print("")
		os.system("rm -rf gobuster-linux-amd64 gobuster-linux-amd64.7z")


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
		print("2) Install Brave, Steam, Sublime-Text(LATEST), Gnome-Tweaks, Spotify, Discord")
		print("----------------------------")
		print("3) Speed up & optimize tweaks")
		print("----------------------------")
		print("4) Install IRC Client (WeeChat)")
		print("----------------------------")
		print("5) Customize the OS ")
		print("----------------------------")
		print("6) Install hacking tools for Ubuntu ")
		print("----------------------------")
		print("7) Wordlists optimized for Penetration Testing")
		print("----------------------------")
		print("8) EXIT ")
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
				print(" === > Downloading and Installing Brave... ")
				line()
				os.system("apt install apt-transport-https curl -y; curl -s https://brave-browser-apt-nightly.s3.brave.com/brave-core-nightly.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-prerelease.gpg add -	; echo \"deb [arch=amd64] https://brave-browser-apt-nightly.s3.brave.com/ stable main\" | sudo tee /etc/apt/sources.list.d/brave-browser-nightly.list ; apt update; apt install brave-browser-nightly -y")
				line()
				print(" === > Installing Steam... ")
				line()
				cmdb3 = os.system("apt-get install -y steam:i386")
				line()
				print(" === > Installing Sublime-Text... ")
				line()
				cmdb6 = os.system("snap set core snapshots.automatic.retention=no; snap install sublime-text --classic")
				line()
				print(" === > Installing Gnome-Tweaks...")
				line()
				cmdb10 = os.system("apt install gnome-tweaks -y")
				line()
				print("Installing Spotify...")
				line()
				os.system("snap install spotify;")
				line()
				print("Installing Htop...")
				line()
				os.system("apt install htop -y")
				line()
				print("Installing Discord...")
				line()
				os.system("snap install discord")
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
					line()
					print("Fetching latest version of Linpeas into /opt/bins directory")
					line()
					#Linpeas
					os.system("https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh; mv linpeas.sh /opt/bins/lp; chmod +x /opt/bins/lp")
					line()
					print("Installing hacking tools: \033[1;34mzbarimg\033[1;m, \033[1;34mbinwalk\033[1;m, \033[1;34mzsteg\033[1;m, \033[1;34mstegoveritas\033[1;m, \033[1;34mstegcracker\033[1;m, \033[1;34msqlmap\033[1;m, \033[1;34mexiftool\033[1;m, \033[1;34msteghide\033[1;m, \033[1;34mforemost\033[1;m, \033[1;34mnmap\033[1;m.")
					line()
					os.system("apt-get install -y zbar-tools nmap binwalk foremost exiftool steghide; gem install zsteg; pip3 install stegcracker; pip3 install stegoveritas")
					line()
					try:
						busterversion = os.popen("curl -s https://raw.githubusercontent.com/OJ/gobuster/9ef3642d170d71fd79093c0aa0c23b6f2a4c1c64/libgobuster/version.go | grep -o \'\"[^\"]\\+\"\' | tr \'\"\' \' \'").read().replace(" ", "").rstrip("\n")

					except:
						print("Failed to detect GoBuster Version, hence skipping.")
						print(busterversion)

					print(f"Installing GoBuster version {busterversion} [LATEST]")
					line()

					os.system(f"wget https://github.com/OJ/gobuster/releases/download/v{busterversion}/gobuster-linux-amd64.7z")

					#Unzipping
					with py7zr.SevenZipFile("gobuster-linux-amd64.7z", mode='r') as z:
						z.extractall()
					os.system("mv gobuster-linux-amd64/gobuster /usr/bin; chmod +x /usr/bin/gobuster")

					line()
					print("Installing Metasploit-Framework...")
					line()
					os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall ; rm -rf msfinstall")



			elif option == "7":
				line()
				print("Fetching the wordlists. This might take a while...")
				line()
				os.system("mkdir -p /opt/dirs; mkdir -p /opt/pass")
				os.system("wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/big.txt -O /opt/dirs/big.txt")
				print("[+] Downloaded \033[1;34mbig.txt\033[1;m under \033[1;34m/opt/dirs/big.txt\033[1;m")
				os.system("wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt -O /opt/pass/rockyou.txt")
				print("[+] Downloaded \033[1;34mrockyou.txt\033[1;m under \033[1;34m/opt/pass/rockyou.txt\033[1;m")
				os.system("cp /opt/dirs/big.txt /opt/pass/; sed -e \'s/^/svc-/\' -i /opt/pass/big.txt; mv /opt/pass/big.txt /opt/pass/krb-wordlist")


			elif option == "8":
				leaving()
				exit()

			else:
				print("")
				print("\033[1;91m[ ✖ ] Wrong command\033[1;m")
				sleep(2)
				os.system("clear")
				break


			print("")
			option2 = input("> Continue [Y/n]: ")
			if option2 == "y":
				break
				options = True
			if option2 == "n":
				leaving()
				sys.exit(1)



