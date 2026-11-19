from utility import *

def parseRows(rows, part):

  xDict={}
  for row in rows:
    rowSplitted=row.split(" ")
    xValue=int(rowSplitted[0].split("=")[1])
    yValue=int(rowSplitted[1].split("=")[1])
    if(part==2):
      width=int(rowSplitted[2].split("=")[1])
      xDict[xValue]=yValue
      xDict[xValue+width-1]=yValue
    else:
      xDict[xValue]=yValue
  return xDict


def solve(part):
  rows=openFile("raw.txt")
  xDict=parseRows(rows, part)
  

  possibleX=list(xDict)
  firstX=possibleX[0]
  firstHeight=xDict[firstX]
  lastX=possibleX[-1]
  lastHeight=xDict[lastX]
  possibleX.pop(0)
  possibleX.pop()

  
  size=0
  currentHeight=0
  


  while(True):
    nextHeight=min(firstHeight, lastHeight)
    size=size+(lastX-firstX+1)*(nextHeight-currentHeight)
    currentHeight=nextHeight
    if(not possibleX):
      break
    moveFirst=firstHeight<=lastHeight
    moveLast=firstHeight>=lastHeight
    if(moveFirst):
      while(possibleX):
        key=possibleX.pop(0)
        if(xDict[key]>firstHeight):
          firstHeight=xDict[key]
          firstX=key
          break
    if(moveLast):
      while(possibleX):
        key=possibleX.pop()
        if(xDict[key]>lastHeight):
          lastHeight=xDict[key]
          lastX=key
          break
  size=size+max(firstHeight, lastHeight)-currentHeight
  return size

evaluateTime(solve,2)