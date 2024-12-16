from utility import *

directions={"<": (-1,0), "^": (0,-1), ">":(1,0), "v":(0,1)}

def parseRows(rows):
  for i, row in enumerate(rows):
    if row=="":
      break
  grid, _, _ =buildGrid(rows[:i+1])
  sequence=""
  for row in rows[i+1:]:
    sequence=sequence+row
  return grid, sequence

def updateGrid(currentPoint, d, walls, grid):
  tentative=sumTupleValueByValue(currentPoint, directions[d])
  firstTentative=tentative
  if(tentative in walls):
    return currentPoint
  while(tentative not in walls):
    if(grid.get(tentative)!=None):
      tentative=sumTupleValueByValue(tentative, directions[d])
    else:
      grid[tentative]="O"
      grid.pop(firstTentative)
      return firstTentative
  return currentPoint



def solve():
  rows=getOldAocInput(15)
  grid, sequence=parseRows(rows)
  walls=set([k for k,v in grid.items() if v=="#"])
  currentPoint=[k for k,v in grid.items() if v=="@"][0]
  grid.pop(currentPoint)

  for d in sequence:
    currentPoint=updateGrid(currentPoint, d, walls, grid)

  boxes=[k for k,v in grid.items() if v=="O"]
  ris=0
  for k in boxes:
    ris=ris+100*k[1]
    ris=ris+k[0]
  return ris

def wideningGrid(grid):
  newGrid={}
  for k,v in grid.items():
    if(v=="#"):
      newGrid[k[0]*2, k[1]]="#"
      newGrid[k[0]*2+1, k[1]]="#"
    elif(v=="O"):
      newGrid[k[0]*2,k[1]]="["
      newGrid[k[0]*2+1, k[1]]="]"
    elif(v=="@"):
      newGrid[k[0]*2, k[1]]="@"
  return newGrid

def updateGridWidened(currentPoint, d, walls, grid):
  tentative=sumTupleValueByValue(currentPoint, directions[d])
  firstTentative=tentative
  if(tentative in walls):
    return currentPoint
  if(grid.get(tentative)==None):
    return tentative
  # border=[tentative]
  # while(not thingInCommonArray(border, walls)):

  # else:
  elementsToMove=[]
  if(d=="<" or d==">"):
    while(tentative not in walls):
      if(grid.get(tentative)!=None):
        elementsToMove.append(tentative)
        tentative=sumTupleValueByValue(tentative, directions[d])
      else:
        elementsToMove.append(tentative)
        for idxPosition in reversed(range(1, len(elementsToMove))):
          grid[elementsToMove[idxPosition]]=grid[elementsToMove[idxPosition-1]]
        grid.pop(firstTentative)
        return firstTentative
    return currentPoint
  if(d=="^" or d=="v"):
    tentativeSet=set()
    tentativeSet.add(tentative)
    if(grid[tentative]=="["):
      tentativeSet.add(sumTupleValueByValue(tentative, (1,0)))
    elif(grid[tentative]=="]"):
      tentativeSet.add(sumTupleValueByValue(tentative, (-1,0)))

    while(not thingInCommonArray(tentativeSet, walls)):
      newTentativeSet=set()
      everythingClear=True
      elementsToMove.append(tentativeSet)
      for t in tentativeSet:
        checkPosition=sumTupleValueByValue(t, directions[d])
        if(checkPosition in walls):
          return currentPoint
        if grid.get(checkPosition)!=None:
          newTentativeSet.add(checkPosition), 
          if(grid[checkPosition]=="["):  
            newTentativeSet.add(sumTupleValueByValue(checkPosition, (1,0)))
          elif(grid[checkPosition]=="]"):
            newTentativeSet.add(sumTupleValueByValue(checkPosition, (-1,0)))
          everythingClear=False

      if everythingClear:
        for layer in reversed(elementsToMove):
          for point in layer:
            grid[sumTupleValueByValue(point, directions[d])]=grid[point]
            grid.pop(point)

        return firstTentative
      else:
        tentativeSet=newTentativeSet

    return currentPoint
  
def stampaGridPoint(grid, point):
  grid[point]="@"
  stampaGrid(grid)
  grid.pop(point)

def solveB():
  rows=getOldAocInput(15)
  grid, sequence=parseRows(rows)
  grid=wideningGrid(grid)
  walls=set([k for k,v in grid.items() if v=="#"])
  currentPoint=[k for k,v in grid.items() if v=="@"][0]
  grid.pop(currentPoint)

  for d in sequence:
    currentPoint=updateGridWidened(currentPoint, d, walls, grid)

  boxes=[k for k,v in grid.items() if v=="["]
  ris=0
  for k in boxes:
    ris=ris+100*k[1]
    ris=ris+k[0]
  return ris

print(solveB())
# print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))

