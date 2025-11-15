from utility import *

directions=[(2,1), (2,-1), (-2,1), (-2,-1), (1, 2), (-1, 2), (1, -2), (-1,-2)]

def parseRows(rows):
  drake=(-1,-1)
  sheeps=[]
  for idxRow, row in enumerate(rows):
    for idxColumn, c in enumerate(row):
      if(c=="D"):
        drake=(idxColumn, idxRow)
      if(c=="S"):
        sheeps.append((idxColumn, idxRow))
  return drake, sheeps, idxRow, idxColumn

def parseRows2(rows):
  drake=(-1,-1)
  sheeps=set()
  bushes=set()
  for idxRow, row in enumerate(rows):
    for idxColumn, c in enumerate(row):
      if(c=="D"):
        drake=(idxColumn, idxRow)
      if(c=="S"):
        sheeps.add((idxColumn, idxRow))
      if(c=="#"):
        bushes.add((idxColumn, idxRow))

def parseRows3(rows):
  drake=(-1,-1)
  sheeps=[]
  bushes=set()
  for idxRow, row in enumerate(rows):
    for idxColumn, c in enumerate(row):
      if(c=="D"):
        drake=(idxColumn, idxRow)
      if(c=="S"):
        sheeps.append((idxColumn, idxRow))
      if(c=="#"):
        bushes.add((idxColumn, idxRow))
      
  return drake, sheeps, bushes, idxRow, idxColumn

def solve():
  rows=openFile("raw.txt") 
  drake, sheeps, maxRow, maxColumn=parseRows(rows)

  drakePositions=[(drake)]
  alreadyBeen=set()

  for _ in range(4):
    newdrakePositions=[]
    for element in drakePositions:
      for d in directions:
        tentative=sumTupleValueByValue(element, d)
        if(tentative[0]<0 or tentative[0]>maxColumn or tentative[1]<0 or tentative[1]>maxRow):
          continue
        if(tentative in alreadyBeen):
          continue
        else:
          alreadyBeen.add(tentative)
          newdrakePositions.append(tentative)
          
    drakePositions=newdrakePositions

  count=0
  for p in alreadyBeen:
    if p in sheeps:
      count=count+1

  return count



def solve2():
  rows=openFile("raw.txt") 
  drake, sheeps, bushes, maxRow, maxColumn=parseRows2(rows)

  drakePositions=set()
  drakePositions.add(drake)

  eaten=0
  for _ in range(20):
    newdrakePositions=set()
    for element in drakePositions:
      for d in directions:
        tentative=sumTupleValueByValue(element, d)
        if(tentative[0]<0 or tentative[0]>maxColumn or tentative[1]<0 or tentative[1]>maxRow):
          continue
        if(tentative not in bushes):
          if tentative in sheeps:
            eaten=eaten+1
            sheeps.remove(tentative)
        newdrakePositions.add(tentative)
    drakePositions=newdrakePositions

    newSheeps=set()
    for sheep in sheeps:
      tentative=sumTupleValueByValue(sheep, (0,1))
      if(tentative[1]>maxRow):
        continue

      if(tentative in bushes):
        newSheeps.add(tentative)
        continue
      if(tentative in drakePositions):
        eaten=eaten+1
        continue
      newSheeps.add(tentative)
    sheeps=newSheeps
  return eaten
  # return rows

def solve3():
  rows=openFile("raw.txt") 
  drake, sheeps, bushes, maxRow, maxColumn=parseRows3(rows)

  drakePositions=set()
  drakePositions.add(drake)

  status={(drake, sheeps[0], sheeps[1], sheeps[2], sheeps[3], sheeps[4]):1}
  print(status)

  while(True):
    newStatus={}
    for state, multiplicity in status.items():
      for d in directions:
        tentative=sumTupleValueByValue(state[0], d)
        if(tentative[0]<0 or tentative[0]>maxColumn or tentative[1]<0 or tentative[1]>maxRow):
          continue
        if(tentative not in bushes):
          if tentative in sheeps:
            newStatus[(d,dppasdfmopasfopasd,pfa,fopsefop)]
            sheeps.remove(tentative)
        newdrakePositions.add(tentative)
    drakePositions=newdrakePositions

    newSheeps=set()
    for sheep in sheeps:
      tentative=sumTupleValueByValue(sheep, (0,1))
      if(tentative[1]>maxRow):
        continue

      if(tentative in bushes):
        newSheeps.add(tentative)
        continue
      if(tentative in drakePositions):
        eaten=eaten+1
        continue
      newSheeps.add(tentative)
    sheeps=newSheeps
  return eaten
  # return rows

print(solve3())

