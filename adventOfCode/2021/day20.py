from utility import *

def parseRows(rows):
  enhancer=rows[0]
  enhancerDict={}
  for i in range(len(enhancer)):
    if(enhancer[i]=="#"):
      enhancerDict[i]=True

  inputImages=rows[2:]
  grid={}
  lenSquare=(len(inputImages))//2
  for i in range(len(inputImages)):
    for j in range(len(inputImages[i])):
      # print(inputImages[i][j])
      if(inputImages[i][j]=="#"):
        grid[(i-lenSquare,j-lenSquare)]=True
  # print(grid)
  return enhancerDict, grid, lenSquare

def printGrid(grid):
  minRow=min([x[0] for x in grid.keys()])
  maxRow=max([x[0] for x in grid.keys()])
  minColumn=min([x[1] for x in grid.keys()])
  maxColumn=max([x[1] for x in grid.keys()])

  # print(grid, minRow, maxRow, minColumn, maxColumn)
  for i in range(minRow, maxRow+1):
    for j in range(minColumn, maxColumn+1):
      element=grid.get((i,j))
      if(element==None):
        print('.',end="")
      else:
        print("#", end="")
    print()

def findIndex(grid, i, j, l):
  if(grid.get((i-1,j-1))):
    s='1'
  else:
    s='0'
  if(grid.get((i-1,j))):
    s=s+'1'
  else:
    s=s+'0'
  if(grid.get((i-1,j+1))):
    s=s+'1'
  else:
    s=s+'0'
  if(grid.get((i,j-1))):
    s=s+'1'
  else:
    s=s+'0'
  if(grid.get((i,j))):
    s=s+'1'
  else:
    s=s+'0'
  if(grid.get((i,j+1))):
    s=s+'1'
  else:
    s=s+'0'
  if(grid.get((i+1,j-1))):
    s=s+'1'
  else:
    s=s+'0'
  if(grid.get((i+1,j))):
    s=s+'1'
  else:
    s=s+'0'
  if(grid.get((i+1,j+1))):
    s=s+'1'
  else:
    s=s+'0'
  return int(s, 2)


def step(grid, enhancerDict, lenSquare, numStep):
  newGrid={}
  for i in range(-lenSquare, lenSquare+1):
    for j in range(-lenSquare, lenSquare+1):
      element=enhancerDict.get(findIndex(grid,i,j, lenSquare))
      if(element):
        newGrid[(i,j)]=element

  if(numStep%2==0):
    for i in range(-lenSquare-2, lenSquare+3):
      newGrid[(-lenSquare-1, i)]=True
      newGrid[(-lenSquare-2, i)]=True
      newGrid[(i, -lenSquare-1)]=True
      newGrid[(i, -lenSquare-2)]=True
      newGrid[(lenSquare+1, i)]=True
      newGrid[(lenSquare+2, i)]=True
      newGrid[(i, lenSquare+1)]=True
      newGrid[(i, lenSquare+2)]=True

  return newGrid

def solve(part):
  rows=getOldAocInput(20)

  enhancerDict, grid, lenSquare=parseRows(rows)

  for i in range(part):
    lenSquare=lenSquare+1
    grid=step(grid, enhancerDict, lenSquare, i)

    

  return len(grid)

print(solve(2))
print(solve(50))