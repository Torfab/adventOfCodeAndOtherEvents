from utility import *

thisRotation=[(0,0), (1,9), (0,9), (1,9)]

# I need it jsut to handle also the example
# The only part that is slow is the first comprehension
# I can improve it by using only borders and not full grid rotation
# But i decided that's enough for the day, and it's slow but not terrible
size=0

# on chainablecheck, the 4 elements means:
# 1 dimension to consider
# 2 dimension to check
# 3 value to check on correct element
# 4 value to check on tenative element
directionDict={(0,1):(0,1,9,0), (0,-1): (0,1,0,9), (1,0): (1,0,9,0), (-1,0):(1,0,0,9)}

def parseInput(rows):
  state="title"
  rowIdx=0
  grids={}
  while(rowIdx<len(rows)):
    if state=="title":
      rowSplitted=rows[rowIdx].split(" ")
      key=int(rowSplitted[1][:-1])
      rowIdx=rowIdx+1
      state="grid"
    elif state=="grid":
      grid, _, _=buildGrid(rows[rowIdx:rowIdx+10])
      grids[key]=grid
      rowIdx=rowIdx+11
      state="title"
  return grids

def checkIfPairable(rightSide, keyParent, grids):

  for key, grid in grids.items():
    if key==keyParent:
      continue
    for _ in range(2):
      for _ in range(4):
        subGridKeys=[k[1] for k in grid.keys() if k[0]==0]
        subGridKeys.sort()
        if subGridKeys==rightSide:
          return 1
        grid=rotateGrid90(grid, (9,9))
      grid=flipGrid(grid, (9,9))
  return 0

def comprehensionGrids(grids):
  keyGrids=list(grids.keys())
  ris=1
  edges=[]
  vertex=[]
  middle=[]
  for key in keyGrids:
    currentGrid=grids[key]
    sidesChainable=0
    for _ in range(4):
      rightSide=[k[1] for k in currentGrid.keys() if k[0]==9]
      rightSide.sort()
      sidesChainable=sidesChainable+checkIfPairable(rightSide, key, grids)
      currentGrid=rotateGrid90(currentGrid, (9,9))
    if(sidesChainable==2):
      vertex.append(key)
      ris=ris*key
    elif(sidesChainable==3):
      edges.append(key)
    else:
      middle.append(key)
  return ris, vertex, edges, middle

#borderTuple parameters: direction
def checkIfChainable(firstPiece, secondPieceDict, borderTuple):
  rightPartFirstPiece=[k[directionDict[borderTuple][0]] for k in firstPiece if k[directionDict[borderTuple][1]]==directionDict[borderTuple][2]]
  rightPartFirstPiece.sort()
  for flip in range(2):
    for keyRotation in range(4):
      partToCheckSecondPiece=[k[directionDict[borderTuple][0]] for k in secondPieceDict.keys() if k[directionDict[borderTuple][1]]==directionDict[borderTuple][3]]
      partToCheckSecondPiece.sort()
      # print(rightPartFirstPiece, partToCheckSecondPiece)
      if rightPartFirstPiece==partToCheckSecondPiece:
        return True, keyRotation, flip
      secondPieceDict=rotateGrid90(secondPieceDict, (9,9))
    secondPieceDict=flipGrid(secondPieceDict, (9,9))
  return False, -1, -1

def orientaGrid(grid, rotation, flip):
  if flip==1:
    grid=flipGrid(grid)
  for _ in range(rotation):
    grid=rotateGrid90(grid, (9,9))
  return grid

def updateGridAndFindFirstTwo(grids, fullPicture, vertex, edges):
  currentSlot=(0,0)
  fullPicture[(0,0)]=vertex[0]
  rotation=0
  firstGrid=grids[vertex[0]]
  while(rotation<4):
    candidates=[]
    firstPiece=firstGrid.keys()
    for key in edges:
      secondPieceDict=grids[key]
      isChainable, chainRotation, chainFlip=checkIfChainable(firstPiece, secondPieceDict, (1,0))
      if(isChainable):
        candidates.append((key, chainRotation, chainFlip))
    if(len(candidates)==1):
      break
    firstGrid=rotateGrid90(firstGrid, (9,9))
    rotation=rotation+1
  # I rotate first pieces and right piece
  grids[vertex[0]]=firstGrid
  trovatoKey, trovatoRotation, trovatoFlip=candidates[0]
  grids[trovatoKey]=orientaGrid(grids[trovatoKey], trovatoRotation, trovatoFlip)
  currentSlot=sumTupleValueByValue(currentSlot, (1,0))
  fullPicture[currentSlot]=trovatoKey
  vertex.remove(fullPicture[(0,0)])
  edges.remove(fullPicture[(1,0)])

def updateGridAndFindFirstVertical(grids, fullPicture, edges):
  gridLeftKeys=grids[fullPicture[(0,0)]].keys()
  directions=[(0,1), (0,-1)]
  candidates=[]
  for d in directions:
    for key in edges:
      secondPieceDict=grids[key]
      isChainable, chainRotation, chainFlip=checkIfChainable(gridLeftKeys, secondPieceDict, d)
      if(isChainable):
        candidates.append((key, chainRotation, chainFlip))
    if len(candidates)==1:
      correctD=d
      break
  trovatoKey, trovatoRotation, trovatoFlip=candidates[0]
  grids[trovatoKey]=orientaGrid(grids[trovatoKey], trovatoRotation, trovatoFlip)
  fullPicture[d]=trovatoKey
  edges.remove(trovatoKey)

  return correctD


