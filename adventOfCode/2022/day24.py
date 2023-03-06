from utility import *

day=24

directionVector=[(1,0), (-1,0), (0,-1), (0,1), (0,0)]
avalancheDict={">": (1,0), "<":(-1,0), "^": (0,-1), "v": (0,1)}

def comprehension(rows):
  grid=dict()
  for idx, row in enumerate(rows):
    for jdx, column in enumerate(row):
      if (column!="."):
        grid[(jdx, idx)]= [column]
  return grid

def realPrint(grid: dict):
  maxX=max(a[0] for a in grid)
  maxY=max(a[1] for a in grid)
  for idx in range(maxY+1):
    for jdx in range(maxX+1):
      if(grid.get((jdx, idx))==None):
        print(".", end="")
        continue
      if(len(grid[(jdx, idx)])>1):
        print(len(grid[(jdx, idx)]), end="")
      else:
        print(grid[(jdx, idx)][0], end="")
    print()
    
def moveAvalanche(grid, maxX, maxY):
  newGrid=dict()
  for tile in grid:
    for element in grid[tile]:
      if (element== "#"):
        newGrid[tile]=["#"]
      elif(element !="E"):
        candidatePosition=sumTupleValueByValue(tile, avalancheDict[element])
        if(candidatePosition[0]==0):
          candidatePosition=(maxX-1, candidatePosition[1])
        elif(candidatePosition[0]==maxX):
          candidatePosition=(1, candidatePosition[1])
        elif(candidatePosition[1]==0):
          candidatePosition=(candidatePosition[0],maxY-1)
        elif(candidatePosition[1]==maxY):
          candidatePosition=(candidatePosition[0],1)
        if(newGrid.get(candidatePosition)==None):
          newGrid[candidatePosition]=[element]
        else:
          newGrid[candidatePosition].append(element)
  return newGrid

def buildCandidates(grid: dict, tile, end, maxY):
  candidates=set()
  for element in directionVector:
    candidate=sumTupleValueByValue(element, tile)
    if (candidate==end):
      return True
    if (candidate not in grid and candidate[0]>=0 and candidate[1]>=0 and candidate[1]<=maxY):
      candidates.add(candidate)
  return candidates

def bfs(border:set, end, grid, maxX, maxY):
  step=0
  newGrid=grid
  while (len(border)>0):
    step=step+1
    newGrid=moveAvalanche(newGrid, maxX, maxY)
    newBorder=set()
    for element in border:
      candidates=buildCandidates(newGrid, element, end, maxY)
      if (candidates==True):
        return newGrid, step
      else:
        newBorder=newBorder.union(candidates)
    border=newBorder

def setupAndSolve(start, end, grid, maxX, maxY):
  border=set()
  border.add(start)

  return bfs(border, end, grid, maxX, maxY)

def solve1():
  rows=getOldAocInput(day)
  grid=comprehension(rows)
  # realPrint(grid)
  maxX=max(a[0] for a in grid)
  maxY=max(a[1] for a in grid)

  _, result=setupAndSolve((1,0), (maxX-1, maxY), grid, maxX, maxY)
  return result

def solve2():
  rows=getOldAocInput(day)
  grid=comprehension(rows)
  # realPrint(grid)
  maxX=max(a[0] for a in grid)
  maxY=max(a[1] for a in grid)

  result=0
  newGrid, tempResult=setupAndSolve((1,0), (maxX-1, maxY), grid, maxX, maxY)
  result=result+tempResult

  newGrid, tempResult=setupAndSolve((maxX-1, maxY), (1,0), newGrid, maxX, maxY)
  result=result+tempResult

  newGrid, tempResult=setupAndSolve((1,0), (maxX-1, maxY), newGrid, maxX, maxY)
  
  return result+tempResult

print(solve1())
print(solve2())