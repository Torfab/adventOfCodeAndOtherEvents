from utility import *

##I'm sad, the part 3 is very very more efficient considering it a dijkstra path through scores


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

def evaScore2(command, dicTop, dicBottom, grid):
  limits=maxGrid(grid)
  currentIdx=1
  score=0
  while(currentIdx in dicTop):
    current=dicTop[currentIdx]
    score=max(score, calculateSingleScore(dicBottom, grid, command, limits[0], current, currentIdx))
    currentIdx=currentIdx+1
  # print("il ", i, "fa", score)
  return score

def evaluateScore(command, dicTop, dicBottom, grid):
  limits=maxGrid(grid)
  currentIdx=1
  scores={}
  while(currentIdx in dicTop):
    current=dicTop[currentIdx]
    currentScore=calculateSingleScore(dicBottom, grid, command, limits[0], current, currentIdx)
    scores[currentIdx]=max(0,currentScore)
    currentIdx=currentIdx+1
  # print("il ", i, "fa", score)
  return scores
  
def solve1():
  rows=openFile("raw.txt")
  commands, grid=parseRows(rows)
  dicTop, dicBottom=setupGame(grid)
  score=0
  for i, command in enumerate(commands):
    score=score+evaScore1(command, i, dicTop, dicBottom, grid)
  return score

def solve2():
  rows=openFile("raw.txt")
  commands, grid=parseRows(rows)
  dicTop, dicBottom=setupGame(grid)
  score=0
  for i, command in enumerate(commands):
    score=score+evaScore2(command, dicTop, dicBottom, grid)
  return score


def solve3():
  rows=openFile("raw.txt")
  commands, grid=parseRows(rows)
  dicTop, dicBottom=setupGame(grid)
  listScores=[]
  for i, command in enumerate(commands):
    scores=evaluateScore(command, dicTop, dicBottom, grid)
    listScores.append(scores)

  elements=dict.fromkeys(listScores[0].keys(), 1)
  permutations=homeMadeDispositions(elements, 6)
  print(len(permutations))
  minScore=1000
  maxScore=0
  for combination in permutations:
    currentScore=0
    for i, element in enumerate(combination):
      currentScore=currentScore+listScores[i][element]
    minScore=min(currentScore, minScore)
    maxScore=max(currentScore, maxScore)
  result=str(minScore)+" "+str(maxScore)
  return result



# print(solve1())
# print(solve2())
print(solve3())