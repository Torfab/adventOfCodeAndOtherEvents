from utilityz import *
import heapq

directions=fromDistanceBuildSetOfDirections(1)

def solve():
  rows= openFile("raw.txt")
  grid, _, _=buildGrid(rows, " ")

  for k,v in grid.items():
    if v=="S":
      start=k
    if v=="E":
      end=k
    if v.isdigit():
      grid[k]=int(v)

  border=[]

  heapq.heappush(border, (0, [], start, 0))
  print(start, end)

  bestReached={start: 0}
  while(True):
    currentTime, currentVisited, currentPosition, currentLevel=heapq.heappop(border)
    if bestReached[currentPosition]<currentTime:
      continue
    currentVisited.append(currentPosition)
    for direction in directions:
      newCurrentPosition=sumTupleValueByValue(currentPosition, direction)
      if(newCurrentPosition in currentVisited or grid.get(newCurrentPosition)==None or grid.get(newCurrentPosition)=="#"):
        continue
      if(newCurrentPosition==end):
        newLevel=0
        if abs(currentLevel-newLevel)>5:
          partialNewTime=(10-abs(currentLevel-newLevel))
        else:
          partialNewTime=(abs(currentLevel-newLevel))
        return currentTime+1+partialNewTime
      
      newLevel=grid[newCurrentPosition]
      if abs(currentLevel-newLevel)>5:
        partialNewTime=(10-abs(currentLevel-newLevel))
      else:
        partialNewTime=(abs(currentLevel-newLevel))

      newTime=currentTime+1+partialNewTime
      if bestReached.get(newCurrentPosition)==None:
        bestReached[newCurrentPosition]=newTime
      if bestReached[newCurrentPosition]>=newTime:
        bestReached[newCurrentPosition]=newTime
        heapq.heappush(border, (currentTime+1+partialNewTime, currentVisited.copy(), newCurrentPosition, newLevel))

def findTime(start, end, grid, bestReached):

  border=[]
  heapq.heappush(border, (0, [], start, 0))
  print(start, end)

  while(len(border)>0):
    currentTime, currentVisited, currentPosition, currentLevel=heapq.heappop(border)
    if bestReached[currentPosition]<currentTime:
      continue
    currentVisited.append(currentPosition)
    for direction in directions:
      newCurrentPosition=sumTupleValueByValue(currentPosition, direction)
      if(newCurrentPosition in currentVisited or grid.get(newCurrentPosition)==None or grid.get(newCurrentPosition)=="#" or grid.get(newCurrentPosition)=="S"):
        continue
      if(newCurrentPosition==end):
        newLevel=0
        if abs(currentLevel-newLevel)>5:
          partialNewTime=(10-abs(currentLevel-newLevel))
        else:
          partialNewTime=(abs(currentLevel-newLevel))
        return currentTime+1+partialNewTime
      
      newLevel=grid[newCurrentPosition]
      if abs(currentLevel-newLevel)>5:
        partialNewTime=(10-abs(currentLevel-newLevel))
      else:
        partialNewTime=(abs(currentLevel-newLevel))

      newTime=currentTime+1+partialNewTime
      if bestReached.get(newCurrentPosition)==None:
        bestReached[newCurrentPosition]=newTime
        heapq.heappush(border, (currentTime+1+partialNewTime, currentVisited.copy(), newCurrentPosition, newLevel))
      if bestReached[newCurrentPosition]>newTime:
        bestReached[newCurrentPosition]=newTime
        heapq.heappush(border, (currentTime+1+partialNewTime, currentVisited.copy(), newCurrentPosition, newLevel))
  return float("inf")



def solve2():
  rows= openFile("raw.txt")
  grid, _, _=buildGrid(rows, " ")

  startingPoints=[]
  for k,v in grid.items():
    if v=="S":
      startingPoints.append(k)
    if v=="E":
      end=k
    if v.isdigit():
      grid[k]=int(v)

  bestReached={}

  for start in startingPoints:
    bestReached[start]=0

  results=[]
  for start in startingPoints:
    results.append(findTime(start, end, grid, bestReached))



  return min(results)


print(solve2())
