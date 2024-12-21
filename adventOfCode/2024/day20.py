from utilityz import *
import heapq

directions=fromDistanceBuildSetOfDirections(1)

# My 2 solutions scaling is very different, main solution is much better when cheatLimit is low
# The manhattan solution is quadratic and is much better when cheatLimit is higher

def solve(part):
  rows=getOldAocInput(20)
  grid, _, _=buildGrid(rows)

  start=[k for k,v in grid.items() if v=="S"][0]
  grid.pop(start)

  end=[k for k,v in grid.items() if v=="E"][0]
  grid.pop(end)

  walls=set(grid.keys())

  visited=set()
  border=[]
  heapq.heappush(border, (0,start))
  
  chain={}
  
  while(len(border)>0):
    score, currentPoint=heapq.heappop(border)
    if(currentPoint in visited):
      continue
    if(currentPoint==end):
      chain[currentPoint]=score
      break
    visited.add(currentPoint)
    for d in directions:
      tentative=sumTupleValueByValue(currentPoint, d)
      if(tentative in walls):
        continue
      if(tentative in visited):
        continue
      heapq.heappush(border, (score+1, tentative))
      chain[currentPoint]=score

  if part=="a":
    limitCheat=2
  if part=="b":
    limitCheat=20
  ris=0
  visited={}
  chainSet=set(chain.keys())
  elementToStart=[k for k,v in chain.items() if v<score-100]
  for element in elementToStart:
    visited[element]=set()
    found=set()
    border=[]
    heapq.heappush(border, (0,element))
    while(len(border)>0):
      score, currentPoint=heapq.heappop(border)
      if(currentPoint in found):
        continue
      found.add(currentPoint)
      for d in directions:
        tentative=sumTupleValueByValue(currentPoint, d)
        if(tentative in found):
          continue
        if(tentative in chainSet):
          if(tentative in visited[element]):
            continue
          else:
            visited[element].add(tentative)
            if(chain[tentative]-chain[element]-score-1>=100):
              ris=ris+1
        if score<limitCheat-1:
          heapq.heappush(border, (score+1, tentative))
  return ris

def solveManhattan(part):
  rows=getOldAocInput(20)
  grid, _, _=buildGrid(rows)

  start=[k for k,v in grid.items() if v=="S"][0]
  grid.pop(start)

  end=[k for k,v in grid.items() if v=="E"][0]
  grid.pop(end)

  walls=set(grid.keys())

  visited=set()
  border=[]
  heapq.heappush(border, (0,start))
  
  chain={}
  
  while(len(border)>0):
    score, currentPoint=heapq.heappop(border)
    if(currentPoint in visited):
      continue
    if(currentPoint==end):
      chain[currentPoint]=score
      break
    visited.add(currentPoint)
    for d in directions:
      tentative=sumTupleValueByValue(currentPoint, d)
      if(tentative in walls):
        continue
      if(tentative in visited):
        continue
      heapq.heappush(border, (score+1, tentative))
      chain[currentPoint]=score

  if part=="a":
    limitCheat=2
  if part=="b":
    limitCheat=20
  ris=0
  chainSet=list(chain.keys())
  for i in range(len(chainSet)-101):
    keyI=chainSet[i]
    scoreI=chain[keyI]
    for j in range(i+1,len(chainSet)):
      keyJ=chainSet[j]
      man=distanceBetweenTwoTuples(keyI, keyJ)
      if man<=limitCheat and chain[keyJ]-scoreI-man>=100:
        ris=ris+1
  return ris

print(solve("a"))
print(solveManhattan("b"))

# def timeElapse():
  # print(solveManhattan("a"))
  # print(solveManhattan("b"))
  # print(solveB())

# evaluateTime(timeElapse)

