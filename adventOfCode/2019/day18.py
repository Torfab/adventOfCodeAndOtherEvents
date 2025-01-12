from utilityz import *
import heapq

directions=fromDistanceBuildListOfDirections(1)

def checkWhatYouCanReach(start, walls, doors, keys, grid, toIgnore, pathStart=0):
  visited=set()
  border=[(start)]
  path=pathStart
  result={}
  while(border):
    newBorder=[]
    while(border):
      currentPoint=border.pop()
      if currentPoint in visited:
        continue
      if currentPoint in keys:
        result[grid[currentPoint]]=path
      visited.add(currentPoint)
      for d in directions:
        tentative=sumTupleValueByValue(currentPoint, d)
        if tentative in walls:
          continue
        if tentative in doors:
          # result[grid[tentative]]=path
          result[grid[tentative]]=path+1
          continue
        newBorder.append(tentative)
    border=newBorder
    path=path+1
  if(toIgnore in result):
    result.pop(toIgnore)
  return result

def updateGraphDictWithFakeDoors(graphDict,fakeDoors):
  foundNewFakeDoor=True
  while foundNewFakeDoor:
    foundNewFakeDoor=False
    newFakeDoors=[]
    for k, element in graphDict.items():
      for side in ["left", "right"]:
        element[side]={item:v for item,v in element[side].items() if item not in fakeDoors}
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
      resultList=checkWhatYouCanReach(tentative, walls, doors, keys, grid, grid[element], 1)
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
    resultList=checkWhatYouCanReach(element, walls, doors, keys, grid, grid[element], 0)
    resultList={x:v for x,v in resultList.items() if x not in fakeDoors}
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
    

def findPathTakingAll(startName, pointNames, side, graphDict, graphKeyDict):

  itemForPermutation={}
  for element in pointNames:
    itemForPermutation[element]=1
  thePermutations=[]
  homeMadePermutations(itemForPermutation, "", len(pointNames), thePermutations)

  currentMin=float("inf")
  currentMinNoGoingBack=float("inf")
  for permutation in thePermutations:
    path=startName+permutation+startName
    permutationLength=graphDict[startName][side][path[1]]

    currentPoint=path[1]
    for element in path[2:-1]:
      permutationLength=permutationLength+graphKeyDict[currentPoint][element]
      currentPoint=element
    currentMinNoGoingBack=min(currentMinNoGoingBack, permutationLength)

    permutationLength=permutationLength+graphKeyDict[currentPoint][startName]
    currentMin=min(currentMin, permutationLength)
  return currentMinNoGoingBack, currentMin

def updateGraphDictAfterTakingAll(graphDict):
  for doorItem in graphDict.values():
    if doorItem.get("takeAll")!=None:
      for side in ["left", "right"]:
        if len([x for x in doorItem[side] if x not in doorItem["takeAll"][0]])==0:
          doorItem.pop(side)
        else:
          doorItem["singleSide"]=doorItem.pop(side)

def joinContiguosDoors(graphDict, graphKeyDict):
  for doorName, doorValue in list(graphDict.items()):
    if doorValue.get("left")!=None and doorValue.get("right")!=None and len(doorValue["left"])==1 and len(doorValue["right"])==1:
      leftElement=list(doorValue["left"])[0]
      if graphDict[leftElement].get("left")!=None and len(graphDict[leftElement]["left"])!=1:
        left=graphDict[leftElement]["left"]
      elif graphDict[leftElement].get("right")!=None and len(graphDict[leftElement]["right"])!=1:
        left=graphDict[leftElement]["right"]
      else:
        left=None
      rightElement=list(doorValue["right"])[0]
      if graphDict[rightElement].get("left")!=None and len(graphDict[rightElement]["left"])!=1:
        right=graphDict[rightElement]["left"]
      elif graphDict[rightElement].get("right")!=None and len(graphDict[rightElement]["right"])!=1:
        right=graphDict[rightElement]["right"]
      else:
        right=None

      if graphDict[leftElement].get("takeAll")!=None:
        takeAll=graphDict[leftElement]["takeAll"]
      elif (graphDict[rightElement].get("takeAll")!=None):
        takeAll=graphDict[rightElement]["takeAll"]
      else:
        takeAll=None
      item={}
      distance=list(doorValue["left"].values())[0]+list(doorValue["right"].values())[0]
      if(takeAll):
        item["takeAll"]=(takeAll[0],takeAll[1]+distance, takeAll[2]+(distance*2))
        if left:
          item["singleSide"]=left
        if right:
          item["singleSide"]=right
      else:
        if left:
          item["left"]=left
        if right:
          item["right"]=right
        if len(left)<len(right):
          check=item["left"]
        else:
          check=item["right"]
        for k,v in check.items():
          check[k]=v+distance
      newKey=leftElement+doorName+rightElement
      graphDict[newKey]=item
      graphDict.pop(leftElement)
      graphDict.pop(rightElement)
      graphDict.pop(doorName)
      
      for v in graphDict.values():
        for sideK,sideV in v.items():
          if sideK=="takeAll":
            continue
          for innerKey in list(sideV):
            if innerKey in newKey:
              sideV[newKey]=sideV[innerKey]
              sideV.pop(innerKey)
      
      for v in graphKeyDict.values():
        for innerKey in list(v):
          if innerKey in newKey:
            v[newKey]=v[innerKey]
            v.pop(innerKey)
          
