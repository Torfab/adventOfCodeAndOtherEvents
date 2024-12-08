from utilityz import *

def buildReversedGrid(grid):
  reversedGrid={}
  for k,v in grid.items():
    if reversedGrid.get(v)==None:
      reversedGrid[v]=[]
    reversedGrid[v].append(k)
  return reversedGrid

def findAntinodes(pointA, pointB, limits):
  setOfAntinodes=set()
  diffTuple=(pointA[0]-pointB[0], pointA[1] - pointB[1])
  tentative=sumTupleValueByValue(pointA, diffTuple)
  if(0<=tentative[0]<=limits[0] and 0<=tentative[1]<=limits[1]):
    setOfAntinodes.add(tentative)
  tentative=sumTupleValueByValue(pointB, (-diffTuple[0], -diffTuple[1]))
  if(0<=tentative[0]<=limits[0] and 0<=tentative[1]<=limits[1]):
    setOfAntinodes.add(tentative)
  return setOfAntinodes

def findAntinodesB(pointA, pointB, limits):
  setOfAntinodes=set()
  setOfAntinodes.add(pointA)
  setOfAntinodes.add(pointB)

  diffTuple=(pointA[0]-pointB[0], pointA[1] - pointB[1])
  tentative=sumTupleValueByValue(pointA, diffTuple)
  while(0<=tentative[0]<=limits[0] and 0<=tentative[1]<=limits[1]):
    setOfAntinodes.add(tentative)
    tentative=sumTupleValueByValue(tentative, diffTuple)
  tentative=sumTupleValueByValue(pointB, (-diffTuple[0], -diffTuple[1]))
  while(0<=tentative[0]<=limits[0] and 0<=tentative[1]<=limits[1]):
    setOfAntinodes.add(tentative)
    tentative=sumTupleValueByValue(tentative, (-diffTuple[0], -diffTuple[1]))
  return setOfAntinodes

def solve(part):
  rows=getOldAocInput(8)
  grid,maxX,maxY=buildGrid(rows, None)
  grid={k:v for k,v in grid.items() if v!="."}
  reversedGrid=buildReversedGrid(grid)

  if part=="a":
    f=findAntinodes
  if part=="b":
    f=findAntinodesB

  antinodes=set()
  for arrayOfAntennas in reversedGrid.values():
    for i in range(len(arrayOfAntennas)-1):
      for j in range(i+1, len(arrayOfAntennas)):
        antinodes=antinodes.union(f(arrayOfAntennas[i],arrayOfAntennas[j],(maxX, maxY)))

  return len(antinodes)

# print(solve())
# print(solveB())

def timeElapse():
  print(solve("a"))
  print(solve("b"))

evaluateTime(timeElapse)