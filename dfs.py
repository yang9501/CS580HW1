#Coded by Loreto Gonzalez-Hernandez
#Introduction to AI

from pyamaze import maze, agent, textLabel
def DFS(m):
    start= (m.rows, m.cols)#coordinate of the start cell >> here is low rigth corner
    explored=[start]#Explored nodes in the frontier
    frontier=[start]#Nodes in the frontier
    #if there are no more nodes to explore
    dfsPath={}
    while len(frontier)>0: #if there are still nodes to explore
        currCell=frontier.pop() #node to explore, 
        if currCell == (1,1):   #if curret node is the goal, stop
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
                if childCell in explored:   #if node has been explored
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                #store the coordinates of the path in a dictionary
                dfsPath[childCell]=currCell
    #The path is stored in backwards, so we need to change it
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath 

m= maze(5,5)
m.CreateMaze() #loopPercent=100 generates more than one path
path = DFS(m)
a = agent(m,footprints=True)
m.tracePath({a:path})
m.run()