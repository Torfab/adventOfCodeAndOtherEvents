from utility import *

def parseRows(rows):
  obstacles=[]
  for row in rows:
    rowSplitted=[int(x) for x in row.split(",")]
    obstacles.append(tuple(rowSplitted))

  return obstacles


def solve():
  rows=openFile("raw.txt")
  obstacles=parseRows(rows)
  currentPositions=set()
  currentPositions.add((0,0)) #height and flaps
  horizontal=0
  for obstacle in obstacles:
    distanceFromZero, heightStart, height=obstacle
    distance=distanceFromZero-horizontal
    heightEnd=heightStart+height

    # Data la distanza dispari e l'altezza corrente pari io posso raggiungere solo numeri dispari
    # Se la distanza fosse pari e l'altezza corrente pario avrei raggiungo solo numeri pari
    # distanza dispari e altezza dispari num pari
    # distanza pari e altezza dispari num dispari
    if (distance+next(iter(currentPositions))[0])%2==0:
      if heightStart%2==0:
        offSet=0
      else:
        offSet=1
    else:
      if heightStart%2==0:
        offSet=1
      else:
        offSet=0      

    realHeight=heightStart+offSet
    reachablePoints=[]
    while(realHeight<heightEnd):
      reachablePoints.append(realHeight)
      realHeight=realHeight+2
    newPositions=set()
    for position in currentPositions:
      currentHeight, flapNumbers=position
      for reachablePoint in reachablePoints:
        newFlapNumbers=(distance+reachablePoint-currentHeight)//2
        if newFlapNumbers<0 or newFlapNumbers>distance:
          continue
        newPositions.add((reachablePoint, flapNumbers+newFlapNumbers))
    currentPositions=newPositions
    horizontal=distanceFromZero



  return currentPositions


print(solve())
