from utility import *
import heapq

direction={
  (0,1):[(0,1),(1,0),(-1,0)],
  (0,-1):[(0,-1),(1,0),(-1,0)],
  (1,0):[(1,0),(0,1),(0,-1)],
  (-1,0):[(-1,0),(0,1),(0,-1)],
}
direction3={
  (0,1):[(0,1), (1,0), (-1,0)],
  (1,0):[(1,0), (0,1)],
  (-1,0):[(-1,0), (0,1)]
}

def solve(selectedTime):
  rows=openFile("raw.txt")
  rows.append("#"*len(rows[0]))
  rows=["#"*len(rows[0])]+rows
  grid,_,_= buildGrid(rows)
  

  rocks=set([k for k, v in grid.items() if v=="#"])
  start=[k for k, v in grid.items() if v=="S"][0]
  plus=set([k for k, v in grid.items() if v=="+"])
  minus=set([k for k, v in grid.items() if v=="-"])
  grid.pop(start)

  time=0
  alt=1000
  border=[(-alt, start, (0,1))]
  visited=set()
  while(time<selectedTime):
    newBorder=[]
    while border:
      currentAlt, point, currentDirection=heapq.heappop(border)
      currentAlt=-currentAlt-1
      for d in direction[currentDirection]:
        tentative=sumTupleValueByValue(point, d)
        dAlt=currentAlt
        if(tentative in rocks):
          continue
        if((tentative, d) in visited):
          continue
        if(tentative in plus):
          dAlt=dAlt+2
        if(tentative in minus):
          dAlt=dAlt-1
        visited.add((tentative, d))
        heapq.heappush(newBorder, (-dAlt, tentative, d))
    time=time+1
    border=newBorder
    visited=set()
  element=heapq.heappop(border)

  return -element[0]

def specificBFS(grid, border, end):

  plus=set([k for k, v in grid.items() if v=="+"])
  minus=set([k for k, v in grid.items() if v=="-"])
  rocks=set([k for k, v in grid.items() if v=="#"])
  visited=set()
  endCounter=0
  endResults=[]

  while(True):
    newBorder=[]
    while border:
      time, currentAlt, point, currentDirection=heapq.heappop(border)
      currentAlt=-currentAlt-1
      time=time+1
      for d in direction[currentDirection]:
        tentative=sumTupleValueByValue(point, d)
        dAlt=currentAlt
        if(tentative in rocks):
          continue
        if((tentative, d) in visited):
          continue
        if(tentative==end):
          endCounter=endCounter+1
          endResults.append((time, -dAlt, tentative, d))
          if(endCounter==100):
            maxValue=max([-res[1]-res[0] for res in endResults])
            endResults=[e for e in endResults if (-e[1]-e[0])>=maxValue-2]
            # for res in endResults:
            #   print("ho raggiunto", grid[end]," in tempo ", res[0], "con altitudine", -res[1], "dalla direzione", res[2])

            return endResults
          continue
        if(tentative in plus):
          dAlt=dAlt+2
        if(tentative in minus):
          dAlt=dAlt-1
        visited.add((tentative, d))
        heapq.heappush(newBorder, (time, -dAlt, tentative, d))
    border=newBorder
    visited=set()

def specificBFS2(grid, border, maxY):

  plus=set([k for k, v in grid.items() if v=="+"])
  minus=set([k for k, v in grid.items() if v=="-"])
  rocks=set([k for k, v in grid.items() if v=="#"])
  visited=set()
  endCounter=0
  endResults=[]
  while(True):
    newBorder=[]
    while border:
      currentAlt, point, currentDirection, lastShit=heapq.heappop(border)
      currentAlt=-currentAlt-1
      for d in direction3[currentDirection]:
        tentative=sumTupleValueByValue(point, d)
        dAlt=currentAlt
        if(tentative in rocks):
          continue
        if((tentative, d) in visited):
          continue
        if(tentative[1]==maxY):
          endCounter=endCounter+1
          endResults.append((-dAlt, tentative, d))
          if(endCounter==100):
            newBorder=[]
            newVisited={}
            for e in endResults:
              if(e in newVisited):
                continue
              if(newVisited.get(e[1])==None):
                newVisited[e[1]]=e[0]
              else:
                newVisited[e[1]]=min(newVisited[e[1]], e[0])
            
            for k,v in newVisited.items():
              newBorder.append((v+1, (k[0], 0), (0,1), lastShit-v+1))

            return newBorder
          continue
        if(tentative in plus):
          dAlt=dAlt+2
        if(tentative in minus):
          dAlt=dAlt-1
        visited.add((tentative, d))
        heapq.heappush(newBorder, (-dAlt, tentative, d, lastShit))
    border=newBorder
    visited=set()

def solve2():
  rows=openFile("raw.txt")
  rows.append("#"*len(rows[0]))
  rows=["#"*len(rows[0])]+rows
  grid,_,_= buildGrid(rows)

  start=[k for k, v in grid.items() if v=="S"][0]
  locations=[]
  locations.append([k for k,v in grid.items() if v=="A"][0])
  locations.append([k for k,v in grid.items() if v=="B"][0])
  locations.append([k for k,v in grid.items() if v=="C"][0])
  locations.append(start)
  border=[(0, -10000, start, (0,1))]
  for l in locations:
    border=specificBFS(grid,border, l)
    # print(l, border)
  res=border[0]
  return res[0]+res[1]+10000


def solve3():

  val=384400-11
  schermate=1+val//6
  offset=11
  return 12*schermate+offset


# print(solve(100))
# print(solve2())


print(solve3())

  