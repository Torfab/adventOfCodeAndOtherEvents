from utility import *
import functools

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

  return drake, sheeps, bushes, idxColumn, idxRow

def parseRows3(rows):
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

def findSafeSpots(rows):
  grid, maxCol, maxRow = buildGrid(rows)
  safeSpots=[]
  for a in range(maxCol+1):
    currentRow=maxRow
    while (grid.get((a,currentRow), '.')=="#"):
      currentRow=currentRow-1
      
    safeSpots.append((a, currentRow+1))
  return(safeSpots)

def solveBSF():
  rows=openFile("raw.txt") 
  drake, sheeps, bushes, maxRow, maxColumn=parseRows3(rows)


  result=0

  safeSpots=findSafeSpots(rows)
  # print(safeSpots)

  listState=[drake]+sheeps
  status={tuple(listState):1}

  lenSheep=len(sheeps)


  sheepMap={}
  for idx, sheep in enumerate(sheeps):
    sheepMap[sheep[0]]=idx+1

  while(len(status)>0):
    newStatus={}
    for state, multiplicity in status.items():
      moved=False
      for idx in range(lenSheep):
        if(state[idx+1]==(-1,-1)):
          continue
        tentative = sumTupleValueByValue(state[idx+1], (0,1))
        if(tentative in safeSpots):
          moved=True
          continue
        if tentative==state[0] and tentative not in bushes:
          continue
        else:
          moved=True
          listedState=list(state)
          listedState[idx+1]=tentative
          newStatus[tuple(listedState)]=newStatus.get(tuple(listedState), 0)+multiplicity
      if(moved==False):
        newStatus[state]=newStatus.get(state,0) + multiplicity
    status=newStatus
    # print(len(status), "post scappati")
    newStatus={}
    for state, multiplicity in status.items():
      for d in directions:
        tentative=sumTupleValueByValue(state[0], d)
        if(tentative[0]<0 or tentative[0]>maxColumn or tentative[1]<0 or tentative[1]>maxRow):
          continue
        listState=list(state)
        if(tentative not in bushes and tentative in listState[1:]):
          columnTaken=tentative[0]
          listState[sheepMap[columnTaken]]=(-1,-1)
          win=True
          for idx in range(lenSheep):
            if(listState[idx+1]!=(-1,-1)):
              win=False
          if(win):
            result=result+multiplicity
            continue
          else:
            listState[0]=tentative
            newStatus[tuple(listState)]=newStatus.get(tuple(listState), 0)+multiplicity
            continue
        listState[0]=tentative
        newStatus[tuple(listState)]=newStatus.get(tuple(listState), 0)+multiplicity
    status=newStatus

  return result


@functools.cache
def howManyVictories(drake, sheeps, bushes, safeSpots, maxRow, maxColumn, turn):
  result=0
  if turn=="S":
    moved=False
    for idx, sheep in enumerate(sheeps):
      tentative=sumTupleValueByValue(sheep, (0,1))
      if(tentative in safeSpots):
        moved=True
        continue
      elif(tentative==drake and tentative not in bushes):
        continue
      else:
        moved=True
        listSheeps=list(sheeps)
        listSheeps[idx]=tentative
        result=result+howManyVictories(drake, tuple(listSheeps), bushes, safeSpots, maxRow, maxColumn, "D")
    if moved==False:
      result=result+howManyVictories(drake, sheeps, bushes, safeSpots, maxRow, maxColumn, "D")
  else:
    for d in directions:
      tentative=sumTupleValueByValue(drake, d)
      if tentative[0]<0 or tentative[0]>maxColumn or tentative[1]<0 or tentative[1]>maxRow:
        continue
      if tentative in bushes:
        result=result+howManyVictories(tentative, sheeps, bushes, safeSpots, maxRow, maxColumn, "S")
      else:
        if tentative in sheeps:
          listSheeps=list(sheeps)
          listSheeps.remove(tentative)
          if(len(listSheeps))==0:
            result=result+1
          else:
            result=result+howManyVictories(tentative, tuple(listSheeps), bushes, safeSpots, maxRow, maxColumn, "S")
        else:
          result=result+howManyVictories(tentative, sheeps, bushes, safeSpots, maxRow, maxColumn, "S")


  return result


def solveDSF():
  
  rows=openFile("raw.txt") 
  drake, sheeps, bushes, maxRow, maxColumn=parseRows3(rows)
  sheeps=tuple(sheeps)
  safeSpots=tuple(findSafeSpots(rows))
  bushes=tuple(bushes)

  vic=howManyVictories(drake, sheeps, bushes, safeSpots, maxRow, maxColumn, "S")


  return vic

# print(solveBSF())
# print(solveDSF())

