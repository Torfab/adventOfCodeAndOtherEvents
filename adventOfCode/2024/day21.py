from utility import *
import functools

directions=fromDistanceBuildSetOfDirections(1)

direcitonsToLetters={(1,0):"E", (-1,0):"W", (0,1):"S", (0,-1):"N"}
lettersToDirection={"E":(1,0), "W":(-1,0), "S":(0,1), "N":(0,-1)}

reachDirectionPad={}
directionPad={}


def buildHistory(history):
  historyDict={}
  for element in history:
    historyDict[element]=historyDict.get(element, 0)+1
  return len(history), historyDict

def buildReachKeys(grid):
  gridKeys=set(grid.keys())

  reachKeyboard={}

  for element in gridKeys:
    border=[(element,[])]
    reachKeyboard[grid[element]]={}
    visited=set()
    while(len(border)>0):
      currentPoint, history=border.pop(0)
      reachKeyboard[grid[element]][grid[currentPoint]]=buildHistory(history)
      if currentPoint in visited:
        continue
      visited.add(currentPoint)
      for d in directions:
        tentative=sumTupleValueByValue(currentPoint, d)
        if tentative in visited:
          continue
        if tentative not in gridKeys:
          continue
        border.append((tentative, history+[direcitonsToLetters[d]]))
  return reachKeyboard

@functools.cache
def findRobotPresses(arrayOfButtonToPress, keyboardNumber):

  finalRis=[]
  if keyboardNumber==1:
    for tentativeButtonToPress in arrayOfButtonToPress:

      currentPoint="A"
      ris=0
      for element, value in tentativeButtonToPress:
        ris=ris+reachDirectionPad[currentPoint][element][0]+value
        currentPoint=element  
      finalRis.append(ris+reachDirectionPad[currentPoint]["A"][0])
    return min(finalRis)

  for tentativeButtonToPress in arrayOfButtonToPress:
    currentPoint="A"
    ris=0

    for element, value in tentativeButtonToPress:
      ris=ris+findRobotPresses(arrayValid(reachDirectionPad[currentPoint][element][1], currentPoint, directionPad), keyboardNumber-1)+value
      currentPoint=element  
    finalRis.append(ris+findRobotPresses(arrayValid(reachDirectionPad[currentPoint]["A"][1], currentPoint, directionPad), keyboardNumber-1))

  return min(finalRis)

def arrayValid(buttonToPress, current, gridToCheck):
  if(len(buttonToPress)==2):
    arrayOfButtonToPress=[]
    startPoint=next(k for k,v in gridToCheck.items() if v==current)
    possibleRoutes=[]
    possibleRoutes.append(buttonToPress.items())
    possibleRoutes.append(list(reversed(buttonToPress.items())))
    for possibility in possibleRoutes:
      currentPoint=startPoint
      valid=True
      for e,v in possibility:
        for _ in range(v):
          tentative=sumTupleValueByValue(currentPoint, lettersToDirection[e])
          currentPoint=tentative
        if(tentative not in gridToCheck):
          valid=False
      if valid:
        arrayOfButtonToPress.append(tuple(possibility))

  else:
    arrayOfButtonToPress=[tuple(buttonToPress.items())]
  return tuple(arrayOfButtonToPress)

def solve(part):
  if(part=="a"):
    numKeyboard=2
  if(part=="b"):
    numKeyboard=25
  rows=getOldAocInput(21)
  keyboardGrid, _, _=buildGrid(["789", "456", "123", ".0A"])
  reachKeyboard=buildReachKeys(keyboardGrid)
  global directionPad
  global reachDirectionPad
  directionPad, _, _=buildGrid([".NA", "WSE"])
  reachDirectionPad=buildReachKeys(directionPad)
  ris=0
  current="A"
  for row in rows:
    singleRowRis=0
    for element in row:
      singleRowRis=singleRowRis+findRobotPresses(arrayValid(reachKeyboard[current][element][1], current, keyboardGrid), numKeyboard)+1
      current=element
    ris=ris+singleRowRis*int(row[:3])
  return ris

print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))