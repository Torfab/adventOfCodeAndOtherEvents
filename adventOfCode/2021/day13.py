from utility import *


def parseRows(rows):
  grid=set()
  folding=[]
  for element in rows:
    if(element==""):
      continue
    if(element[0].isdigit()):
      x,y=element.split(",")
      grid.add((int(x),int(y)))
    else:
      verso=element[11]
      number=element[13:]
      folding.append({"verso":verso, "number": int(number)})
  return grid, folding

def printGrid(grid,x, y):

  # print(grid)
  for j in range(x+1):
    for i in range(y+1):
      if((i,j) in grid):
        print("█", end="")
      else:
        print(".", end="")
    print()

def fold(grid, singleFold, initialX, initialY):
  if(singleFold["verso"]=="y"):
    tupleToCheck=1
  else:
    tupleToCheck=0

  newGrid=set()
  for element in grid:
    if element[tupleToCheck]==singleFold["number"]:
      continue
    if element[tupleToCheck]<singleFold["number"]:
      newGrid.add(element)
    if element[tupleToCheck]>singleFold["number"]:
      if(tupleToCheck==0):
        newGrid.add((initialX-element[0], element[1]))
      else:
        newGrid.add((element[0], initialY-element[1]))
  if(tupleToCheck==1):
    initialY=singleFold["number"]-1
  if(tupleToCheck==0):
    initialX=singleFold["number"]-1

  return newGrid, initialX, initialY


def solve(part):
  rows=getOldAocInput(13)
  # rows=getOldAocInput(-1)

  grid, folding = parseRows(rows)

  filteredFolding=[f for f in folding if f["verso"]=="x"]
  initialX=max(filteredFolding, key=lambda x: x["number"])["number"]*2
  filteredFolding=[f for f in folding if f["verso"]=="y"]
  initialY=max(filteredFolding, key=lambda x: x["number"])["number"]*2

  for singleFold in folding:
    grid, initialX, initialY= fold(grid, singleFold, initialX, initialY)
    if(part=="a"):
      return len(grid)
  
  printGrid(grid, initialY, initialX)


print(solve("a"))
solve("b")