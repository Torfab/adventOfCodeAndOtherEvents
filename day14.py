from utilities import *

distanceVector=[(1,0), (-1,0), (0,1), (0,-1)]

def mark(grid, a,b):
  coordinatesA=a.split(",")
  coordinatesB=b.split(",")
  coordinatesA=(int(coordinatesA[0]), int(coordinatesA[1]))
  coordinatesB=(int(coordinatesB[0]), int(coordinatesB[1]))

  if(coordinatesA[0]==coordinatesB[0]):
    distance=abs(coordinatesB[1]-coordinatesA[1])
    distanceIdx=2
    if(coordinatesB[1]<coordinatesA[1]):
      startingPoint=coordinatesB
    else:
      startingPoint=coordinatesA
  if(coordinatesA[1]==coordinatesB[1]):
    distance=abs(coordinatesB[0]-coordinatesA[0])
    distanceIdx=0
    if(coordinatesB[0]<coordinatesA[0]):
      startingPoint=coordinatesB
    else:
      startingPoint=coordinatesA

  for element in range(distance+1):
    grid[startingPoint]="#"
    startingPoint=sumTupleValueByValue(startingPoint,distanceVector[distanceIdx])
  return

def putSandInGrid(startPoint, grid: dict, maxY, part):
  if(part=='b'):
    if(startPoint in grid.keys()):
      return False
  while(startPoint[1]<(maxY+1)):
    candidatePoint=sumTupleValueByValue(startPoint,distanceVector[2])
    if(candidatePoint not in grid.keys()):
      startPoint=candidatePoint
      continue
    candidatePoint=sumTupleValueByValue(startPoint,distanceVector[2])
    candidatePoint=sumTupleValueByValue(candidatePoint,distanceVector[1])
    if(candidatePoint not in grid.keys()):
      startPoint=candidatePoint
      continue
    candidatePoint=sumTupleValueByValue(startPoint,distanceVector[2])
    candidatePoint=sumTupleValueByValue(candidatePoint,distanceVector[0])
    if(candidatePoint not in grid.keys()):
      startPoint=candidatePoint
      continue
    grid[startPoint]='o'
    return True
  if(part=='a'):
    return False
  if(part=='b'):
    grid[startPoint]='o'
    return True

def printGrid(grid: dict , maxX, maxY):

  for row in range(maxY+2):
    for column in range(480,maxX+50):
      if(grid.get((column, row))!=None):
        print(grid[(column, row)], end='')
      else:
        print('.', end='')
    print()

def solve(part):
  gridDict=dict()

  rows=getAocInput(14)
  for element in rows:
    coordinates=element.split(" ->")
    for idx in range(len(coordinates)-1):
      mark(gridDict, coordinates[idx], coordinates[idx+1])

  maxY=max([a[1] for a in gridDict.keys()])
  maxX=max([a[0] for a in gridDict.keys()])

  step=0
  sandStartPoint=(500,0)
  
  while (True):
    
    if(not putSandInGrid(sandStartPoint, gridDict, maxY, part)):
      return step
    step=step+1
    # printGrid(gridDict, maxX, maxY)

print(solve('a'))
print(solve('b'))
