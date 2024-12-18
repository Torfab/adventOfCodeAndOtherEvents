from utility import *
import heapq

directions=fromDistanceBuildSetOfDirections(1)

def solve():
  rows=openFile("raw.txt")
  first, last= rows[0].split(".")
  rows[0]=first+"S"+last
  grid, _, _=buildGrid(rows)
  
  start=[k for k,v in grid.items() if v=="S"][0]
  ends=[k for k,v in grid.items() if v=="H"]


  border=[]
  visited=[]
  time=0
  keys=grid.keys()
  heapq.heappush(border, (time, start))
  while(len(border)>0):
    time, current=heapq.heappop(border)
    if current in visited:
      continue
    visited.append(current)
    time=time+1
    for direction in directions:
      tentative=sumTupleValueByValue(current, direction)
      if(tentative[1]<0):
        continue
      if tentative in ends:
        return time*2
      if tentative in keys:
        continue
      heapq.heappush(border, (time, tentative))

def pruneDecoy(rows):
  maxX=len(rows[0])-1
  for i in range(len(rows)):
    if rows[i][1]=="E":
      rows[i]=rows[i][0]+"."+rows[i][2:]
    if rows[i][maxX-1]=="R":
      rows[i]=rows[i][:maxX-1]+"."+rows[i][maxX-1:]

def solve2():
  rows=openFile("raw.txt")
  first, last= rows[0].split(".")
  rows[0]=first+"S"+last

  ends={}
  grid, _, _=buildGrid(rows)
  for k,v in grid.items():
    if v!="#" and v!="~" and v!="S":
      if(ends.get(v)==None):
        ends[v]=[k]
      else:
        ends[v].append(k)
  for k,v in ends.items():
    for position in v:
      grid.pop(position)

  start=[k for k,v in grid.items() if v=="S"][0]
  ends=[v for v in ends.values()]



  grid[(start[0], start[1]-1)]="#" 

  endsMask={}
  for i in range(len(ends)):
    for element in ends[i]:
      endsMask[element]=i

  border=[]
  visited=set()
  found= tuple(False for _ in range(len(ends)))
  time=0
  keys=set(grid.keys())
  heapq.heappush(border, (time, start, found))
  count=0
  while(len(border)>0):
    count=count+1
    time, current, found=heapq.heappop(border)
    if(count%1000000==0):
      print(time, len(border), len(visited), sum(found))
    if((current, found) in visited):
      continue
    visited.add((current,found))
    time=time+1
    for direction in directions:
      tentative=sumTupleValueByValue(current, direction)
      if(tentative==start and False not in found):
        return time
      if tentative in keys:
        continue

      if endsMask.get(tentative)==None:
        newFound=found
      else:
        newFound=found[:endsMask[tentative]] + (True,) + found[endsMask[tentative]+1:]
      if((tentative, newFound) not in visited):
        heapq.heappush(border, (time, tentative, newFound))        

def bfs(rows, startLabel):
  ends={}
  grid, maxX, maxY=buildGrid(rows)
  for k,v in grid.items():
    if v!="#" and v!="~" and v!=startLabel:
      if(ends.get(v)==None):
        ends[v]=[k]
      else:
        ends[v].append(k)
  for k,v in ends.items():
    for position in v:
      grid.pop(position)

  start=[k for k,v in grid.items() if v==startLabel][0]
  ends=[v for v in ends.values()]
  for i in range(maxX):
    grid[(i, -1)]="#"
  for i in range(maxY):
    grid[(-1, i)]="#"
    grid[(maxX+1, i)]="#"
  endsMask={}

  for i in range(len(ends)):
    for element in ends[i]:
      endsMask[element]=i

  border=[]
  visited=set()
  found= tuple(False for _ in range(len(ends)))
  time=0
  keys=set(grid.keys())
  heapq.heappush(border, (time, start, found))
  while(len(border)>0):
    time, current, found=heapq.heappop(border)
    if((current, found) in visited):
      continue
    visited.add((current,found))
    time=time+1
    for direction in directions:
      tentative=sumTupleValueByValue(current, direction)
      if(tentative==start and False not in found):
        return time
      if tentative in keys:
        continue

      if endsMask.get(tentative)==None:
        newFound=found
      else:
        newFound=found[:endsMask[tentative]] + (True,) + found[endsMask[tentative]+1:]
      if((tentative, newFound) not in visited):
        heapq.heappush(border, (time, tentative, newFound))        

def solve3(part):
  rows=openFile("raw.txt")
  first, last= rows[0].split(".")
  rows[0]=first+"S"+last

  if(part!=3):
    return bfs(rows, "S")

  pruneDecoy(rows)

  split=[(0,84, "E"),(83,172, "S"), (171,255, "R")]
  results=[]
  for element in split:
    newRows=[]
    for row in rows:
      newRows.append(row[element[0]:element[1]])
    results.append(bfs(newRows, element[2]))
  return sum(results)

print(solve3(2))
