from utility import *

rows=openFile("input.txt")

def createBoardVuota():
  board=[]
  for _ in range(7):
    temp=[]
    for _ in range(7):
      temp.append("N")
    board.append(temp)
  return board

def printBoard(board: list):
  for row in board:
    for column in row:
      print(column, end="")
    print()

def checkVictoryHorizontal(board, riga, colonna):
  element=board[riga][colonna]
  newElement=element
  count=1
  
  #conto i simboli uguali a destra
  colonnaTemp=colonna+1
  while(element==newElement and colonnaTemp<7):
    newElement=board[riga][colonnaTemp]
    if(newElement==element):
      count=count+1
      # print("trovatodx")
    colonnaTemp=colonnaTemp+1

  #conto i simboli uguali a sinistra, per prima cosa resetto
  newElement=element
  colonnaTemp=colonna-1
  while(element==newElement and colonnaTemp>=0):
    newElement=board[riga][colonnaTemp]
    if(newElement==element):
      count=count+1
      # print("trovatosx")
    colonnaTemp=colonnaTemp-1
  # print(count)
  if(count>3):
    return True
  
  return False

def checkVictoryVertical(board, riga, colonna):
  element=board[riga][colonna]
  newElement=element
  count=1

  #conto i simboli uguali verso il basso
  rigaTemp=riga+1
  while(element==newElement and rigaTemp<7):
    newElement=board[rigaTemp][colonna]
    if(newElement==element):
      count=count+1
    rigaTemp=rigaTemp+1

  if(count>3):
    return True
  
  return False

def checkVictoryDiagonal1(board, riga, colonna):
  element=board[riga][colonna]
  newElement=element
  count=1
  
  #conto i simboli uguali in basso a destra
  rigaTemp=riga+1
  colonnaTemp=colonna+1
  while(element==newElement and colonnaTemp<7 and rigaTemp<7):
    newElement=board[rigaTemp][colonnaTemp]
    if(newElement==element):
      # print("trovatose")
      count=count+1
    colonnaTemp=colonnaTemp+1
    rigaTemp=rigaTemp+1

  #conto i simboli uguali in alto a sinistra, per prima cosa resetto
  newElement=element
  colonnaTemp=colonna-1
  rigaTemp=riga-1
  while(element==newElement and colonnaTemp>=0 and rigaTemp>=0):
    newElement=board[rigaTemp][colonnaTemp]
    if(newElement==element):
      # print("trovatouw")
      count=count+1
    colonnaTemp=colonnaTemp-1
    rigaTemp=rigaTemp-1

  # print(count)
  # printBoard(board)
  # print()
  if(count>3):
    return True
  
  return False

def checkVictoryDiagonal2(board, riga, colonna):
  element=board[riga][colonna]
  newElement=element
  count=1
  
  #conto i simboli uguali in basso a sinistra
  rigaTemp=riga+1
  colonnaTemp=colonna-1
  while(element==newElement and colonnaTemp>=0 and rigaTemp<7):
    newElement=board[rigaTemp][colonnaTemp]
    if(newElement==element):
      count=count+1
    colonnaTemp=colonnaTemp-1
    rigaTemp=rigaTemp+1


  #conto i simboli uguali in alto a destra, per prima cosa resetto
  newElement=element
  colonnaTemp=colonna+1
  rigaTemp=riga-1
  while(element==newElement and colonnaTemp<7 and rigaTemp>=0):
    newElement=board[rigaTemp][colonnaTemp]
    if(newElement==element):
      count=count+1
    colonnaTemp=colonnaTemp+1
    rigaTemp=rigaTemp-1

  if(count>3):
    return True
  
  return False

def playAMove(board: list, move: int, char):
  move=int(move)-1
  for index in range(7):
    if (board[index][move]!='N'):
      index=index-1
      break
  board[index][move]=char
  if(checkVictoryHorizontal(board, index, move) or checkVictoryVertical(board, index, move) or checkVictoryDiagonal1(board, index, move) or checkVictoryDiagonal2(board, index, move)):
    return True
  return False

def prossimoTurno(turno):
  if(turno=='A'):
    return 'B'
  if(turno=='B'):
    return 'C'
  if(turno=='C'):
    return 'A'

def play(game: str):
  board=createBoardVuota()
  turno='A'
  vittoria='N'
  for element in game:
    risultato=playAMove(board, element, turno)
    if(risultato):
      vittoria=turno
      # print("ale")
      break
    turno=prossimoTurno(turno)
  # printBoard(board)
  return vittoria

vittorieA=0
vittorieB=0
vittorieC=0

for game in rows:
  risultato=play(game)
  # print(risultato)
  if(risultato=='A'):
    vittorieA=vittorieA+1
  if(risultato=='B'):
    vittorieB=vittorieB+1
  if(risultato=='C'):
    vittorieC=vittorieC+1

# print(play('1244222777766333252764114517362555561153634761434'))

print(vittorieA*vittorieB*vittorieC)