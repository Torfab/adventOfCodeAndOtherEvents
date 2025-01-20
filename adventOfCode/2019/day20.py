from utility import *
import heapq

directions=fromDistanceBuildSetOfDirections(1)

def buildPortalGrid(grid):
  literals={}
  portals={}
  found=set()

  for element, value in grid.items():
    if element in found:
      continue
    if value.isupper():
      found.add(element)
      if element in portals.keys():
        continue
      portalKey=-1
      for d in directions:
        tentative=sumTupleValueByValue(element, d)
        if(grid.get(tentative)==None):
          portalKey=tentative
        if(grid.get(tentative)!=None and grid[tentative].isupper()):
          found.add(tentative)
          innerTentative=sumTupleValueByValue(d, tentative)
          if grid.get(innerTentative)==None:
            portalKey=innerTentative
          portalLiteral=value+grid[tentative]
      if portalLiteral in literals:
        portalToUpdate=portalLiteral
      elif portalLiteral[::-1] in literals:
        portalToUpdate=portalLiteral[::-1]
      else:
        literals[portalLiteral]=portalKey
        continue
      portals[portalKey]=literals[portalToUpdate]
      portals[literals[portalToUpdate]]=portalKey
  return portals, literals

def checkOuter(currentPoint, minBound, maxBound):
  if currentPoint[0]==minBound[0]+3 or currentPoint[0]==maxBound[0]-3:
    return True
  if currentPoint[1]==minBound[1]+3 or currentPoint[1]==maxBound[1]-3:
    return True
  return False

def buildGraph(literals, portals, grid):
  start=literals["AA"]
  end=literals["ZZ"]
  nodesToCheck=list(portals.keys())+[start]+[end]
  maxBound=maxGrid(grid)
  minBound=minGrid(grid)
  graph={}
  for k in nodesToCheck:
    results=[]
    border=[k]
    visited=set()
    i=0
    while(border):
      newBorder=[]
      while(border):
        currentPoint=border.pop()
        if currentPoint in visited:
          continue
        visited.add(currentPoint)
        if(currentPoint==end):
          results.append((currentPoint, i, 0))
        if(currentPoint in portals and k!=currentPoint):
          if checkOuter(currentPoint, minBound, maxBound):
            level=1
          else:
            level=-1
          results.append((currentPoint, i, level))
        for d in directions:
          tentative=sumTupleValueByValue(currentPoint, d)
          if tentative in visited:
            continue
          if tentative in grid:
            continue
          if tentative not in grid:
            newBorder.append(tentative)
      border=newBorder
      i= i+1
    graph[k]=results
  return graph

def recursiveBFS(start, end, literals, portals, grid):
  graph=buildGraph(literals, portals, grid)
  visited={}
  border=[]
  heapq.heappush(border, (0, start, 0))
  while(border):
    currentLength, currentPoint, currentLevel=heapq.heappop(border)
    if((currentPoint, currentLevel) in visited):
      if currentLength>=visited[(currentPoint, currentLevel)]:
        continue
    visited[(currentPoint, currentLevel)]=currentLength
    for nodePoint, nodeLength, levelToAdd in graph[currentPoint]:
      if currentLevel+levelToAdd>0:
        continue
      if (nodePoint, currentLevel) == (end, 0):
        return currentLength+nodeLength
      if nodePoint==end:
        continue
      if portals.get(nodePoint):
        heapq.heappush(border, (currentLength+nodeLength+1, portals[nodePoint], currentLevel+levelToAdd))
      else:
        heapq.heappush(border, (currentLength+nodeLength, nodePoint, currentLevel+levelToAdd))




def simpleBFS(start, end, portals, grid):

  border=[start]
  visited=set()
  i=0
  while(border):
    newBorder=[]
    i=i+1
    while(border):
      currentPoint=border.pop()
      if currentPoint in visited:
        continue
      visited.add(currentPoint)
      if currentPoint in portals and portals[currentPoint] not in visited:
          newBorder.append(portals[currentPoint])
          continue

      for d in directions:
        tentative=sumTupleValueByValue(d, currentPoint)
        if tentative in visited:
          continue
        if tentative in grid:
          continue
        if tentative==end:
          return i
        newBorder.append(tentative)
    border=newBorder

def solve(part):
  rows=getOldAocInput(20)
  grid, _, _=buildGrid(rows)
  maxBoundaries=maxGrid(grid)
  cageElements=cageGridWithWalls(maxBoundaries)
  for c in cageElements:
    grid[c]="#"
  portals, literals=buildPortalGrid(grid)
  start=literals["AA"]
  end=literals["ZZ"]
  if part=="a":
    return simpleBFS(start, end, portals, grid)
  if part=="b":
    return recursiveBFS(start, end, literals, portals, grid)


  return "UH"

print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
