from utility import *


day=22

directionVector=[(1,0), (0,1), (-1,0), (0,-1)]
orientationVector=['>', 'v', '<', 'ʌ']

def rotate(rotation):
  if(rotation=="L"):
    directionVector.insert(0,directionVector.pop())
    orientationVector.insert(0,orientationVector.pop())
  if(rotation=="R"):
    directionVector.append(directionVector.pop(0))
    orientationVector.append(orientationVector.pop(0))

def comprehension(rows):
  grid=dict()
  for idxRow, row in enumerate(rows):
    if(row==""):
      break
    for idxElement, element in enumerate(row):
      if(element!=" "):
        grid[(idxElement+1, idxRow+1)]=element

  arrayOfCommands=rows[idxRow+1].replace("L", " L ").replace("R", " R ").split(" ")
  return grid, arrayOfCommands

def findWarp(direction, tile, grid):
  if(direction==(1,0)):
    return (min(element[0] for element in grid if element[1]==tile[1]),tile[1])
  if(direction==(-1,0)):
    return (max(element[0] for element in grid if element[1]==tile[1]),tile[1])
  if(direction==(0,1)):
    return (tile[0], min(element[1] for element in grid if element[0]==tile[0]))
  if(direction==(0,-1)):
    return (tile[0], max(element[1] for element in grid if element[0]==tile[0]))

# sory for everybody i use cubeshape of my input, if you have different disposition it won't work
def findWarpInCube(direction, tile, grid):
  candidateTile=sumTupleValueByValue(direction, tile)
  if(51<=tile[0]<=100 and 1<=tile[1]<=50):
    face=1
  if(101<=tile[0]<=150 and 1<=tile[1]<=50):
    face=2
  if(51<=tile[0]<=100 and 51<=tile[1]<=100):
    face=3
  if(51<=tile[0]<=100 and 101<=tile[1]<=150):
    face=4
  if(1<=tile[0]<=50 and 101<=tile[1]<=150):
    face=5
  if(1<=tile[0]<=50 and 151<=tile[1]<=200):
    face=6


  # destra
  # if(face==1 and direction ==(1,0)):#absurd
  #   return (101, candidateTile[1])

  #sinistra
  if(face==1 and direction ==(-1,0)):
    rotate("L")
    rotate("L")
    return (1, 151-candidateTile[1]), ["R", "R"] #1=150 50=101

  #su
  if(face==1 and direction ==(0,-1)):
    rotate("R")
    return ((1, tile[0]+100)), ["L"] #0=151

  #giu
  # if(face==1 and direction ==(0,1)): #absurd
  #   return (51, tile[1])
  
  #destra
  if(face==2 and direction ==(1,0)):
    rotate("L")
    rotate("L")
    return (100, 151-candidateTile[1]), ["R", "R"]

  #sinistra
  # if(face==2 and direction ==(-1,0)): #absurd
  #   return (1, 150-candidateTile[1]) 

  #su
  if(face==2 and direction==(0,-1)):
    return (candidateTile[0]-100, 200), [] #0=151

  #giu
  if(face==2 and direction==(0,1)): 
    rotate("R")
    return (100, candidateTile[0]-50), ["L"]

  #destra
  if(face==3 and direction ==(1,0)):
    rotate("L")
    return (candidateTile[1]+50, 50), ["R"]

  # sinistra
  if(face==3 and direction ==(-1,0)):
    rotate("L")
    return (candidateTile[1]-50, 101), ["R"]

  #su
  # if(face==2 and direction==(0,-1)): #absurd
  #   return (candidateTile[0]-100, 200) 

  #giu
  # if(face==2 and direction==(0,1)): #absurd
  #   return (100, candidateTile[0]-50)

  #destra
  if(face==4 and direction ==(1,0)):
    rotate("L")
    rotate("L")
    return (150, 151-candidateTile[1]), ["R", "R"]


  # sinistra
  # if(face==4 and direction ==(-1,0)): 
  #   return (candidateTile[1]-50, 101) 

  #su
  # if(face==4 and direction==(0,-1)): #absurd
  #   return (candidateTile[0]-100, 200) 

  #giu
  if(face==4 and direction==(0,1)):
    rotate("R")
    return (50, candidateTile[0]+100), ["L"]

  #destra
  # if(face==5 and direction ==(1,0)): #absurd
  #   return (150, 151-candidateTile[1])

  # sinistra
  if(face==5 and direction ==(-1,0)): 
    rotate("R")
    rotate("R")
    return (51, 151-candidateTile[1]), ["L", "L"]

  #su
  if(face==5 and direction==(0,-1)):
    rotate("R")
    return (51, candidateTile[0]+50), ["L"]

  #giu
  # if(face==5 and direction==(0,1)): #absurd
  #   return (50, candidateTile[1]+100)


  #destra
  if(face==6 and direction ==(1,0)):
    rotate("L") 
    return (candidateTile[1]-100, 150), ["R"]

  # sinistra
  if(face==6 and direction ==(-1,0)): 
    rotate("L")
    return (candidateTile[1]-100, 1), ["R"]

  #su
  # if(face==5 and direction==(0,-1)): #absurd
  #   return (51, candidateTile[0]+50) 

  #giu
  if(face==6 and direction==(0,1)): #absurd
    return (candidateTile[0]+100, 1), []



def stamp(tile, grid):
  grid[tile]=orientationVector[0]

def goForwardInCube(currentPosition, steps, grid):
  for element in range(steps):
    candidatePosition=sumTupleValueByValue(currentPosition, directionVector[0])
    arrayOfRotation=[]
    if(grid.get(candidatePosition)==None):
      candidatePosition, arrayOfRotation=findWarpInCube(directionVector[0], currentPosition, grid)
    if(grid[candidatePosition]=="#"):
      for rotation in arrayOfRotation:
        rotate(rotation)
      return currentPosition
    currentPosition=candidatePosition
    stamp(currentPosition, grid)
  return currentPosition

def goForward(currentPosition, steps, grid):
  for element in range(steps):
    candidatePosition=sumTupleValueByValue(currentPosition, directionVector[0])
    if(grid.get(candidatePosition)==None):
      candidatePosition=findWarp(directionVector[0], candidatePosition, grid)
    if(grid[candidatePosition]=="#"):
      return currentPosition
    currentPosition=candidatePosition
    stamp(currentPosition, grid)
  return currentPosition

def realPrint(grid: dict):
  maxX=max(element[0] for element in grid)
  maxY=max(element[1] for element in grid)
  for i in range(1,maxY+1):
    for j in range(1, maxX+1):
      element=grid.get((j,i))
      if(element==None):
        print(" ", end="")
      else:
        print(element, end="")
    print()
  print()

def calculateResult(tile, orientation):
  if(orientation==">"):
    orientationValue=0
  if(orientation=="v"):
    orientationValue=1
  if(orientation=="<"):
    orientationValue=2
  if(orientation=="ʌ"):
    orientationValue=3
  return (tile[1]*1000+tile[0]*4+orientationValue)

def solve(forwardFunction):
  while(directionVector[0]!=(1,0)):
    rotate("R")
  rows=getOldAocInput(day)
  grid, arrayOfCommands=comprehension(rows)
  currentPosition=(min(element[0] for element in grid if element[1]==1), 1)
  stamp(currentPosition, grid)
  for command in arrayOfCommands:
    if (command=="L" or command=="R"):
      rotate(command)
      stamp(currentPosition, grid)
    else:
      currentPosition=forwardFunction(currentPosition, int(command), grid)
  return calculateResult(currentPosition, orientationVector[0])


print(solve(goForward))
print(solve(goForwardInCube))
