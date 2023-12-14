from utility import *

directions=fromDistanceBuildListOfDirections(1) 

# Cycle detection

def parseRow(rows):
  grid={}
  for y in range(len(rows)):
    for x in range(len(rows)):
      if(rows[y][x]=="#"):
        grid[(x,y)]={"value": "#", "moved": False}
      if(rows[y][x]=="O"):
        grid[(x,y)]={"value": "O", "moved": False}
  return grid

def stampaGrid(grid):
  maxX=max(grid.keys(), key=lambda x: x[0])[0]+1
  maxY=max(grid.keys(), key=lambda x: x[1])[1]+1

  for y in range(maxY):
    for x in range(maxX):
      if(grid.get((x,y))==None):
        print(".", end="")
      else:
        print(grid[(x,y)]["value"], end="")
    print()

def tiltNorth(grid):
  while(True):
    newGrid={}
    everythingStill=True
    for k, element in grid.items():
      if (element["value"]=="O"):
        tentativePosition=sumTupleValueByValue(k, directions[3])
      else:
        newGrid[k]=element
        continue
      if (tentativePosition[1]>-1 and(grid.get((tentativePosition))==None or grid.get((tentativePosition))["moved"]==True)):
        
        newGrid[tentativePosition]={"value":"O", "moved": False}
        element["moved"]=True
        everythingStill=False
      else:
        newGrid[k]=element
    grid=newGrid
    if(everythingStill):
      break
  return grid

def tiltWest(grid):
  while(True):
    newGrid={}
    everythingStill=True
    for k, element in grid.items():
      if (element["value"]=="O"):
        tentativePosition=sumTupleValueByValue(k, directions[2])
      else:
        newGrid[k]=element
        continue
      if (tentativePosition[0]>-1 and(grid.get((tentativePosition))==None or grid.get((tentativePosition))["moved"]==True)):
        
        newGrid[tentativePosition]={"value":"O", "moved": False}
        element["moved"]=True
        everythingStill=False
      else:
        newGrid[k]=element
    grid=newGrid
    if(everythingStill):
      break
  return grid

def tiltSouth(grid, maxY):
  while(True):
    newGrid={}
    everythingStill=True
    for k, element in grid.items():
      if (element["value"]=="O"):
        tentativePosition=sumTupleValueByValue(k, directions[0])
      else:
        newGrid[k]=element
        continue
      if (tentativePosition[1]<maxY and(grid.get((tentativePosition))==None or grid.get((tentativePosition))["moved"]==True)):
        
        newGrid[tentativePosition]={"value":"O", "moved": False}
        element["moved"]=True
        everythingStill=False
      else:
        newGrid[k]=element
    grid=newGrid
    if(everythingStill):
      break
  return grid

def tiltEast(grid, maxX):
  while(True):
    newGrid={}
    everythingStill=True
    for k, element in grid.items():
      if (element["value"]=="O"):
        tentativePosition=sumTupleValueByValue(k, directions[1])
      else:
        newGrid[k]=element
        continue
      if (tentativePosition[0]<maxX and(grid.get((tentativePosition))==None or grid.get((tentativePosition))["moved"]==True)):
        
        newGrid[tentativePosition]={"value":"O", "moved": False}
        element["moved"]=True
        everythingStill=False
      else:
        newGrid[k]=element
    grid=newGrid
    if(everythingStill):
      break
  return grid

def doCycle(grid, maxX, maxY):
  grid=tiltNorth(grid)
  grid=tiltWest(grid)
  grid=tiltSouth(grid, maxY)
  grid=tiltEast(grid, maxX)
  return grid

def countGrid(grid):
  maxY=max(grid.keys(), key=lambda x: x[1])[1]+1
  result=0
  for element in grid.keys():
    if(grid[element]["value"]=="O"):
      result=result+maxY-element[1]
  return result

def findLastIndex(arr, element):
  idx=-1
  for i in range(len(arr)):
    if(arr[i]==element):
      idx=i
  return idx

def solve(part):
  rows=getOldAocInput(14)
  grid=parseRow(rows)
  if(part=="a"):
    grid=tiltNorth(grid)
    return countGrid(grid)
  maxY=max(grid.keys(), key=lambda x: x[1])[1]+1
  maxX=max(grid.keys(), key=lambda x: x[0])[0]+1
  subSequenceMin=4
  subSequence=[]
  arrayResults=[]
  startSubSequence=-1
  while(True):
    grid=doCycle(grid, maxX, maxY)
    partialResult=countGrid(grid)
    if(startSubSequence==-1):
      idx=findLastIndex(arrayResults, partialResult)
      if(idx!=-1):
        startSubSequence=idx
        subSequence.append(partialResult)
    else:
      if(partialResult==arrayResults[startSubSequence] and len(subSequence)>subSequenceMin):
        break
      if(partialResult==arrayResults[idx+1]):
        subSequence.append(partialResult)
        idx=idx+1
      else:
        startSubSequence=-1
        subSequence=[]

    arrayResults.append(partialResult)
  idxOfCycle=(1000000000-startSubSequence)%(len(subSequence))
  return subSequence[idxOfCycle-1]


print(solve("a"))
print(solve("b"))