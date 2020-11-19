#!/usr/bin/env python3
import os
import time
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import font as tkfont
import tkinter as Settings


def Fix_monitor():
	#os.system("sudo nano /boot/config.txt")
	#
	fin = open("/boot/config.txt", "r")
	t = 0
	while(True):
		#read next line
		line = fin.readline()
		#if line is empty, you are done with all lines in the file
		if not line:
			break
		#you can access the line
		if line.strip() == "disable_overscan=1":
			t = 1
			break
	if t == 0:
		f = open("/boot/config.txt", "at")
		f.write('\noverscan_left=16\noverscan_right=16\noverscan_top=16\noverscan_bottom=16\ndisable_overscan=1\n')
		f.close()
#Fix_monitor()
def make_textmenu(ui):
	global the_menu
	the_menu = Menu(ui, tearoff=0)
	the_menu.add_command(label="Cut")
	the_menu.add_command(label="Copy")
	the_menu.add_command(label="Paste")
	the_menu.add_separator()
	the_menu.add_command(label="Select all")
def callback_select_all(event):
	# select text after 50ms
	ui.after(50, lambda:event.widget.select_range(0, 'end'))
def show_textmenu(event):
	e_widget = event.widget
	the_menu.entryconfigure("Cut",command=lambda: e_widget.event_generate("<<Cut>>"))
	the_menu.entryconfigure("Copy",command=lambda: e_widget.event_generate("<<Copy>>"))
	the_menu.entryconfigure("Paste",command=lambda: e_widget.event_generate("<<Paste>>"))
	the_menu.entryconfigure("Select all",command=lambda: e_widget.select_range(0, 'end'))
	the_menu.tk.call("tk_popup", the_menu, event.x_root, event.y_root)
#########
def Complete():
	#print("complete OK")
	def Reboot():
		ui.quit()
		os.system("sudo reboot")
	def Later():
		top.quit()
	size16 = tkfont.Font(size = 16)
	size12 = tkfont.Font(size = 12)
	size13 = tkfont.Font(size = 13)
	size11 = tkfont.Font(size = 11)
	top = Toplevel()
	top.geometry("400x82+745+449")
	top.title("Completed!")
	top.configure(bg='gray85')
	Completed = Label(top, text= " Reboot now to apply settings!", bg="gray85", fg="black", font=size12)
	past = Label(top, text= "  ", bg="gray85")
	Reboot = Button(top, text="Reboot", command= Reboot, bg="gray80")
	Later = Button(top, text="Later!", command= Later, bg="gray80" )
	Completed.grid(row = 0, column = 0)
	past.grid(row = 1, column = 0)
	Reboot.grid(row = 2, column = 0, sticky = 'WN', padx = 20)
	Later.grid(row = 2, column = 1, sticky = 'EN', padx = 71)
def ApplyExit():
	test_t = ""
	if(e0.get() != test_t):
		SetNetwork()
	#
	if(eUrl.get() !="https://"):
		#print("url ok")
		AddUrl()
	SetDisplay()
	SetTimeDisplay()
	#print("Apply OK")
	Complete()
	#
	Check_update_ui()
#KeyBoard
def Out(event):
    n = 1
def ShowKB_e0(event): 
    create(frame, e0)
    #e0.bind("<FocusIn>", Out)
def ShowKB_e1(event):
    create(frame, e1)
def ShowKB_eUrl(event): 
    create(frame, eUrl)
#def Outfocus(event):
    #print(event.type) 
#Map
alphabets = [
	['esc','~','!','@','#','$','%','^','&','*','(',')','_','Backspace'],
    ['`','1','2','3','4','5','6','7','8','9','0','-','=','+'],
    ['Tab','q','w','e','r','t','y','u','i','o','p','[',']',"\\"],
    ['Caps Lock','a','s','d','f','g','h','j','k','l',':','"','Enter'],
    ['Shift','z','x','c','v','b','n','m',',','.','/','Shift'],
    ['Space']
]    
uppercase = False  
def select(entry, value):
    global uppercase
    if value == "Space":
        value = ' '
    elif value == 'Enter':
        value = '\n'
    elif value == 'Tab':
        value = '\t'
    elif value == 'esc':
        ui.quit()
    elif value == "Backspace":
        if isinstance(entry, Entry):
            entry.delete(len(entry.get())-1, 'end')
        else: # tk.Text
            entry.delete('end - 2c', 'end')
    elif value in ('Caps Lock', 'Shift'):
        uppercase = not uppercase # change True to False, or False to True
    else:
        if uppercase:
            value = value.upper()
        entry.insert('end', value)
def create(window, entry):
    window.configure(background="gray30")
    #window.wm_attributes("-alpha", 0.7)
    for y, row in enumerate(alphabets):
        x = 0
        #for x, text in enumerate(row):
        for text in row:
            if text in ('Enter', 'Shift','Backspace', 'Caps Lock','+'):
                width = 10
                height = 2
                columnspan = 2
            elif text == 'Space':
                width = 80
                height = 2
                columnspan = 16
            else:                
                width = 5
                height = 2
                columnspan = 1
            Button(window, text=text, width=width, height = height, font = size13,
                      command=lambda value=text: select(entry, value),
                      padx=1, pady=1, bd=5, bg="black", fg="white",
                     ).grid(row=y, column=x, columnspan=columnspan)
            x += columnspan
            window.grid(row=7, column=0, columnspan = 6, sticky = 'S')
    #ui.geometry("1049x722")
