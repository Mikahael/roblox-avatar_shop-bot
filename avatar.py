#D E S T I N Y#4693
#www.github.com/Mikahael
#
import time
import datetime
import webbrowser
import pyautogui



'''
README**
File created by PCMODDER/DESTINY/AVAROHANA
All rights reserved to the group above - licensed soon
Works only for WINDOWS with FIREFOX!
Licensed under Mozzila Public License 2.0
#
TO USE **
Fill out day, night, and url
Edit click duration only if necessary - bad net
#
INSTALLATION**
Install python 3.10 - latest
Install python-pip - should be installed with python
Install pyautogui - pip install pyautogui
QUESTIONS??**
Message me on discord - #D E S T I N Y#4693
'''



#time of release
#aka min time
#
day = '21:47:00'
#
#add 1 or 2 minute after time of release
#aka max time
#
night = '21:48:00'
#
#give the url
#
url = "https://www.roblox.com/catalog/6340213/Roundy"
#
#
#click duration - recommened 3-5
#
#
click = 5



#enter message
print('Thanks to PCMODDER/DESTINY/AVAROHANA\n')
print('Not the time yet, waiting for the time!')
print('Runs under MILITARY TIME only!')
print('Time set ---> '+day)

#establish the loop
while(True):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    #calulate time between min and max
    #global variable not needed
    if current_time > day and current_time < night:
        # Register Firefox as a browser with webbrowser module
        webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
        #
        #
        x1, y1 = 1042, 409
        x2, y2 = 900, 747
        # Begin the process
        print("Process has begun\n")
        webbrowser.get("firefox").open(url)
        pyautogui.moveTo(x1, y1)
        pyautogui.click(duration=click)
        pyautogui.moveTo(x2, y2)
        pyautogui.click(duration=2)
        #
        print('Process finished')
        print('Bot created by PCMODDER / DESTINY / AVAROHANA!')
        #break loop
        break
        
#To whomsoever this may concern, all rights to PCMODDER/PC231392/Mikahael, as the license states.
#We are not liable to any damages - however there should be none.
#Licensed under Mozzila Public License 2.0
