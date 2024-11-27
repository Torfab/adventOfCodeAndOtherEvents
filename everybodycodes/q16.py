from utilityz import *
import functools

# Not a fan of global variables, but after initialization these are just lookup table and i didn't want to carry them over functions
cyclingCounter=[]
faceWheels=[]
possibilities=[-1,0,1]

def parseRows(rows):
  global cyclingCounter
  global faceWheels
  cyclingCounter=cyclingCounter+[int(x) for x in rows[0].split(",")]
  faceWheels=faceWheels+[[] for _ in range(len(cyclingCounter))]
  
  for row in rows[2:]:
    for i in range(len(cyclingCounter)):
      face=row[4*i:4*(i+1)].strip()
      if(face):
        faceWheels[i].append(face)

def putSpaceInFace(face):
  segments=len(face)//3
  temp=[]
  for i in range(segments):
    temp.append(face[3*i:3*(i+1)])
  return " ".join(temp)

def faceCalculator(face):
  newFace=""
  for i in range(len(face)):
    if (i-1)%3==0:
      continue
    newFace=newFace+face[i]
  result={}
  for element in newFace:
    if(result.get(element)==None):
      result[element]=0
    result[element]=result[element]+1
  coinCounter=0
  for v in result.values():
    coinCounter=coinCounter+max(0, v-2)
  return coinCounter

def doPresses(current, leverPress):
  coin=0
  temp=""
  for _ in range(leverPress):
    temp=""
    for i in range(len(current)):
      current[i]=(current[i]+cyclingCounter[i])%len(faceWheels[i])
      temp=temp+faceWheels[i][current[i]]

    coin=coin+faceCalculator(temp)
  return coin, temp, current

def solve():
  rows=openFile("raw.txt")
  parseRows(rows)
  current=[0 for _ in range(len(cyclingCounter))]
  return putSpaceInFace(doPresses(current, 100)[1])


def solve2(manyPresses):
  rows=openFile("raw.txt")
  parseRows(rows)
  current=[0 for _ in range(len(cyclingCounter))]
  firstCycle=tuple(current)
  counter=0
  while(True):
    for i in range(len(current)):
      current[i]=(current[i]+cyclingCounter[i])%len(faceWheels[i])
      counter=counter+1
    if(tuple(current)==firstCycle):
      break
    
  cycleCoin=doPresses(current, counter)[0]
  manyCycles=manyPresses//counter
  offset=manyPresses%counter

  cycleCoin=cycleCoin*manyCycles
  cycleCoin=cycleCoin+doPresses(current, offset)[0]

  return cycleCoin

@functools.cache
def cachedDfs(current, scadenza):
  if(scadenza==0):
    return (0,0)
  scadenza=scadenza-1
  results=[]
  for element in possibilities:
    newCurrent=[x+element for x in current]
    coinStep,_, banana=doPresses(newCurrent, 1)
    pressed=cachedDfs(tuple(banana), scadenza)
    results.append(coinStep+pressed[0])
    results.append(coinStep+pressed[1])
  
  return (max(results), min(results))

def solve3(manyPresses):
  rows=openFile("raw.txt")
  parseRows(rows)
  current=tuple([0 for _ in range(len(cyclingCounter))])
  return cachedDfs(current, manyPresses)

print(solve())