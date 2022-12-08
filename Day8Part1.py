import os
treeMap = []
def checkVertical(h, w, heightBound):
	global treeMap
	treeValue = treeMap[h][w]
	#check to 0
	upVisible = True
	a = h - 1
	while a >= 0:
		if treeMap[a][w] >= treeValue:
			upVisible = False
			break
		a = a - 1
	#check to bound
	downVisible = True
	a = h + 1
	while a <= heightBound:
		if treeMap[a][w] >= treeValue:
			downVisible = False
			break
		a = a + 1
	return (upVisible or downVisible)
def checkHorizontal(h, w, widthBound):
	global treeMap
	treeValue = treeMap[h][w]
	#check to 0
	leftVisible = True
	a = w - 1
	while a >= 0:
		if treeMap[h][a] >= treeValue:
			leftVisible = False
			break
		a = a - 1
	#check to bound
	rightVisible = True
	a = w + 1
	while a <= widthBound:
		if treeMap[h][a] >= treeValue:
			rightVisible = False
			break
		a = a + 1
	return (leftVisible or rightVisible)
def checkVisible(width,height,h,w):
	heightBound = height - 1
	widthBound = width - 1
	if checkVertical(h, w, heightBound) or checkHorizontal(h, w, widthBound):
		return True
	else:
		return False

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

#count edges
edgeTrees = (2 * len(treeMap[0])) - 4 #-4 to account for corners
for row in treeMap:
	edgeTrees += 2

interiorTrees = 0
for h in range(1,width-1):
	for w in range(1,height-1):
		if checkVisible(width,height,h,w):
			interiorTrees += 1
print interiorTrees + edgeTrees