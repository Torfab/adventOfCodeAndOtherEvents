from utility import *
import heapq

directions={(1,0):[(1,0), (0,-1), (0,1)], (-1,0):[(-1,0), (0,-1), (0,1)], (0,1): [(0,1), (1,0), (-1,0)], (0,-1): [(0,-1), (1,0), (-1,0)]}

#part 2 e part 3 risolta pen & paper trovando il ciclo migliore e la strada a li in avanti, mi riprometto di guardare qualche altro sviluppatore più bravo e vedere come lo ha implementato

def followLine(cell, movement, walls, sulfurs, mainRoad):
  step=1
  sulfursTaken=[]
  current=cell
  while (current[1]!=mainRoad):
    
    step=step+1
    for d in directions[movement]:
      tentative=sumTupleValueByValue(d, current)
      if tentative not in walls:
        current=tentative
        movement=d
        if current in sulfurs:
          sulfursTaken.append(current)
        break
    
  # print("found main road after", step)
  return current, step, sulfursTaken


def buildRoads(start, end, sulfurs, walls):
  startRow=start[1]
  cell=start

  realRoads={}

  while cell!=end:

    tentative=sumTupleValueByValue(cell, (0,1))
    if tentative not in walls:
      subCell, subSteps, subSulfur=followLine(tentative, (0,1), walls, sulfurs, startRow)
      realRoads[cell]=realRoads.get(cell, {})
      realRoads[cell][subCell]=realRoads[cell].get(subCell, [])
      realRoads[cell][subCell].append((subSteps, subSulfur))

    tentative=sumTupleValueByValue(cell, (0,-1))
    if tentative not in walls:
      subCell, subSteps, subSulfur=followLine(tentative, (0,-1), walls, sulfurs, startRow)
      realRoads[cell]=realRoads.get(cell, {})
      realRoads[cell][subCell]=realRoads[cell].get(subCell, [])
      realRoads[cell][subCell].append((subSteps, subSulfur))
      
    #check top and down

    #check forawrd  
    tentative=sumTupleValueByValue(cell, (1,0))
    if tentative == end:
      realRoads[cell]=realRoads.get(cell, {})
      realRoads[cell][tentative]=[(1, [])]
      realRoads[tentative]={}
      realRoads[tentative][cell]=[(1, [])]
      return realRoads
    else:
      realRoads[cell]=realRoads.get(cell, {})
      realRoads[cell][tentative]=[(1, [])]
      cell=tentative

    tentative=sumTupleValueByValue(cell, (-1,0))
    if tentative == end:
      realRoads[cell]=realRoads.get(cell, {})
      realRoads[cell][tentative]=[(1, [])]
      realRoads[tentative]={}
      realRoads[tentative][cell]=[(1, [])]
      return realRoads
    else:
      realRoads[cell]=realRoads.get(cell, {})
      realRoads[cell][tentative]=[(1, [])]

  return realRoads

def buildShortcuts(start, sulfurs, realRoads, end=None, me=None):
  print()
  print("STO FACENDO", me)
  if(me):
    sulfurs=[x for x in sulfurs if x!=me]
  allFindables=len(sulfurs)*2
  if (end):
    allFindables=allFindables+1
  print(len(sulfurs), sulfurs)
  border=[]
  heapq.heappush(border, (0, start))
  foundRoad={}
  visited=set()
  founds=0
  print("DAJEMBARE", allFindables)
  while (founds<allFindables):
    # print(foundRoad)
    currentStep, currentCell=heapq.heappop(border)
    if currentCell in visited:
      continue
    if currentCell==end:
      foundRoad["end"]=[(currentStep, "end")]
      founds=founds+1
    visited.add(currentCell)
    for key, value in realRoads[currentCell].items():
      for road in value:
        if road[1]:
          for element in road[1]:
            if element==me:
              print("uh")
              continue
          # foundRoad[road[0]]=road[1]
            foundRoad[element]=foundRoad.get(element,[])
            foundRoad[element].append((road[0]+currentStep, key))
            founds=founds+1
        heapq.heappush(border, (currentStep+road[0], key))
  print()
  print("sulfurs", sulfurs)
  print("foudRoad", foundRoad)
  return foundRoad

def solve():
  rows=openFile("test.txt")
  grid, maxX, maxY=buildGrid(rows)

  start=[x for x,y in grid.items() if y=="S"][0]
  end=[x for x,y in grid.items() if y=="E"][0]
  print(end)
  sulfurs=[x for x,y in grid.items() if y=="@"]
  walls=set([x for x,y in grid.items() if y=="#"])
  additionalWalls=cageGridWithWalls((maxX,maxY))
  walls=walls|additionalWalls

  realRoads=buildRoads(start, end, sulfurs, walls)

  # print(realRoads)

  startShorcut=buildShortcuts(start, sulfurs, realRoads)
  allShortcut={}
  allShortcut[start]=startShorcut

  for element, value in startShorcut.items():
    for stepPosition in value:
      print(element)
      step, position=stepPosition
      theShortCut=buildShortcuts(position, sulfurs, realRoads, end, element)
      allShortcut[position]=theShortCut
  
  print()
  print()

  print(len(allShortcut))

  #FINALMENTE DJAKSTRA

  border=[]

  heapq.heappush(border, (0, start, frozenset()))

  visited=set()

  minSolution=float("inf")

  while(border):
    currentStep, currentCell, status=heapq.heappop(border)
    print(currentStep, currentCell)
    if(currentStep>minSolution):
      print("sono arrivato a", currentStep, "quindi sono sicuro di", minSolution)
      return minSolution
    
    if len(status)==len(sulfurs):
      print("FINITO", currentStep, currentCell, allShortcut[currentCell]["end"][0][0])
      print()
      print("mi trovo a ", currentCell, "secondo me per arrivare a", end, "servono", allShortcut[currentCell]["end"][0][0], "passi")
      print()

      # print(status, sulfurs)
      minSolution=min(minSolution, currentStep+allShortcut[currentCell]["end"][0][0])
      continue
    if((currentCell, status) in visited):
      continue

    for interestPoint, road in allShortcut[currentCell].items():
      if interestPoint in status or interestPoint=="end":
        continue
      else:
        for realRoad in road:
          heapq.heappush(border, (currentStep+realRoad[0], realRoad[1], status| {interestPoint}))


  
  return minSolution

def solve2():
  rows=openFile("test.txt")
  grid, _, _ = buildGrid(rows)


print(solve2())
