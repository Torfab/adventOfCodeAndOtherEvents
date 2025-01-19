from utilityz import *
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

def recursiveBFS(literals, portals, grid):
  #BUILDGRAPH
  #TRAVERSE WITH DIJKSTRA
  return



def simpleBFS(literals, portals, grid):
  start=literals["AA"]
  end=literals["ZZ"]

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
  if part=="a":
    return simpleBFS(literals, portals, grid)
  if part=="b":
    return recursiveBFS(literals, portals, grid)


  return "UH"

# print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
