from utility import *
import math

def evaluateDistance(oldPosition, currentPosition):
  oldx, oldy, oldz=[int(x) for x in oldPosition.split(" ")]
  newx, newy, newz=[int(x) for x in currentPosition.split(" ")]
  
  distancex=abs(oldx-newx)
  distancey=abs(oldy-newy)
  distancez=abs(oldz-newz)

  distance3d= distancex*distancex+distancey*distancey+distancez*distancez
  distance3d= int(math.sqrt(distance3d))
  return distance3d

rows=openFile("input.txt")

oldPosition=rows[0]

accumulatore=0
for element in rows[1:]:
  currentPosition=element
  accumulatore=accumulatore+evaluateDistance(oldPosition, currentPosition)
  oldPosition=currentPosition

print(accumulatore)
