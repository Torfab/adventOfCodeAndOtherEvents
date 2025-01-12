from utilityz import *

directions=fromDistanceBuildListOfDirections(1)

def checkWhatYouCanReach(start, walls, doors, keys, grid, toPrint):
  visited=set()
  border=[(start)]
  path=0
  result=[]
  while(border):
    path=path+1
    newBorder=[]
    while(border):
      currentPoint=border.pop()
      if currentPoint in visited:
        continue
      if currentPoint in keys:
        result.append(grid[currentPoint])
      visited.add(currentPoint)
      for d in directions:
        tentative=sumTupleValueByValue(currentPoint, d)
        if tentative in walls:
          continue
        if tentative in doors:
          # result[grid[tentative]]=path
          result.append(grid[tentative])
          continue
        newBorder.append(tentative)
    border=newBorder
  if(toPrint[0] in result):
    result.remove(toPrint[0])
  return result

def updateGraphDictWithFakeDoors(graphDict,fakeDoors):
  foundNewFakeDoor=True
  while foundNewFakeDoor:
    foundNewFakeDoor=False
    newFakeDoors=[]
    for k, element in graphDict.items():
      for side in ["left", "right"]:
        element[side]=[item for item in element[side] if item not in fakeDoors]
        if(len(element[side])==0):
          newFakeDoors.append(k)
          foundNewFakeDoor=True
    for element in newFakeDoors:
      graphDict.pop(element)
    fakeDoors.extend(newFakeDoors)

def buildGraphDictFromDoors(doors, grid, walls, keys, fakeDoors):
  graphDict={}
  for element in doors:
    going="left"
    item={}
    isFake=False
    for d in directions:
      tentative=sumTupleValueByValue(d,element)
      if(tentative in walls):
        continue
      resultList=checkWhatYouCanReach(tentative, walls, doors, keys, grid, (grid[element], d))
      if len(resultList)==0:
        fakeDoors.append(grid[element])
        isFake=True
      item[going]=resultList
      if(going=="left"):
        going="right"
    if not isFake:
      graphDict[grid[element]]=item
  updateGraphDictWithFakeDoors(graphDict,fakeDoors)
  return graphDict, fakeDoors

def buildGraphKeyDict(keys, walls, doors, grid, fakeDoors):
  graphKeyDict={}
  for element in keys:
    for d in directions:
      tentative=sumTupleValueByValue(d,element)
      if(tentative in walls):
        continue
      resultList=checkWhatYouCanReach(tentative, walls, doors, keys, grid, (grid[element], d))
      resultList=[x for x in resultList if x not in fakeDoors]
      break
    graphKeyDict[grid[element]]=resultList
  return graphKeyDict

def findReachables(start, points, walls, startLength):
  visited=set()
  border=[start]
  pathLength=startLength
  newBorder=[]
  reachables={}
  while(border):
    newBorder=[]
    while (border):
      currentPoint=border.pop()
      if currentPoint in visited:
        continue
      visited.add(currentPoint)
      for d in directions:
        tentative=sumTupleValueByValue(d, currentPoint)
        if tentative in points and reachables.get(tentative)==None:
            reachables[tentative]=pathLength+1
        if tentative in walls:
          continue
        if tentative==start:
          continue
        if tentative in visited:
          continue
        newBorder.append(tentative)
    border=newBorder
    pathLength=pathLength+1
  return reachables
    

def findPathTakingAll(startName, pointNames, side, grid, doors, keys, walls):
  if side=="left":
    directionsToCheck=directions
  else:
    directionsToCheck=reversed(directions)
  

  points=[]
  reverseDictPoint={}
  for pointName in pointNames:
    for element in keys:
      if grid[element]==pointName:
        break
    points.append(element)
    reverseDictPoint[pointName]=element

  for element in doors:
    if grid[element]==startName:
      break
  start=element

  internalGrid={}
  for d in directionsToCheck:
    tentative=sumTupleValueByValue(start, d)
    if tentative in walls:
      continue
    else:
      break
  internalGrid[start]=findReachables(tentative, points, walls, 1)

  for element in points:
    internalGrid[element]=findReachables(element, [x for x in points if x!=element]+[start], walls, 0)

  
  itemForPermutation={}
  for element in pointNames:
    itemForPermutation[element]=1
  thePermutations=[]
  homeMadePermutations(itemForPermutation, "", len(pointNames), thePermutations)

  currentMin=float("inf")
  for permutation in thePermutations:
    permutationLength=0
    ris=[]
    for letter in permutation:
      ris.append(reverseDictPoint[letter])
    path=[start]+ris+[start]

    currentPoint=path[0]
    for element in path[1:]:
      permutationLength=permutationLength+internalGrid[currentPoint][element]
      currentPoint=element
    currentMin=min(currentMin, permutationLength)
  return currentMin

