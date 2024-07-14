'''
    This modified dfs works just like a regular depth first search except when a cell has nowhere to go 
    due to it have already visted the neighboring cells or they are blocked it pops the leftmost element of the stack
    giving it a performance that is constantly between depth and breadth first search.
    for more info check out https://medium.com/@birukg500/depth-breadth-first-search-bef6cf6182ca
'''

from pyamaze import maze, agent, textLabel, COLOR
from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def pop_left(self):
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0
    

def moded_DFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    
    explored = [start]
    frontier = Stack()
    frontier.push(start)
    dSearch = []

    while not frontier.is_empty():
        currCell = frontier.pop()
        dSearch.append(currCell)

        if currCell == m._goal:
            break

        poss = 0
        blocked = 0 # we keep count of the neighbors that aren't available 
        for d in 'ESNW':
            if m.maze_map[currCell][d] == False:
                blocked += 1
            else:
                if d == 'E':
                    child = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    child = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    child = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    child = (currCell[0] + 1, currCell[1])
                
                if child in explored:
                    blocked += 1
                    continue

                poss += 1
                explored.append(child)
                frontier.push(child)
        
        if poss > 1:
            m.markCells.append(currCell)
        
        #if blocked is 4 ,the cells have no valid neighbors
        if blocked == 4:
            left= frontier.pop_left()
            frontier.push(left)

    return dSearch

if __name__ == '__main__':
    m = maze(20, 25)  # Change to any size
    m.CreateMaze(loopPercent=10)
    dSearch = moded_DFS(m)

    a = agent(m, footprints=True, shape='arrow', color=COLOR.cyan)
    m.tracePath({a: dSearch}, showMarked=True, delay=50)
    print("the number of cells visted using a moded depth first algorithm: ",len(dSearch))
    m.run()
