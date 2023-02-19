from pyamaze import maze, agent, textLabel
from queue import PriorityQueue

def h(targetNode, goalNode):
	return abs(goalNode[0] - targetNode[0]) + abs(goalNode[1] - targetNode[1])

def AStar(m):
	start = (m.rows, m.cols)
	end = (1,1)

	openSet = PriorityQueue()
	aStarPath = {}
	gScore = {}
	fScore ={}

	for cell in m.grid:
		gScore[cell] = float('inf')
		fScore[cell] = float('inf')
	gScore[start] = 0
	fScore[start] = h(start, end)
	openSet.put((fScore[start], start))

	while not openSet.empty():
		openGet = openSet.get()
		currCell = openGet[1]
		print (currCell)
		if currCell == end:   #if curret node is the goal, stop
			break
		#explore each node, the order for visit is 'East,South, West, North
		for d in 'EWSN':
            #verify if the direction is open, i.e. there is not a "wall" between nodes
			if m.maze_map[currCell][d] == True:     #The path is open
				if d=='E':
					childCell = (currCell[0],currCell[1]+1) #move agent to the right column
				elif d=='W':
					childCell = (currCell[0],currCell[1]-1) #move agent to the left column
				elif d=='S':
					childCell = (currCell[0]+1,currCell[1]) #move agent to the bottom row  
				elif d=='N':
					childCell = (currCell[0]-1,currCell[1]) #move agent to the up row

				tentativeGScore = gScore[currCell] + 1
				tentativeFScore = tentativeGScore + h(childCell, end)

				if tentativeFScore < fScore[childCell]:
					gScore[childCell] = tentativeGScore
					fScore[childCell] = tentativeFScore
					openSet.put((tentativeFScore, childCell))
					aStarPath[childCell] = currCell
	fwdPath={}
	cell=(1,1)
	while cell!=start:
		fwdPath[aStarPath[cell]]=cell
		cell=aStarPath[cell]
	return fwdPath 


#rows and cols must are variables, so factual values are needed to avoid errors
rows = 80
cols = 100
m = maze(rows,cols)
m.CreateMaze() #create a maze with one path
pathAStar = AStar(m)
a = agent(m, footprints = True)
m.tracePath({a:pathAStar})
#m.maze_map gives list of walls for all cells as a dictionary 
l=textLabel(m,'Path Length',len(m.path)+1) #display the cost of the solution
m.run()