def stampaGraph(graph):
  for k,v in graph.items():
    print(k, v)

def exploreMaze(k,v, fullGraphDict):

  border=[]
  keysTaken=set()
  currentPoint="@"
  visited=set()
  visited.add("WUS")
  heapq.heappush(border, (v, k, currentPoint, keysTaken, visited, []))

  currentMaxFound=float("inf")
  fastHistory=[]
  
  while(border):
    currentLength, currentPoint, previousPoint, keysTaken, visited, history=heapq.heappop(border)
    if currentLength>currentMaxFound:
      print("scartare")
      continue
    visited=visited.copy()
    visited.add(currentPoint)
    history=history+[(currentPoint, currentLength)]
    currentItem=fullGraphDict[currentPoint]
    if(currentItem["isDoor"]):
      #COMPORTATI DA DOOR
      if currentItem.get("takeAll")!=None:
        #Porta Take all
        newKeysTaken=keysTaken.copy()
        for element in currentItem["takeAll"][0]:
          newKeysTaken.add(element)
        currentLength=currentLength+currentItem["takeAll"][2]
        if len(newKeysTaken)==15 and "WUS" in currentItem["singleSide"]:
          finalLength=currentLength+currentItem["singleSide"]["WUS"]
          if currentMaxFound>finalLength:
            currentMaxFound=finalLength
            fastHistory=history

          # print("finito in", currentLength+currentItem["singleSide"]["WUS"], "ed il min è", currentMaxFound, "ho visitato", visited)
          continue
        for element, value in currentItem["singleSide"].items():
          if element in visited:
            continue
          if element.islower():
            heapq.heappush(border, (currentLength+value, element, currentPoint, newKeysTaken, visited, history))
          if element.isupper() and all(x.lower() in newKeysTaken for x in element):
            heapq.heappush(border, (currentLength+value, element, currentPoint, newKeysTaken, visited, history))
      else:
        # PORTA NORMALE
        if(previousPoint) in currentItem["left"]:
          checkSide=currentItem["right"]
        else:
          checkSide=currentItem["left"]
        for element, value in checkSide.items():
          if element in visited:
            continue
          if element.islower():
            heapq.heappush(border, (currentLength+value, element, currentPoint, keysTaken, visited, history))
          if element.isupper() and all(x.lower() in keysTaken for x in element):
            heapq.heappush(border, (currentLength+value, element, currentPoint, keysTaken, visited, history))
    else:
      #Comportati da key
      newKeysTaken=keysTaken.copy()
      newKeysTaken.add(currentPoint)
      if len(newKeysTaken)==15 and "WUS" in currentItem:
        finalLength=currentLength+currentItem["WUS"]
        if currentMaxFound>finalLength:
          currentMaxFound=finalLength
          fastHistory=history
        # print("finito in", currentLength+currentItem["WUS"], "ed il min è", currentMaxFound, "ho visitato", visited)
        continue

      for element, value in currentItem.items():
        if element in visited:
          continue
        if element.islower():
          heapq.heappush(border, (currentLength+value, element, currentPoint, newKeysTaken, visited, history))
        if element.isupper() and all(x.lower() in newKeysTaken for x in element):
          heapq.heappush(border, (currentLength+value, element, currentPoint, newKeysTaken, visited, history))

  print(fastHistory)
  return currentMaxFound

