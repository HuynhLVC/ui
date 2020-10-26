#!/usr/bin/env python3

import os
os.system("sudo apt-get install python3-tk")
os.system("sudo apt-get install python-tk")
os.system("sudo mv /home/pi/Desktop/install_folder/icon /usr")
os.system("sudo mv /home/pi/Desktop/install_folder/program /usr")
fin = open("/home/pi/Desktop/Calendar.Desktop", "wt")
fin.write('''[Desktop Entry]
Type=Application
Name= Lịch Thông Minh
Icon=/usr/icon/My_calendar_logo.png
Exec=sudo python3 /usr/program/ui.py
X-Desktop-File-Install-Version=0.20''')
fin.close()
os.system("sudo chmod +x /home/pi/Desktop/Calendar.Desktop")

os.system("sudo rm -r /home/pi/Desktop/install_folder")