def updateGraphDictAfterTakingAll(graphDict):
  for doorItem in graphDict.values():
    if doorItem.get("takeAll")!=None:
      for side in ["left", "right"]:
        doorItem[side]=[x for x in doorItem[side] if x not in doorItem["takeAll"][0]]
        if len(doorItem[side])==0:
          doorItem.pop(side)

def findPathTwoPoints(start, end, grid, walls):
  start=[k for k,v in grid.items() if v==start][0]
  end =[k for k,v in grid.items() if v==end][0]

  visited=set()
  border=[start]
  pathLength=0
  while(border):
    newBorder=[]
    while(border):
      currentPoint=border.pop()
      if currentPoint in visited:
        continue
      visited.add(currentPoint)
      for d in directions:
        tentative=sumTupleValueByValue(d, currentPoint)
        if tentative==end:
          return pathLength+1
        if tentative in visited:
          continue
        if tentative in walls:
          continue
        newBorder.append(tentative)
    border=newBorder
    pathLength=pathLength+1

def joinContiguosDoors(graphDict, grid, walls):
  for doorName, doorValue in list(graphDict.items()):
    if doorValue.get("left")!=None and doorValue.get("right")!=None and len(doorValue["left"])==1 and len(doorValue["right"])==1:
      if graphDict[doorValue["left"][0]].get("left")!=None and len(graphDict[doorValue["left"][0]]["left"])!=1:
        left=graphDict[doorValue["left"][0]]["left"]
      elif graphDict[doorValue["left"][0]].get("right")!=None and len(graphDict[doorValue["left"][0]]["right"])!=1:
        left=graphDict[doorValue["left"][0]]["right"]
      else:
        left=None
      if graphDict[doorValue["right"][0]].get("left")!=None and len(graphDict[doorValue["right"][0]]["left"])!=1:
        right=graphDict[doorValue["right"][0]]["left"]
      elif graphDict[doorValue["right"][0]].get("right")!=None and len(graphDict[doorValue["right"][0]]["right"])!=1:
        right=graphDict[doorValue["right"][0]]["right"]
      else:
        left=None
      if graphDict[doorValue["left"][0]].get("takeAll")!=None:
        takeAll=graphDict[doorValue["left"][0]]["takeAll"]
      elif (graphDict[doorValue["right"][0]].get("takeAll")!=None):
        takeAll=graphDict[doorValue["right"][0]]["takeAll"]
      else:
        takeAll=None
      item={}
      if left:
        item["left"]=left
      if right:
        item["right"]=right
      if(takeAll):
        item["takeAll"]=(takeAll[0],takeAll[1]+findPathTwoPoints(doorValue["left"][0], doorValue["right"][0], grid, walls))
      
      graphDict[doorValue["left"][0]+doorName+doorValue["right"][0]]=item
      graphDict.pop(doorValue["left"][0])
      graphDict.pop(doorValue["right"][0])
      graphDict.pop(doorName)
          


def solve():
  rows=getOldAocInput(15)
  grid,_,_=buildGrid(rows)
  
  walls=[k for k,v in grid.items() if v=="#"]
  items=[(v,k) for k,v in grid.items() if v!="#"]
  start=[k for k,v in grid.items() if v=="@"][0]

  # First Recognition

  items.sort()
  items.pop(0)
  doors=set([x[1] for x in items[:26]])
  keys=set([x[1] for x in items[26:]])

  checkWhatYouCanReach(start, walls, doors, keys, grid, (start,0))

  graphDict, fakeDoors=buildGraphDictFromDoors(doors, grid, walls, keys, [])
  doorNames=set(graphDict.keys())
  
  fakeDoors=set(fakeDoors)
  graphKeyDict=buildGraphKeyDict(keys, walls, doors, grid, fakeDoors)

  takeAll=[]
  for doorName, value in graphDict.items():
    for side in ["left", "right"]:
      if thingInCommonArray(value[side], doorNames):
        continue
      else:
        takeAll.append((doorName, value[side], side))
  

  for element in takeAll:
    graphDict[element[0]]["takeAll"]=(element[1],findPathTakingAll(element[0], element[1], element[2], grid, doors, keys, walls))
  updateGraphDictAfterTakingAll(graphDict)
  joinContiguosDoors(graphDict, grid, walls)

  print(graphDict)

  for element in graphDict:
    for side in ["left", "right"]:
      return
      # if lelement[side]
  # comprimables={x:v for x,v in graphKeyDict.items() if len(v)==1}

  # print(graphDict)
  # print(comprimables)

  # print(fakeDoors)
  # print(graphDict)
  # print(graphKeyDict)

print(solve())

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# evaluateTime(timeElapse)