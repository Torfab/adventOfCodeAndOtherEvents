from utilityz import *

distances=fromDistanceBuildSetOfRadialDirections3D(1)

def fromDistanceBuildSetOfRadialDirections4D(distance):
  resultSet=set()
  for x in range(-distance, distance+1):
    for y in range(-distance, distance+1):
      for z in range(-distance, distance+1):
        for w in range(-distance, distance+1):
          resultSet.add((x,y,z,w))
  resultSet.remove((0,0,0,0))
  return resultSet

distances4D=fromDistanceBuildSetOfRadialDirections4D(1)

def sumTupleValueByValue4D(a,b):
  return a[0]+b[0], a[1]+b[1], a[2]+b[2], a[3]+b[3]

def countNeighbours(point, cubes):
  ris=0
  for d in distances:
    if(sumTriplettesValueByValue(point, d) in cubes):
      ris=ris+1
  return ris

def countNeighbours4D(point, cubes):
  ris=0
  for d in distances4D:
    if(sumTupleValueByValue4D(point, d) in cubes):
      ris=ris+1
  return ris

def doAnIteration(cubes):
  newCubes=set()
  maxX, maxY=maxGrid(cubes)
  maxZ= max(a[2] for a in cubes)
  minX, minY, minZ=min(a[0] for a in cubes),min(a[1] for a in cubes),min(a[2] for a in cubes)
  for x in range(minX-1,maxX+2):
    for y in range(minY-1,maxY+2):
      for z in range(minZ-1,maxZ+2):
        if (x,y,z) in cubes:
          if 2<=countNeighbours((x,y,z), cubes)<=3:
            newCubes.add((x,y,z))
        else:
          if countNeighbours((x,y,z), cubes)==3:
            newCubes.add((x,y,z))
  return newCubes

def doAnIteration4D(cubes):
  newCubes=set()
  maxX, maxY, maxZ, maxW=max(a[0] for a in cubes),max(a[1] for a in cubes),max(a[2] for a in cubes),max(a[3] for a in cubes)
  minX, minY, minZ, minW=min(a[0] for a in cubes),min(a[1] for a in cubes),min(a[2] for a in cubes),min(a[3] for a in cubes)
  for x in range(minX-1,maxX+2):
    for y in range(minY-1,maxY+2):
      for z in range(minZ-1,maxZ+2):
        for w in range(minW-1,maxW+2):
          if (x,y,z,w) in cubes:
            if 2<=countNeighbours4D((x,y,z,w), cubes)<=3:
              newCubes.add((x,y,z,w))
          else:
            if countNeighbours4D((x,y,z,w), cubes)==3:
              newCubes.add((x,y,z,w))
  return newCubes


def solve():
  rows=getOldAocInput(17)
  grid, _, _=buildGrid(rows)
  cubes=set()
  for k in grid.keys():
    cubes.add((k[0], k[1], 0))
  for _ in range(6):
    cubes=doAnIteration(cubes)
  return len(cubes)

def solveB():
  rows=getOldAocInput(17)
  grid, _, _=buildGrid(rows)
  cubes=set()
  for k in grid.keys():
    cubes.add((k[0], k[1], 0,0))
  for _ in range(6):
    cubes=doAnIteration4D(cubes)
  return len(cubes)
  

print(solveB())

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# evaluateTime(timeElapse)