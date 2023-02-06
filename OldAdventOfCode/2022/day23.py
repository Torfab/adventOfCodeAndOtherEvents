from utility import *

day=23

directionVector=[(0,-1),(0, 1),(-1,0),(1,0)]
directionToCheck={(0,-1): [(-1,-1),(0,-1), (1,-1)], (0, 1): [(-1,1),(0,1), (1,1)], (-1,0): [(-1,-1),(-1,0), (-1,1)], (1,0): [(1,-1),(1,0), (1,1)]}

def realPrint(grid: dict):
  maxX=max(element[0] for element in grid)
  minX=min(element[0] for element in grid)
  maxY=max(element[1] for element in grid)
  minY=min(element[1] for element in grid)
  for i in range(minY,maxY+1):
    for j in range(minX, maxX+1):
      element=grid.get((j,i))
      if(element==None):
        print(".", end="")
      else:
        print(element, end="")
    print()
  print()

def comprehension(rows):
  grid=dict()
  for idxy, y in enumerate(rows):
    for idxx, x in enumerate(y):
      if(x=="#"):
        grid[(idxx,idxy)]="#"
  return grid

def moveElf(startTile, endTile, grid:dict):
  grid.pop(startTile)
  grid[endTile]="#"

def isFreeSpace(elf, direction, grid):
  result= True
  for element in directionToCheck[direction]:
    if(grid.get(sumTupleValueByValue(elf, element))!=None):
      result=False
  return result

def findCandidatePosition(elf, grid):
  candidateTile=elf
  freeDirection=0
  for direction in directionVector:
    if(isFreeSpace(elf, direction, grid)):
      freeDirection=freeDirection+1
      if(candidateTile==elf):
        candidateTile=sumTupleValueByValue(elf, direction)
  if(freeDirection==4):
    return elf
  return candidateTile


def doRound(grid):
  gridOfMoves=dict()
  for elf in grid:
    candidatePosition=findCandidatePosition(elf, grid)
    if(candidatePosition!=elf):
      if(candidatePosition in gridOfMoves.keys()):
        gridOfMoves.pop(candidatePosition)
      else:
        gridOfMoves[candidatePosition]=elf

  for candidate, actual in gridOfMoves.items():
    moveElf(actual, candidate, grid)

  directionVector.append(directionVector.pop(0))

  return len(gridOfMoves)

def calculateSpacesZones(grid):
  maxX=max(element[0] for element in grid)
  minX=min(element[0] for element in grid)
  maxY=max(element[1] for element in grid)
  minY=min(element[1] for element in grid)
  x=maxX-minX+1
  y=maxY-minY+1

  return (x*y)-len(grid)

def solve1():
  rows= getOldAocInput(day)
  grid=comprehension(rows)
  for round in range(10):
    doRound(grid)

  return calculateSpacesZones(grid)

def solve2():
  rows= getOldAocInput(day)
  grid=comprehension(rows)
  round=0
  while(True):
    round=round+1
    moves=doRound(grid)
    if(moves==0):
      return round

print(solve1())
print(solve2())