#WiFi
def WifiTab():
	create(frame, e0)
	destroyRotateDl()
	destroyAddUrl()
	destroyTimeTab()
	#...
	ui.geometry("1049x759")
	NetLabel.grid(row=0, column=3)
	Label0.grid(row=1, column=2)
	e0.grid(row=1, column=3)
	Label1.grid(row=2, column=2)
	e1.grid(row=2, column=3)
	#NetApply.grid(row=4, column=4, sticky='ES')
	e0.bind("<FocusIn>", ShowKB_e0) #Keyboard
	#e0.bind("<FocusOut>", Outfocus)
	e1.bind("<FocusIn>", ShowKB_e1)
def SetNetwork(): #For root & Pi
		#Completed.grid(row=3, column=4, sticky = 'S')
		#print (">>>I.Set Wifi Name&Pass:")
		ssid = e0.get()
		#print("ssid = " + ssid)
		passwd = e1.get()
		#print("passWd = " + passwd)
		fin = open("/etc/wpa_supplicant/wpa_supplicant.conf", "rt")
		data = fin.read()
		data = data.replace('''update_config=1''', '''update_config=1
network={
	ssid="''' + ssid + '''"
	psk="''' + passwd + '''"
    key_mgmt=WPA-PSK
}''')
		fin.close()
		fin = open("/etc/wpa_supplicant/wpa_supplicant.conf", "wt")
		fin.write(data)
		fin.close()
		#os.system("sudo nano /etc/wpa_supplicant/wpa_supplicant.conf")
#DISPLAY rotate
def RotateTab():
	destroyWifi()
	destroyAddUrl()
	destroyTimeTab()
	
	window.grid_remove() #
	ui.geometry("1049x408")#
	
	Up_Choice.grid(row=1, column=3, sticky='W')
	R_Choice.grid(row=2, column=3, sticky='W')
	Down_Choice.grid(row=3, column=3, sticky='W')
	L_Choice.grid(row=4, column=3, sticky='W')
	DlLabel.grid(row=0, column=3)
	#AfterbootLabelgrid(row=0, column=4)
	ChoiceLabel.grid(row=1, column=2, sticky='N')
	
	ChoiceLabel_2.grid(row=1, column=3, sticky='N')
	
	Size_choice.grid(row=3, column=3, sticky='E')
	#ChoiceSize_box.grid(row=2, column=3, sticky='E')
	AutoFix_Choice.grid(row=2, column=3, sticky='E')
	Default_Choice.grid(row=1, column=3, sticky='E')
	
	
	
	#DlApply.grid(row=4, column=4, sticky='ES')
	
def SetDisplay(): ##For root & Pi
	#os.system("sudo nano /boot/config.txt")
	#print(v.get())
	n = v.get()
	test = 0
	fin = open("/boot/config.txt", "r")
	while(True):
		#read next line
		line = fin.readline()
		#if line is empty, you are done with all lines in the file
		if not line:
			break
		#you can access the line
		if line.strip() == "display_rotate=0":
			f = open("/boot/config.txt", "rt")
			data = f.read()
			data = data.replace('display_rotate=0','display_rotate=' + str(n))
			f.close()
			f = open("/boot/config.txt", "wt")
			f.write(data)
			f.close()
			test = test + 1
			#print("replaced")
		if line.strip() == "display_rotate=1":
			f = open("/boot/config.txt", "rt")
			data = f.read()
			data = data.replace('display_rotate=1','display_rotate=' + str(n))
			f.close()
			f = open("/boot/config.txt", "wt")
			f.write(data)
			f.close()
			test = test + 1
		if line.strip() == "display_rotate=2":
			f = open("/boot/config.txt", "rt")
			data = f.read()
			data = data.replace('display_rotate=2','display_rotate=' + str(n))
			f.close()
			f = open("/boot/config.txt", "wt")
			f.write(data)
			f.close()
			test = test + 1
		if line.strip() == "display_rotate=3":
			f = open("/boot/config.txt", "rt")
			data = f.read()
			data = data.replace('display_rotate=3','display_rotate=' + str(n))
			f.close()
			f = open("/boot/config.txt", "wt")
			f.write(data)
			f.close()
			test = test + 1
	fin.close
	#print(test)
	if test == 0:
		f = open("/boot/config.txt", "at")
		f.write('\ndisplay_rotate=' + str(n));
		f.close()
	#os.system("sudo nano /boot/config.txt")
	


