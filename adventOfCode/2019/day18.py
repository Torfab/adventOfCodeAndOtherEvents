from utilityz import *

directions=fromDistanceBuildSetOfDirections(1)

def checkWhatYouCanReach(start, walls, doors, keys, grid, toPrint):
  visited=set()
  border=[(start)]
  path=0
  # result={}
  result=[]
  while(border):
    path=path+1
    newBorder=[]
    while(border):
      currentPoint=border.pop()
      if currentPoint in visited:
        continue
      if currentPoint in keys:
        # result[grid[currentPoint]]=path-1
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
  fakeDoors=[]

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
      print(grid[element], resultList)
      if len(resultList)==0:
        fakeDoors.append(grid[element])
        isFake=True
      item[going]=resultList
      if(going=="left"):
        going="right"
    if not isFake:
      graphDict[grid[element]]=item
  
  foundNewFakeDoor=False
  while not foundNewFakeDoor:
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
    fakeDoors=fakeDoors+newFakeDoors
  
  print(fakeDoors)
  print(len(graphDict))



    

  return graphDict

print(solve())

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# evaluateTime(timeElapse)