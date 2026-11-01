from utility import *


directions=[(0,-1), (1,0), (0,1), (-1,0)]
radialDirections=fromDistanceBuildSetOfRadialDirections(1)

directionDic={0:"su", 1:"destra", 2:"giu", 3:"sinistra"}

def solve1():
  rows=openFile("raw.txt")
  grid, _, _=buildGrid(rows)

  current=[x for x,y in grid.items() if y=="@"][0]
  end=[x for x,y in grid.items() if y=="#"][0]
  directionIndex=-1

  found=set()
  found.add(current)

  steps=0
  while(True):
    directionIndex=(directionIndex+1)%4
    tentative=sumTupleValueByValue(current, directions[directionIndex])
    while(tentative in found):
      directionIndex=(directionIndex+1)%4
      tentative=sumTupleValueByValue(current, directions[directionIndex])
    steps=steps+1
    current=tentative
    found.add(current)
    if(current==end):
      return steps
    print(current)

def buildEnds(end):
  ends=set()
  for i in range(4):
    ends.add(sumTupleValueByValue(end, directions[i]))
  return ends

def checkEnds(ends, steps):
  if len(ends)==0:
    return steps
  return 0


def checkValidityAndUpdate(current, directionIndex, found, ends):
  if current in found:
    return False
  plus=(directionIndex+1)%4
  if(sumTupleValueByValue(current, directions[directionIndex-1]) in found and sumTupleValueByValue(current, directions[plus]) in found):
    nextTile=sumTupleValueByValue(current, directions[directionIndex])
    
    if(nextTile in found):
      found.add(current)
      if current in ends:
        ends.remove(current)
    return False
  return True

def fullCheckAround(current, found, ends):
  for i in range(4):
    tentative=sumTupleValueByValue(current, directions[i])
    if(tentative in found):
      continue
    checkValidityAndUpdate(tentative, i, found, ends)


def solve2():
  rows=openFile("raw.txt")
  grid, _, _=buildGrid(rows)

  current=[x for x,y in grid.items() if y=="@"][0]
  end=[x for x,y in grid.items() if y=="#"][0]
  
  ends=buildEnds(end)
  directionIndex=-1

  found=set()
  found.add(current)
  found.add(end)

  steps=0
  while(True):
    fullCheckAround(current, found, ends)
    if checkEnds(ends, steps):
      return steps
    directionIndex=(directionIndex+1)%4
    tentative=sumTupleValueByValue(current, directions[directionIndex])
    while(tentative in found or tentative == end):
      directionIndex=(directionIndex+1)%4
      tentative=sumTupleValueByValue(current, directions[directionIndex])
    steps=steps+1
    current=tentative
    found.add(current)
    if(current in ends):
      ends.remove(current)
      # print("trovato dopo", steps)
      if checkEnds(ends, steps):
        return steps
    # print("sono in", current, "dopo", steps, "sono andato a", directionDic[directionIndex], "devo ancora trovare", ends)

def buildEndsPart3(walls, reachables):
  targets=set()
  for wall in walls:
    for direction in directions:
      tentative= sumTupleValueByValue(wall, direction)
      if tentative in reachables:
        targets.add(tentative)
  return targets

def buildReachables(walls, start, safesX, safesY):
  newSafesX=(safesX[0]-1, safesX[1]+1)
  newSafesY=(safesY[0]-1, safesY[1]+1)
  border=set([start])
  reached=set([start])
  while(border):
    newBorder=set()
    for element in border:
      for direction in directions:
        tentative=sumTupleValueByValue(element, direction)
        if tentative in walls or tentative in reached:
          continue
        if tentative[0] in newSafesX or tentative[1] in newSafesY:
          continue
        reached.add(tentative)
        newBorder.add(tentative)
    border=newBorder
  return reached

def updateGrid(current, walls, sounds, safesX, safesY):
  if current in safesX or current in safesY:
    return
  safes=set()
  startingPoints=[]
  for direction in radialDirections:
    tentative=sumTupleValueByValue(current, direction)
    if(tentative in walls or tentative in sounds):
      continue
    startingPoints.append(tentative)
  for point in startingPoints:
    fastBreak=False
    subSafes=set([point])
    border=set([point])
    while(border):
      newBorder=set()
      for element in border:
        for direction in directions:
          tentative=sumTupleValueByValue(element, direction)
          if(tentative in walls or tentative in sounds or tentative in subSafes):
            continue
          if(tentative in safes or tentative[0] in safesX or tentative[1] in safesY):
            fastBreak=True
            break
          newBorder.add(tentative)
          subSafes.add(tentative)
        if(fastBreak):
          break
      border=newBorder
      if(fastBreak):
        break
    if fastBreak:
      
      safes.update(subSafes)
    else:
      sounds.update(subSafes)

def solve3():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows)

  walls=set([x for x,y in grid.items() if y=="#"])
  start=[x for x,y in grid.items() if y=="@"][0]
  sounds=set([start])
  safesX=(-1, maxX+1)
  safesY=(-1, maxY+1)
  reachables=buildReachables(walls, start, safesX, safesY)
  targets=buildEndsPart3(walls, reachables)
  directionsPart3=[(0,-1),(0,-1),(0,-1),(1,0),(1,0),(1,0),(0,1),(0,1),(0,1),(-1,0),(-1,0),(-1,0)]
  directionIndex=-1
  lenDirections=len(directionsPart3)
  current=start
  steps=0
  while(targets):
    steps=steps+1
    directionIndex=(directionIndex+1)%lenDirections
    tentative=sumTupleValueByValue(current, directionsPart3[directionIndex])
    while(tentative in walls or tentative in sounds):
      directionIndex=(directionIndex+1)%lenDirections
      tentative=sumTupleValueByValue(current, directionsPart3[directionIndex])
    sounds.add(tentative)
    current=tentative
    targets.discard(tentative)
    minG=minGrid(grid)
    maxG=maxGrid(grid)
    safesX=(minG[0]-1, maxG[0]+1)
    safesY=(minG[1]-1, maxG[1]+1)
    updateGrid(tentative, walls, sounds, safesX, safesY)
    targets.difference_update(sounds)

    for element in sounds:
      grid[element]="+"
      grid[current]="@"

    # print("step", steps)
    # stampaGrid(grid)
    # print()

    
  return steps


print(solve3())