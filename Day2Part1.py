import os

def getPoints(opp, you):
	score = 0
	if you == 'X':
		score = 1
		if opp == 'A':
			score = score + 3
		if opp == 'B':
			pass
		if opp == 'C':
			score = score + 6
	if you == 'Y':
		score = 2
		if opp == 'A':
			score = score + 6
		if opp == 'B':
			score = score +3
		if opp == 'C':
			pass
	if you == 'Z':
		score = 3
		if opp == 'A':
			pass
		if opp == 'B':
			score = score + 6
		if opp == 'C':
			score = score + 3
	return score


file = open("Day2Input.txt")

totalScore = 0
for line in file:
	opp, you = line.strip().split(" ")
	totalScore = totalScore + getPoints(opp,you)

print totalScore

