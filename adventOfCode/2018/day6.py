from utility import *


directions=fromDistanceBuildSetOfDirections(1)

def parseCoordinates(rows):
  listCoordinates=[]
  for row in rows:
    rowSplitted=row.split(", ")
    listCoordinates.append((int(rowSplitted[0]), int(rowSplitted[1])))
  return listCoordinates

def findFiniteCandidates(elements):
  #cerco gli altri elementi nelle 4 zone E S W N
  candidates=[]
  for element in elements:
    setFound=set()
    for innerElement in elements:

      if innerElement==element:
        continue

      dx=innerElement[0]-element[0]
      dy=innerElement[1]-element[1]

      if dx>=abs(dy):
        setFound.add("E")
      if dx<=-abs(dy):
        setFound.add("W")
      if (dy>=abs(dx)):
        setFound.add("N")
      if (dy<=-abs(dx)):
        setFound.add("S")
      if len(setFound)==4:
        candidates.append(element)
        break
        

  return candidates

def isCandidateClosest(current, candidate, elements):
  mainDistance=distanceBetweenTwoTuples(current, candidate)
  for element in elements:
    if(element!=candidate and distanceBetweenTwoTuples(current, element)<=mainDistance):
      return False
  return True

def floodFillResult(candidate, elements):
  count=1
  border=[]
  border.append(candidate)
  visited=set()
  visited.add(candidate)
  while(border):
    newBorder=[]
    for cell in border:
      for d in directions:
        tentative=sumTupleValueByValue(cell, d)
        if(tentative in visited):
          continue
        visited.add(tentative)
        if(isCandidateClosest(tentative, candidate, elements)):
          count=count+1
          newBorder.append(tentative)
    border=newBorder
  return count 

def calculateMedianPoint(elements):
  xList=list(x[0] for x in elements)
  xList.sort()
  yList=list(x[1] for x in elements)
  yList.sort()
  return (xList[len(xList)//2],yList[len(yList)//2])


def distanceIntoThreshold(current, elements, distanceThreshold):
  distance=0
  for element in elements:
    distance=distance+distanceBetweenTwoTuples(current, element)
    if distance>=distanceThreshold:
      return False
  return True
      

def floodFillDistance(start, elements, distanceThreshold):
  border=[]
  border.append(start)
  visited=set()
  count=0
  while(border):
    newBorder=[]
    for cell in border:
      if cell in visited:
        continue
      visited.add(cell)
      if not distanceIntoThreshold(cell, elements, distanceThreshold):
        continue
      # buona
      count=count+1
      for d in directions:
        tentative=sumTupleValueByValue(d, cell)
        if tentative not in visited:
          newBorder.append(tentative)
    border=newBorder
  return count

def solve(part):
  rows=openFile("raw.txt")
  elements=parseCoordinates(rows)
  if(part==1):
    candidates=findFiniteCandidates(elements)

    maxResult=0
    for candidate in candidates:
      maxResult=max(maxResult, floodFillResult(candidate, elements))
    return maxResult
  if part==2:
    epicenter=calculateMedianPoint(elements)
    return floodFillDistance(epicenter, elements, 10000)

def totalSolve():
  return solve(1), solve(2)

evaluateTime(totalSolve)