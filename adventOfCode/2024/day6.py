from utility import *

directions=[(0,-1),(1,0),(0,1),(-1,0)]

def guardLoopA(currentPosition, walls, limits):
  maxX=limits[0]
  maxY=limits[1]
  grid={}
  currentDirectionIdx=0
  while(0<=currentPosition[0]<=maxX and 0<=currentPosition[1]<=maxY):
    grid[currentPosition]="█"
    tentative=sumTupleValueByValue(currentPosition, directions[currentDirectionIdx])
    while(tentative in walls):
      currentDirectionIdx=(currentDirectionIdx+1)%len(directions)
      tentative=sumTupleValueByValue(currentPosition, directions[currentDirectionIdx])
    currentPosition=tentative
  return list(grid.keys())

def guardLoopB(currentPosition, walls, limits):
  maxX=limits[0]
  maxY=limits[1]
  currentDirectionIdx=0
  visited=set()
  while(0<=currentPosition[0]<=maxX and 0<=currentPosition[1]<=maxY):
    if (currentPosition, currentDirectionIdx) in visited:
      return 1
    visited.add((currentPosition, currentDirectionIdx))
    tentative=sumTupleValueByValue(currentPosition, directions[currentDirectionIdx])
    while(tentative in walls):
      currentDirectionIdx=(currentDirectionIdx+1)%len(directions)
      tentative=sumTupleValueByValue(currentPosition, directions[currentDirectionIdx])
    currentPosition=tentative
  return 0

def solve():
  rows=getOldAocInput(6)
  grid, maxX, maxY=buildGrid(rows)
  currentPosition=[k for k,v in grid.items() if v=="^"][0]
  walls=set([k for k,v in grid.items() if v=="#"])
  return  len(guardLoopA(currentPosition, walls, (maxX, maxY)))

def solveB():
  rows=getOldAocInput(6)
  grid, maxX, maxY=buildGrid(rows, None)
  currentPosition=[k for k,v in grid.items() if v=="^"][0]
  walls=set([k for k,v in grid.items() if v=="#"])
  grid[currentPosition]="."
  possibleWalls=guardLoopA(currentPosition, walls, (maxX, maxY))

  ris=0
  for elementIdx in range(len(possibleWalls)):
    ris=ris+guardLoopB(currentPosition, walls.union(set([possibleWalls[elementIdx]])), (maxX, maxY))
  return ris

print(solve())
print(solveB())
# print(solveB())

