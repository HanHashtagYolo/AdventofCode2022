import os

file = open("Day1Input1.txt")

elf = 1
calorieCnt = []
calories = 0
newmax = 0
sortedCalories = []

for line in file:
	if len(line.strip()) > 0:
		num = int(line.strip())
		calories = calories + num
	else:
		calorieCnt.append(calories)
		calories = 0

calorieCnt.append(calories)
calorieCnt.sort(reverse=True)
print calorieCnt[0] + calorieCnt[1] + calorieCnt[2]