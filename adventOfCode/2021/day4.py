from utility import *


def comprehension(rows):
  bingoes=[]

  numBingo=0
  for idx, element in enumerate(rows):
    if(idx==0):
      bingoNumbers= element.split(",")
      continue
    if((idx-2)%6==0):
      bingoes.append([])
      bingoes[numBingo].append([dict(value=a, marked=False) for a in element.split(" ") if a!=''])
    if((idx-2)%6>0 and(idx-2)%6<4):
      bingoes[numBingo].append([dict(value=a, marked=False) for a in element.split(" ") if a!=''])
    if((idx-2)%6==4):
      bingoes[numBingo].append([dict(value=a, marked=False) for a in element.split(" ") if a!=''])
      numBingo=numBingo+1

  return bingoes, bingoNumbers


def checkNumber(element, bingo):
  for row in range(5):
    for column in range(5):
      if (bingo[row][column]["value"]==element):
        bingo[row][column]["marked"]=True
        return True
  return False

def checkIfWinLine(bingo):
  for row in range(5):
    winnerMarker=0
    for column in range(5):
      if(bingo[row][column]["marked"]==True):
        winnerMarker=winnerMarker+1
    if(winnerMarker==5):
      return True
  return False

def checkIfWinColumn(bingo):
  for idxColumn in range(5):
    winnerMarker=0
    for idxRow in range(5):
      if(bingo[idxRow][idxColumn]["marked"]==True):
        winnerMarker=winnerMarker+1
    if(winnerMarker==5):
      return True
  return False

def checkIfWin(bingo):
  return checkIfWinLine(bingo) or checkIfWinColumn(bingo)

def calculateWin(bingo, numberCalled):
  sum=0
  for row in bingo:
    for element in row:
      if(element["marked"]==False):
        sum=sum+int(element["value"])
  return sum*int(numberCalled)

def solve1():
  rows=getAocInput(4,2021)

  bingoes, bingoNumbers=comprehension(rows)

  for element in bingoNumbers:
    for bingo in bingoes:
      if(checkNumber(element, bingo)):
        if(checkIfWin(bingo)):
          return calculateWin(bingo, element)

def solve2():
  rows=getAocInput(4,2021)

  bingoes, bingoNumbers=comprehension(rows)

  for element in bingoNumbers:
    winnerBoards=[]
    for bingoIdx, bingo in enumerate(bingoes):
      if(checkNumber(element, bingo)):
        if(checkIfWin(bingo)):
          winnerBoards.append(bingoIdx)
    winnerBoards.sort(reverse=True)
    for boardIdx in winnerBoards:
      lastWinningBingo=bingoes.pop(boardIdx)
      lastWinningElement=element

  return calculateWin(lastWinningBingo, lastWinningElement)

print(solve1())
print(solve2())