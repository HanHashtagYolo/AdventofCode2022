import os
import string

file = open("Day3Input.txt")

items = []
for line in file:
	line = line.strip()
	midPoint = len(line)/2
	comp1 = line[:midPoint]
	comp2 = line[midPoint:]
	for item in comp1:
		if item in comp2:
			items.append(item)
			break

print items
total = 0
for letter in items:
	if letter in string.ascii_lowercase:
		total = total + (ord(letter) - 96)
	else:
		total = total + (ord(letter) - 38)
print total
	
