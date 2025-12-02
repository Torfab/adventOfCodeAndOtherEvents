from utility import *

def parseRows(rows):
  grid, maxX, maxY=buildGrid(rows)
  return grid, maxX, maxY

def rotateGrid(grid):
  maxX, maxY=maxGrid(grid)
  position=next(k for k, v in grid.items() if k[1] == maxY)
  currentMax=maxX
  iteration=0
  newGrid={}
  startPosition=position
  currentMovement=(0,-1)
  for _ in range (maxX//2+1):
    for i in range(maxX-currentMax, currentMax+1):
      newGrid[(i, iteration)]=grid[position]
      position=sumTupleValueByValue(position, currentMovement)
      if currentMovement==(0,-1):
        currentMovement=(-1,0)    
      else:
        currentMovement=(0,-1)
    iteration=iteration+1
    startPosition=sumTupleValueByValue(startPosition, (1,-1))
    position=startPosition
    currentMovement=(0,-1)
    currentMax=currentMax-1
  return newGrid


def solve():
  rows=openFile("raw.txt")
  grid, _, _=parseRows(rows)
  count=0
  for k,v in grid.items():
    if v=="#":
      continue
    else:
      if grid.get(sumTupleValueByValue(k, (1,0)))=="T":
        count=count+1
      if (k[0]-k[1])%2==1 and grid.get(sumTupleValueByValue(k, (0,1)))=="T":
        count=count+1
  return count


directionsOdd=[(1,0), (-1,0), (0,1)]
directionsEven=[(1,0), (-1,0), (0,-1)]

def solve2():
  rows=openFile("raw.txt")
  grid, _, _=parseRows(rows)
  start = next(k for k, v in grid.items() if v == "S")
  end = next(k for k, v in grid.items() if v == "E")

  border=set()
  border.add(start)
  alreadySeen=set()
  newBorder=set()
  iteration=0
  while(border):
    iteration=iteration+1
    while(border):
      position=border.pop()
      isEven=(position[0]+position[1])%2==0
      alreadySeen.add(position)

      if isEven:
        theDirections=directionsEven
      else:
        theDirections=directionsOdd
      for d in theDirections:
        tentative=sumTupleValueByValue(position, d)
        if tentative in alreadySeen:
          continue
        if tentative==end:
          return iteration
        if grid.get(tentative)=="T":
          newBorder.add(tentative)
    border=newBorder
    newBorder=set()
  return None

directionsOddJump=[(1,0), (-1,0), (0,1), (0,0)]
directionsEvenJump=[(1,0), (-1,0), (0,-1), (0,0)]

def solve3():
  rows=openFile("raw.txt")
  grid, _, _=parseRows(rows)
  start = next(k for k, v in grid.items() if v == "S")
  end = next(k for k, v in grid.items() if v == "E")
  grids=[]
  grids.append(grid)
  grids.append(rotateGrid(grid))
  grids.append(rotateGrid(grids[1]))
  border=set()
  border.add(start)
  alreadySeen=set()
  newBorder=set()
  iteration=0
  jumpGrid=1

  while(border):
    iteration=iteration+1
    while(border):
      position=border.pop()
      isEven=(position[0]+position[1])%2==0
      alreadySeen.add((position[0], position[1], (jumpGrid-1)%3))
      if isEven:
        theDirections=directionsEvenJump
      else:
        theDirections=directionsOddJump
      for d in theDirections:
        tentative=sumTupleValueByValue(position, d)
        if tentative in alreadySeen:
          continue
        if tentative==end:
          return iteration
        if grids[jumpGrid].get(tentative)=="T":
          newBorder.add(tentative)
    jumpGrid=(jumpGrid+1)%3
    border=newBorder
    newBorder=set()
  return None

# print(solve())
print(solve3())
