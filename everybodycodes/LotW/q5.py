from utilityz import *

directions=fromDistanceBuildSetOfRadialDirections(1)

def parseRows(rows):
  return rows

def calculateBorders(lands, notLands):
  borders=set()
  for element in lands:
    for direction in directions:
      tentative=sumTupleValueByValue(element, direction)
      if(tentative) in notLands:
        borders.add(tentative)
  return borders

def calculateAlive(grid, element):
  count=0
  for direction in directions:
    tentative=sumTupleValueByValue(element, direction)
    if grid.get(tentative):
      if(grid[tentative]=="#" or grid[tentative]=="1"):
        count=count+1
  return count>=5

def calculateSandAlive(grid, element):
  count=0
  for direction in directions:
    tentative=sumTupleValueByValue(element, direction)
    if grid.get(tentative):
      if(grid[tentative]=="="):
        count=count+1
  return count>=5

def calculateTreeAlive(grid, element):
  count=0
  for direction in directions:
    tentative=sumTupleValueByValue(element, direction)
    if grid.get(tentative):
      if(grid[tentative]=="="):
        return False
      if(grid[tentative]=="@"):
        count=count+1
  return count>=4

def calculateSandBorders(lands, sands):
  borders=set()
  for element in sands:
    for direction in directions:
      tentative = sumTupleValueByValue(element, direction)
      if tentative in lands:
        borders.add(tentative)
  return borders

def solve(part):
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows)
  grid[(maxX//2, maxY//2)]="#"

  lands=set([x for x,y in grid.items() if y=="#"])
  notLands=set([x for x,y in grid.items() if y!="#"])
  borders=calculateBorders(lands, notLands)
  while(True):
    toBecomeLand=[]
    for element in borders:
      if(calculateAlive(grid, element)):
        toBecomeLand.append(element)

    if(len(toBecomeLand)==0):
      break
    for element in toBecomeLand:
      grid[element]="#"
      lands.add(element)
      notLands.remove(element)

    borders=calculateBorders( lands, notLands)

  for key in grid:
    if grid[key]!="#":
      grid[key]="."
  for i in range(maxX+1):
    grid[(i, -1)]="."
    grid[(i, maxY+1)]="."
    notLands.add((i, -1))
    notLands.add((i, maxY+1))
  for i in range(maxY+1):
    grid[(-1, i)]="."
    grid[(maxX+1, i)]="."
  
  if(part==1):
    return len(lands)

  toBecomeSand=set()
  for element in notLands:
    for direction in directions:
      tentative=sumTupleValueByValue(element, direction)
      if tentative in lands:
        toBecomeSand.add(tentative)

  sands=set()
  for element in toBecomeSand:
    sands.add(element)
    lands.remove(element)
    grid[element]="="

  borders=calculateSandBorders(lands, sands)

  

  while(True):
    toBecomeSand=[]
    for element in borders:
      if(calculateSandAlive(grid, element)):
        toBecomeSand.append(element)

    if(len(toBecomeSand)==0):
      break

    for element in toBecomeSand:
      sands.add(element)
      lands.remove(element)
      grid[element]="="

    borders=calculateSandBorders(lands, sands)

  stampaGrid(grid)

  if(part==2):
    return len(sands)

  treeDirections=fromDistanceBuildSetOfRadialDirections(2)
  treeDirections.remove((-2,-2))
  treeDirections.remove((2,2))
  treeDirections.remove((-2,2))
  treeDirections.remove((2,-2))

  toBecomeTree=set()
  for element in lands:
    good=True
    for direction in treeDirections:
      tentative=sumTupleValueByValue(element, direction)
      if(grid.get(tentative)!="#"):
        good=False
        break
    if(good):
      toBecomeTree.add(element)

  trees=set()
  for element in toBecomeTree:
    trees.add(element)
    lands.remove(element)
    grid[element]="@"

  for i in range(2):
    toBecomeTree=set()
    for element in lands:
      if calculateTreeAlive(grid, element):
        toBecomeTree.add(element)

    for element in toBecomeTree:
      trees.add(element)
      lands.remove(element)
      grid[element]="@"

  for key in grid:
    if(grid[key]=="@"):
      grid[key]="█"
    else:
      grid[key]=" "

  stampaGridNormalized(grid)
  return len(trees)
        



print(solve(3))
