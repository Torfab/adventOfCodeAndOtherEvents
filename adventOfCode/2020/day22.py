from utility import *

def parseRows(rows):
  state="firstDeck"
  firstDeck=[]
  secondDeck=[]
  for row in rows:
    if state=="firstDeck":
      if(row==""):
        state="secondDeck"
        continue
      if(row[0].isdigit()):
        firstDeck.append(int(row))
    else:
      if(row[0].isdigit()):
        secondDeck.append(int(row))
  return firstDeck, secondDeck

def doARound(firstDeck, secondDeck):
  firstCard=firstDeck.pop(0)
  secondCard=secondDeck.pop(0)
  if(firstCard>secondCard):
    firstDeck.append(firstCard)
    firstDeck.append(secondCard)
  else:
    secondDeck.append(secondCard)
    secondDeck.append(firstCard)


def findWinner(firstDeck, secondDeck):
  while(len(firstDeck)>0 and len(secondDeck)>0):
    doARound(firstDeck, secondDeck)
  if len(firstDeck)==0:
    return 2
  elif len(secondDeck)==0:
    return 1

def doARoundB(firstDeck, secondDeck, gameDones):
  tupledDecks=(tuple(firstDeck),tuple(secondDeck))
  if tupledDecks in gameDones:
    return True
  gameDones.add(tupledDecks)
  firstCard=firstDeck.pop(0)
  secondCard=secondDeck.pop(0)
  if(len(firstDeck)>=firstCard and len(secondDeck)>=secondCard):
    winner=findWinnerB(firstDeck[:firstCard], secondDeck[:secondCard])
  else:
    if(firstCard>secondCard):
      winner=1
    else:
      winner=2
  if winner==1:
    firstDeck.append(firstCard)
    firstDeck.append(secondCard)
  else:
    secondDeck.append(secondCard)
    secondDeck.append(firstCard)
  return False

  
def findWinnerB(firstDeck, secondDeck):
  gamesDone=set()
  while(len(firstDeck)>0 and len(secondDeck)>0):
    if(doARoundB(firstDeck, secondDeck, gamesDone)):
      return 1
  if len(firstDeck)==0:
    return 2
  else:
    return 1

def playerScore(winningDeck):
  ris=0
  i=1
  for element in reversed(winningDeck):
    ris=ris+element*i
    i=i+1
  return ris

def solve(part):
  rows=getOldAocInput(22)
  firstDeck, secondDeck= parseRows(rows)
  if part=="a":
    winningPlayer=findWinner(firstDeck, secondDeck)
  elif part=="b":
    winningPlayer=findWinnerB(firstDeck, secondDeck)
  if(winningPlayer==1):
    return playerScore(firstDeck)
  else:
    return playerScore(secondDeck)


print(solve("a"))
print(solve("b"))
# print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))