def exploreMazeFinal(k,v,fullGraphDict):

  border=[]
  keysTaken=set()
  currentPoint="WUS"
  visited=set()
  visited.add("WUS")
  heapq.heappush(border, (v, k, currentPoint, keysTaken, visited, []))

  currentMaxFound=float("inf")
  fastHistory=None
  
  while(border):
    currentLength, currentPoint, previousPoint, keysTaken, visited, history=heapq.heappop(border)
    if currentLength>currentMaxFound:
      continue
    visited=visited.copy()
    visited.add(currentPoint)
    history=history+[(currentPoint, currentLength)]
    currentItem=fullGraphDict[currentPoint]
    if(currentItem["isDoor"]):
      #COMPORTATI DA DOOR
      if currentItem.get("takeAll")!=None:
        #Porta Take all
        newKeysTaken=keysTaken.copy()
        for element in currentItem["takeAll"][0]:
          newKeysTaken.add(element)
        currentLength=currentLength+currentItem["takeAll"][2]
        if len(newKeysTaken)==11:
          finalLength=currentLength+currentItem["takeAll"][1]-currentItem["takeAll"][2]
          if(currentMaxFound>finalLength):
            currentMaxFound=finalLength
            fastHistory=history
          # print("finito in", currentLength+currentItem["singleSide"]["WUS"], "ed il min è", currentMaxFound, "ho visitato", visited)
          continue
        for element, value in currentItem["singleSide"].items():
          if element in visited:
            continue
          if element.islower():
            heapq.heappush(border, (currentLength+value, element, currentPoint, newKeysTaken, visited, history))
          if element.isupper() and all(x.lower() in newKeysTaken for x in element):
            heapq.heappush(border, (currentLength+value, element, currentPoint, newKeysTaken, visited, history))
      else:
        # PORTA NORMALE
        if(previousPoint) in currentItem["left"]:
          checkSide=currentItem["right"]
        else:
          checkSide=currentItem["left"]
        for element, value in checkSide.items():
          if element in visited:
            continue
          if element.islower():
            heapq.heappush(border, (currentLength+value, element, currentPoint, keysTaken, visited, history))
          if element.isupper() and all(x.lower() in keysTaken for x in element):
            heapq.heappush(border, (currentLength+value, element, currentPoint, keysTaken, visited, history))
    else:
      #Comportati da key
      newKeysTaken=keysTaken.copy()
      newKeysTaken.add(currentPoint)
      if len(newKeysTaken)==11:
        if currentMaxFound>currentLength:
          currentMaxFound=currentLength
        fastHistory=history
        # print("finito in", currentLength+currentItem["WUS"], "ed il min è", currentMaxFound, "ho visitato", visited)
        continue

      for element, value in currentItem.items():
        if element in visited:
          continue
        if element.islower():
          heapq.heappush(border, (currentLength+value, element, currentPoint, newKeysTaken, visited, history))
        if element.isupper() and all(x.lower() in newKeysTaken for x in element):
          heapq.heappush(border, (currentLength+value, element, currentPoint, newKeysTaken, visited, history))

  print(fastHistory)
  return currentMaxFound

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


  # checkWhatYouCanReach(start, walls, doors, keys, grid, (start,0))

  graphDict, fakeDoors=buildGraphDictFromDoors(doors, grid, walls, keys, [])
  doorNames=set(graphDict.keys())
  
  startList={k:v for k,v in checkWhatYouCanReach(start, walls, doors, keys, grid, grid[start], 0).items() if k not in doorNames and k not in fakeDoors}
  print("@",startList)


  fakeDoors=set(fakeDoors)
  graphKeyDict=buildGraphKeyDict(keys, walls, doors, grid, fakeDoors)

  takeAll=[]
  for doorName, value in graphDict.items():
    for side in ["left", "right"]:
      if thingInCommonArray(value[side], doorNames):
        continue
      else:
        takeAll.append((doorName, list(value[side]), side))

  for element in takeAll:
    singleRun, goingBack=findPathTakingAll(element[0], element[1], element[2], graphDict, graphKeyDict)
    graphDict[element[0]]["takeAll"]=(element[1], singleRun, goingBack)
    for point in element[1]:
      graphKeyDict.pop(point)

  updateGraphDictAfterTakingAll(graphDict)
  joinContiguosDoors(graphDict, graphKeyDict)

  fullGraphDict={}
  for k,v in graphDict.items():
    fullGraphDict[k]=v
    fullGraphDict[k]["isDoor"]=True
  
  for k,v in graphKeyDict.items():
    fullGraphDict[k]=v
    fullGraphDict[k]["isDoor"]=False

  stampaGraph(fullGraphDict)
  startPoints=startList
  solutions=[]
  for k,v in startPoints.items():
    solutions.append(exploreMaze(k,v, fullGraphDict))
  print(solutions)
  fastWus=min(solutions)


  if(len(graphDict["WUS"]["left"])<len(graphDict["WUS"]["right"])):
    check=graphDict["WUS"]["left"]
  else:
    check=graphDict["WUS"]["right"]
  wusPoints={}
  for k,v in check.items():
    if k.isupper():
      continue
    else:
      wusPoints[k]=v
  solutions=[]
  for k,v in wusPoints.items():
    solutions.append(exploreMazeFinal(k,v,fullGraphDict))
  print(solutions)
  return fastWus+min(solutions)

print(solve())

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# evaluateTime(timeElapse)