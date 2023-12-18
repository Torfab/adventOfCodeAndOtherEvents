from utility import *
import heapq

finish=-1
maxX=0
maxY=0
endPoint=(0,0)
#N=0 E=1 S=2 W=3
directions=[(0,-1), (1,0), (0,1), (-1,0)]

def checkValidPosition(tentativePosition):
  if(tentativePosition[0]<0 or tentativePosition[0]>maxX):
    return False
  if(tentativePosition[1]<0 or tentativePosition[1]>maxY):
    return False
  return True

def sumTupleValueByValuez(a,b):
  return a[0]+b[0], a[1]+b[1]

def checkAndPutDirectioned(value, x, y, direction, times, newDirection, borders, rows, visited, minCount, maxCount):
  if(newDirection==direction):
    if(times==maxCount):
        return
    if(times<minCount):
      tentativePosition=sumTupleValueByValuez((x,y), directions[direction])
      if(checkValidPosition(tentativePosition)):
        newTime=times+1
        if((tentativePosition[0], tentativePosition[1],direction,newTime) in visited):
          return
        visited.add((tentativePosition[0], tentativePosition[1], direction, newTime))
        newValue=value+int(rows[tentativePosition[1]][tentativePosition[0]])
        heapq.heappush(borders, (newValue, tentativePosition[0], tentativePosition[1], direction, newTime))  
        return
  else:
    if(times<minCount):
      return
  tentativePosition=sumTupleValueByValuez((x,y), directions[newDirection])
  if(checkValidPosition(tentativePosition)):
    newTime=1
    if(newDirection==direction):
      newTime=times+1
    
    if((tentativePosition[0], tentativePosition[1],newDirection,newTime) in visited):
      return
    visited.add((tentativePosition[0], tentativePosition[1], newDirection, newTime))
    newValue=value+int(rows[tentativePosition[1]][tentativePosition[0]])
    heapq.heappush(borders, (newValue, tentativePosition[0], tentativePosition[1], newDirection, newTime))  

def solve(part):

  if(part=="a"):
    minCount=0
    maxCount=3
  else:
    minCount=4
    maxCount=10

  rows=getOldAocInput(17)
  global maxX, maxY, endPoint
  maxX=len(rows[0])-1
  maxY=len(rows)-1
  endPoint=(maxX, maxY)

  borders=[]
  heapq.heappush(borders, (0, 0, 0, -1, 0))
  heapq.heappush(borders, (0, 0, 0, 2, 0))
  #x,y,D,c
  visited={(0, 0, 0, 0)}
  count=0
  while(True):
    value, x,y, direction, times=heapq.heappop(borders)
    if((x,y)==endPoint and times>=minCount):
      finish=value
      break

    if(direction==1):
      checkAndPutDirectioned(value, x, y, direction, times,  0, borders, rows, visited, minCount, maxCount)
      checkAndPutDirectioned(value, x, y, direction, times,  1, borders, rows, visited, minCount, maxCount)
      checkAndPutDirectioned(value, x, y, direction, times,  2, borders, rows, visited, minCount, maxCount)
    elif(direction==2):
      checkAndPutDirectioned(value, x, y, direction, times,  1, borders, rows, visited, minCount, maxCount)
      checkAndPutDirectioned(value, x, y, direction, times,  2, borders, rows, visited, minCount, maxCount)
      checkAndPutDirectioned(value, x, y, direction, times,  3, borders, rows, visited, minCount, maxCount)
    elif(direction==0):
      checkAndPutDirectioned(value, x, y, direction, times,  0, borders, rows, visited, minCount, maxCount)
      checkAndPutDirectioned(value, x, y, direction, times,  1, borders, rows, visited, minCount, maxCount)
      checkAndPutDirectioned(value, x, y, direction, times,  3, borders, rows, visited, minCount, maxCount)
    elif(direction==3):
      checkAndPutDirectioned(value, x, y, direction, times,  0, borders, rows, visited, minCount, maxCount)
      checkAndPutDirectioned(value, x, y, direction, times,  2, borders, rows, visited, minCount, maxCount)
      checkAndPutDirectioned(value, x, y, direction, times,  3, borders, rows, visited, minCount, maxCount)

    count=count+1
    
  return finish

print(solve("a"))
print(solve("b"))