from random import randint
from pyamaze import maze,agent,COLOR
from queue import PriorityQueue




def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2) + abs(y1-y2)

def greedy(m, start, goal):
    score={cell:float('inf') for cell in m.grid}
    score[start]=h(start,goal)

    open=PriorityQueue()
    open.put((h(start,goal),start))
    greedyPath={}
    greedySearch = []
    while not open.empty():
        currCell=open.get()[1]
        greedySearch.append(currCell)
        if currCell==goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_score=h(childCell,goal)

                if temp_score < score[childCell]:
                    score[childCell]= temp_score
                    open.put((temp_score,childCell))
                    greedyPath[childCell]=currCell
    path={}
    cell=goal
    while cell!=start:
        path[greedyPath[cell]]=cell
        cell=greedyPath[cell]
    return path, greedySearch



def aStar(m, start, goal):
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,goal)

    open=PriorityQueue()
    open.put((h(start,goal),h(start,goal),start))
    aStarPath={}
    aStarSearch = []
    while not open.empty():
        currCell=open.get()[2]
        aStarSearch.append(currCell)
        if currCell==goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,goal)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,goal),childCell))
                    aStarPath[childCell]=currCell
    path={}
    cell=goal
    while cell!=start:
        path[aStarPath[cell]]=cell
        cell=aStarPath[cell]
    return path, aStarSearch


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
    solpathA, dfssearchpath = aStar(m,start,goal)
    solpathB, greedypath = greedy(m,start,goal)
    agentA=agent(m,c,d,footprints=True,filled = True, shape = 'square')
    agentB=agent(m,c,d,footprints=True, shape='square', color=COLOR.red)
    m.tracePath({agentB:dfssearchpath},delay = 100)
    m.tracePath({agentA:solpathA},delay = 10)
    agentC=agent(m,c,d,footprints=True,filled = True, shape = 'square', color=COLOR.black)
    agentD=agent(m,c,d,footprints=True, shape='square', color=COLOR.yellow)
    m.tracePath({agentD:greedypath},delay = 100)
    m.tracePath({agentC:solpathB},delay = 10)
    m.run()