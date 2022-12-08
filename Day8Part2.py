import os
treeMap = []
def vertScore(h, w, heightBound):
	global treeMap
	treeValue = treeMap[h][w]
	#check to 0
	upScore = 0
	a = h - 1
	while a >= 0:
		upScore = upScore + 1
		if treeMap[a][w] >= treeValue:
			break
		a = a - 1
	#check to bound
	downScore = 0
	a = h + 1
	while a <= heightBound:
		downScore = downScore + 1
		if treeMap[a][w] >= treeValue:
			break
		a = a + 1
	return upScore * downScore
def horzScore(h, w, widthBound):
	global treeMap
	treeValue = treeMap[h][w]
	#check to 0
	leftScore = 0
	a = w - 1
	while a >= 0:
		leftScore = leftScore + 1
		if treeMap[h][a] >= treeValue:
			break
		a = a - 1
	#check to bound
	rightScore = 0
	a = w + 1
	while a <= widthBound:
		rightScore = rightScore + 1
		if treeMap[h][a] >= treeValue:
			break
		a = a + 1
	return leftScore * rightScore
def getScore(width,height,h,w):
	heightBound = height - 1
	widthBound = width - 1
	return vertScore(h, w, heightBound) * horzScore(h, w, widthBound)


file = open("Day8Input.txt")


height = 0
width = 0
for line in file:
	line = line.strip()
	rowArray = []
	for item in line:
		rowArray.append(int(item))
	treeMap.append(rowArray)
width = len(rowArray)
height = len(treeMap)

scenicScore = 0
newScore = 0
for h in range(1,width-1):
	for w in range(1,height-1):
		newScore = getScore(width,height,h,w) 
		if newScore > scenicScore:
			scenicScore = newScore

print scenicScore