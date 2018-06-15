
from gpiozero import DigitalInputDevice
import time
import subprocess
import sys,os
from datetime import datetime, timedelta
from pid import PidFile

with PidFile(piddir='/home/pi/run/'):

	radar = DigitalInputDevice(17, pull_up=False, bounce_time=2.0)
	laststatus = 0
	while True:
		if radar.is_active == False:              
			if laststatus==1:
				if (datetime.now()-lastseen) > timedelta(minutes=8):
					subprocess.Popen('vcgencmd display_power 0', shell=True).wait()
					laststatus=0
		elif radar.is_active == True:           
			lastseen = datetime.now()
		        if laststatus==0:
        	        subprocess.Popen('vcgencmd display_power 1', shell=True).wait()
	            laststatus=1
		time.sleep(1)