#
	def add_disable_overscan():
		fin = open("/boot/config.txt", "r")
		check_now = 0
		while(True):
			#read next line
			line = fin.readline()
			#if line is empty, you are done with all lines in the file
			if not line:
				break
			if line.strip() == "disable_overscan=1":
				check_now = 1
		if check_now == 0:
			#print("check now Auto_ OK")
			f = open("/boot/config.txt", "at")
			f.write('\ndisable_overscan=1');
			f.close()
	def delete_group_and_mode():
		fin = open("/boot/config.txt", "r")
		while(True):
			line = fin.readline()
			if not line:
				break
			#you can access the line
			if line.strip() == "hdmi_group=1":
				f = open("/boot/config.txt", "rt")
				data = f.read()
				data = data.replace('hdmi_group=1','')
				f.close()
				f = open("/boot/config.txt", "wt")
				f.write(data)
				f.close()
			if line.strip() == "hdmi_group=2":
				f = open("/boot/config.txt", "rt")
				data = f.read()
				data = data.replace('hdmi_group=2','')
				f.close()
				f = open("/boot/config.txt", "wt")
				f.write(data)
				f.close()
		######
		######
		for x in range(100):
			f = open("/boot/config.txt","r")
			lines = f.readlines()
			f.close()
			f = open("/boot/config.txt","w")
			for line in lines:
				if line!="hdmi_mode="+ str(x):
					f.write(line)
			f.close()
		
		
	#print(v_r_size.get())
	s = v_r_size.get()
	#print(s)
	if s == 0:
		delete_group_and_mode()
		#Delete_command
		f = open("/boot/config.txt", "rt")
		data = f.read()
		data = data.replace('disable_overscan=1','')
		f.close()
		f = open("/boot/config.txt", "wt")
		f.write(data)
		f.close()
		#...
	if s == 1:
		delete_group_and_mode()
		#Delete_command_and_...
		add_disable_overscan()
	#Tuy chon:
	if s == 2:
		delete_group_and_mode()
		add_disable_overscan()
		Choice_now = ChoiceSize_box.get()
		#line1_now = 0
		#line2_now = 0
		def check_for_group_1():
			line1_now = 0
			line2_now = 0
			#check_line1..:
			fin = open("/boot/config.txt", "r")
			while(True):
				#read next line
				line = fin.readline()
				if not line:
					break
				if line.strip() == "hdmi_group=2":
					f = open("/boot/config.txt", "rt")
					data = f.read()
					data = data.replace('hdmi_group=2',line1)
					f.close()
					f = open("/boot/config.txt", "wt")
					f.write(data)
					f.close()
					line1_now = 1
					break
				if line.strip() == line1:
					line1_now = 1
					break
			#add if chua co:
			if line1_now == 0:
				f = open("/boot/config.txt", "at")
				f.write('\n'+line1);
				f.close()
				
			##Check_line2..:
			fin = open("/boot/config.txt", "r")
			while(True):
				#read next line
				line = fin.readline()
				if not line:
					break
				if line.strip() == line2:
					line2_now = 1
					break
			#add if chua co:
			if line2_now == 0:
				f = open("/boot/config.txt", "at")
				f.write('\n'+line2);
				f.close()
		def check_for_group_2():
			line1_now = 0
			line2_now = 0
			#check_line1..:
			fin = open("/boot/config.txt", "r")
			while(True):
				#read next line
				line = fin.readline()
				if not line:
					break
				if line.strip() == "hdmi_group=1":
					f = open("/boot/config.txt", "rt")
					data = f.read()
					data = data.replace('hdmi_group=1',line1)
					f.close()
					f = open("/boot/config.txt", "wt")
					f.write(data)
					f.close()
					line1_now = 1
					break
				if line.strip() == line1:
					line1_now = 1
					break
			#add if chua co:
			#print(line1_now)
			if line1_now == 0:
				f = open("/boot/config.txt", "at")
				f.write('\n'+line1);
				f.close()
				
			##Check_line2..:
			fin = open("/boot/config.txt", "r")
			while(True):
				#read next line
				line = fin.readline()
				if not line:
					break
				if line.strip() == line2:
					line2_now = 1
					break
			#add if chua co:
			if line2_now == 0:
				f = open("/boot/config.txt", "at")
				f.write('\n'+line2);
				f.close()
		if Choice_now ==' CEA-640x480(4:3)':
			line1 = "hdmi_group=1"
			line2 = "hdmi_mode=1"
			check_for_group_1()
				
		if Choice_now ==' CEA-720x480(4:3)':
			line1 = "hdmi_group=1"
			line2 = "hdmi_mode=2"
			check_for_group_1()
			
		if Choice_now ==' CEA-1280x720(16:9)':
			line1 = "hdmi_group=1"
			line2 = "hdmi_mode=4"
			check_for_group_1()
			
		if Choice_now ==' CEA-1920x1080(16:9)':
			line1 = "hdmi_group=1"
			line2 = "hdmi_mode=16"
			check_for_group_1()
			
		if Choice_now ==' CEA-3840x2160(16:9)':
			line1 = "hdmi_group=1"
			line2 = "hdmi_mode=97"
			check_for_group_1()
			
		#####
		
		if Choice_now ==' DMT-480p(4:3)':
			line1 = "hdmi_group=2"
			line2 = "hdmi_mode=2"
			check_for_group_2()
			
		if Choice_now ==' DMT-800x600(4:3)':
			line1 = "hdmi_group=2"
			line2 = "hdmi_mode=9"
			check_for_group_2()
			
		if Choice_now ==' DMT-1024x768(4:3)':
			line1 = "hdmi_group=2"
			line2 = "hdmi_mode=16"
			check_for_group_2()
			
		if Choice_now ==' DMT-1280x720(16:9)':
			ine1 = "hdmi_group=2"
			line2 = "hdmi_mode=85"
			check_for_group_2()
			
		if Choice_now ==' DMT-1600x1200(4:3)':
			line1 = "hdmi_group=2"
			line2 = "hdmi_mode=51"
			check_for_group_2()
			
		if Choice_now ==' DMT-1920x1080(16:9)':
			line1 = "hdmi_group=2"
			line2 = "hdmi_mode=82"
			check_for_group_2()
			
		if Choice_now ==' DMT-1280x1024(5:4)':
			line1 = "hdmi_group=2"
			line2 = "hdmi_mode=35"
			check_for_group_2()
			
			
		#Delete_command_and_...
			
                        
                        
		
				
		
	
