import subprocess
import time

### FILL THESE VALUES FIRST! ###

#phonesky_button_1.png
X_1 = 0
Y_1 = 0

#phonesky_button_2.png
X_2 = 0
Y_2 = 0

for app in open("applist.txt"):
	print("Installing: " + app)
	subprocess.Popen("adb shell am start -a android.intent.action.VIEW -d \'market://details?id=" + app + "\'", shell=True)
	time.sleep(5)
	subprocess.Popen("adb shell input tap " + str(X_1) + " " + str(Y_1), shell=True)
	time.sleep(2)
	subprocess.Popen("adb shell input tap " + str(X_2) + " " + str(Y_2), shell=True)
	time.sleep(2)
