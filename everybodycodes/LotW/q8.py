from utility import *

def calculateSaved(sunDirection, borderToCheck, grid):
  
  saved=set()
  for element in borderToCheck:
    current=element
    currentShadow=grid[current]
    if(grid[current]>0):
      saved.add(current)
    else:
      grid[current]=grid[current]+1
    while(True):
      currentShadow=currentShadow-1
      tentative=sumTupleValueByValue(sunDirection, current)
      if(grid.get(tentative)==None):
        break
      current=tentative
      if(grid[current]<1):
        grid[current]=grid[current]+1
      else:
        if(grid[current]>currentShadow):
          currentShadow=grid[current]
          saved.add(current)
  return saved

def buildTurns(grid, maxX, maxY):

  turns=[]
  sunDirection=(1,1)
  borderToCheck=[x for x in grid.keys() if x[1]==0]
  current=borderToCheck[0]
  while(True):
    tentative=sumTupleValueByValue(current, (-1,1))
    if(grid.get(tentative)!=None):
      current=tentative
      borderToCheck.append(current)
    else:
      break

  turns.append((sunDirection, borderToCheck))

  sunDirection=(-1,1)
  borderToCheck=[x for x in grid.keys() if x[1]==0]
  current=borderToCheck[-1]
  while(True):
    tentative=sumTupleValueByValue(current, (1,1))
    if(grid.get(tentative)!=None):
      current=tentative
      borderToCheck.append(current)
    else:
      break

  turns.append((sunDirection, borderToCheck))

  sunDirection=(-2,0)
  borderToCheck=[x for x in grid.keys() if x[0]==maxX]
  current=borderToCheck[0]
  while(True):
    tentative=sumTupleValueByValue(current, (-1,-1))
    if(grid.get(tentative)!=None):
      current=tentative
      borderToCheck.append(current)
    else:
      break
  current=borderToCheck[0]
  while(True):
    tentative=sumTupleValueByValue(current, (-1,1))
    if(grid.get(tentative)!=None):
      current=tentative
      borderToCheck.append(current)
    else:
      break

  turns.append((sunDirection, borderToCheck))

  sunDirection=(-1,-1)
  borderToCheck=[x for x in grid.keys() if x[1]==maxY]
  current=borderToCheck[-1]
  while(True):
    tentative=sumTupleValueByValue(current, (1,-1))
    if(grid.get(tentative)!=None):
      current=tentative
      borderToCheck.append(current)
    else:
      break

  turns.append((sunDirection, borderToCheck))

  sunDirection=(1,-1)
  borderToCheck=[x for x in grid.keys() if x[1]==maxY]
  current=borderToCheck[0]
  while(True):
    tentative=sumTupleValueByValue(current, (-1,-1))
    if(grid.get(tentative)!=None):
      current=tentative
      borderToCheck.append(current)
    else:
      break

  turns.append((sunDirection, borderToCheck))

  sunDirection=(2,0)
  borderToCheck=[x for x in grid.keys() if x[0]==0]
  current=borderToCheck[0]
  while(True):
    tentative=sumTupleValueByValue(current, (1,-1))
    if(grid.get(tentative)!=None):
      current=tentative
      borderToCheck.append(current)
    else:
      break
  current=borderToCheck[0]
  while(True):
    tentative=sumTupleValueByValue(current, (1,1))
    if(grid.get(tentative)!=None):
      current=tentative
      borderToCheck.append(current)
    else:
      break

  turns.append((sunDirection, borderToCheck))
  
  return turns

  
def solve(part):

  rows=openFile("raw.txt")
  grid,maxX,maxY=buildGrid(rows)
  grid={x:int(y) for x,y in grid.items()}
  turns=buildTurns(grid, maxX, maxY)
  if part==1:
    return len(calculateSaved(turns[0][0], turns[0][1], grid))
  
  lenTurns=len(turns)
  result=0
  if part==2:
    for i in range(lenTurns):
      result=result+len(calculateSaved(turns[i][0], turns[i][1], grid))
    return result
  
  turnsIdx=0
  warriors=0
  result=0
  step=0
  while(warriors<100000):
    step=step+1
    saved=calculateSaved(turns[turnsIdx][0],turns[turnsIdx][1],grid)
    for element in saved:
      grid[element]=grid[element]+1
      if(grid[element]==10):
        grid[element]=-2
        warriors=warriors+1
    result=result+len(saved)
    turnsIdx=(turnsIdx+1)%lenTurns
  #print(step)
  return result

# print(solve(1))
# print(solve(2))
print(solve(3))