#...
#AddURL
def UrlTab():
	create(frame, eUrl)
	destroyWifi()
	destroyRotateDl()
	destroyTimeTab()
	#
	ui.geometry("1049x759")
	UrlLabel.grid(row=0, column=3)
	Label31.grid(row=1, column=2)
	eUrl.grid(row=1, column=3)
	#UrlApply.grid(row=4, column=4, sticky='ES')
	#
	eUrl.bind("<FocusIn>", ShowKB_eUrl) #Keyboard
	#
def AddUrl(): #For root & Pi
	url = eUrl.get()
	UserURL_new = url
	fin = open("/etc/xdg/lxsession/LXDE-pi/autostart", "wt") # replace all
	fin.write('''@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
@xset s off
@xset -dpms
@xset s 0 0
@xset s noblank
@xset s noexpose
@xset dpms 0 0 0
@chromium-browser --noerrdialogs --incognito --autoplay-policy=no-user-gesture-required --check-for-update-interval=1 --simulate-critical-update --kiosk ''' + url + "\n");
	fin.close()
	if UserURL_new != "":
		f = open("/usr/program/ui.py", "rt")
		data = f.read()
		data = data.replace(UserURL,UserURL_new)
		f.close()
		f = open("/usr/program/ui.py", "wt")
		f.write(data)
		f.close()
	#os.system("sudo nano /etc/xdg/lxsession/LXDE-pi/autostart")
	#Completed.grid(row=3, column=4, sticky = 'S')
##TTME On-Off
def TimeTab():
	destroyWifi()
	destroyRotateDl()
	destroyAddUrl()
	window.grid_remove() #
	ui.geometry("1049x408")# 950x350 old
	TimeLabel.grid(row= 0, column= 3)
	cmLabel.grid(row= 1, column= 3, sticky = 'N')
	OnLabel.grid(row= 2, column= 2, sticky = 'N')
	OffLabel.grid(row= 3, column= 2)
	On_Label.grid(row= 2, column= 3, sticky = 'NW')
	Off_Label.grid(row= 3, column= 3, sticky = 'W')
	hOn_box.grid(row= 2, column= 3,  sticky = 'W') #rowspan = 2
	mOn_box.grid(row= 2, column= 3) #rowspan = 2
	hOff_box.grid(row= 3, column= 3,  sticky = 'SW') #rowspan = 2
	mOff_box.grid(row= 3, column= 3, sticky = 'S') #rowspan = 2
	#On_frame.grid(row= 3, column= 3, rowspan = 2, sticky = 'WN')
	#Off_frame.grid(row= 3, column= 3, rowspan = 2, sticky = 'EN', padx=35)
	#Time_Apply.grid(row= 4, column= 4, sticky = 'ES')
def convertTime(t):
	if t == "00":
		t = "0"
	if int(t) < 10 and int(t) > 0:
		t = t.replace("0", "")
	return t
