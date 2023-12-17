from utility import *

directions={"U":(0,-1), "D":(0,1), "R":(1,0), "L":(-1,0)}

def parseRows(rows):
  grid={}
  for y in range(len(rows)):
    for x in range(len(rows[y])):
      if(rows[y][x]!="."):
        grid[(x,y)]=rows[y][x]
  return grid

def stampaGrid(grid):
  maxX=max(grid.keys(), key=lambda x: x[0])[0]+1
  maxY=max(grid.keys(), key=lambda x: x[1])[1]+1
  for y in range(maxY):
    for x in range(maxX):
      if(grid.get((x,y))==None):
        print('.', end="")
      else:
        print(grid[(x,y)], end="")
    print()

def checkValidPosition(tentativePosition):
  if(tentativePosition[0]<0 or tentativePosition[0]>=maxX):
    return False
  if(tentativePosition[1]<0 or tentativePosition[1]>=maxY):
    return False
  return True

def tryPutBeam(beams, tentativePosition, lastMovement):
  if(beams.get(tentativePosition)==None):
    beams[tentativePosition]={"U":False, "R":False, "L":False, "D": False}
    beams[tentativePosition][lastMovement]=True
  else:
    if(beams[tentativePosition][lastMovement]):
      return False
    else:
      beams[tentativePosition][lastMovement]=True
  return True

def checkAndPutNewPosition(tentativePosition, border, movement):
  if(checkValidPosition(tentativePosition)):
    border.append({"pos": tentativePosition, "lastDirection":movement})

def countValue(border, grid):
  
  beams={}
  while(len(border)>0):
    elementBorder=border.pop(0)
    currentPosition=elementBorder["pos"]
    lastMovement=elementBorder["lastDirection"]
    if(not tryPutBeam(beams, currentPosition, lastMovement)):
      continue
    if(grid.get(currentPosition)==None):
      checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions[lastMovement]), border, lastMovement)
      continue
    if(grid[currentPosition]=="|"):
      if(lastMovement=="U" or lastMovement=="D"):
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions[lastMovement]), border, lastMovement)
      else:
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["U"]), border, "U")
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["D"]), border, "D")
    if(grid[currentPosition]=="-"):
      if(lastMovement=="R" or lastMovement=="L"):
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions[lastMovement]), border, lastMovement)
      else:
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["L"]), border, "L")
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["R"]), border, "R")
    if(grid[currentPosition]=="/"):
      if(lastMovement=="U"):
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["R"]), border, "R")
      elif(lastMovement=="R"):
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["U"]), border, "U")
      elif(lastMovement=="D"):
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["L"]), border, "L")      
      elif(lastMovement=="L"):
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["D"]), border, "D")  
    if(grid[currentPosition]=="\\"):
      if(lastMovement=="U"):
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["L"]), border, "L")
      elif(lastMovement=="R"):
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["D"]), border, "D")
      elif(lastMovement=="D"):
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["R"]), border, "R")      
      elif(lastMovement=="L"):
        checkAndPutNewPosition(sumTupleValueByValue(currentPosition, directions["U"]), border, "U")
  return len(beams)

def solve(part):
  rows=getOldAocInput(16)
  grid=parseRows(rows)
  global maxX
  maxX=max(grid.keys(), key=lambda x: x[0])[0]+1
  global maxY
  maxY=max(grid.keys(), key=lambda x: x[1])[1]+1
  if(part=="a"):
    border=[{"pos":(0,0), "lastDirection":"R"}]
    return (countValue(border,grid))
  results= []

  for x in range(maxX):
    border=[{"pos": (x, 0), "lastDirection":"D"}]
    results.append(countValue(border,grid))
    border=[{"pos": (x, maxY-1), "lastDirection":"U"}]
    results.append(countValue(border,grid))
  for y in range(maxY):
    border=[{"pos": (0, y), "lastDirection":"R"}]
    results.append(countValue(border,grid))
    border=[{"pos": (maxY-1, y), "lastDirection":"L"}]
    results.append(countValue(border,grid))   
  return max(results)

print(solve("a"))
print(solve("b"))