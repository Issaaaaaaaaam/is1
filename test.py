from random import randint
from pyamaze import maze,agent,COLOR

def DFS(m,start,goal):

    explored=[start] # stack to keep track of the explored cells 
    neighbors=[start] # keep track of the neighbors of the current cell 
    dfssearch = []
    dfsPath={}

    while len(neighbors)>0:
        currCell=neighbors.pop()
        explored.append(currCell)
        dfssearch.append(currCell)
        if currCell==goal:
            break
        for direction in 'ESNW':
            if m.maze_map[currCell][direction]==True:
                if direction =='E':
                    childCell=(currCell[0],currCell[1]+1)

                elif direction =='W':
                    childCell=(currCell[0],currCell[1]-1)

                elif direction =='S':
                    childCell=(currCell[0]+1,currCell[1])

                elif direction =='N':
                    childCell=(currCell[0]-1,currCell[1])

                if childCell in explored:
                    continue
                neighbors.append(childCell)
                dfsPath[childCell]=currCell # we write the path on reverse so that there is no duplicate keys. 
    path={}
    cell=goal
    while cell!=start:
        path[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return path, dfssearch 


def BFS(m,start,goal):

    explored=[start] # stack to keep track of the explored cells 
    neighbors=[start] # keep track of the neighbors of the current cell 
    bfssearch = []
    bfsPath={}
    while len(neighbors)>0:
        currCell = neighbors.pop(0)
        bfssearch.append(currCell)
        if currCell==goal:
            break
        for direction in 'ESNW':
            if m.maze_map[currCell][direction]==True:
                if direction =='E':
                    childCell=(currCell[0],currCell[1]+1)

                elif direction =='W':
                    childCell=(currCell[0],currCell[1]-1)

                elif direction =='S':
                    childCell=(currCell[0]+1,currCell[1])

                elif direction =='N':
                    childCell=(currCell[0]-1,currCell[1])

                if childCell in explored:
                    continue
                explored.append(childCell)
                neighbors.append(childCell)
                bfsPath[childCell]=currCell # we write the path on reverse so that there is no duplicate keys. 
    path={}
    cell=goal
    while cell!=start:
        path[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return path, bfssearch 




if __name__=='__main__':
    a = randint(1,25)
    b = randint(1,25)
    c = randint(1,25)
    d = randint(1,25)
    goal = (a,b)
    start = (c,d)
    m=maze(25,25)
    m.CreateMaze(a,b,loopPercent=100)
    solpath, dfssearchpath = BFS(m,start,goal)
    agentA=agent(m,c,d,footprints=True,filled = True, shape = 'square')
    agentB=agent(m,c,d,footprints=True, shape='square', color=COLOR.red)
    m.tracePath({agentB:dfssearchpath},delay = 10)
    m.tracePath({agentA:solpath},delay = 10)
    m.run()