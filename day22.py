from utilities import *


day=22

directionVector=[(1,0), (0,1), (-1,0), (0,-1)]
orientationVector=['>', 'v', '<', 'ʌ']

def rotate(rotation):
  if(rotation=="L"):
    directionVector.insert(0,directionVector.pop())
    orientationVector.insert(0,orientationVector.pop())
  if(rotation=="R"):
    directionVector.append(directionVector.pop(0))
    orientationVector.append(orientationVector.pop(0))

def comprehension(rows):
  grid=dict()
  for idxRow, row in enumerate(rows):
    if(row==""):
      break
    for idxElement, element in enumerate(row):
      if(element!=" "):
        grid[(idxElement+1, idxRow+1)]=element

  arrayOfCommands=rows[idxRow+1].replace("L", " L ").replace("R", " R ").split(" ")
  return grid, arrayOfCommands

def findWarp(direction, tile, grid):
  if(direction==(1,0)):
    return (min(element[0] for element in grid if element[1]==tile[1]),tile[1])
  if(direction==(-1,0)):
    return (max(element[0] for element in grid if element[1]==tile[1]),tile[1])
  if(direction==(0,1)):
    return (tile[0], min(element[1] for element in grid if element[0]==tile[0]))
  if(direction==(0,-1)):
    return (tile[0], max(element[1] for element in grid if element[0]==tile[0]))

def stamp(tile, grid):
  grid[tile]=orientationVector[0]

def goForward(currentPosition, steps, grid):
  for element in range(steps):
    candidatePosition=sumTupleValueByValue(currentPosition, directionVector[0])
    if(grid.get(candidatePosition)==None):
      candidatePosition=findWarp(directionVector[0], candidatePosition, grid)
    if(grid[candidatePosition]=="#"):
      return currentPosition
    currentPosition=candidatePosition
    stamp(currentPosition, grid)
  return currentPosition

def realPrint(grid: dict):
  maxX=max(element[0] for element in grid)
  maxY=max(element[1] for element in grid)
  for i in range(1,maxY+1):
    for j in range(1, maxX+1):
      element=grid.get((j,i))
      if(element==None):
        print(" ", end="")
      else:
        print(element, end="")
    print()
  print()

def calculateResult(tile, orientation):
  if(orientation==">"):
    orientationValue=0
  if(orientation=="v"):
    orientationValue=1
  if(orientation=="<"):
    orientationValue=2
  if(orientation=="ʌ"):
    orientationValue=3
  return (tile[1]*1000+tile[0]*4+orientationValue)

def solve():
  rows=getAocInput(day)
  grid, arrayOfCommands=comprehension(rows)
  currentPosition=(min(element[0] for element in grid if element[1]==1), 1)
  stamp(currentPosition, grid)
  for command in arrayOfCommands:
    if (command=="L" or command=="R"):
      rotate(command)
      stamp(currentPosition, grid)
    else:
      currentPosition=goForward(currentPosition, int(command), grid)
  return calculateResult(currentPosition, orientationVector[0])


print(solve())
