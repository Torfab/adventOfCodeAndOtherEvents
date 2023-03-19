from utility import *

day=17

blocks=[dict(height=1,gridPlace=[(0,0),(1,0),(2,0),(3,0)]),
          dict(height=3,gridPlace=[(1,0),(0,1),(1,1),(2,1),(1,2)]), 
          dict(height=3,gridPlace=[(0,0),(1,0),(2,0),(2,1),(2,2)]), 
          dict(height=4,gridPlace=[(0,0),(0,1),(0,2),(0,3)]),
          dict(height=2,gridPlace=[(0,0),(0,1),(1,0),(1,1)])]

directionVector=[(1,0),(-1,0),(0,1),(0,-1)]

def printBlocks():
  for element in blocks:
    for j in reversed(range(4)):
      for i in range(4):
        if((i,j) in element["gridPlace"]):
          print("#", end="")
        else:
          (print(".", end=""))
      print()
    print()

def goDown(potentialPlace, grid: dict ):
  newPotentialPlace=dict()
  for element in potentialPlace:
    newPosition=sumTupleValueByValue(element, directionVector[3])
    newPotentialPlace[newPosition]="#"
    if(newPosition in grid):
      return potentialPlace, True
  return newPotentialPlace, False

def moveByJetStream(potentialPlace, grid, jetStream, jetStreamIndex):
  if(jetStream[jetStreamIndex]==">"):
    direction=0
  elif(jetStream[jetStreamIndex]=="<"):
    direction=1
  else:
    print("absurd")

  newPotentialPlace=dict()
  for element in potentialPlace:
    newPosition=sumTupleValueByValue(element, directionVector[direction])
    newPotentialPlace[newPosition]="#"
    if(newPosition[0]<0 or newPosition[0]>6 or newPosition in grid):
      return potentialPlace
  return newPotentialPlace



def placeBlock(idx, grid: dict, maxHeight, jetStream, jetStreamIndex, step):
  start=(2,maxHeight+4)
  potentialPlace=dict()
  for element in blocks[idx]["gridPlace"]:
    newPosition=sumTupleValueByValue(element, start)
    potentialPlace[newPosition]="#"

  steps=0
  blocked=False
  while(not blocked):
    steps=steps+1
    potentialPlace=moveByJetStream(potentialPlace, grid, jetStream, jetStreamIndex)
    jetStreamIndex=(jetStreamIndex+1)%len(jetStream)
    potentialPlace, blocked=goDown(potentialPlace, grid)
  grid.update(potentialPlace)
  maxHeight=max(maxHeight, blocks[idx]["height"]+4-steps+maxHeight)

  return maxHeight, jetStreamIndex

def printGrid(maxHeight, grid: dict):
  print(maxHeight, grid)
  for row in reversed(range(maxHeight+1)):
    for column in range(7):
      if(grid.get((column,row))!=None):
        print(grid.get((column,row)), end='')
      else:
        print(".", end='')
    print()


def solve1():
  rows=getOldAocInput(day)
  jetStream=rows[0]
  jetStreamIndex=0

  blockIdx=0
  maxHeight=0
  grid=dict()
  for element in range(7):
    grid[(element, 0)]='-'


  for step in range(2022):
    maxHeight, jetStreamIndex=placeBlock(blockIdx, grid, maxHeight, jetStream, jetStreamIndex, step)
    blockIdx=(blockIdx+1)%5

  return maxHeight

def solve2():
  rows=getOldAocInput(day)
  jetStream=rows[0]
  jetStreamIndex=0

  blockIdx=0
  maxHeight=0
  grid=dict()
  for element in range(7):
    grid[(element, 0)]='-'


  for step in range(1730):
    maxHeight, jetStreamIndex=placeBlock(blockIdx, grid, maxHeight, jetStream, jetStreamIndex, step)
    blockIdx=(blockIdx+1)%5
  
  # Value manually found checking if index of input would've repeat on a single rock, they did, 
  # After that i checked the delta height in every repetition, and i divided the trillion cases minus the first part before converging to the cycle, with the steps of a cycle.
  # The remainder is 1190 so i do single 1190 steps to complete the simulation
  # Sadly you can't use to check your result with different inputs, i want to change it to be more generalized
  for step in range(1190):
    maxHeight, jetStreamIndex=placeBlock(blockIdx, grid, maxHeight, jetStream, jetStreamIndex, step)
    blockIdx=(blockIdx+1)%5

  maxHeight=maxHeight+574712642*2681 
  return maxHeight
  


print(solve1())
print(solve2())