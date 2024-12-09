from utilityz import *

def parseRows(rows):
  row=rows[0]
  state=0
  singleArray=[]
  idx=0
  for element in row:
    quantity=int(element)
    if state==0:
      singleArray.append((quantity, idx, False))
      idx=idx+1
      state=1
    else:
      singleArray.append((quantity, idx, True))
      state=0
  singleArray.append((1, idx+1, True))
  return singleArray

def compact(arrayFull, arrayFree):
  idx=1
  while(len(arrayFree)>1):
    quantity, currentID=arrayFull.pop()
    while(arrayFree[0]==0):
      arrayFree.pop(0)
      idx=idx+1
    if(quantity<arrayFree[0]):
      arrayFull.insert(idx,(quantity, currentID))
      arrayFree[0]=arrayFree[0]-quantity
      arrayFree[-1]=arrayFree[-1]+quantity
      idx=idx+1
    elif(quantity==arrayFree[0]):
      arrayFull.insert(idx,(quantity, currentID))
      arrayFree.pop(0)
      arrayFree[-1]=arrayFree[-1]+quantity
      idx=idx+2
    else:
      arrayFull.insert(idx, (arrayFree[0], currentID))
      arrayFull.append((quantity-arrayFree[0], currentID))
      arrayFree.pop(0)
      arrayFree[-1]=arrayFree[-1]+arrayFree[0]
      idx=idx+2
  return arrayFull

def compactB(stateArray):
  # stampaSingleArray(stateArray)
  elementToNavigate=reversed([k for k in stateArray if k[2]==False])
  for element in elementToNavigate:
    quantity=element[0]
    idValue=element[1]
    indexToMove=stateArray.index((quantity, idValue, False))
    tempIdx=0

    while(True):
      if(stateArray[tempIdx][2]==False):
        tempIdx=tempIdx+1
        continue
      if(tempIdx>indexToMove):
        break

      # print(stateArray[tempIdx][0], quantity)
      if(quantity<=stateArray[tempIdx][0]):
        # print("uuhhhh")
        stateArray[indexToMove]=(stateArray[indexToMove][0], stateArray[indexToMove][1], True)
        if(stateArray[indexToMove+1][2]==True):
          innerQuantity, _, _=stateArray.pop(indexToMove)
          stateArray[indexToMove]=(stateArray[indexToMove][0]+innerQuantity, stateArray[indexToMove][1], stateArray[indexToMove][2])
        if(stateArray[indexToMove-1][2]==True):
          innerQuantity, _, _=stateArray.pop(indexToMove)
          stateArray[indexToMove-1]=(stateArray[indexToMove-1][0]+innerQuantity, stateArray[indexToMove-1][1], stateArray[indexToMove-1][2])
        # print("inserted", idValue, "per", quantity, "in ", tempIdx)
        stateArray.insert(tempIdx,(quantity, idValue, False))
        if stateArray[tempIdx+1][0]==quantity:
          stateArray.pop(tempIdx+1)
        else:
          stateArray[tempIdx+1]=(stateArray[tempIdx+1][0]-quantity,stateArray[tempIdx+1][1], stateArray[tempIdx+1][2])
        # print(stateArray)
        break
      tempIdx=tempIdx+1
  return stateArray

def checksumB(stateArray):
  idx=0
  ris=0
  for element in stateArray:
    if element[2]==True:
      idx=idx+element[0]
      continue
    for _ in range(element[0]):
      ris=ris+idx*element[1]
      idx=idx+1
  return ris

def checksumA(arrayFull):
  idx=0
  ris=0
  for element in arrayFull:
    for _ in range(element[0]):
      ris=ris+idx*element[1]
      idx=idx+1
  return ris

def solveA():
  rows=getOldAocInput(9)
  stateArray=parseRows(rows)
  arrayFull=list([(x[0], x[1]) for x in stateArray if x[2]==False])
  arrayFree=list([x[0] for x in stateArray if x[2]==True])
  ris=compact(arrayFull, arrayFree)
  return checksumA(ris)

def solveB():
  rows=getOldAocInput(9)
  stateArray=parseRows(rows)
  ris=compactB(stateArray)
  return checksumB(ris)


# print(solve())
# print(solveB())

def timeElapse():
  print(solveA())
  # print(solveB())

evaluateTime(timeElapse)