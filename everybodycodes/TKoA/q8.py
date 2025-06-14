from utility import *

def solve():
  blocksAvailable=int(openFile("raw.txt")[0])

  layerBlocksNeeded=1
  while(blocksAvailable>0):
    blocksAvailable=blocksAvailable-layerBlocksNeeded
    layerBlocksNeeded=layerBlocksNeeded+2
  
  missingBlocks=-blocksAvailable
  layerBlocksNeeded=layerBlocksNeeded-2

  return missingBlocks*layerBlocksNeeded


def solve2():
  numbOfNullPointerPriests=int(openFile("raw.txt")[0])
  priestAcolytes=1111
  blocksAvailable=20240000

  blocksAvailable=blocksAvailable-1

  layerWidth=1
  layerThickness=1

  while(blocksAvailable>0):
    layerWidth=layerWidth+2
    layerThickness=(layerThickness*numbOfNullPointerPriests)%priestAcolytes
    blocksAvailable=blocksAvailable-layerWidth*layerThickness
  

  missingBlocks=-blocksAvailable
  return missingBlocks*layerWidth


def calculateBlocksNeeded(structure, npPriests, priestAcolytes):
  lenStructure=len(structure)
  removeBlocks=0
  for idx in range(1,lenStructure-1):
    removeBlocks=removeBlocks+npPriests*lenStructure*structure[idx]%priestAcolytes

  return sum(structure)-removeBlocks

def solve3():
  numbOfNullPointerPriests=int(openFile("raw.txt")[0])
  priestAcolytes=10
  blocksAvailable=202400000

  layerThickness=1
  structure=[1]
  while(True):
    layerThickness=(layerThickness*numbOfNullPointerPriests)%priestAcolytes
    layerThickness=layerThickness+priestAcolytes
    structure=[x+layerThickness for x in structure]
    structure.insert(0, layerThickness)
    structure.append(layerThickness)
    blocksNeeded=calculateBlocksNeeded(structure, numbOfNullPointerPriests, priestAcolytes)
    if(calculateBlocksNeeded(structure, numbOfNullPointerPriests, priestAcolytes)>blocksAvailable):
      break
  
    
    
  

  missingBlocks=-blocksAvailable+blocksNeeded
  return missingBlocks


# print(solve())
# print(solve2())
print(solve3())



