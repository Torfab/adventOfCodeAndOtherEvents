from utilityz import *
from intCode import *

def checkXY(atLeastX, atLeastY, commands):
  _, output, _, _, _=runCommands(commands.copy(), inputs=[atLeastX, atLeastY])
  return output[0]

def findFirstRight(atLeastX, atLeastY, commands):
  while(True):
    _, output, _, _, _=runCommands(commands.copy(), inputs=[atLeastX, atLeastY])
    if(output[0]==1):
      return atLeastX
    atLeastX=atLeastX+1

def findHowManyRight(atLeastX, atLeastY, commands):
  i=0
  while(True):
    atLeastX=atLeastX+1
    _, output, _, _, _=runCommands(commands.copy(), inputs=[atLeastX, atLeastY])
    if(output[0]!=1):
      return i
    i=i+1

def solve(part):
  rows=getOldAocInput(19)
  commands=parseIntCode(rows)

  if part=="a":
    grid={}
    for x in range(50):
      for y in range(50):
        _, output, _, _, _=runCommands(commands.copy(), inputs=[x,y])
        if output[0]==0:
          continue
        grid[(x,y)]=output[0]
    return len(grid)

  atLeastX=0
  atLeastY=100

  while(True):
    atLeastX=findFirstRight(atLeastX, atLeastY, commands)
    if(checkXY(atLeastX, atLeastY, commands)==1 and checkXY(atLeastX+99, atLeastY, commands)==1):
      numRight=findHowManyRight(atLeastX+99, atLeastY, commands)
      if(checkXY(atLeastX, atLeastY+99, commands)==0):
        newNum=findFirstRight(atLeastX, atLeastY+99, commands)
        if newNum-atLeastX-numRight<=0:
          # return atLeastX, atLeastY, newNum, numRight
          return (atLeastX+numRight)*10000+atLeastY
      else:
        return atLeastX*10000+atLeastY
    atLeastY=atLeastY+1



print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# evaluateTime(timeElapse)