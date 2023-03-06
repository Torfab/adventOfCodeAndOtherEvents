from utility import *

directions=dict(D=[-1,0], U=[1,0], R=[0,1], L=[0,-1])

def calculateDistance(coordinate1, coordinate2):
  return max(abs(coordinate1[0]-coordinate2[0]), abs(coordinate1[1]-coordinate2[1]))

def moveTail(coordinateHead, coordinateTail):
  if(calculateDistance(coordinateHead, coordinateTail)>1):

    if(coordinateHead[1]>coordinateTail[1]):
      coordinateTail[1]=coordinateTail[1]+1
    elif(coordinateHead[1]<coordinateTail[1]):
      coordinateTail[1]=coordinateTail[1]-1

    if(coordinateHead[0]>coordinateTail[0]):
      coordinateTail[0]=coordinateTail[0]+1
    elif(coordinateHead[0]<coordinateTail[0]):
      coordinateTail[0]=coordinateTail[0]-1

  return coordinateTail  

def moveHead(coordinateHead, direction):
  return sumArrayValueByValue(coordinateHead, directions[direction])

def moveRope(rope, direction):
  newRope=[]
  newCoordinateHead= moveHead(rope[0], direction)
  newRope.append(newCoordinateHead)
  for knotIndex in range(1,len(rope)):
    newRope.append(moveTail(newRope[knotIndex-1], rope[knotIndex]))
    
  return newRope

def solve(knots):
  rows= getOldAocInput(9)
  rope=[]
  for number in range(knots):
    rope.append([0,0])

  visistatedSet=set()
  visistatedSet.add(str(rope[-1]))

  for element in rows:
    splitted=element.split(" ")
    direction=splitted[0]
    quantity=int(splitted[1])
    for number in range(quantity):
      rope = moveRope(rope, direction)
      visistatedSet.add(str(rope[-1]))
    
      

  return len(visistatedSet)

print(solve(2))
print(solve(10))