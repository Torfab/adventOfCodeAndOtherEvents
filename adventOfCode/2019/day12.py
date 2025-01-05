from utility import *

def parseRows(rows):
  orbitals=[]   
  for row in rows:
    rowSplitted=row.split("=")
    x=int(rowSplitted[1].split(",")[0])
    y=int(rowSplitted[2].split(",")[0])
    z=int(rowSplitted[3].split(">")[0])
    orbitals.append({"x":x, "y":y, "z":z, "speedX":0, "speedY":0, "speedZ":0})
  return orbitals

def checkCoordinate(coordinate, orbitals, curIdx, tarIdx):
  if orbitals[curIdx][coordinate]<orbitals[tarIdx][coordinate]:
    return curIdx, tarIdx
  elif orbitals[curIdx][coordinate]>orbitals[tarIdx][coordinate]:
    return tarIdx, curIdx
  else:
    return -1, -1

def updatePosition(orbitals):
  for orbital in orbitals:
    orbital["x"]=orbital["x"]+orbital["speedX"]
    orbital["y"]=orbital["y"]+orbital["speedY"]
    orbital["z"]=orbital["z"]+orbital["speedZ"]

def updateSpeed(orbitals):
  for curIdx in range(len(orbitals)-1):
    for tarIdx in range(curIdx,len(orbitals)):
      maxIdx, minIdx=checkCoordinate("x", orbitals, curIdx, tarIdx)
      if(minIdx!=-1):
        orbitals[minIdx]["speedX"]=orbitals[minIdx]["speedX"]-1
        orbitals[maxIdx]["speedX"]=orbitals[maxIdx]["speedX"]+1
      maxIdx, minIdx=checkCoordinate("y", orbitals, curIdx, tarIdx)
      if(minIdx!=-1):
        orbitals[minIdx]["speedY"]=orbitals[minIdx]["speedY"]-1
        orbitals[maxIdx]["speedY"]=orbitals[maxIdx]["speedY"]+1
      maxIdx, minIdx=checkCoordinate("z", orbitals, curIdx, tarIdx)
      if(minIdx!=-1):
        orbitals[minIdx]["speedZ"]=orbitals[minIdx]["speedZ"]-1
        orbitals[maxIdx]["speedZ"]=orbitals[maxIdx]["speedZ"]+1

def evaluateResult(orbitals):
  ris=0
  for orbital in orbitals:
    potential=abs(orbital["x"])+abs(orbital["y"])+abs(orbital["z"])
    kinetic=abs(orbital["speedX"])+abs(orbital["speedY"])+abs(orbital["speedZ"])
    totalEnergy=potential*kinetic
    ris=ris+totalEnergy
  return ris

def solve():
  rows=getOldAocInput(12)
  orbitals=parseRows(rows)

  for _ in range(1000):
    updateSpeed(orbitals)
    updatePosition(orbitals)

  return evaluateResult(orbitals)

def solveB():
  rows=getOldAocInput(12)
  orbitals=parseRows(rows)

  xTuple=(orbitals[0]["x"], orbitals[0]["speedX"], orbitals[1]["x"], orbitals[1]["speedX"], orbitals[2]["x"], orbitals[2]["speedX"], orbitals[3]["x"], orbitals[3]["speedX"])
  yTuple=(orbitals[0]["y"], orbitals[0]["speedY"], orbitals[1]["y"], orbitals[1]["speedY"], orbitals[2]["y"], orbitals[2]["speedY"], orbitals[3]["y"], orbitals[3]["speedY"])
  zTuple=(orbitals[0]["z"], orbitals[0]["speedZ"], orbitals[1]["z"], orbitals[1]["speedZ"], orbitals[2]["z"], orbitals[2]["speedZ"], orbitals[3]["z"], orbitals[3]["speedZ"])
  i=0
  xLen=0
  xArray=[]
  yLen=0
  yArray=[]
  zLen=0
  zArray=[]
  while(True):
    updateSpeed(orbitals)
    updatePosition(orbitals)
    if xLen<2 and xTuple==(orbitals[0]["x"], orbitals[0]["speedX"], orbitals[1]["x"], orbitals[1]["speedX"], orbitals[2]["x"], orbitals[2]["speedX"], orbitals[3]["x"], orbitals[3]["speedX"]):
      xLen=xLen+1
      xArray.append(i)
      if(xLen==2 and yLen==2 and zLen==2):
        break
    if yLen<2 and yTuple==(orbitals[0]["y"], orbitals[0]["speedY"], orbitals[1]["y"], orbitals[1]["speedY"], orbitals[2]["y"], orbitals[2]["speedY"], orbitals[3]["y"], orbitals[3]["speedY"]):
      yLen=yLen+1
      yArray.append(i)
      if(xLen==2 and yLen==2 and zLen==2):
        break
    if zLen<2 and zTuple==(orbitals[0]["z"], orbitals[0]["speedZ"], orbitals[1]["z"], orbitals[1]["speedZ"], orbitals[2]["z"], orbitals[2]["speedZ"], orbitals[3]["z"], orbitals[3]["speedZ"]):
      zLen=zLen+1
      zArray.append(i)  
      if(xLen==2 and yLen==2 and zLen==2):
        break
    i=i+1
  xCycle=xArray[1]-xArray[0]
  yCycle=yArray[1]-yArray[0]
  zCycle=zArray[1]-zArray[0]
  
  return lcm(lcm(xCycle, yCycle), zCycle)

print(solve())
print(solveB())
