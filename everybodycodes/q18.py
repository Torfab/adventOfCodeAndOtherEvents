from utility import *
import heapq

directions=fromDistanceBuildSetOfDirections(1)

def solve():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows)
  starts=[]
  for j in [(0,-1), (maxX,maxX+1)]:
    for i in range(maxY):
      if(grid.get((j[0],i))==None):
        starts.append((j[0],i))
        grid[(j[0],i)]="S"
        grid[(j[1],i)]="#"

  targets=set([k for k,v in grid.items() if v=="P"])
  found=set()
  grid={k:v for k,v in grid.items() if v=="#"}
  visited=set()
  border=[]
  for start in starts:
    heapq.heappush(border, (0, start))
  while border:
    time, currentPlace=heapq.heappop(border)
    if currentPlace in visited:
      continue
    visited.add(currentPlace)
    time=time+1

    for d in directions:
      tentative=sumTupleValueByValue(currentPlace, d)
      if grid.get(tentative)==None and tentative not in visited:
        if(tentative in targets):
          found.add(tentative)
          if(len(found)==len(targets)):
            return time
        heapq.heappush(border, (time, tentative))

def bfs(grid, targets, start, minTimeFound):
  found=set()
  visited=set()
  border=[]
  heapq.heappush(border, (0, start))
  totalTimeNeeded=0
  while border:
    time, currentPlace=heapq.heappop(border)
    if currentPlace in visited:
      continue
    visited.add(currentPlace)
    time=time+1

    for d in directions:
      tentative=sumTupleValueByValue(currentPlace, d)
      if grid.get(tentative)==None and tentative not in visited:
        if(tentative in targets and tentative not in found):
          totalTimeNeeded=totalTimeNeeded+time
          if(totalTimeNeeded>minTimeFound):
            return minTimeFound
          found.add((tentative))
          if(len(found)==len(targets)):
            return totalTimeNeeded
        heapq.heappush(border, (time, tentative))

def solve2():
  rows=openFile("raw.txt")
  grid, _, _=buildGrid(rows, "k")
  targets=set([k for k,v in grid.items() if v=="P"])
  starts=[k for k,v in grid.items() if v=="."]

  grid={k:v for k,v in grid.items() if v=="#"}

  minTimeFound=float("inf")
  for s in starts:
    minTimeFound=min(bfs(grid, targets, s, minTimeFound), minTimeFound)
  return minTimeFound

print(solve2())