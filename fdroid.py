import subprocess
import time

### FILL THESE VALUES FIRST ###

#fdroid_button_1.png
X_1 = 0
Y_1 = 0

#fdroid_button_2.png
X_2 = 0
Y_2 = 0

subprocess.Popen("adb shell pm list packages | sed \'s/package://g\' > diff_fdroid.txt", shell=True)
subprocess.Popen("wget https://f-droid.org/FDroid.apk", shell=True)
adb install FDroid.apk
for app in open("applist.txt"):
	print("Checking: " + app)
	if app not in open("diff_fdroid.txt"):
		print("Installing: " + app)
		subprocess.Popen("adb shell am start -a android.intent.action.VIEW -d \'market://details?id=" + app + "\'", shell=True)
		time.sleep(1)
                #comment the line below if you're a /g/entooman
		subprocess.Popen("adb shell input tap " + str(X_1) + " " + str(Y_1), shell=True)
		time.sleep(1)
		subprocess.Popen("adb shell input tap " + str(X_2) + " " + str(Y_2), shell=True)
		time.sleep(1)
