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
      endPoint=xSplit
    elif(xSplit[0]<ySplit[0]):
      startingPoint=xSplit
      endPoint=ySplit


    currentPoint=startingPoint
    markPoint(currentPoint, markedDictionary)
    for element in range(abs(xSplit[0]-ySplit[0])):

      currentPoint=sumArrayValueByValue(currentPoint, distanceVector[2])

      if(startingPoint[1]>endPoint[1]):
        currentPoint=sumArrayValueByValue(currentPoint, distanceVector[1])
      else:
        currentPoint=sumArrayValueByValue(currentPoint, distanceVector[0])
      markPoint(currentPoint, markedDictionary)

def solve(markerFunction):
  rows=getAocInput(5,2021)
  markedDictionary=dict()
  for element in rows:
    splitted=element.split(" -> ")
    xSplit=splitted[1].split(",")
    ySplit=splitted[0].split(",")

    markerFunction(xSplit, ySplit, markedDictionary)
  
  return len([a for a in markedDictionary.values() if a>1])

print(solve(markGrid))
print(solve(markGridSpecial))