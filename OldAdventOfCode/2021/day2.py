from utility import *

distanceVector=dict(forward=[0,1],down=[1,0],up=[-1,0])

def solve1():
  rows=getAocInput(2,2021)
  startCoordinates=[0,0]
  for element in rows:
    splitted=element.split(" ")
    value=int(splitted[1])

    startCoordinates=sumArrayValueByValue(startCoordinates, multiplyArrayByValue(distanceVector[splitted[0]], value))

  
  return startCoordinates[0]*startCoordinates[1]

def solve2():
  rows=getAocInput(2,2021)
  position=0
  depth=0
  aim=0
  for element in rows:
    splitted=element.split(" ")
    value=int(splitted[1])

    if(splitted[0]=="down"):
      aim=aim+value
    if(splitted[0]=="up"):
      aim=aim-value
    if(splitted[0]=="forward"):
      position=position+value
      depth=depth+(value*aim)

  return position*depth

print(solve1())
print(solve2())