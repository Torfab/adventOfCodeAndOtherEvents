from utility import *

def parseRows(rows):
  grid={}
  for y in range(len(rows)): 
    for x in range(len(rows[y])):
      if(rows[y][x]!="."):
        grid[(x,y)]=rows[y][x]

  return grid, maxGrid(grid)[0], maxGrid(grid)[1]

def moveCucumber(symbol, axis, direction, grid, limit):
  moved=0
  newGrid={}
  for k,v in grid.items():
    if v==symbol:
      tentativePosition=sumTupleValueByValue(k, direction)
      if (tentativePosition[axis]>limit):
        tentativePosition=list(tentativePosition)
        tentativePosition[axis]=0
        tentativePosition=tuple(tentativePosition)
      if (grid.get(tentativePosition)==None):
        newGrid[tentativePosition]=v
        moved=moved+1
      else:
        newGrid[k]=v
    else:
      newGrid[k]=v
  return moved, newGrid


def solve():
  rows=getOldAocInput(25)
  grid, maxX, maxY=parseRows(rows)
  moved=1
  idx=0
  while(moved!=0):
    idx=idx+1
    moved=0
    newMoved, grid=moveCucumber(">", 0,  (1,0), grid, maxX)
    moved=moved+newMoved
    newMoved, grid=moveCucumber("v", 1, (0,1), grid, maxY)
    moved=moved+newMoved
  return idx  

print(solve())