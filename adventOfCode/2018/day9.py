from utility import *
from collections import deque

def parseRows(rows):
  rowSplitted=rows[0].split(" ")
  return int(rowSplitted[0]), int(rowSplitted[6])

def playATurn(scoreGrid, plate, currentPlayer, turn):
  if(turn%23==0):
    scoreGrid[currentPlayer]=scoreGrid[currentPlayer]+turn
    plate.rotate(7)
    ballRemoved=plate.popleft()
    scoreGrid[currentPlayer]=scoreGrid[currentPlayer]+ballRemoved
  else:
    plate.rotate(-2)
    plate.appendleft(turn)
  return 

def solve(part):
  rows=openFile("raw.txt")
  players, balls=parseRows(rows)
  if(part==2):
    balls=balls*100
  # print(players, balls)
  scoreGrid={i:0 for i in range(players)}

  plate=deque([0])
  turn=0
  currentPlayer=0
  while(turn<-balls):
    turn=turn+1
    currentPlayer=(currentPlayer+1)%players
    playATurn(scoreGrid, plate, currentPlayer, turn)

  return max(scoreGrid.values())

print(solve(1))
print(solve(2))