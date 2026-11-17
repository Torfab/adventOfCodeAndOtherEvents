from utility import *

# FINALLY proud of a solution regarding time and strategy

directions=fromDistanceBuildSetOfDirections(1)

def parseRows(rows):
  return rows

def solve():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows, neutralElement="#")
  maxBoundaries=maxGrid(grid)
  walls=set(grid.keys())
  walls=walls | cageGridWithWalls(maxBoundaries)

  start=(0,0)
  end=(maxX, maxY)

  visited=set()

  border=[start]

  step=0
  while(border):
    step=step+1
    newBorder=[]
    for current in border:
      if current in visited:
        continue
      visited.add(current)

      for d in directions:
        tentative=sumTupleValueByValue(current, d)
        if (tentative in walls or tentative in visited):
          continue
        if (tentative==end):
          return step
        newBorder.append(tentative)
    border=newBorder

def solve2():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows)
  road=set(grid.keys())
  count=0
  for element in road:
    for d in directions:
      if sumTupleValueByValue(d, element) not in road:
        count=count+1
  return count

def countHerbs(start, end, currentDirection, road):
  count=0
  current=start
  orientedDirectionsTouchingLeft={(1,0):[(0,-1), (1,0), (0,1), (-1,0)], (0,-1):[(-1,0), (0,-1), (1,0), (0,1)], (-1,0):[(0,1), (-1,0), (0,-1),(1,0)], (0,1):[(1,0), (0,1), (-1,0), (0,-1)]}
  while(current!=end):
    for d in orientedDirectionsTouchingLeft[currentDirection]:
      tentative=sumTupleValueByValue(d, current)
      if tentative not in road:
        count=count+1
      else:
        currentDirection=d
        current=tentative
        break

  if(currentDirection==(1,0) or currentDirection==(-1,0)):
    count=count+2
  else:
    count=count+1

  return count

def solve3():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows)
  road=set(grid.keys())

  start=(0,0)
  end=(maxX, maxY)

  firstPart=countHerbs(start, end, (1,0), road)
  secondPart=countHerbs(end, start, (-1,0), road)

  # print(firstPart)
  # print(secondPart)

  return  min(firstPart, secondPart)

print(solve3())
