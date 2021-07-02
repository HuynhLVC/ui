#!/usr/bin/env python3

import os
from shutil import copyfile

os.system("git clone https://github.com/HuynhLVC/ui.git")

os.system("sudo apt-get install python3-tk")
os.system("sudo apt-get install python-tk")
#
os.system("mkdir -p /usr/icon")
os.system("mkdir -p /usr/program")

os.system("mkdir -p /usr/program/Backup")
copyfile("/etc/wpa_supplicant/wpa_supplicant.conf", "/usr/program/Backup/wpa_supplicant.conf") #WifiBackup
copyfile("/boot/config.txt", "/usr/program/Backup/config.txt") #DisplayBackup
copyfile("/etc/xdg/lxsession/LXDE-pi/autostart", "/usr/program/Backup/autostart") #UrlBackup
#TimeBackup is REMOVE file created to Reset



os.system("sudo mv /home/pi/ui/ui.py /usr/program")

os.system("sudo mv /home/pi/ui/iconui.png /usr/icon")
os.system("sudo mv /home/pi/ui/My_calendar_logo.png /usr/icon")
os.system("sudo mv /home/pi/ui/My_calendar_logo.png /usr/icon")
os.system("sudo mv /home/pi/ui/rotate.png /usr/icon")
os.system("sudo mv /home/pi/ui/setting.png /usr/icon")
os.system("sudo mv /home/pi/ui/time.png /usr/icon")
os.system("sudo mv /home/pi/ui/url.png /usr/icon")
os.system("sudo mv /home/pi/ui/whiteWifi.png /usr/icon")
os.system("sudo mv /home/pi/ui/wifi.png /usr/icon")

fin = open("/home/pi/Desktop/Calendar.Desktop", "wt")
fin.write('''[Desktop Entry]
Type=Application
Name= Lịch Thông Minh
Icon=/usr/icon/My_calendar_logo.png
Exec=sudo python3 /usr/program/ui.py
X-Desktop-File-Install-Version=0.20''')
fin.close()
os.system("sudo chmod +x /home/pi/Desktop/Calendar.Desktop")

os.system("sudo apt-get install unclutter")
os.system("sudo rm -r /home/pi/ui")
os.system("sudo rm -r /home/pi/Downloads/install")

