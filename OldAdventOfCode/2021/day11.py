from utility import *

distanceVector=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

def markElement(key, grid, size, arrayOfFlashed):
  if(key not in arrayOfFlashed):
    grid[key]=grid[key]+1
    if(grid[key]==10):
      grid[key]=0
      arrayOfFlashed.append(key)
      for distance in distanceVector:
        candidatePosition=sumTupleValueByValue(key, distance)
        if(0<=candidatePosition[0]<size and 0<=candidatePosition[1]<size):
          markElement(candidatePosition, grid, size, arrayOfFlashed)

def solve1():
  rows=getAocInput(11,2021)
  dictGrid=dict()
  size=len(rows)
  for idx,row in enumerate(rows):
    for jdx, column in enumerate(row):
      dictGrid[(idx,jdx)]=int(column)

  flashes=0
  for step in range(100):
    arrayOfFlashed=[]
    for key in dictGrid.keys():
      if (key not in arrayOfFlashed):
        markElement(key, dictGrid, size, arrayOfFlashed)
    flashes=flashes+len(arrayOfFlashed)
    arrayOfFlashed=[]
  return flashes

def solve2():
  rows=getAocInput(11,2021)
  dictGrid=dict()
  size=len(rows)
  for idx,row in enumerate(rows):
    for jdx, column in enumerate(row):
      dictGrid[(idx,jdx)]=int(column)

  steps=0
  while(True):
    steps=steps+1
    arrayOfFlashed=[]
    for key in dictGrid.keys():
      if (key not in arrayOfFlashed):
        markElement(key, dictGrid, size, arrayOfFlashed)
    if(len(arrayOfFlashed)==len(dictGrid)):
      return steps
    arrayOfFlashed=[]


print(solve1())
print(solve2())