def SetTimeDisplay():   #redef for /root OR /home/pi/ 
	mOn = mOn_box.get()
	hOff = hOff_box.get()
	mOff = mOff_box.get()
	#Convert 00 => 0
	hOn = convertTime(hOn_box.get())
	mOn = convertTime(mOn)
	hOff = convertTime(hOff)
	mOff = convertTime(mOff)
	fin = open("/home/pi/rpi-hdmi.sh", "wt") #create/open  #paste .sh
	fin.write('''#!/bin/sh
	# Enable and disable HDMI output on the Raspberry Pi
	is_off ()
	{
		tvservice -s | grep "TV is off" >/dev/null
	}
	case $1 in
		off)
			tvservice -o
		;;
		on)
			if is_off
			then
				tvservice -p
				curr_vt=`fgconsole`
				if [ "$curr_vt" = "1" ]
				then
					chvt 2
					chvt 1
				else
					chvt 1
					chvt "$curr_vt"
				fi
			fi
		;;
		status)
			if is_off
			then
				echo off
			else
				echo on
			fi
		;;
		*)
			echo "Usage: $0 on|off|status" >&2
			exit 2
		;;
	esac
	exit 0
	''')
	fin.close()
	#os.system("sudo nano /home/pi/rpi-hdmi.sh") #CHECK
	os.system("sudo chmod +x /home/pi/rpi-hdmi.sh")
	#Create file py Time On Off Display
	fin = open("/home/pi/OnOffDisplay.py", "wt") #create file On_Off
	fin.write('''#!/usr/bin/python3
#!/usr/bin/env python3
import os
import datetime
import time
hOff = ''' + hOff + '''
mOff = ''' + mOff + '''
hOn = ''' + hOn + '''
mOn = ''' + mOn + '''
while True:
	t = datetime.datetime.now()
	hNow = t.hour
	mNow = t.minute
	#print(sNow)
	if hNow == hOff and mNow == mOff:
		os.system("sudo /home/pi/rpi-hdmi.sh off")
		#print(mNow)
		#time.sleep(59)
	elif hNow == hOn and mNow == mOn:
		os.system("sudo /home/pi/rpi-hdmi.sh on")
		#time.sleep(59)
	time.sleep(1)
''') #edit sOn = mOn ... delete (print..) Time sleep
	os.system("mkdir -p /home/pi/.config/autostart") #create folder
	#Create file auto 
	fin = open("/home/pi/.config/autostart/auto.desktop", "wt") #create/paste file Auto after boot _ edit to /home/pi/.config or /root/.config
	fin.write('''[Desktop Entry]
Encoding=UTF-8
Name=OnOffDisplay autostart
Comment=Start file auto py on backg
Exec=nohup /home/pi/OnOffDisplay.py &''')
	fin.close()
	#chmod +x for file
	os.system("sudo chmod +x /home/pi/OnOffDisplay.py") #Tested file Ok
	#Completed.grid(row=3, column=4, sticky = 'S')
	#os.system("sudo nano /home/pi/OnOffDisplay.py") #CHECK OnOffDisplay.py
	#os.system("sudo nano /home/pi/.config/autostart/auto.desktop") #CHECK auto.desktop
	#Switch current time
	hOn = convertTime(hOn_box.get()) #delete
	mOn = convertTime(mOn)
	hOff = convertTime(hOff)
	mOff = convertTime(mOff)
	#fin = open("/usr/program/TimeCurrent.txt", "wt") #create file if file not found or replace
	#fin.write("""""")
	#fin.close()
def GetTimeOld():
	for i in range(0, 60):
		text_hOn = "hOn = " + str(i)
		text_mOn = "mOn = " + str(i)
		text_hOff = "hOff = " + str(i)
		text_mOff = "mOff = " + str(i)
		fin = open("/home/pi/OnOffDisplay.py", "r")
		while(True):
		#read next line
			line = fin.readline()
		#if line is empty, you are done with all lines in the file
			if not line:
				break
		#you can access the line
			if line.strip() == text_hOn:
				hOn_box.current(i)
				#print("found hOn")
			if line.strip() == text_mOn:
				mOn_box.current(i)
				#print("found mOn")
			if line.strip() == text_hOff:
				hOff_box.current(i)
				#print("found hOff")
			if line.strip() == text_mOff:
				mOff_box.current(i)
				#print("found mOff")
		fin.close
##DISTROY
def destroyWifi():
	NetLabel.grid_remove()
	Label0.grid_remove()
	Label1.grid_remove()
	e0.grid_remove()
	e1.grid_remove()
	NetApply.grid_remove()
	#Completed.grid_remove()
	#window.grid_remove() #ESC
	#ui.geometry("950x350")
def destroyRotateDl():
	Up_Choice.grid_remove()
	R_Choice.grid_remove()
	Down_Choice.grid_remove()
	L_Choice.grid_remove()
	DlLabel.grid_remove()
	ChoiceLabel.grid_remove()
	DlApply.grid_remove()
	
	ChoiceLabel_2.grid_remove()
	Default_Choice.grid_remove()
	AutoFix_Choice.grid_remove()
	ChoiceSize_box.grid_remove()
	Size_choice.grid_remove()
	ChoiceLabel_3.grid_remove()
	#Completed.grid_remove()
	#window.grid_remove() #ESC
	#ui.geometry("950x350")
def destroyAddUrl():
	UrlLabel.grid_remove()
	Label31.grid_remove()
	eUrl.grid_remove()
	UrlApply.grid_remove()
	#Completed.grid_remove()
	#window.grid_remove() #ESC
	#ui.geometry("950x350")
def destroyTimeTab():
	TimeLabel.grid_remove()
	cmLabel.grid_remove()
	OnLabel.grid_remove()
	OffLabel.grid_remove()
	On_Label.grid_remove()
	Off_Label.grid_remove()
	hOn_box.grid_remove()
	mOn_box.grid_remove()
	hOff_box.grid_remove()
	mOff_box.grid_remove()
	Time_Apply.grid_remove()
	#Completed.grid_remove()
	#window.grid_remove() #ESC
	#ui.geometry("950x350")
######## 
ui = Tk()
frame = Frame(ui) #KeyBoard
window = frame
#ui.iconphoto(False, Tk.PhotoImage(file='/root/Desktop/My_icon/pngbarn.png'))
ui.title("Settings")
ui.configure(bg='gray30')
size16 = tkfont.Font(size = 16)
size12 = tkfont.Font(size = 12)
size13 = tkfont.Font(size = 13)
size11 = tkfont.Font(size = 11)
        ### WIFI Creating Label widget:
