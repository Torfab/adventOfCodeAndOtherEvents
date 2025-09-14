from utility import *

directions=fromDistanceBuildSetOfDirections(1)

def parseRows(rows):
  dice=[]
  last=False
  for row in rows:
    if(not row):
      last=True
      continue
    if(last):
      track=[int(x) for x in row]
      break
    rowSplitted=row.split("[")[1]
    faces=rowSplitted.split("]")[0]
    faces=[int(x) for x in faces.split(",")]
    seed=int(rowSplitted.split("=")[1])
    dice.append({"id": row[0], "faces": faces, "seed":seed, "current":0, "length":len(faces), "pulse":seed, "currentTrackPosition":0})
  return dice, track

def parseRows2(rows):
  dice=[]
  last=False
  grid=[]
  for row in rows:
    if(not row):
      last=True
      continue
    if(last):
      grid.append(row)
      continue
    rowSplitted=row.split("[")[1]
    faces=rowSplitted.split("]")[0]
    faces=[int(x) for x in faces.split(",")]
    seed=int(rowSplitted.split("=")[1])
    dice.append({"id": row[0], "faces": faces, "seed":seed, "current":0, "length":len(faces), "pulse":seed, "currentTrackPosition":0})

  grid, _, _= buildGrid(grid)
  return dice, grid

def updateDie(die, roll_number):
  pulse=die["pulse"]
  spin=roll_number*pulse
  currentResult=(die["current"]+spin)%die["length"]
  die["current"]=currentResult
  pulse=pulse+spin
  pulse=pulse%die["seed"]
  die["pulse"]=pulse+1+roll_number+die["seed"]
  return die["faces"][currentResult]

def solve1():
  rows=openFile("raw.txt")
  dice, _=parseRows(rows)
  score=0
  roll_number=0
  while (score<10000):
    roll_number=roll_number+1
    for die in dice:
      score=score+updateDie(die, roll_number)
  return roll_number

def solve2():
  rows=openFile("raw.txt")
  dice, track=parseRows(rows)
  resultScores=[]
  lenTrack=len(track)
  for die in dice:
    roll_number=0
    while(True):
      roll_number=roll_number+1
      updateDie(die, roll_number)
      if(track[die["currentTrackPosition"]]==die["faces"][die["current"]]):
        die["currentTrackPosition"]=die["currentTrackPosition"]+1
        if(die["currentTrackPosition"]==lenTrack):
          resultScores.append(roll_number)
          break
  result=[]
  greatherThan=0
  for _ in range(len(resultScores)):
    currentMin=100000
    for idxElement in range(len(resultScores)):
      if (resultScores[idxElement]>greatherThan and resultScores[idxElement] < currentMin):
        currentMin=resultScores[idxElement]
        minIdx=idxElement
    result.append(str(minIdx+1))
    greatherThan=currentMin
  return ",".join(result)

def solve3():
  rows=openFile("raw.txt")
  dice, grid=parseRows2(rows)
  dicePositions=[]
  for die in dice:
    roll_number=0
    diePositions=[]
    while(roll_number<10000):
      roll_number=roll_number+1
      updateDie(die, roll_number)
      diePositions.append(str(die["faces"][die["current"]]))
    dicePositions.append(diePositions)
  
  traversedSet=set()
  for walk in dicePositions:
    border=[((x,y), 0) for (x,y) in grid if grid[(x,y)]==walk[0]]
    traversedSingular=set()
    while(border):
      currentPosition, history=border.pop()
      if (currentPosition, history) in traversedSingular:
        continue
      traversedSingular.add((currentPosition, history))
      traversedSet.add(currentPosition)
      history=history+1
      for d in directions:
        tentative=sumTupleValueByValue(currentPosition,d)
        if grid.get(tentative, None)==walk[history]:
          if (tentative, history) in traversedSingular:
            continue
          border.append((tentative, history))
      if grid.get(currentPosition)==walk[history]:
        if (currentPosition, history) in traversedSingular:
          continue        
        border.append((currentPosition, history))

  newGrid={(x,y):"█" for (x,y) in traversedSet}
  return len(traversedSet)

# print(solve1())
# print(solve2())
print(solve3())