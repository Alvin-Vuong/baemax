import subprocess

# assume we already have database of emotion

# if happy, will play upbeat, happy songs (fuck yeah! songs)
# if sad, either play slow, "sad" songs OR can play pick-me-up song
# if angry, either play "anger" song
# if calm = relaxed/normal state, play not sad song
# if nervous, play pumped-up songs OR relaxed music 

# 0 = low or negative, 1 = high or positive
# 0 = low&negative, 1 (01) = low&positive, 2 (10) = high&negative, 3 (11) = high&positive

# INPUT 1: HAPPY
emotion = 0
if emotion == 0:

	#filepath="path of the batch file"
	filepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/SadSongs.bat"
	p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

	stdout, stderr = p.communicate()
	print p.returncode 
	# 0 if success

elif emotion == 1:
	
	#filepath="path of the batch file"
	filepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/CalmSongs.bat"
	p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

	stdout, stderr = p.communicate()
	print p.returncode 
	# 0 if success

elif emotion == 2:

	#filepath="path of the batch file"
	filepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/AngrySongs.bat"
	p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

	stdout, stderr = p.communicate()
	print p.returncode 
	# 0 if success
	
elif emotion == 3:

	#filepath="path of the batch file"
	filepath="C:/Users/Allison/Documents/GitHub/baemax/PlayingSong/HappySongs.bat"
	p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

	stdout, stderr = p.communicate()
	print p.returncode 
	# 0 if success