def updateGridAndFindFullRow(directionToBuild, grids, fullPicture, bucketEnd, bucketMid):
  current=directionToBuild
  while(current[0]<size-1):

    gridLeftKeys=grids[fullPicture[current]].keys()
    current=sumTupleValueByValue(current,(1,0))
    bucketToCheck=bucketMid
    if(current[0]==size-1):
      bucketToCheck=bucketEnd
    candidates=[]
    for key in bucketToCheck:
      secondPieceDict=grids[key]
      isChainable, chainRotation, chainFlip=checkIfChainable(gridLeftKeys, secondPieceDict, (1,0))
      if(isChainable):
        candidates.append((key, chainRotation, chainFlip))
    trovatoKey, trovatoRotation, trovatoFlip=candidates[0]
    grids[trovatoKey]=orientaGrid(grids[trovatoKey], trovatoRotation, trovatoFlip)
    fullPicture[current]=trovatoKey
    bucketToCheck.remove(trovatoKey)

def updateGridAndFindNextVertical(currentPoint, directionToBuild, grids, fullPicture, bucket):
  gridLeftKeys=grids[fullPicture[currentPoint]].keys()
  currentPoint=sumTupleValueByValue(currentPoint, directionToBuild)
  candidates=[]
  for key in bucket:
    secondPieceDict=grids[key]
    isChainable, chainRotation, chainFlip=checkIfChainable(gridLeftKeys, secondPieceDict, directionToBuild)
    if(isChainable):
      candidates.append((key, chainRotation, chainFlip))
  trovatoKey, trovatoRotation, trovatoFlip=candidates[0]
  grids[trovatoKey]=orientaGrid(grids[trovatoKey], trovatoRotation, trovatoFlip)
  fullPicture[currentPoint]=trovatoKey
  bucket.remove(trovatoKey)
  # fullPicture[d]=

def buildFullPictureAndUpdateGrid(grids, vertex, edges, middle):
  fullPicture={}
  updateGridAndFindFirstTwo(grids, fullPicture, vertex, edges)
  updateGridAndFindFullRow((1,0), grids, fullPicture, vertex, edges)
  directionToBuild=updateGridAndFindFirstVertical(grids, fullPicture, edges)
  currentPoint=directionToBuild
  for _ in range(size-3):
    updateGridAndFindFullRow(currentPoint, grids, fullPicture, edges, middle)
    updateGridAndFindNextVertical(currentPoint, directionToBuild, grids, fullPicture, edges)
    currentPoint=sumTupleValueByValue(currentPoint, directionToBuild)
  updateGridAndFindFullRow(currentPoint, grids, fullPicture, edges, middle)
  updateGridAndFindNextVertical(currentPoint, directionToBuild, grids, fullPicture, vertex)
  currentPoint=sumTupleValueByValue(currentPoint, directionToBuild)
  updateGridAndFindFullRow(currentPoint, grids, fullPicture, vertex, edges)
  
  if (min([k[1] for k in fullPicture.keys()])==1-size):
    fullPicture={(k[0], k[1]+size-1):v for k,v in fullPicture.items()}
  return fullPicture

def buildNewGiantGrid(grids, fullPicture):
  newGiantGrid={}
  for x in range(size):
    for y in range(size):
      grid=grids[fullPicture[(x,y)]]
      for key in grid.keys():
        newGiantGrid[(key[0]+10*x, key[1]+10*y)]="#"
  return newGiantGrid

def buildHowToReachSeaMonster(seaMonster):
  seaMonsterKeys=list(seaMonster.keys())
  startPoint=seaMonsterKeys[0]
  allElements=[]
  for k in seaMonsterKeys[1:]:
    allElements.append((k[0]-startPoint[0],k[1]-startPoint[1]))
  return allElements

def checkMonsterFromKey(key, howToReach, newGiantGrid):
  for monsterPoint in howToReach:
    if sumTupleValueByValue(key, monsterPoint) not in newGiantGrid:
      return False
  return True

def updateKeysOfMonster(keysOfMonster, howToReach, newGiantGrid):
  newGiantGridSet=set(newGiantGrid.keys())
  for key in newGiantGridSet:
    if(checkMonsterFromKey(key, howToReach, newGiantGridSet)):
      keysOfMonster.add(key)
      for element in howToReach:
        keysOfMonster.add(sumTupleValueByValue(element, key))

def solve(part):
  rows=getOldAocInput(20)
  grids=parseInput(rows)
  global size
  size=int(len(grids)**(1/2))
  ris, vertex, edges, middle=comprehensionGrids(grids)
  if(part=="a"):
    return ris
  fullPicture=buildFullPictureAndUpdateGrid(grids, vertex, edges, middle)
  newGiantGrid=buildNewGiantGrid(grids, fullPicture)

  columnsToRemove=[]
  rowsToRemove=[]  

  for i in range(12):
    columnsToRemove.append(10*i)
    columnsToRemove.append(10*i+9)
    rowsToRemove.append(10*i)
    rowsToRemove.append(10*i+9)
  newGiantGrid=removeRowsAndColumnsFromGrid(newGiantGrid, rowsToRemove, columnsToRemove)

  seaMonster=["                  # ","#    ##    ##    ###", " #  #  #  #  #  #   "]
  seaMonster, _, _=buildGrid(seaMonster, " ")
  keysOfMonster=set()
  for _ in range(2):
    for _ in range(4):
      howToReach=buildHowToReachSeaMonster(seaMonster)
      updateKeysOfMonster(keysOfMonster, howToReach, newGiantGrid)
      seaMonster=rotateGrid90(seaMonster)
    seaMonster=flipGrid(seaMonster)

  return len(newGiantGrid)-len(keysOfMonster)

print(solve("a"))
print(solve("b"))
# print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))
