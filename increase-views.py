#@author  Hussam Soufi: hussam1soufi@gmail.com

import webbrowser
import time
import os
url = "https://www.youtube.com/watch?v=G4gWUnzRLQU&t=4s" #the video URL
while True:
    webbrowser.open(url)
    time.sleep(1.5*60) #set the time of the video in seconds
    #os.system("taskkill /im firefox.exe /f") #if you use firefox
    os.system("taskkill /im chrome.exe /f")   #if you use chrome
