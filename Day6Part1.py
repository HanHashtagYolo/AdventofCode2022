import os

file = open("Day6Input.txt")
a = file.readline().strip()

startMark = []
stopI = 0
for i in range(0,len(a)-3):
	startMark = a[i:i+4]
	isStart = True
	for letter in startMark:
		if startMark.count(letter) > 1:
			isStart = False
			break
	if isStart:
		stopI = i
		break

print i, i+4

