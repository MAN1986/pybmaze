'''
    This modified dfs works just like modified dfs algorithm except it pops the middle element of the stack should the cell have no neighbors
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

    def pop_middle(self):
        if len(self.items) == 0:
            raise IndexError("pop_middle from an empty stack")
        middle_index = len(self.items) // 2
        return self.items[middle_index]

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
        blocked = 0
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

        if blocked == 4:
            middle_index = len(frontier.items) // 2
            middle = frontier.items[middle_index]
            del frontier.items[middle_index]
            frontier.push(middle)

    return dSearch


if __name__ == '__main__':
    m = maze(20, 25)  # Change to any size
    m.CreateMaze(loopPercent=10)
    dSearch = moded_DFS(m)

    a = agent(m, footprints=True, shape='arrow', color=COLOR.cyan)
    m.tracePath({a: dSearch}, showMarked=True, delay=50)
    print("the number of cells visted using a middle moded depth first algorithm: ",len(dSearch))
    m.run()