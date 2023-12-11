from utility import *

def parseRows(rows):
  allCubes={}
  for row in rows:
    flagLight=-1
    rowSplitted=row.split(" ")
    if(rowSplitted[0]=="on"):
      flagLight=+1
    rowSplitted=rowSplitted[1].split(",")
    cubeKey=[]
    for splitted in rowSplitted:
      cubeKey.extend([int(x) for x in splitted[2:].split("..")])
    cubeKey=tuple(cubeKey)
    allCubes[cubeKey]=flagLight
  return allCubes

def solve(part):
  if(part=="a"):
    rows=getOldAocInput(22)[:20]
  elif(part=="b"):
    rows=getOldAocInput(22)
  rawCubes=parseRows(rows)
  allCubes={}
  count=0
  for rawCube, rawValue in rawCubes.items():
    update={}
    for realCube, realValue in allCubes.items():
      ix0=max(rawCube[0], realCube[0])
      iy0=max(rawCube[2], realCube[2])
      iz0=max(rawCube[4], realCube[4])
      ix1=min(rawCube[1], realCube[1])
      iy1=min(rawCube[3], realCube[3])
      iz1=min(rawCube[5], realCube[5])
      if(ix0<=ix1 and iy0<=iy1 and iz0<=iz1):
        if(update.get((ix0, ix1, iy0, iy1, iz0, iz1))==None):
          update[(ix0, ix1, iy0, iy1, iz0, iz1)]=-realValue
        else:
          update[(ix0, ix1, iy0, iy1, iz0, iz1)]=update[(ix0, ix1, iy0, iy1, iz0, iz1)]-realValue
    if rawValue>0:
      if(update.get(rawCube)==None):
        update[rawCube]=rawValue
      else:
        update[rawCube]=update[rawCube]+rawValue
    allCubes= {key: allCubes.get(key, 0) + update.get(key, 0) for key in set(allCubes)|set(update)}
    count=count+1
  result=0
  for cubeKey, cubeValue in allCubes.items():
    result=result+(cubeKey[1]-cubeKey[0]+1)*(cubeKey[3]-cubeKey[2]+1)*(cubeKey[5]-cubeKey[4]+1)*cubeValue
  return result

print(solve("a"))
print(solve("b"))