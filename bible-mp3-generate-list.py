import glob, os

# Generate list of chapters from mp3 files

# Change folders
os.chdir('/home/user/bible/')

# Get list of mp3 files in folder
mp3list = glob.glob("*.mp3")
# Sort mp3 list by name since they are already ordered by number
mp3list.sort()

# Input "66 Revelation Chapter 01.mp3"
# Target list structure output: ["66 Revelation","01"],
for x in mp3list:
	list = x.split(" Chapter ")
	verse = list[1].split(".")
	out = '["'+list[0]+'","'+verse[0]+'"],'
	print(out)
