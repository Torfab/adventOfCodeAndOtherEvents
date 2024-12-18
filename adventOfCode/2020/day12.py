from utility import *

setOfOrientation=[(1,0,"E"), (0,1, "N"), (-1,0,"W"),(0,-1,"S")]

def move(cardinal, value, current):
  if(cardinal=="E"):
    current["E"]=current["E"]+value
  if(cardinal=="W"):
    current["E"]=current["E"]-value
  if(cardinal=="N"):
    current["N"]=current["N"]+value
  if(cardinal=="S"):
    current["N"]=current["N"]-value

def solveA():
  rows=getOldAocInput(12)

  current={"N":0, "E":0}
  direction=0


  for row in rows:
    command=row[0]
    value=int(row[1:])
    if(command=="F"):
      move(setOfOrientation[direction][2], value, current)
    elif(command=="R"):
      value=value//90
      direction=(direction-value)%4
    elif(command=="L"):
      value=value//90
      direction=(direction+value)%4
    else:
      move(command, value, current)
  return abs(current["E"])+abs(current["N"])

def solveB():
  rows=getOldAocInput(12)

  currentShip={"E":0, "N":0}
  currentWayPoint={"E":10, "N":1}
  direction=0


  for row in rows:
    command=row[0]
    value=int(row[1:])
    if(command=="F"):
      currentShip["E"]=currentShip["E"]+currentWayPoint["E"]*value
      currentShip["N"]=currentShip["N"]+currentWayPoint["N"]*value
    elif(command=="R"):
      currentWayPoint["E"], currentWayPoint["N"]=simpleRotation(currentWayPoint["E"], currentWayPoint["N"], value)
    elif(command=="L"):
      currentWayPoint["E"], currentWayPoint["N"]=simpleRotation(currentWayPoint["E"], currentWayPoint["N"], 360-value)
    else:
      move(command, value, currentWayPoint)

  return abs(currentShip["E"])+abs(currentShip["N"])



# print(solveA())
print(solveB())
