import subprocess
import re

#varCommand = C:\Users\Paul\Desktop\TestExe.cmd
varCommand = raw_input ("Enter URL")

myProcess = subprocess.Popen(
	[varCommand],
	stdout = subprocess.PIPE,
	stderr = subprocess.PIPE)
	
out, error = myProcess.communicate()

print out