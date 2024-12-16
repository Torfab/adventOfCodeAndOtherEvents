from utility import *
import heapq

directions=[(1,0), (0,1), (-1,0), (0,-1)]

def solve(part):
  rows=getOldAocInput(16)
  grid,_,_=buildGrid(rows)
  startPoint=[k for k,v in grid.items() if v=="S"][0]
  endPoint=[k for k,v in grid.items() if v=="E"][0]
  grid.pop(startPoint)
  grid.pop(endPoint)
  walls=set(grid.keys())

  border=[]
  heapq.heappush(border, (0, startPoint, 0, [startPoint]))
  visited={}
  score=float("inf")
  sits=set()
  while(len(border)>0):
    cValue, cPosition, cDirection, history=heapq.heappop(border)
    if(cValue>score):
      continue
    if(cPosition==endPoint):
      if(part=="a"):
        return cValue
      score=cValue
      for element in history:
        sits.add(element)
      continue

    oldValue=visited.get((cPosition, cDirection))
    if oldValue!=None and oldValue<cValue:
      continue
    visited[(cPosition, cDirection)]=cValue
    tentative=sumTupleValueByValue(cPosition, directions[cDirection])
    if(tentative not in walls):
      if visited.get((tentative, cDirection), score)>cValue:
        heapq.heappush(border, (cValue+1, tentative, cDirection, history+[tentative]))

    newDirection=(cDirection+1)%4
    tentative=sumTupleValueByValue(cPosition, directions[newDirection])
    if(tentative not in walls):
      if visited.get((tentative, newDirection), score)>cValue:
        heapq.heappush(border, (cValue+1001, tentative, newDirection, history+[tentative]))
    
    newDirection=(cDirection-1)%4
    tentative=sumTupleValueByValue(cPosition, directions[newDirection])
    if(tentative==endPoint):
      return cValue+1001
    if(tentative not in walls):
      if visited.get((tentative, newDirection), score)>cValue:
        heapq.heappush(border, (cValue+1001, tentative, newDirection, history+[tentative]))
  if(part=="b"):
    return len(sits)

print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# evaluateTime(timeElapse)