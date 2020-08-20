import pyttsx3
import os
pyttsx3.speak("hello may i know your name")
name=input()
while True:
	
	pyttsx3.speak("Hello"+name)
	pyttsx3.speak("which operation you would like to run")
	command=input()
	command.lower()
	if(("run" in command)or ("execute" in command) or ("open" in command)) and (("media" in command) or ("player" in command)) and ("not" not in command):
		os.system("start wmplayer")
	elif(("run" in command)or ("execute" in command) or ("open" in command)) and ("mail" in command) and ("not" not in command):
		os.system("start chrome www.gmail.com")
	elif(("run" in command)or ("execute" in command) or ("open" in command)) and (("internet" in command)or ("explorer" in command)) and ("not" not in command):
		os.system("start iexplore")
	elif(("run" in command)or ("execute" in command) or ("open" in command)) and ("calcultor" in command) and ("not" not in command):
		os.system("start chrome www.calculator.net")
	elif(("run" in command)or ("execute" in command) or ("open" in command)) and (("sql" in command) or ("mysql" in command)) and ("not" not in command):
		os.system("start MySQLInstallerConsole")
	elif("close" in command) or ("exit" in command):
		break
	else:
		pyttsx3.speak("operation not available")