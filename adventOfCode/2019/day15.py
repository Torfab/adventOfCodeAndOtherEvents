from utilityz import *
from intCode import *

directions={1:(0,-1), 2:(0,1), 3:(-1,0), 4:(1,0)}
simpleDirections=fromDistanceBuildSetOfDirections(1)

def buildGrid(commands):
  cursor=0
  relativeBase=0
  currentPoint=(0,0)
  startPoint=currentPoint
  grid={currentPoint:"S"}
  tentativeD=1
  # first thing first, find first north wall
  feedback=-1
  while(feedback!=0):
    commands, outputs, cursor, _, relativeBase=runCommands(commands, tentativeD, pauseMode=True, cursor=cursor, relativeBase=relativeBase)
    feedback=outputs[0]
    if feedback==1:
      grid[sumTupleValueByValue(currentPoint, directions[tentativeD])]="+"
      currentPoint=sumTupleValueByValue(currentPoint, directions[tentativeD])
  feedback=-1
  tentativeD=4
  currentPoint=(0,0)
  pathResult=[]
  path=0
  while(True):
    commands, outputs, cursor, _, relativeBase=runCommands(commands, tentativeD, pauseMode=True, cursor=cursor, relativeBase=relativeBase)
    feedback=outputs[0]
    walled=False
    if feedback==0:
      grid[sumTupleValueByValue(currentPoint, directions[tentativeD])]="#"
      walled=True
    elif feedback==1:
      grid[sumTupleValueByValue(currentPoint, directions[tentativeD])]=" "
      currentPoint=sumTupleValueByValue(currentPoint, directions[tentativeD])
      path=path+1
      if currentPoint==startPoint:
        pathResult.append(path)
        grid[currentPoint]="S"
        break
    elif feedback==2:
      grid[sumTupleValueByValue(currentPoint, directions[tentativeD])]="E"
      currentPoint=sumTupleValueByValue(currentPoint, directions[tentativeD]) 
      endPoint=currentPoint
      path=path+1
      pathResult.append(path)
      path=0

      # break
    
    if walled:
      if tentativeD==1:
        tentativeD=4
      elif tentativeD==2:
        tentativeD=3
      elif tentativeD==3:
        tentativeD=1
      elif tentativeD==4:
        tentativeD=2
    else:
      if tentativeD==1:
        tentativeD=3
      elif tentativeD==2:
        tentativeD=4
      elif tentativeD==3:
        tentativeD=2
      elif tentativeD==4:
        tentativeD=1
  return startPoint, endPoint, grid

def solve(part):
  rows=getOldAocInput(15)
  commands=parseIntCode(rows)
  startPoint, endPoint, grid=buildGrid(commands)

  
  walls=set([k for k,v in grid.items() if v=="#"])

  # We have the full grid, now we just go bfs
  if part=="a":
    border=[(0, startPoint)]
    visited=set()
    while(True):
      distance,currentPoint=border.pop(0)
      if currentPoint in visited:
        continue
      visited.add(currentPoint)
      for d in simpleDirections:
        tentative=sumTupleValueByValue(currentPoint, d)
        if tentative in walls:
          continue
        if tentative in visited:
          continue
        if tentative==endPoint:
          return distance+1
        border.append((distance+1, tentative))
  if part=="b":
    visited=set()
    i=0
    newBorder=[endPoint]
    while(len(newBorder)>0):
      border=newBorder
      newBorder=[]
      while(len(border)>0):
        currentElement=border.pop()
        if currentElement in visited:
          continue
        visited.add(currentElement)
        for d in simpleDirections:
          tentative=sumTupleValueByValue(currentElement, d)
          if tentative in walls:
            continue
          if tentative in visited:
            continue
          newBorder.append(tentative)
      i=i+1
  return i-1

print(solve("a"))
print(solve("b"))
