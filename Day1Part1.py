import os

file = open("Day1Input1.txt")

calories = 0
newmax = 0

for line in file:
	if len(line.strip()) > 0:
		num = int(line.strip())
		calories = calories + num
	else:
		if calories > newmax:
			newmax = calories
		calories = 0

if calories > newmax:
	newmax = calories
print newmax