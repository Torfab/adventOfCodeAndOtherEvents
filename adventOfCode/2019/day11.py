from utility import *
from intCode import *

directions=[(0,-1),(1,0),(0,1),(-1,0)]

def solve(part):
  rows=getOldAocInput(11)
  commands=parseIntCode(rows)
  finish=False
  theInput=0
  cursor=0
  currentTile=(0,0)
  currentDirection=0
  relativeBase=0
  grid={(0,0):blockChar}
  while(finish!=True):
    if(grid.get(currentTile)==None or grid.get(currentTile)=="."):
      theInput=0
    else:
      theInput=1
    _, output, cursor, finish, relativeBase=runCommands(commands, cursor=cursor, inputs=theInput, pauseMode=True, relativeBase=relativeBase)
    if(finish):
      break
    if(output[0]==1):
      grid[currentTile]=blockChar
    elif(output[0]==0):
      grid[currentTile]="."
    else:
      print("non può essere")
    # print(output, "quindi coloro")
    _, output, cursor, finish, relativeBase=runCommands(commands, cursor=cursor, inputs=theInput, pauseMode=True, relativeBase=relativeBase)
    if(finish):
      break
    if output[0]==1:
      currentDirection=(currentDirection+1)%4
    elif output[0]==0:
      currentDirection=(currentDirection-1)%4
    else:
      print("non può essere movement")
    # print(output, "quindi mi muovo")
    currentdirectionValue=directions[currentDirection]
    currentTile=sumTupleValueByValue(currentTile, currentdirectionValue)
  if part=="a":
    return len(grid)
  if part=="b":
    stampaGrid(grid)

print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
