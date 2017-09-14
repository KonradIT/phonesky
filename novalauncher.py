import subprocess
import time

#Nova.txt: launcher.db componentName (https://i.imgur.com/Bp8q4TH.png)
file = open('nova.txt', 'r')
text = file.read()
subprocess.Popen("adb shell pm list packages | grep " + app.split("/")[0] + " > app.txt", shell=True)
for app in text:
	print("Checking: " + app.split("/")[0])
	file = open('app.txt', 'r')
	text = file.read()
	if "package:"+app.split("/")[0] != text:
		print("TEST" + text)
		print("TEST2"+app.split("/")[0])
