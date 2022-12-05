import os
import string

file = open("Day3Input.txt")

items = []
sacks = []
for line in file:
	sacks.append(line.strip())

total = 0
for i in range(0,len(sacks)-1,3):
	for item in sacks[i]:
		if item in sacks[i+1] and item in sacks[i+2]:
			if item in string.ascii_lowercase:
				total = total + (ord(item) - 96)
			else:
				total = total + (ord(item) - 38)
			break

print total