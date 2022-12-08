import os

file = open("Day7Input.txt")

fileStruct = {}
currentDir = ''
for line in file:
	line = line.strip()
	if '$' in line:
		if 'cd' in line:
			if '..' in line:
				currentDir = currentDir[:currentDir[:-1].rfind('/')] + '/'
				if currentDir == '':
					currentDir = '/'
			else:
				if '/' in line:
					currentDir = '/'
				else:
					currentDir = currentDir + line.split(' ')[2] + '/'

	else:
		if 'dir' not in line:
			size = int(line.split(' ')[0])
			if currentDir not in fileStruct:
				fileStruct[currentDir] = size
			else:
				fileStruct[currentDir] = fileStruct[currentDir] + size

dirSize = {}
currentSum = 0
for item in fileStruct:
	currentSum = 0
	currentDir = ''
	dirs = item[:-1].split('/')
	for folder in dirs:
		currentDir = currentDir + folder + '/'
		if currentDir in dirSize:
			dirSize[currentDir] = dirSize[currentDir] + fileStruct[item]
		else:
			dirSize[currentDir] = fileStruct[item]

total = 0
for d in dirSize:
	if dirSize[d] <= 100000:
		total = total + dirSize[d]
print total



