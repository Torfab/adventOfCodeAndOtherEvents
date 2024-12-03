from utility import *

directions=fromDistanceBuildSetOfRadialDirections(1)

def iterateGrid(grid, howManySeats, keepContinue):
  newGrid={}
  for key, value in grid.items():
    count=0
    for d in directions:
      check=sumTupleValueByValue(key, d)
      element=grid.get(check)
      if not keepContinue:
        if element=="#":
          count=count+1
      else:
        while(element!=None):
          if element=="#":
            count=count+1
            break
          elif element=="L":
            break
          check=sumTupleValueByValue(check, d)
          element=grid.get(check)
    
    if(value=="L" and count==0):
      newGrid[key]="#"
    elif(value=="#" and count>=howManySeats):
      newGrid[key]="L"
    else:
      newGrid[key]=value
  return newGrid
    

def solve(part):
  rows=getOldAocInput(11)
  newGrid, _, _=buildGrid(rows, "k")
  if part=="a":
    howManySeats=4
    keepContinue=False
  if part=="b":
    howManySeats=5
    keepContinue=True

  oldGrid={}
  while(oldGrid!=newGrid):
    oldGrid, newGrid=newGrid, iterateGrid(newGrid, howManySeats, keepContinue)
    

  return len([k for k,v in newGrid.items() if v=="#"])


print(solve("a"))
print(solve("b"))
