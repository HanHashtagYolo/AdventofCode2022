import os

def getPoints(opp, you):
	score = 0
	if you == 'X':
		if opp == 'A':
			score = score + 3
		if opp == 'B':
			score = score + 1
		if opp == 'C':
			score = score + 2
	if you == 'Y':
		score = 3
		if opp == 'A':
			score = score + 1
		if opp == 'B':
			score = score + 2
		if opp == 'C':
			score = score + 3
	if you == 'Z':
		score = 6
		if opp == 'A':
			score = score + 2
		if opp == 'B':
			score = score + 3
		if opp == 'C':
			score = score + 1
	return score


file = open("Day2Input.txt")

totalScore = 0
for line in file:
	opp, you = line.strip().split(" ")
	totalScore = totalScore + getPoints(opp,you)

print totalScore