NetLabel = Label(ui, text="Wi-Fi            ", bg="gray30", fg="white", font=size16) #SSID
Label0 = Label(ui, text="Tên (SSID) ", bg="gray30", fg="white", font=size12) #SSID
e0 = Entry(ui, width=50, bg="ghost white", fg="black")
#e0.insert(0, "Enter WIFI name") #edit Language
Label1 = Label(ui, text=" Mật khẩu :   ", bg="gray30", fg="white", font=size12) #Pass
e1 = Entry(ui, width=50, bg="ghost white", fg="black", borderwidth=1)
#e1.insert(0, "Enter the network security key") #edit Language
NetApply = Button(ui, text=" Apply  ", command=SetNetwork)

        ### RotateDisplay Creating Label widget:
DlLabel = Label(ui, text="  Xoay & Tùy Chỉnh Kích Thước Màn Hình", bg="gray30", fg="white", font=size16) #Rotate Display
ChoiceLabel = Label(ui, text="         Xoay:  ", bg="gray30", fg="white", font=size12) 
#
ChoiceLabel_2 = Label(ui, text="     Kích thước:    ", bg="gray30", fg="white", font=size12)
ChoiceLabel_3 = Label(ui, text="   *--Lựa chọn--:", bg="gray30", fg="white", font=size12)


def select_size_choice():
	Size_choice.select()
	Size_choice.flash()
	#grid Box_size
	ChoiceSize_box.grid(row=4, column=3, sticky='EN')
	ChoiceLabel_3.grid(row=4, column=3, sticky='N')
def select_default():
	Default_Choice.select()
	Default_Choice.flash()
	#print(v_r_size.get())
	ChoiceSize_box.grid_remove()
	ChoiceLabel_3.grid_remove()
def select_autofix():
	AutoFix_Choice.select()
	AutoFix_Choice.flash()
	ChoiceSize_box.grid_remove()
	ChoiceLabel_3.grid_remove()
		
v_r_size = IntVar()
Size_choice = Radiobutton(ui, bg="gray80", fg="black", width = 16, height = 1,
            text="     Tùy chỉnh           ",
            padx = 5, 
            variable=v_r_size, 
            value=2, command = select_size_choice)
Default_Choice = Radiobutton(ui, bg="gray80", fg="black", width = 16, height = 1,
            text="     Mặc định           ",
            padx = 5, 
            variable=v_r_size, 
            value=0, command = select_default)
AutoFix_Choice = Radiobutton(ui, bg="gray80", fg="black", width = 16, height = 1,
            text="   Tự động tràn       ",
            padx = 5, 
            variable=v_r_size, 
            value=1, command = select_autofix)
#
v_t_size = StringVar
ChoiceSize_box = Combobox(ui, textvariable = v_t_size, width = 17, height = 4, font = size11)
ChoiceSize_box['values'] = (' CEA-640x480(4:3)',  
                        ' CEA-720x480(4:3)', 
                        ' CEA-1280x720(16:9)', 
                        ' CEA-1920x1080(16:9)', 
                        ' CEA-3840x2160(16:9)', 
                        ' DMT-480p(4:3)',  
                        ' DMT-800x600(4:3)',  
                        ' DMT-1024x768(4:3)',  
                        ' DMT-1280x720(16:9)',  
                        ' DMT-1600x1200(4:3)',  
                        ' DMT-1920x1080(16:9)',  
                        ' DMT-1280x1024(5:4)')       

#
#
AfterbootLabel = Label(ui, text="Settings will be applied after reboot", bg="gray30", fg="white", font=size12)
def select_Up():
	Up_Choice.select()
	Up_Choice.flash()
def select_R():
	R_Choice.select()
	R_Choice.flash()
def select_Down():
	Down_Choice.select()
	Down_Choice.flash()
def select_L():
	L_Choice.select()
	L_Choice.flash()
v = IntVar()
Up_Choice = Radiobutton(ui, bg="gray80", fg="black",
            text=" Hướng Lên      ",
            padx = 5, 
            variable=v, 
            value=0, command = select_Up)
            
R_Choice = Radiobutton(ui, bg="gray80", fg="black",
            text=" Xoay Phải       ",
            padx = 5, 
            variable=v, 
            value=1, command = select_R)
            
Down_Choice  = Radiobutton(ui, bg="gray80", fg="black",
            text=" Hướng Xuống  ",
            padx = 5, 
            variable=v, 
            value=2, command = select_Down)
            
L_Choice = Radiobutton(ui, 
            text=" Xoay Trái        ", bg="gray80", fg="black",
            padx = 5, 
            variable=v, 
            value=3, command = select_L)   #.pack(anchor=W)
            
f = open("/boot/config.txt", "r")
check_size = 0
while(True):
	#read next line
	line = f.readline()
	#if line is empty, you are done with all lines in the file
	if not line:
		break
	#you can access the line
	if line.strip() == "display_rotate=0":
		Up_Choice.select()
		Up_Choice.flash()
	if line.strip() == "display_rotate=1":
		R_Choice.select()
		R_Choice.flash()
	if line.strip() == "display_rotate=2":
		Down_Choice.select()
		Down_Choice.flash()
	if line.strip() == "display_rotate=3":
		L_Choice.select()
		L_Choice.flash()
		#print(line.strip() + " old")
		
	if line.strip() == "disable_overscan=1":
		AutoFix_Choice.select()
		AutoFix_Choice.flash()
		check_size = 1
	
	#close file
	f.close
