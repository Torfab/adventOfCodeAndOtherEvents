from utility import *
import heapq

directions=fromDistanceBuildSetOfDirections(1)

def parseRows(rows, maxLimits):
  walls=set()
  for row in rows[:1025]:
    rowSplitted=row.split(",")
    walls.add((int(rowSplitted[0]), int(rowSplitted[1])))
  walls=walls.union(cageGridWithWalls((maxLimits[0],maxLimits[1])))
  return walls

def myBfs(startPoint, endPoint, walls):
  border=[]
  heapq.heappush(border, (0, startPoint, [startPoint]))
  visited=set()
  while(len(border)>0):
    score, currentPoint, history=heapq.heappop(border)
    if(currentPoint in visited):
      continue
    visited.add(currentPoint)
    for d in directions:
      tentative=sumTupleValueByValue(currentPoint, d)
      if(tentative==endPoint):
        return score+1, history
      if(tentative in walls or tentative in visited):
        continue
      heapq.heappush(border, (score+1, tentative, history+[tentative]))
  return -1, None

def solve(part, maxLimits=(70,70)):
  rows=getOldAocInput(18)
  walls=parseRows(rows, maxLimits)
  startPoint=(0,0)
  endPoint=(maxLimits[0], maxLimits[1])
  result, history=myBfs(startPoint, endPoint, walls)
  if part=="a":
    return result
  goodPath=set(history)
  startElement=1025
  while(True):
    startElement=startElement+1
    newWallElement=rows[startElement].split(",")
    wallPoint=(int(newWallElement[0]), int(newWallElement[1]))
    walls.add(wallPoint)
    if wallPoint not in goodPath:
      continue
    result, history=myBfs(startPoint, endPoint, walls)
    if(result==-1):
      return str(wallPoint[0])+","+str(wallPoint[1])
    goodPath=set(history)
    
    
print(solve("a"))
print(solve("b"))
