from utilityz import *

directions=fromDistanceBuildSetOfDirections(1)
def findHikes(start, grid):

  border=[(start, 0)]
  found=set()
  ris=0
  while(len(border)!=0):
    currentPoint, currentValue=border.pop(0)
    for d in directions:
      tentative=sumTupleValueByValue(currentPoint, d)
      if(grid.get(tentative)==currentValue+1):
        if(grid[tentative]==9):
          ris=ris+1
          found.add(tentative)
          continue
        border.append((tentative, currentValue+1))
  return len(found), ris



def solve(part):
  rows=getOldAocInput(10)
  grid, _, _= buildGrid(rows)
  grid={k:int(v) for k,v in grid.items()}
  startPoints=[position for position, value in grid.items() if value==0]
  ris=0
  if(part=="a"):
    idx=0
  elif(part=="b"):
    idx=1
  for start in startPoints:
    ris=ris+findHikes(start, grid)[idx]
  
  return ris


print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# evaluateTime(timeElapse)