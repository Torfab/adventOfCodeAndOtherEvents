from utility import *

distances=fromDistanceBuildSetOfRadialDirections(1)

def parseRows(rows):
  return rows

def solve(part):
  rows=getOldAocInput(4)
  rows=parseRows(rows)
  grid, _, _=buildGrid(rows)

  result=0
  newGrid=grid
  grid={}
  while(grid!=newGrid):
    grid=newGrid
    newGrid={}
    for k in grid.keys():
      count=0
      for d in distances:
        if grid.get(sumTupleValueByValue(k, d)):
          count=count+1
      if count<4:
        result=result+1
      else:
        newGrid[k]=grid[k]
    if(part=="a"):
      return result
  return result


print(solve("a"))
print(solve("b"))