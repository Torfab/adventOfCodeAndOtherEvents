from utility import *

directions=[(0,-1),(1,0),(0,1),(-1,0)]

def guardLoopA(currentPosition, walls, outside):

  gridSet=set()
  currentDirectionIdx=0
  while(currentPosition not in outside):
    gridSet.add(currentPosition)
    tentative=sumTupleValueByValue(currentPosition, directions[currentDirectionIdx])
    while(tentative in walls):
      currentDirectionIdx=(currentDirectionIdx+1)%len(directions)
      tentative=sumTupleValueByValue(currentPosition, directions[currentDirectionIdx])
    currentPosition=tentative
  return gridSet

def guardLoopB(currentPosition, walls, outside):
  currentDirectionIdx=0
  d=directions[currentDirectionIdx]
  visited=set()
  while(currentPosition not in outside):
    tentative=sumTupleValueByValue(currentPosition, d)
    if tentative not in walls:
      currentPosition=tentative
    else:
      currentDirectionIdx=(currentDirectionIdx+1)%len(directions)
      d=directions[currentDirectionIdx]  
      if (currentPosition, currentDirectionIdx) in visited:
        return 1
      visited.add((currentPosition, currentDirectionIdx))
  return 0

def buildOutside(limits):
  outside=set()
  for x in range(-1,limits[0]+2):
    outside.add((x,-1))
    outside.add((x,limits[1]+1))
  for y in range(-1,limits[1]+2):
    outside.add((-1,y))
    outside.add((limits[0]+1,y))
  return outside

def solve(part):
  rows=getOldAocInput(6)
  grid, maxX, maxY=buildGrid(rows, None)
  currentPosition=[k for k,v in grid.items() if v=="^"][0]
  walls=set([k for k,v in grid.items() if v=="#"])
  outside=buildOutside((maxX,maxY))
  possibleWalls=guardLoopA(currentPosition, walls, outside)
  if(part=="a"):
    return len(possibleWalls)
  possibleWalls.remove(currentPosition)
  ris=0
  for element in possibleWalls:
    ris=ris+guardLoopB(currentPosition, walls.union(set([element])), outside)
  return ris

print(solve("a"))
print(solve("b"))

