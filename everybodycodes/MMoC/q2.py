from utility import *


directions=[(0,-1), (1,0), (0,1), (-1,0)]

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

print(solve2())