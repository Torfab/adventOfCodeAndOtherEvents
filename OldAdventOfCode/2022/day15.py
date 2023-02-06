from utility import *


def mark(position:tuple, grid:dict):
  if(grid.get(position)==None):
    grid[position]="#"
  else:
    if(grid[position]=="B"):
      return False
  return True

def fromXAndDistanceBuildVectorMarker(x, distance):
  arrayOfResult=[]
  if(distance>=0):
    arrayOfResult.append(x)
  for i in range(1,distance+1):
    arrayOfResult.append(x+i)
    arrayOfResult.append(x-i)
  return arrayOfResult

def resolve(yToCheck):
  rows=getOldAocInput(15)

  setAtIndex=set()

  toRemove=[]

  for element in rows:
    splitted=element.split(" ")
    x1=int(splitted[2][:-1].split("=")[1])
    y1=int(splitted[3][:-1].split("=")[1])
    x2=int(splitted[8][:-1].split("=")[1])
    y2=int(splitted[9].split("=")[1])
    if(y2==yToCheck):
      toRemove.append(x2)
    deltaDistance=distanceBetweenTwoTuples((x1,y1),(x2,y2))-distanceBetweenTwoTuples((x1,y1), (x1, yToCheck))

    for xIdx in fromXAndDistanceBuildVectorMarker(x1, deltaDistance):
      setAtIndex.add(xIdx)
  
  for element in toRemove:
    setAtIndex.discard(element)

  return len(setAtIndex)

def checkIfInRange(sensorDict:dict, coordinates=(3156345,3204261)):
  for element in sensorDict:
    distance=distanceBetweenTwoTuples(coordinates,element)
    if(distance<=sensorDict[element]):
      return False
  return True



def resolve2():
  rows=getOldAocInput(15)

  sensorDict=dict()

  for element in rows:
    splitted=element.split(" ")
    x1=int(splitted[2][:-1].split("=")[1])
    y1=int(splitted[3][:-1].split("=")[1])
    x2=int(splitted[8][:-1].split("=")[1])
    y2=int(splitted[9].split("=")[1])

    deltaDistance=distanceBetweenTwoTuples((x1,y1),(x2,y2))

    sensorDict[(x1,y1)]=deltaDistance

  for sensor in sensorDict:
    
    for element in fromDistanceBuildSetOfDirections(sensorDict[sensor]+1):
      candidate=sumTupleValueByValue(sensor, element)
      if(candidate[0]<0 or candidate[0]>4000000):
        continue
      if(candidate[1]<0 or candidate[1]>4000000):
        continue
      if(checkIfInRange(sensorDict, candidate)):
        return candidate[0]*4000000+candidate[1]

print(resolve(2000000))
print(resolve2())