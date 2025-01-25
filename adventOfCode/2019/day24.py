from utility import *

directions=fromDistanceBuildListOfDirections(1)
recursiveDirections=[(d[0], d[1], 0) for d in directions]

def checkInfested(grid, point):
  howMany=0
  for d in directions:
    if sumTupleValueByValue(point, d) in grid:
      howMany=howMany+1
  if(point in grid):
    if(howMany==1):
      return True
    else:
      return False
  else:
    if(howMany==2 or howMany==1):
      return True
    else:
      return False
    
def checkRecursiveInfested(grid, point):
  pointsToCheck=set([sumTriplettesValueByValue(point, d) for d in recursiveDirections])
  pointsToCheck.discard((2,2,point[2]))

  if point[0]==0:
    pointsToCheck.add((1,2, point[2]+1))
  if point[0]==4:
    pointsToCheck.add((3,2, point[2]+1))
  if point[1]==0:
    pointsToCheck.add((2,1, point[2]+1))
  if point[1]==4:
    pointsToCheck.add((2,3, point[2]+1))
  if point[0]==1 and point[1]==2:
    for i in range(5):
      pointsToCheck.add((0,i, point[2]-1))
  if point[0]==3 and point[1]==2:
    for i in range(5):
      pointsToCheck.add((4,i, point[2]-1))
  if point[0]==2 and point[1]==1:
    for i in range(5):
      pointsToCheck.add((i,0, point[2]-1))
  if point[0]==2 and point[1]==3:
    for i in range(5):
      pointsToCheck.add((i,4, point[2]-1))
  howMany=0
  for p in pointsToCheck:
    if p in grid:
      howMany=howMany+1
  if(point in grid):
    if(howMany==1):
      return True
    else:
      return False
  else:
    if(howMany==2 or howMany==1):
      return True
    else:
      return False

def calculateScore(grid):
  power=0
  score=0
  for y in range(5):
    for x in range(5):
      if (x,y) in grid:
        score =score+2**power
      power=power+1
  return score

def solve(part):
  rows=getOldAocInput(24)
  grid, _, _=buildGrid(rows)
  if part=="a":
    historyOfGrid=set()
    oldGrid={}
    while(tuple(grid.keys()) not in historyOfGrid):
      historyOfGrid.add(tuple(grid.keys()))
      oldGrid=grid
      grid={}
      for y in range(5):
        for x in range(5):
          if(checkInfested(oldGrid, (x,y))):
            grid[(x,y)]="#"
      
    return calculateScore(grid)
  if part=="b":
    grid={(k[0], k[1], 0):v for k,v in grid.items()}
    for i in range(200):
      minZ=min(k[2] for k in grid.keys())
      maxZ=max(k[2] for k in grid.keys())
      oldGrid=grid
      grid={}
      for y in range(5):
        for x in range(5):
          if(x==2 and y==2):
            continue
          for z in range(minZ-1, maxZ+2):
            if(checkRecursiveInfested(oldGrid, (x,y,z))):
              grid[(x,y,z)]="#"
    return len(grid)

print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
