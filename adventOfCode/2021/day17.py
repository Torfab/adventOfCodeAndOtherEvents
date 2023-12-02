from utility import *

def parseRows(rows):
  row=rows[0]
  newRows=row.split("=")
  xRange=newRows[1].split(",")[0]
  yRange=newRows[2]
  xRange=[int(x) for x in xRange.split('..')]
  yRange=[int(y) for y in yRange.split('..')]
  return xRange[0], xRange[1], yRange[1], yRange[0]

def step(Sx, Sy, Px, Py):
  Px=Px+Sx
  Py=Py+Sy

  newX=0
  if(Sx>0):
    newX=Sx-1
  if(Sx<0):
    newX=Sx+1
  
  newY=Sy-1
  return newX, newY, Px, Py

def checkTargetArea(Px, Py, targetArea):
  if(targetArea[0]<=Px<=targetArea[1] and targetArea[2]<=Py<=targetArea[3]):
    return True
  return False

def countTouchesX(maxX, borderLeft, borderRight):
  touches=0
  xPosition=0
  firstTouch=-1
  iteration=1
  while(xPosition<=borderRight and maxX>0):

    xPosition=xPosition+maxX

    if(borderLeft<=xPosition<=borderRight):
      if(firstTouch==-1):
        firstTouch=iteration
      touches=touches+1

    maxX=maxX-1
    iteration=iteration+1
  
  if(maxX==0):
    lastTouch=123123
  else:
    lastTouch=firstTouch+touches-1
  return (firstTouch, lastTouch)


def countTouchesY(speedY, borderUp, borderDown):
  currentY=0
  firstTouch=-1
  iteration=0
  touches=0
  while(currentY>=borderDown):
    if(currentY<=borderUp):
      if(firstTouch==-1):
        firstTouch=iteration
      touches=touches+1
    
    currentY=currentY+speedY
    speedY=speedY-1
    iteration=iteration+1

  return (firstTouch, firstTouch+touches-1)

def checkIfInRange(tupleA, tupleB):
  if(tupleB[0]<tupleA[0]):
    tupleA, tupleB= tupleB, tupleA

  if(tupleA[1]<tupleB[0]):
    return False
  
  return True



def solve(part):
  rows=getOldAocInput(17)
  targetArea = parseRows(rows)

  currentSpeedX=7
  currentSpeedY=2

  currentX=0
  currentY=0

  currentSpeedX, currentSpeedY, currentX, currentY=step(currentSpeedX, currentSpeedY, currentX, currentY)

  
  ySpeed=targetArea[3]*(-1)-1
  if(part=="a"):
    maxHeight=(ySpeed)*(ySpeed+1)//2
    return maxHeight

  if(part=="b"): 

    dictX={}

    maxX=targetArea[1]
    
    while(maxX>0):
      countTouchesXvar=countTouchesX(maxX, targetArea[0], targetArea[1])
      if(countTouchesXvar[0]!=-1):
        dictX[maxX]=countTouchesX(maxX, targetArea[0], targetArea[1])
      maxX=maxX-1


    dictY={}
    for y in range(targetArea[3], ySpeed+1):
      dictY[y]=countTouchesY(y, targetArea[2], targetArea[3])

    touches=0
    for x in dictX.keys():
      for y in dictY.keys():
        if(checkIfInRange(dictX[x], dictY[y])):
          touches=touches+1

    return touches
  
  
# print(solve("a"))
print(solve("b"))