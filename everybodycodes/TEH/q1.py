from utilityz import *

commandBehaviour={"L":(-1,0), "R":(1,0)}

def parseRows(rows):
  grid=[]
  commands=[]
  for row in rows:
    if not row:
      continue
    if row[0] == "L" or row[0]=="R":
      commands.append(row)
    if row[0]=="." or row[0]=="*":
      grid.append(row)
  newGrid, _, _=buildGrid(grid)
  return commands, newGrid

def setupGame(grid):
  limits=maxGrid(grid)
  current=0
  dicTop={}
  dicBottom={}
  idxDic=1
  while(current<limits[0]+1):
    dicTop[idxDic]=(current,-1)
    dicBottom[(current,limits[1])]=idxDic
    current=current+2
    idxDic=idxDic+1

  return dicTop, dicBottom

def calculateSingleScore(dicBottom, grid, command, rightBorder, current, idxStart):
  idxCommand=0
  while current not in dicBottom:
    tentative=sumTupleValueByValue(current, (0,1))
    if(tentative in grid):
      # print("ho sbattuto contro", tentative, "vado verso ", commandBehaviour[command[idxCommand]])
      tentative=sumTupleValueByValue(tentative, commandBehaviour[command[idxCommand]])
      idxCommand=idxCommand+1
      if(tentative[0]<0):
        tentative=(1,tentative[1])
      if(tentative[0]>rightBorder):
        tentative=(rightBorder-1, tentative[1])
    current=tentative
  score=max(dicBottom[current]*2-idxStart, 0)
  # print("parte da", i+1, "arriva a", current, "che vale", dicBottom[current])
  # print("fa",score)
  return score

def evaScore1(command, i, dicTop, dicBottom, grid):
  print(i)
  current=dicTop[i+1]
  limits=maxGrid(grid)
  return calculateSingleScore(dicBottom, grid, command, limits[0], current, i+1)

def evaScore2(command, i, dicTop, dicBottom, grid):
  limits=maxGrid(grid)
  currentIdx=1
  score=0
  while(currentIdx in dicTop):
    current=dicTop[currentIdx]
    score=max(score, calculateSingleScore(dicBottom, grid, command, limits[0], current, currentIdx))
    currentIdx=currentIdx+1
  # print("il ", i, "fa", score)
  return score


def solve(evaScore):
  rows=openFile("raw.txt")
  commands, grid=parseRows(rows)
  dicTop, dicBottom=setupGame(grid)
  score=0
  for i, command in enumerate(commands):
    score=score+evaScore(command, i, dicTop, dicBottom, grid)
  return score


# print(solve(eni1))
# print(solve(eni2))
# print(solve(evaScore1))
print(solve(evaScore2))