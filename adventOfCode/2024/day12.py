from utility import *

directions=fromDistanceBuildSetOfDirections(1)

def solve():
  rows=getOldAocInput(12)
  grid,_,_=buildGrid(rows)
  visited=set()
  ris=0
  for point, value in grid.items():
    if point in visited:
      continue
    area=0
    fences=0
    border=[point]
    while(len(border)>0):
      currentPoint=border.pop()
      if currentPoint in visited:
        continue
      visited.add(currentPoint)
      area=area+1
      for d in directions:
        tentative=sumTupleValueByValue(currentPoint, d)
        if grid.get(tentative)!=value:
          fences=fences+1
        else:
          border.append(tentative)
    ris=ris+area*fences

  return ris
def sidesOrizontal(subArea, grid, value):
  minX, minY=minGrid(subArea)
  maxX, maxY=maxGrid(subArea)
  sides=0
  for j in range(minY, maxY+1):
    modeRight=True
    found=False
    for i in range(minX, maxX+1):
      if(modeRight==True):
        if(grid[(i,j)]==value and (i,j) in subArea):
          if(grid.get((i, j-1))!=value):
            if not found:
              found=True
              sides=sides+1
          else:
            found=False
        else:
          modeRight=False
          found=False
      
      if(modeRight==False):
        if(grid[(i,j)]!=value):
          if (grid.get((i,j-1))==value and (i,j-1) in subArea):
            if not found:
              found=True
              sides=sides+1
          else:
            found=False
        else:
          modeRight=True
          if (grid.get((i,j-1))!=value and (i,j) in subArea):
            found=True
            sides=sides+1
          else:
            found=False
  found=False
  for i in range(minX, maxX+1):
    if (grid.get((i,maxY))==value and (i, maxY) in subArea):
      if not found:
        found=True
        sides=sides+1
    else:
      found=False
  return sides

def sidesVertical(subArea, grid, value):
  minX, minY=minGrid(subArea)
  maxX, maxY=maxGrid(subArea)
  sides=0
  for i in range(minX, maxX+1):
    modeRight=True
    found=False
    for j in range(minY, maxY+1):
      if(modeRight==True):
        if(grid[(i,j)]==value and (i,j) in subArea):
          if(grid.get((i-1, j))!=value):
            if not found:
              found=True
              sides=sides+1
          else:
            found=False
        else:
          modeRight=False
          found=False
      
      if(modeRight==False):
        if(grid[(i,j)]!=value):
          if (grid.get((i-1,j))==value and (i-1,j) in subArea):
            if not found:
              found=True
              sides=sides+1
          else:
            found=False
        else:
          modeRight=True
          if (grid.get((i-1,j))!=value and (i,j) in subArea):
            found=True
            sides=sides+1
          else:
            found=False

  found=False
  for j in range(minY, maxY+1):
    if (grid.get((maxX,j))==value and (maxX,j) in subArea):
      if not found:
        found=True
        sides=sides+1
    else:
      found=False
  return sides

def evaluateSides(subArea, grid, value):      
  return sidesVertical(subArea, grid, value)+sidesOrizontal(subArea, grid, value)

def solveB():
  rows=getOldAocInput(12)
  grid,_,_=buildGrid(rows)
  visited=set()
  ris=0
  for point, value in grid.items():
    if point in visited:
      continue
    subArea=set()
    area=0
    border=[point]
    while(len(border)>0):
      currentPoint=border.pop()
      if currentPoint in visited:
        continue
      visited.add(currentPoint)
      subArea.add(currentPoint)
      area=area+1
      different=0
      for d in directions:
        tentative=sumTupleValueByValue(currentPoint, d)
        if grid.get(tentative)!=value:
          different=different+1
        else:
          border.append(tentative)
    ris=ris+area*evaluateSides(subArea, grid, value)
  return ris

print(solve())
print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# evaluateTime(timeElapse)