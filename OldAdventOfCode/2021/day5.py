from utility import *

distanceVector=[[0,1],[0,-1],[1,0],[-1,0]]

def markPoint(a, markedDictionary):
  markedDictionary[str(a)]= (markedDictionary.get(str(a)) or 0) +1

def markGrid(xSplit, ySplit, markedDictionary: dict):
  
  xSplit=[int(a) for a in xSplit]
  ySplit=[int(a) for a in ySplit]

  if(xSplit[0]==ySplit[0]):
    for element in range(min(xSplit[1], ySplit[1]), max(xSplit[1], ySplit[1])+1):
      markPoint([xSplit[0], element], markedDictionary)
      
    return
  if(xSplit[1]==ySplit[1]):
    for element in range(min(xSplit[0], ySplit[0]), max(xSplit[0], ySplit[0])+1):
      markPoint([element, xSplit[1]], markedDictionary)      

    return
  return

def markGridSpecial(xSplit, ySplit, markedDictionary: dict):
  markGrid(xSplit, ySplit, markedDictionary)
  xSplit=[int(a) for a in xSplit]
  ySplit=[int(a) for a in ySplit]

  if(abs(xSplit[0]-ySplit[0])==abs(xSplit[1]-ySplit[1])):
    if(xSplit[0]>ySplit[0]):
      startingPoint=ySplit
    elif(xSplit[0]<ySplit[0]):
      startingPoint=xSplit

    markPoint(startingPoint, markedDictionary)

    currentPoint=startingPoint
    for element in range(abs(xSplit[0]-ySplit[0])):

      if(startingPoint[1]>startingPoint[0]):
        currentPoint=sumArrayValueByValue(startingPoint, distanceVector[2])
      else:
        currentPoint=sumArrayValueByValue(startingPoint, distanceVector[3])
      markPoint(currentPoint, markedDictionary)

def solve(markerFunction):
  rows=getAocInput(-1)
  markedDictionary=dict()
  for element in rows:
    splitted=element.split(" -> ")
    xSplit=splitted[0].split(",")
    ySplit=splitted[1].split(",")

    markerFunction(xSplit, ySplit, markedDictionary)
  
  print(markedDictionary)

  return len([a for a in markedDictionary.values() if a>1])

# print(solve(markGrid))
print(solve(markGridSpecial))