if check_size == 0:
	Default_Choice.select()
	Default_Choice.flash()
	
DlApply = Button(ui, text=" Apply  ", command = SetDisplay) #Apply

        ### URL Creating Label widget:
UrlLabel = Label(ui, text="URL              ", bg="gray30", fg="white", font= size16)
Label31 = Label(ui, text="Nhập URL", bg="gray30", fg="white", font= size12) #
eUrl = Entry(ui, width=50, bg="ghost white", fg="black")

UserURL = "https://"
eUrl.insert(0, UserURL) #edit Language
UrlApply = Button(ui, text=" Apply  ", command= AddUrl)

		### Time On-Off screen Creating Label widget:
TimeLabel = Label(ui, text="Đặt lịch tự động Tắt & Mở            ", bg="gray30", fg="white", font= size16)
cmLabel = Label(ui, text="Automatic configuration will be applied after reboot!                   ", bg="gray30", fg="white", font= size12)
OnLabel = Label(ui, text="                     Mở vào lúc:   ", bg="gray30", fg="white", font= size12) #
OffLabel = Label(ui, text="                     Tắt vào lúc:  ", bg="gray30", fg="white", font= size12) #
On_Label = Label(ui, text="         Giờ                                             Phút   ", bg="gray30", fg="white")
Off_Label = Label(ui, text="         Giờ                                             Phút   ", bg="gray30", fg="white")
Time_Apply = Button(ui, text=" Apply  ", command = SetTimeDisplay) #On_Label.config(text=str(hOn))
####BOx_Time_On
#On_frame = Frame(ui)
hOn_items = list(range(0, 24))
for i in range(0, 24):
	if i < 10:
		hOn_items[i] = str("0" + str(i))
	else:
		hOn_items[i] = str(i)
hOn_box = Combobox(ui, values = hOn_items, width = 10, height = 9, font = size11)	
hOn_box.current(7) #defaut value
#minute
mOn_items = list(range(0, 60))
for i in range(0, 60):
	if i < 10:
		mOn_items[i] = str("0" + str(i))
	else:
		mOn_items[i] = str(i)
mOn_box = Combobox(ui, values = mOn_items, width = 10, height = 9, font = size11)
mOn_box.current(0) #defaut value
######BOx_Time_Off
#Off_frame = Frame(ui)
hOff_items = list(range(0, 24))
for i in range(0, 24):
	if i < 10:
		hOff_items[i] = str("0" + str(i))
	else:
		hOff_items[i] = str(i)
hOff_box = Combobox(ui, values = hOff_items, width = 10, height = 5, font = size11)	
hOff_box.current(22) #defaut value
mOff_items = list(range(0, 60))
for i in range(0, 60):
	if i < 10:
		mOff_items[i] = str("0" + str(i))
	else:
		mOff_items[i] = str(i)
mOff_box = Combobox(ui, values = mOn_items, width = 10, height = 5, font = size11)
mOff_box.current(0) #defaut value
#
#OK = Button(ui, text="OK", command=print_choice) #button 
#TimeApply = Button(ui, text=" Apply  ", command= )
#19/11/20
#os.system("sudo rm -r /home/pi/versionui")

#time.sleep(10)
def Show_update():
	def Update():
		os.system("sudo rm /usr/program/ui.py")
		os.system("sudo mv /home/pi/ui/ui.py /usr/program")
		
		#os.system("sudo rm -r /home/pi/versionui")
		top_done = Toplevel()
		top_done.geometry("400x82+745+449")
		top_done.title("Đã hoàn tất cập nhật!")
		top_done.configure(bg='gray85')
		Completed = Label(top_done, text= " Sẽ khởi động lại phần mềm", bg="gray85", fg="black", font=size12)
		Completed.grid(row = 0, column = 0)
		time.sleep(2)
		ui.quit()
		#os.system("sudo python3 /usr/program/ui.py")
		os.system("sudo rm -r /home/pi/ui")
		os.system("sudo rm -r /home/pi/versionui")
	def Later():
		os.system("sudo rm -r /home/pi/ui")
		top.quit()
		os.system("sudo rm -r /home/pi/versionui")
	size16 = tkfont.Font(size = 16)
	size12 = tkfont.Font(size = 12)
	size13 = tkfont.Font(size = 13)
	size11 = tkfont.Font(size = 11)
	top = Toplevel()
	top.geometry("310x82+745+449")
	top.title("Cập nhật Lịch Thông Minh!")
	top.configure(bg='gray85')
	Completed = Label(top, text= "     Đã tải xuống version mới!\nKhởi động lại ứng  sau khi cập nhật!", bg="gray85", fg="black", font=size12)
	#past = Label(top, text= "  ", bg="gray85")
	Completed.grid(row = 0, column = 0)
	Update = Button(top, text="Cập nhật!", command= Update, bg="gray80")
	Later = Button(top, text=" Thoát! ", command= Later, bg="gray80" )
	
	#past.grid(row = 1, column = 0)
	Update.grid(row = 1, column = 0, sticky = 'WN', padx = 30)
	Later.grid(row = 1, column = 0, sticky = 'EN', padx = 20)
