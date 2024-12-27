from utilityz import *

thisRotation=[(0,0), (1,9), (0,9), (1,9)]

def carveGrid(grid):
  grid={k:v for k,v in grid.items() if k[0]==0 or k[0]==9 or k[1]==0 or k[1]==9}
  return grid

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
      grid=carveGrid(grid)
      grids[key]=grid
      rowIdx=rowIdx+11
      state="title"
  return grids

def checkIfPairable(rightSide, keyParent, grids):

  for key, grid in grids.items():
    if key==keyParent:
      continue
    gridKeys=[x for x in grid.keys()]

    keyRotation=0
    
    while(keyRotation<4):
      xy=thisRotation[keyRotation][0]
      val=thisRotation[keyRotation][1]
      subGridKeys=[x[(xy+1)%2] for x in gridKeys if x[xy]==val]
      if subGridKeys==rightSide:
        # print(subGridKeys, rightSide, key, keyRotation, "STRAIGHT")
        return 1
      subGridKeys=[9-x for x in reversed(subGridKeys)]
      if subGridKeys==rightSide:
        # print(subGridKeys, rightSide, key, keyRotation, "FLIPPED")
        return 1

      keyRotation=keyRotation+1
    

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
    rightSide=[k[1] for k in currentGrid.keys() if k[0]==9]
    sidesChainable=sidesChainable+checkIfPairable(rightSide, key, grids)
    rightSide=[k[1] for k in currentGrid.keys() if k[0]==0]
    sidesChainable=sidesChainable+checkIfPairable(rightSide, key, grids)
    rightSide=[k[0] for k in currentGrid.keys() if k[1]==9]
    sidesChainable=sidesChainable+checkIfPairable(rightSide, key, grids)
    rightSide=[k[0] for k in currentGrid.keys() if k[1]==0]
    sidesChainable=sidesChainable+checkIfPairable(rightSide, key, grids)
    if(sidesChainable==2):
      vertex.append(key)
      ris=ris*key
    elif(sidesChainable==3):
      edges.append(key)
    else:
      middle.append(key)
  return ris, vertex, edges, middle

def checkIfChainable(firstPiece, secondPieceDict):
  rightPartFirstPiece=[k[1] for k in firstPiece if k[0]==9]

  keyRotation=0
  while(keyRotation<4):
    xy=thisRotation[keyRotation][0]
    val=thisRotation[keyRotation][1]
    partToCheckSecondPiece=[x[(xy+1)%2] for x in secondPieceDict.keys() if x[xy]==val]
    if rightPartFirstPiece==partToCheckSecondPiece:
      return True, keyRotation, 0
    partToCheckSecondPiece=[9-x for x in reversed(partToCheckSecondPiece)]
    if rightPartFirstPiece==partToCheckSecondPiece:
      return True, keyRotation, 1

    keyRotation=keyRotation+1
  return False, -1, -1

def solve(part):
  rows=getOldAocInput(20)
  grids=parseInput(rows)
  ris, vertex, edges, middle=comprehensionGrids(grids)
  if(part=="a"):
    return ris 
  fullPicture={}
  currentSlot=(0,0)
  fullPicture[(0,0)]=vertex[0]
  rotation=0
  firstGrid=grids[vertex[0]]
  while(rotation<4):
    candidates=[]
    firstPiece=firstGrid.keys()
    for key in edges:
      secondPieceDict=grids[key]
      isChainable, chainRotation, chainFlip=checkIfChainable(firstPiece, secondPieceDict)
      if(isChainable):
        candidates.append((key, chainRotation, chainFlip))
    if(len(candidates)==1):
      print("una sola")
      break
    firstGrid=grid90Rotation(firstGrid, (9,9))
    rotation=rotation+1

  # I rotate first pieces and right piece
  grids[vertex[0]]=firstGrid
  trovatoKey, trovatoRotation, trovatoFlip=candidates[0]
  if trovatoRotation>1:
    trovatoFlip=(trovatoFlip+1)%2
  gridToRotate=grids[trovatoKey]
  for _ in range(trovatoRotation):
    gridToRotate=grid90Rotation(gridToRotate, (9,9))
  # if(trovatoFlip==1):
  #   gridToRotate={(9-k[0], 9-k[1]):"#" for k in gridToRotate.keys()}
  grids[trovatoKey]=gridToRotate

  currentSlot=sumTupleValueByValue(currentSlot, (1,0))
  fullPicture[currentSlot]=trovatoKey
  stampaGrid(grids[fullPicture[(0,0)]])
  print()
  stampaGrid(grids[fullPicture[(1,0)]])

  # trovatoKey
  # print(candidato)
  # grids[candidates[0][0]]=
    
  input()


  print(fullPicture)

# print(solve("a"))
print(solve("b"))
# print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))
