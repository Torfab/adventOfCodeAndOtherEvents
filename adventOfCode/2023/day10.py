from utility import *

def parseRows(rows):
  grid={}
  
  for y in range(len(rows)):
    for x in range(len(rows[y])):
      if(rows[y][x]=="S"):
        coordS=(x,y)
      grid[(x,y)]=rows[y][x]
  return grid, coordS

directions={"D":(0,1), "U":(0,-1), "R":(1,0), "L":(-1,0)}
norths=["|", "F", "7"]


def toMark(border: list, potentialMarked, grid):
  wrong=False
  checkLeft=border[0]
  count=0
  while(checkLeft[0]>=0):
    checkLeft=sumTupleValueByValue(checkLeft, directions["L"])
    if(grid.get(checkLeft) in norths):
      count=count+1
  if(count%2==0):
    wrong=True
  while(len(border)>0):
    theTuple=border.pop()
    for element in directions.values():
      newCoords=sumTupleValueByValue(theTuple, element)
      if(newCoords not in grid):
        wrong=True
        continue
      if(grid[newCoords]!="." or newCoords in potentialMarked):
        continue
      else:
        potentialMarked.append(newCoords)
        border.append(newCoords)
  return wrong

def printGrid(grid):
  maxX=max(grid.keys(), key=lambda x: x[0])[0]+1
  maxY=max(grid.keys(), key=lambda x: x[1])[1]+1

  for y in range(maxY):
    for x in range(maxX):
      print(grid[(x,y)], end="")
    print()

def solve(part):
  rows=getOldAocInput(10)
  grid, startPoint=parseRows(rows)

  #hardCoded first direction from being S spot
  lastMovement="R"
  currentPoint=sumTupleValueByValue(startPoint, directions["R"])
  currentPointSymbol=grid[currentPoint]
  elementInLoop=[currentPoint]

  while(currentPointSymbol!="S"):
    if(currentPointSymbol=="-"):
      if(lastMovement=="R"):
        lastMovement="R"
        currentPoint=sumTupleValueByValue(currentPoint, directions["R"])
      elif(lastMovement=="L"):
        lastMovement="L"
        currentPoint=sumTupleValueByValue(currentPoint, directions["L"])
    elif(currentPointSymbol=="|"):
      if(lastMovement=="U"):
        lastMovement="U"
        currentPoint=sumTupleValueByValue(currentPoint, directions["U"])
      elif(lastMovement=="D"):
        lastMovement="D"
        currentPoint=sumTupleValueByValue(currentPoint, directions["D"])    
    elif(currentPointSymbol=="L"):
      if(lastMovement=="D"):
        lastMovement="R"
        currentPoint=sumTupleValueByValue(currentPoint, directions["R"])
      elif(lastMovement=="L"):
        lastMovement="U"
        currentPoint=sumTupleValueByValue(currentPoint, directions["U"])
    elif(currentPointSymbol=="J"):
      if(lastMovement=="R"):
        lastMovement="U"
        currentPoint=sumTupleValueByValue(currentPoint, directions["U"])
      elif(lastMovement=="D"):
        lastMovement="L"
        currentPoint=sumTupleValueByValue(currentPoint, directions["L"])
    elif(currentPointSymbol=="7"):
      if(lastMovement=="R"):
        lastMovement="D"
        currentPoint=sumTupleValueByValue(currentPoint, directions["D"])
      elif(lastMovement=="U"):
        lastMovement="L"
        currentPoint=sumTupleValueByValue(currentPoint, directions["L"])
    elif(currentPointSymbol=="F"):
      if(lastMovement=="L"):
        lastMovement="D"
        currentPoint=sumTupleValueByValue(currentPoint, directions["D"])
      elif(lastMovement=="U"):
        lastMovement="R"
        currentPoint=sumTupleValueByValue(currentPoint, directions["R"])
    currentPointSymbol=grid[currentPoint]
    elementInLoop.append(currentPoint)
  if(part=="a"):
    return len(elementInLoop)//2
  
  newGrid={}
  for element in grid.keys():
    if (element in elementInLoop):
      newGrid[element]=grid[element]
    else:
      newGrid[element]="."
  grid=newGrid
  maxX=max(grid.keys(), key=lambda x: x[0])[0]+1
  maxY=max(grid.keys(), key=lambda x: x[1])[1]+1

  marked=[]
  notMarked=[]
  for y in range(maxY):
    for x in range(maxX):
      if(grid[(x,y)]=="."):
        if((x,y) in marked or (x,y) in notMarked):
          continue
        potentialMarked=[(x,y)]
        wrong=toMark([(x,y)], potentialMarked, grid)
        if(wrong):
          notMarked.extend(potentialMarked)
        else:
          marked.extend(potentialMarked)
  return len(marked)


print(solve("a"))
print(solve("b"))