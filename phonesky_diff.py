import subprocess
import time

subprocess.Popen("adb shell pm list packages | sed \'s/package://g\' > diff.txt", shell=True)

for app in open("applist.txt"):
	print("Checking: " + app)
	if app not in open("diff.txt"):
		input("/ENTER/: ")
		subprocess.Popen("adb shell am start -a android.intent.action.VIEW -d \'market://details?id=" + app + "\'", shell=True)
		time.sleep(5)
