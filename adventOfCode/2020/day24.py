from utility import *

directions={"ne":(1,-1), "e":(1,0), "se":(0,1), "sw":(-1,1), "w":(-1, 0), "nw":(0,-1)}

def findTile(row):
  current=(0,0)
  idx=0
  while(idx<len(row)):
    if row[idx]=="s" or row[idx]=="n":
      command=row[idx:idx+2]
      idx=idx+2
    else:
      command=row[idx]
      idx=idx+1
    current=sumTupleValueByValue(current, directions[command])
      
  return current

def solve(part):
  rows=getOldAocInput(24)
  switchedTiles={}
  for row in rows:
    tile=findTile(row)
    switchedTiles[tile]= not switchedTiles.get(tile, False)
  blackTiles=set([k for k, v in switchedTiles.items() if v])
  if part=="a":
    return len(blackTiles)

  for _ in range(100):
    maxX, maxY=maxGrid(blackTiles)
    maxX, maxY=maxX+1, maxY+1

    minX, minY=minGrid(blackTiles)
    minX, minY=minX-1, minY-1
    newTiles=set()
    for x in range(minX, maxX+1):
      for y in range(minY, maxY+1):
        current=(x,y)
        countBlacks=0
        for d in directions.values():
          if sumTupleValueByValue(current, d) in blackTiles:
            countBlacks=countBlacks+1
        if current in blackTiles:
          if countBlacks==1 or countBlacks==2:
            newTiles.add(current)
        else:
          if countBlacks==2:
            newTiles.add(current)
    blackTiles=newTiles
  return len(blackTiles)

print(solve("a"))
print(solve("b"))
# print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))
