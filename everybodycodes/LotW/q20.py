from utility import *

numSegmentDict={" ": 0, "0":6, "1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6, "+":2, "-":1, "=": 2, "A":6}

base11Dict={"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10}

changeItSelf={"0":["6", "9", "A"], "1":[], "2":["3"], "3":["2", "5"], "4":[], "5":["3"], "6": ["0", "A", "9"], "7":[], "8": [], "9": ["0", "A", "6"], "A": ["6", "9", "0"], "+": [], "-": [], " ": [], "=": []}

removeDict={"0":[], "1":[], "2": [], "3": [], "4": [], "5": [], "6": ["5"], "7": ["1"], "8":["9", "6", "A", "0"], "9": ["3", "5"], "A":[] , "+":["-"], "-": [], "=": [], " ": []}

addDict={"0": ["8"], "1": ["7"], "2": [], "3": ["9"], "4": [], "5":["9", "6"], "6":["8"], "7":[], "8":[], "9": ["8"], "A": ["8"], "+": [], "-": ["+"], "=": [], " ": []}

def parseRows(rows):
  return rows

def base11(num):
  number=0
  for position, char in enumerate(reversed(num)):
    number=number+base11Dict[char]*(11**position)
  return number

def fromIntegerToBase11(integer):
  result=[]

  while (integer!=0):
    reminder=str(integer%11)
    if(reminder=="10"):
      reminder="A"
    result.append(reminder)

    integer=integer//11
  result.reverse()
  return ''.join(result)


def evaluateSide(side):
  sideSplitted=side.split(" ")
  num1=base11(sideSplitted[0])
  num2=base11(sideSplitted[2])

  if(sideSplitted[1]=="+"):
    return num1+num2
  else:
    return num1-num2

def fullCheckEquationValid(row, base11, tryFix):
  if(tryFix):
    return isEquationValid(row, base11) or tryMovingOnePiece(row)
  else:
    return isEquationValid(row, base11)

def isEquationValid(row, base11):

  rowSplitted=row.split(" = ")
  if(not base11):
    return eval(rowSplitted[0])==eval(rowSplitted[1])
  return evaluateSide(rowSplitted[0])==evaluateSide(rowSplitted[1])


def solve(part):
  rows=openFile("raw.txt")
  rows=parseRows(rows)

  base11=False
  tryFix=False
  if(part==2):
    base11=True
  if(part==3):
    base11=True
    tryFix=True
  
  segments=0
  for row in rows:
    if(fullCheckEquationValid(row, base11, tryFix)):
      for char in row:
        segments=segments+numSegmentDict[char]  

  if(base11):
    return fromIntegerToBase11(segments)
  else:
    return segments

def tryMovingOnePiece(row):

  destructuredRow=list(row)
  for idx, char in enumerate(destructuredRow):
    for element in changeItSelf[char]:
      tempDestructuredRow=list(destructuredRow)
      tempDestructuredRow[idx]=element
      if(isEquationValid("".join(tempDestructuredRow), True)):
        return True
    for removedChar in removeDict[char]:
      for jdx, addableChar in enumerate(destructuredRow):
        if(idx==jdx):
          continue
        for addedChar in addDict[addableChar]:
          tempDestructuredRow=list(destructuredRow)
          tempDestructuredRow[idx]=removedChar
          tempDestructuredRow[jdx]=addedChar
          if(isEquationValid("".join(tempDestructuredRow), True)):
            return True
  return False

print(solve(3))