def Check_update_ui():
	#os.system("sudo rm -r /home/pi/versionui")
	fin = open("/home/pi/versionui/version.txt", "r")
	check_now = 0
	while(True):
		line = fin.readline()
		if not line:
			break
		if line.strip() == version:
			print("line.strip() == version")
			
			
			size12 = tkfont.Font(size = 12)
			top = Toplevel()
			top.geometry("347x82+745+449")
			top.title("Cập nhật Lịch Thông Minh!")
			top.configure(bg='gray85')
			Completed = Label(top, text= "   Phiên bản hiện tại đã là bản mới nhất!\n" + version, bg="gray85", fg="black", font=size12)
			past = Label(top, text= "  ", bg="gray85")
			Completed.grid(row = 0, column = 0)
			
			os.system("sudo rm -r /home/pi/versionui")
			break
		else:
			os.system("sudo rm -r /home/pi/ui")
			os.system("git clone https://github.com/HuynhLVC/ui.git")
			Show_update()
			break
			
#
import urllib.request
def connect(host='https://youtube.com'):
	try:
		urllib.request.urlopen(host) #Python 3.x
		return True
	except:
		return False
	#check
#def waitting_show():
def Update():
	#
	if connect():
		os.system("git clone https://github.com/HuynhLVC/versionui.git")
		Check_update_ui()
		#print("connect -> check_update")
	else:
		#print("no internet")
		size12 = tkfont.Font(size = 12)
		top = Toplevel()
		top.geometry("347x82+745+449")
		top.title("Thông báo cập nhật!")
		top.configure(bg='gray85')
		Completed = Label(top, text= "không có kết nối internet!", bg="gray85", fg="black", font=size12)
		past = Label(top, text= "  ", bg="gray85")
		Completed.grid(row = 0, column = 0)
		#os.system("sudo rm -r /home/pi/versionui")
	
	
#### MENU
iconWifi = PhotoImage(file = r"/usr/icon/wifi.png")
Wifiimage = iconWifi.subsample(11, 11)
iconDl = PhotoImage(file = r"/usr/icon/rotate.png")
Dlimage = iconDl.subsample(18, 18)
iconUrl = PhotoImage(file = r"/usr/icon/url.png")
Urlimage = iconUrl.subsample(10, 10)
iconTime = PhotoImage(file = r"/usr/icon/time.png")
Timeimage = iconTime.subsample(18, 18)
Net = Button(ui, image = Wifiimage, compound=LEFT, text = "Wi-Fi   ", bg="gray80", fg="black",width=275, height=45, font=size13 , borderwidth=3, command = WifiTab) 
Dl = Button(ui,image = Dlimage, compound=LEFT, text = "Màn Hình & Xoay   ", bg="gray80", fg="black",width=275, height=45, font=size13, borderwidth=3, command = RotateTab) # when not (icon compound=LEFT,) width=27, height=2,
Url = Button(ui, image = Urlimage, compound=LEFT, text = "Nhập URL   ", bg="gray80", fg="black",width=275, height=45, font=size13, borderwidth=3, command = UrlTab)
Tdl = Button(ui, image = Timeimage, compound=LEFT, text = "Tắt & Mở tự động   ", bg="gray80",width=275, height=45, font=size13, borderwidth=3, command = TimeTab) # 
ExitBt = Button(ui, text = "< Áp Dụng >", bg="gray80", fg="black",width=25, height=2, font=size13, borderwidth=3, command = ApplyExit) 
Update = Button(ui, compound=LEFT, text = "Bản cập nhật", bg="gray80",width=25, height=2, font=size13, borderwidth=3, command = Update) # 
KeyUse = Label(ui, text= "                                                                       Khởi động lại để chắc chắc cài đặt được áp dụng! - (ESC để hủy và thoát!) ", bg="gray30", fg="white", font=size12)

# Shoving it into the screen
Net.grid(row=0, column=0, sticky = 'W')
Dl.grid(row=1, column=0, sticky = 'W')
Url.grid(row=2, column=0, sticky = 'W') 
Tdl.grid(row=3, column=0, sticky = 'W')

Update.grid(row=4, column=0, sticky = 'W')
ExitBt.grid(row=5, column=0, sticky = 'W')
KeyUse.grid(row=6, column =0, columnspan = 5, sticky =  'S')
#Update
WifiTab()
create(frame, e0)
if os.path.exists("/home/pi/OnOffDisplay.py") == True:
	GetTimeOld()
#
ui.geometry("1049x759+400+100") #Zise def 950x350
#ui.geometry("1049x722+400+100") #Zise def 950x350
#ui.iconbitmap('/usr/icon/My_calender_logo.ico')
##Start_Paste_Entry
make_textmenu(ui)
# bind the feature to all Entry widget
ui.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_textmenu)
ui.bind_class("Entry", "<Control-a>", callback_select_all)
##End_Paste_Entry
##Update&Upgrade:
version = "version_1.5"

ui.mainloop()
