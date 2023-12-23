from utility import *

directions={"^":(0,-1), ">":(1,0), "v":(0,1), "<":(-1,0)}

maxX=None
maxY=None

def parseRows(rows):
  grid={}

  for y in range(len(rows)):
    for x in range(len(rows[0])):
      grid[(x,y)]=rows[y][x]
  global maxX
  global maxY
  maxX=max(element[0] for element in grid)
  maxY=max(element[1] for element in grid)
  return grid

def stampaGrid(grid):
  for y in range(maxY+1):
    for x in range(maxX+1):
      print(grid[(x,y)], end="")
    print()

def findRoute(currentPoint, marked, endPoint, maxResult, grid):

  while(currentPoint!=endPoint):
    marked.add(currentPoint)

    #slope behaviour
    for k in directions.keys():
      if(currentPoint==k):
        currentPoint=sumTupleValueByValue(currentPoint, directions[k])
        marked.add(currentPoint)

    tentativePositions=[]

    for direction in directions.values():

      tentativePosition=sumTupleValueByValue(currentPoint, direction)
      symbol=grid[tentativePosition]

      if(symbol=="#" or tentativePosition in marked):
        continue

      elif (symbol=="."):
        tentativePositions.append(tentativePosition)
      elif (symbol=="v"):
        if(direction==(0,-1)):
          continue
        else: 
          tentativePositions.append(tentativePosition)
      elif (symbol=="<"):
        if(direction==(1,0)):
          continue
        else:
          tentativePositions.append(tentativePosition)
      elif (symbol=="^"):
        if(direction==(0,1)):
          continue
        else: 
          tentativePositions.append(tentativePosition)
      elif (symbol==">"):
        if(direction==(-1,0)):
          continue
        else: 
          tentativePositions.append(tentativePosition)
      
    if(len(tentativePositions)==0):
      return
    
    #non sbranchio per la strada principale
    currentPoint=tentativePositions[0]
    
    if(len(tentativePositions)>1):
      for element in tentativePositions[1:]:
        findRoute(element, marked.copy(), endPoint, maxResult, grid)
      
  # print("found route", len(marked))
  if(maxResult[0]<len(marked)):
    maxResult[0]=len(marked)
    # print("nuovo massimo", len(marked))
  return

def findRouteNoSlopes(grid, currentPoint, lastPosition, myGraph):
  i=0
  while(currentPoint not in myGraph.keys()):
    
    i=i+1

    for direction in directions.values():

      tentativePosition=sumTupleValueByValue(currentPoint, direction)
      
      if(grid[tentativePosition]!="#" and tentativePosition!=lastPosition):
        lastPosition=currentPoint
        currentPoint=tentativePosition
        break

  return i+1, currentPoint
        
  

def buildGraph(grid, startPoint):
  myGraph={}
  border=[]
  marked=set()

  border.append(startPoint)

  while(len(border)>0):
    currentPosition=border.pop(0)
    marked.add(currentPosition)

    tentativePositions=[]

    count=0
    for direction in directions.values():
      tentativePosition= sumTupleValueByValue(currentPosition, direction)
      if(grid[tentativePosition]!="#"):
        count=count+1
      if(grid[tentativePosition] != "#" and tentativePosition not in marked):
        tentativePositions.append(tentativePosition)
    
    if(count>2):
      #diramazione
      myGraph[currentPosition]=[]
  
    for element in tentativePositions:
      border.append(element)

  myGraph[(1,0)]=[]
  myGraph[(maxX-1, maxY)]=[]
    
  for element in myGraph.keys():

    tentativePositions=[]

    
    for direction in directions.values():
      tentativePosition=sumTupleValueByValue(element, direction)
      if(grid[tentativePosition]=="#"):
        continue
      else:
        tentativePositions.append(tentativePosition)
    
    for route in tentativePositions:
      value, connection = findRouteNoSlopes(grid, route, element , myGraph)
      myGraph[element].append({"value": value, "endPoint": connection})
    
  return myGraph

def stampaGraph(graph):
  for k,v in graph.items():
    print(k,v)

def findRouteGraph(myGraph, currentNode, endNode, marked, result, maxResult):
  if(currentNode==endNode):
    if(maxResult[0]<result):
      maxResult[0]=result
    return

  marked.add(currentNode)

  for newNode in myGraph[currentNode]:
    if(newNode["endPoint"] in marked):
      continue

    findRouteGraph(myGraph, newNode["endPoint"], endNode, marked.copy(), result+newNode["value"], maxResult)

  return

def solve(part):
  rows=getOldAocInput(23)
  grid=parseRows(rows)

  #chiudo la griglia per evitare la fuoriuscita del path
  grid[(1,-1)]="#"
  grid[(maxX-1, maxY+1)]="#"
  startPoint=(1,0)
  endPoint=(maxX-1, maxY)

  if(part=="a"):
    maxResult=[0]
    findRoute(startPoint, set(), endPoint, maxResult, grid)
    return maxResult[0]

  if(part=="b"):
    for element in grid.keys():
      if (grid[element] in directions.keys()):
        grid[element]="."


    myGraph= buildGraph(grid, startPoint)
    # stampaGraph(graph)
    
    marked=set()
    marked.add((1,0))

    currentNode=myGraph[startPoint][0]["endPoint"]
    endNode=myGraph[endPoint][0]["endPoint"]

    result=0
    result=result+myGraph[startPoint][0]["value"]
    result=result+myGraph[endPoint][0]["value"]

    maxResult=[0]

    findRouteGraph(myGraph, currentNode, endNode, marked, result, maxResult)

    return maxResult[0]

print(solve("a"))
print(solve("b"))
