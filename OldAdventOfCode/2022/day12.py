from utility import *

distanceVector=[[0,1],[0,-1],[-1,0],[1,0]]

def heightOfElement(element):
  return ord(element)-97

def comprehension(rows):
  newRows=[]
  for idx, element in enumerate(rows):
    newRows.append([])
    for jdx, height in enumerate(element):
      if(height=='S'):
        startingPoint=[idx,jdx]
        newRows[idx].append(heightOfElement('a'))
        continue
      if(height=='E'):
        endingPoint=[idx, jdx]
        newRows[idx].append(heightOfElement('z'))
        continue
      newRows[idx].append(heightOfElement(height))
  
  return newRows, startingPoint, endingPoint



def solve(part):
  rows= getOldAocInput(12)
  rows, startingPoint, endingPoint= comprehension(rows)

  startingPoints=[]
  if(part=="a"):
    startingPoints.append(startingPoint)
  if(part=="b"):
    for idx,row in enumerate(rows):
      for jdx, column in enumerate(row):
        if(column==0):
          startingPoints.append([idx,jdx])

  coordinatesVisitedFromStart=[]
  borderOfSearch=[]

  for element in startingPoints:
    coordinatesVisitedFromStart.append(element)
    borderOfSearch.append(element)


  round=0
  while(len(borderOfSearch)>0):
    for idx in reversed(range(len(borderOfSearch))):
      avoid=[]
      currentPosition=borderOfSearch[idx]
      if(currentPosition[0]==0):
        avoid.append(2)
      if(currentPosition[0]==len(rows)-1):
        avoid.append(3)
      if(currentPosition[1]==0):
        avoid.append(1)
      if(currentPosition[1]==len(rows[0])-1):
        avoid.append(0)
      
      for direction in range(4):
        if direction in avoid:
          continue
        newPosition=sumArrayValueByValue(borderOfSearch[idx],distanceVector[direction])
        
        if(rows[currentPosition[0]][currentPosition[1]]-(rows[newPosition[0]][newPosition[1]])>=-1):
          if(str(newPosition) not in coordinatesVisitedFromStart):
            if(str(newPosition)==str(endingPoint)):
              return round+1
            coordinatesVisitedFromStart.append(str(newPosition))
            borderOfSearch.append(newPosition)
      borderOfSearch.pop(idx)
    round=round+1

print(solve("a"))
print(solve("b"))