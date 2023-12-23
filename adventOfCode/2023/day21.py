from utility import *

maxX=0
maxY=0

distances=fromDistanceBuildSetOfDirections(1)
def parseRows(rows):
  global maxX
  global maxY
  maxY=len(rows)-1
  maxX=len(rows)-1
  grid={}
  for y in range(len(rows)):
    for x in range(len(rows[y])):
      if(rows[y][x]=="."):
        grid[(x,y)]=True
      if(rows[y][x]=="S"):
        grid[(x,y)]=True
        startPoint=(x,y)

  return grid, startPoint

def stampaGrid(grid, startPoint):
  for y in range(maxY+1):
    for x in range(maxX+1):
      if ((x,y)==startPoint):
        print("S", end="")
        continue
      if(grid.get((x,y))!=None):
        print(".", end="")
        continue
      print("#", end="")
    print()

def solveA():
  rows=getOldAocInput(21)
  grid, startPoint=parseRows(rows)
  border=set()
  border.add(startPoint)
  # border.add(startPoint)
  result = countCerchi(64, grid, border)
  return result
  

def wizardry(x, centralOffset, gridLength, isStart):
  singleDirectionBranch=((x-centralOffset)//gridLength)+1

  restosingleDirectionBranch=x-(singleDirectionBranch*gridLength)+centralOffset-1

  offset=0
  if(isStart and restosingleDirectionBranch>centralOffset-1):
    offset = 4
    singleDirectionBranch = singleDirectionBranch+1
  singleDirectionBranch=singleDirectionBranch+1

  quadratoEsterno=((2*singleDirectionBranch)-1)**2 

  return singleDirectionBranch-offset//4, (quadratoEsterno- 2 * singleDirectionBranch*(singleDirectionBranch-1) -offset)
  
def inizioUltimoCardinals(n):
  return 66+131*(n-2)

def countCerchi(steps, grid, border):
  for _ in range(steps):
    newBorder=set()
    for element in border:
      for direction in distances:
        tentativePosition=sumTupleValueByValue(element, direction)
        if(grid.get(tentativePosition)!=None):
          newBorder.add(tentativePosition)
    border=newBorder
  return len(border)

def solveB(x):
  distanceDegliStart, theGridStarted=wizardry(x, 66, 131, True)

  if(distanceDegliStart%2==0):
    completedWithCenter=(distanceDegliStart-2)*(distanceDegliStart-2)
    completedNOCenter=(distanceDegliStart-3)*(distanceDegliStart-3)
  else:
    completedWithCenter=(distanceDegliStart-3)*(distanceDegliStart-3)
    completedNOCenter=(distanceDegliStart-2)*(distanceDegliStart-2)
  
  #7201 7218
  result=completedWithCenter*7218
  result=result+completedNOCenter*7201

  #26501365   #26501235

  inizioultimo=inizioUltimoCardinals(distanceDegliStart)

  
  #13 + 36 +8

  estremoEsternoStepsToDo=x-inizioultimo

  estremoInternoStepsToDo=estremoEsternoStepsToDo+131
  banana=0

  if(inizioultimo+66<=x):
    cornerEsternoStepsToDo=estremoEsternoStepsToDo-66

    howMuchCornerEsterno=distanceDegliStart-1
    banana=howMuchCornerEsterno-2
  else:
    cornerEsternoStepsToDo=estremoEsternoStepsToDo+65
    howMuchCornerEsterno=distanceDegliStart-2
  cornerInternoStepsToDo=cornerEsternoStepsToDo+131

  howMuchCornerInterno=howMuchCornerEsterno-1
  
  rows=getOldAocInput(21)
  grid, _=parseRows(rows)

  casiCardinali=[(0,65),(maxX,65), (65, 0), (65, maxY)]
  for element in casiCardinali:
    border=set()
    border.add(element)
    result=result+countCerchi(estremoEsternoStepsToDo, grid, border)
    border=set()
    border.add(element)
    result=result+countCerchi(estremoInternoStepsToDo, grid, border)

  casiCorner=[(0,0), (0, maxY), (maxX,maxY), (maxX,0)]
  for element in casiCorner:
    border=set()
    border.add(element)
    result=result+howMuchCornerEsterno*countCerchi(cornerEsternoStepsToDo, grid, border)
    border=set()
    border.add(element)
    result=result+howMuchCornerInterno*countCerchi(cornerInternoStepsToDo, grid, border)
    if(banana>0):
      result=result+banana*countCerchi(cornerInternoStepsToDo+131, grid, border)
  return result

print(solveA())
print(solveB(26501365))


