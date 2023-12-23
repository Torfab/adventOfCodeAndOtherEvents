from utility import *
import heapq

X1=0
Y1=1
Z1=2
X2=3
Y2=4
Z2=5

def buildBlocks(rows):
  blocks=[]
  for element in rows:
    element=element.replace("~", ",")
    element=[int(x) for x in element.split(",")]
    heapq.heappush(blocks, (min(element[Z1], element[Z2]), element)) 
  return blocks

def countBrinDown(zMin, block, tower):
  zMin=zMin-1
  i=0
  while(zMin>0): 
    i=i+1
    for x in range(block[X1], block[X2]+1):
      for y in range(block[Y1], block[Y2]+1):
        if(tower.get((x,y,zMin))!=None):
          return i-1
    zMin=zMin-1
  return i

def updateTower(countDown, blockId, block, towerGrid, towerBlock):
  towerBlock[blockId]=[]
  for x in range(block[X1], block[X2]+1):
    for y in range(block[Y1], block[Y2]+1):
      for z in range(block[Z1], block[Z2]+1):
        towerGrid[(x,y,z-countDown)]=blockId
        towerBlock[blockId].append((x,y,z-countDown))

def findEssentials(towerBlock, towerGrid):
  essentialTowerSustain=set()

  for k,v in towerBlock.items():

    sustainers=set()
    for coordinates in v:
      found=towerGrid.get((coordinates[0], coordinates[1], coordinates[2]-1))
      if(found!=None and found!=k):
        sustainers.add(towerGrid[(coordinates[0], coordinates[1], coordinates[2]-1)])

    if(len(sustainers)==1):
      essentialTowerSustain.add(list(sustainers)[0])
  return essentialTowerSustain

def checkIfDown(zMin, blocks, towerGrid):

  zMin=zMin-1
  i=0
  while(zMin>0): 
    i=i+1
    for element in blocks:
      if (towerGrid.get((element[0], element[1], zMin))!=None):
        return min(1, i-1), i-1
    zMin=zMin-1
  return min(1, i), i

def updateTowerB(countDown, blocks, blockId, towerGrid):
  for element in blocks:
    towerGrid[(element[0],element[1],element[2]-countDown)]=blockId

def countBricksBringDown(towerBlocks:dict, element):

  towerGrid={}
  blockId=0
  result=0
  for k,v in towerBlocks.items():
    if(k==element):
      continue
    blockId=blockId+1

    zMin= min(v, key=lambda x: x[2])[2]
    partialResult, bricksDown=checkIfDown(zMin, v, towerGrid)
    updateTowerB(bricksDown, v, blockId, towerGrid)
    result=result+partialResult

  return result

def solve(part):
  rows=getOldAocInput(22)
  blocks=buildBlocks(rows)

  towerGrid={}
  towerBlock={}
  blockId=0
  while(len(blocks)>0):
    blockId=blockId+1
    zMin, block=heapq.heappop(blocks)
    countDown=countBrinDown(zMin, block, towerGrid)
    updateTower(countDown, blockId, block, towerGrid, towerBlock)
  
  essentialTowerSustain= findEssentials(towerBlock, towerGrid)

  if(part=="a"):
    return len(towerBlock)-len(essentialTowerSustain)
  elif(part=="b"):
    result=0
    for element in essentialTowerSustain:
      result=result+countBricksBringDown(towerBlock, element)
    return result


print(solve("a"))
print(solve("b"))


