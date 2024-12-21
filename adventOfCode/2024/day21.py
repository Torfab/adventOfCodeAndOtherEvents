from utilityz import *

directions=fromDistanceBuildSetOfDirections(1)

direcitonsToLetters={(1,0):"E", (-1,0):"W", (0,1):"S", (0,-1):"N"}
lettersToDirection={"E":(1,0), "W":(-1,0), "S":(0,1), "N":(0,-1)}

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

def findRobot1Presses(arrayOfButtonToPress, reachDirectionPad):

  finalRis=[]
  for tentativeButtonToPress in arrayOfButtonToPress:


    currentPoint="A"
    ris=0
    for element, value in tentativeButtonToPress:
      ris=ris+reachDirectionPad[currentPoint][element][0]+value
      currentPoint=element  
    finalRis.append(ris+reachDirectionPad[currentPoint]["A"][0])
  return min(finalRis)

def findRobot2Presses(arrayOfButtonToPress, reachDirectionPad, directionPad):

  finalRis=[]
  for tentativeButtonToPress in arrayOfButtonToPress:
    currentPoint="A"
    ris=0

    for element, value in tentativeButtonToPress:
      ris=ris+findRobot1Presses(arrayValid(reachDirectionPad[currentPoint][element][1], currentPoint, directionPad), reachDirectionPad)+value
      currentPoint=element  

    finalRis.append(ris+findRobot1Presses(arrayValid(reachDirectionPad[currentPoint]["A"][1], currentPoint, directionPad), reachDirectionPad))
  return min(finalRis)

def arrayValid(buttonToPress, current, keyboardGrid):
  if(len(buttonToPress)==2):
    arrayOfButtonToPress=[]
    startPoint=next(k for k,v in keyboardGrid.items() if v==current)
    currentPoint=startPoint
    valid=True
    for e,v in buttonToPress.items():
      for _ in range(v):
        tentative=sumTupleValueByValue(currentPoint, lettersToDirection[e])
        currentPoint=tentative
      if(tentative not in keyboardGrid):
        valid=False
    if valid:
      arrayOfButtonToPress.append(list(buttonToPress.items()))
    
    currentPoint=startPoint
    valid=True
    for e,v in reversed(buttonToPress.items()):
      for _ in range(v):
        tentative=sumTupleValueByValue(currentPoint, lettersToDirection[e])
      if(tentative not in keyboardGrid):
        valid=False
      currentPoint=tentative
    if valid:
      arrayOfButtonToPress.append(list(reversed(buttonToPress.items())))
  else:
    arrayOfButtonToPress=[list(buttonToPress.items())]
  return arrayOfButtonToPress

def solve():
  rows=getOldAocInput(21)
  keyboardGrid, _, _=buildGrid(["789", "456", "123", ".0A"])
  reachKeyboard=buildReachKeys(keyboardGrid)
  directionPad, _, _=buildGrid([".NA", "WSE"])
  reachDirectionPad=buildReachKeys(directionPad)
  ris=0
  current="A"
  for row in rows:
    singleRowRis=0
    for element in row:

      buttonToPressKeyboard=reachKeyboard[current][element][1]
      tempRis=findRobot2Presses(arrayValid(buttonToPressKeyboard, current, keyboardGrid), reachDirectionPad, directionPad)+1
      current=element
      singleRowRis=singleRowRis+tempRis
    print(singleRowRis)
    ris=ris+singleRowRis*int(row[:3])
  return ris

print(solve())
