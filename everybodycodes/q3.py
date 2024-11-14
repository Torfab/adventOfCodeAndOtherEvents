from utilityz import *

directions=fromDistanceBuildSetOfDirections(1)
radialDirections=fromDistanceBuildSetOfRadialDirections(1)

banana={}

def isPond(coords, grid):
  for direction in radialDirections:
    if(grid.get(sumTupleValueByValue(coords,direction))==None):
      return True
  return False

def isBorder(coords, grid):
  for direction in directions:
    if(grid.get(sumTupleValueByValue(coords,direction))==None):
      return True
  return False

def solve(borderFunction):
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGridWithDots(rows)
  for key in grid:
    grid[key]=1
  counter=len(grid)
  currentLayer=1
  while(len(grid)>0):
    newGrid={}
    for element in grid:
      if(not borderFunction(element, grid)):
        newGrid[element]=currentLayer+1
    
    grid=newGrid
    counter=counter+len(newGrid)
    currentLayer=currentLayer+1
    print()
  return counter

# print(solve(isBorder))
print(solve(isPond))

