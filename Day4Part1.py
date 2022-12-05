import os

file = open("Day4Input.txt")

subsetCnt = 0
for line in file:
	elf1, elf2 = line.strip().split(',')
	elf1split = elf1.split('-')
	elf2split = elf2.split('-')
	elf1range = range(int(elf1.split('-')[0]),int(elf1.split('-')[1])+1)
	elf2range = range(int(elf2.split('-')[0]),int(elf2.split('-')[1])+1)
	if set(elf2range).issubset(set(elf1range)) or set(elf1range).issubset(set(elf2range)):
		subsetCnt = subsetCnt + 1
print subsetCnt