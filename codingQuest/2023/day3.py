import requests

response = requests.get("https://codingquest.io/api/puzzledata?puzzle=20")
rows = response.text.splitlines()

# print(rows)

dictPlayers={0: "x", 1: "o"}

# def stampaGrid(grid):
#   for row in grid:
#     for column in row:
#       print(column, "", end="")
#     print()

def playMove(grid, move, player):
  move=int(move)
  row=((move-1)//3)
  column=((move-1)%3)
  grid[row][column]=player
  # print(grid)

def checkLines(grid):
  for j in range(3):
    if(grid[j][0]!=0 and grid[j][0] == grid[j][1] == grid[j][2]):
      return grid[j][0]
  return None

def checkColumns(grid):
  for j in range(3):
    if(grid[0][j]!=0 and grid[0][j] == grid[1][j] == grid[2][j]):
      return grid[0][j]
  return None

def checkDiagonals(grid):
  if(grid[0][0]!=0 and grid[0][0] == grid[1][1] == grid[2][2]):
    return grid[0][0]

  if(grid[0][2]!=0 and grid[0][2] == grid[1][1] == grid[2][0]):
    return grid[0][2]

  return None

def checkWinningCondition(grid):
  return None or checkLines(grid) or checkColumns(grid) or checkDiagonals(grid)

def playGame(moves):
  grid=[[0,0,0],[0,0,0], [0,0,0]]
  playerIndex=0
  for move in moves.split(" "):

    playMove(grid, move, dictPlayers[playerIndex%2])

    check=checkWinningCondition(grid)

    if(check):
      # stampaGrid(grid)
      # print("ha vinto ", check, end="\n\n")
      return check
    
    playerIndex=playerIndex+1
  return 0

def solve():
  dictResults={0:0, 'o':0, 'x':0}

  for row in rows:
    gameResult=playGame(row)
    dictResults[gameResult]=dictResults[gameResult]+1

  # print(dictResults)
  risultato=1
  for value in dictResults.values():
    risultato=risultato*value
  return risultato

print(solve())

# print(playGame('2 4 5 8 1 3 9 6 7'))

