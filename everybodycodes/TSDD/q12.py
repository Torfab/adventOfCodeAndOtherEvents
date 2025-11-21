from utility import *

directions= fromDistanceBuildSetOfDirections(1)

def parseRows(rows):
  return rows


def solve(part):
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  barrels, maxX,maxY=buildGrid(rows)

  barrels={k: int(v) for k,v in barrels.items()}
  

  start=(0,0)
  border=set()
  if(part=="a"):
    border.add(start)
  if(part=="b"):
    border.add(start)
    border.add((maxX, maxY))

  count=0
  while(border):
    current=border.pop()
    count=count+1
    for d in directions:
      tentative=sumTupleValueByValue(current, d)
      if(barrels[current]>=barrels.get(tentative,1000)):
        border.add(tentative)
    barrels[current]=barrels[current]+1000

  return count

def checkExplosions(ogBarrels, start):

  barrels=dict(ogBarrels)
  border=set()
  border.add(start)
  count=0
  while(border):
    current=border.pop()
    count=count+1
    for d in directions:
      tentative=sumTupleValueByValue(current, d)
      if(barrels[current]>=barrels.get(tentative,1000)):
        border.add(tentative)
    barrels[current]=barrels[current]+1000

  return count, barrels

def solve3():
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  barrels, _,_=buildGrid(rows)

  barrels={k: int(v) for k,v in barrels.items()}
  ogBarrels=dict(barrels)

  barrelsToExplode=[]
  result=0
  candidates=dict(barrels)
  maxExplosions=0
  resultingGrid={}
  maxKey=0
  for key in candidates.keys():
    explosions, tentativeGrid=checkExplosions(barrels, key)
    if(explosions>maxExplosions):
      maxExplosions=explosions
      resultingGrid=tentativeGrid
      maxKey=key
  result=result+maxExplosions
  barrels=resultingGrid
  barrelsToExplode.append(maxKey)

  candidates={k:v for k,v in barrels.items() if v <100}
  maxExplosions=0
  resultingGrid={}
  maxKey=0
  for key in candidates.keys():
    explosions, tentativeGrid=checkExplosions(barrels, key)
    if(explosions>maxExplosions):
      maxExplosions=explosions
      resultingGrid=tentativeGrid
      maxKey=key
  result=result+maxExplosions
  barrels=resultingGrid
  barrelsToExplode.append(maxKey)

  candidates={k:v for k,v in barrels.items() if v <100}
  maxExplosions=0
  resultingGrid={}
  maxKey=0
  for key in candidates.keys():
    explosions, tentativeGrid=checkExplosions(barrels, key)
    if(explosions>maxExplosions):
      maxExplosions=explosions
      maxKey=key
  barrelsToExplode.append(maxKey)


  newBorder=set()
  for element in barrelsToExplode:
    newBorder.add(element)
  count=0
  
  exploded=set()

  while(newBorder):
    border=newBorder
    newBorder=set()
    while(border):
      square=border.pop()
      if(square in exploded):
        print("ah ecco")
        continue
      count=count+1
      exploded.add(square)
      for d in directions:
        tentative=sumTupleValueByValue(square, d)
        if(tentative in exploded):
          continue
        if(ogBarrels[square]>=ogBarrels.get(tentative,1000)):
          newBorder.add(tentative)
      ogBarrels[key]=ogBarrels[key]+1000
  ogBarrels={k:str(v) for k,v in ogBarrels.items() if k not in exploded}
  return count







# print(solve("a"))
# print(solve("b"))
print(solve3())
