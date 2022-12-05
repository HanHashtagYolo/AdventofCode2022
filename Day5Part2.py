import os

stacks = {}
def doMoves(numFromTo):
	global stacks
	num = numFromTo[0]
	From = numFromTo[1]
	To = numFromTo[2]
	for i in range(num,0,-1):
		stacks[To].append(stacks[From][0-i])
	for j in range(0,num):
		stacks[From].pop()

file = open("Day5Input.txt")
text = file.read()
stack, moves = text.split('\n\n')

stack = stack.split('\n')
moves = moves.split('\n')

lastNum = int(stack[-1].strip().split(' ')[-1])

for i in range(1,lastNum+1):
	stacks[i] = []

for j in range(0,len(stack)-1):
	for k in range(0,len(stack[j]),4):
		if '[' in stack[j][k:k+3]:
			stacks[(k/4)+1].append(stack[j][k+1])
for item in stacks:
	stacks[item].reverse()

moveList = []
for item in moves:
	numFromTo = []
	temp = item.split(' ')
	numFromTo.append(int(temp[1]))
	numFromTo.append(int(temp[3]))
	numFromTo.append(int(temp[5]))
	moveList.append(numFromTo)

for move in moveList:
	doMoves(move)

output = ''
for item in stacks:
	output = output+stacks[item][-1]

print output