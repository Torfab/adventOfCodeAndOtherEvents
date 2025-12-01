from utility import *

def parseRows(rows):
  obstacles={}
  for row in rows:
    rowSplitted=[int(x) for x in row.split(",")]
    obstacles[rowSplitted[0]]=obstacles.get(rowSplitted[0], [])+[(rowSplitted[1], rowSplitted[2])]

  return obstacles


def solve():
  rows=openFile("raw.txt")
  obstacles=parseRows(rows)
  currentPositions=set()
  currentPositions.add((0,0)) #height and flaps
  horizontal=0
  obstaclesKeys=list(obstacles.keys())
  obstaclesKeys.sort()
  for obstaclesKey in obstaclesKeys:
    reachablePoints=[]
    distance=obstaclesKey-horizontal
    for obstacle in obstacles[obstaclesKey]:
      heightStart, height=obstacle
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
    horizontal=obstaclesKey

  return min([x[1] for x in currentPositions])


print(solve())
