import os

file = open("Day4Input.txt")

overlap = 0
for line in file:
	elf1, elf2 = line.strip().split(',')
	elf1split = elf1.split('-')
	elf2split = elf2.split('-')
	elf1range = range(int(elf1.split('-')[0]),int(elf1.split('-')[1])+1)
	elf2range = range(int(elf2.split('-')[0]),int(elf2.split('-')[1])+1)
	for number in elf1range:
		if number in elf2range:
			overlap = overlap+1
			break
print overlap