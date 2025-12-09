from utilityz import *


def parseRows(rows):
  grid, maxX, maxY=buildGrid(rows)
  start=filterGrid(grid, "S")[0]
  return grid, maxX, maxY,start

def solve():
  rows=getOldAocInput(7)
  grid, maxX, maxY, start=parseRows(rows)

  newBorder=set()
  newBorder.add(start)
  hitted=set()
  while(newBorder):
    border=newBorder
    newBorder=set()
    while(border):
      position=border.pop()
      if position[1]>maxY:
        continue
      if grid.get(position, None)=="^":
        hitted.add(position)
        tentative=sumTupleValueByValue(position, (1,1))
        if tentative[0]>=0 and tentative[0]<=maxX:
          newBorder.add(sumTupleValueByValue(position, (1,1)))
        tentative=sumTupleValueByValue(position, (-1,1))
        if tentative[0]>=0 and tentative[0]<=maxX:
          newBorder.add(sumTupleValueByValue(position, (-1,1)))
      else:
        newBorder.add(sumTupleValueByValue(position, (0,1)))
  return len(hitted)

def solve2():
  rows=getOldAocInput(7)
  grid, maxX, maxY, start=parseRows(rows)

  newBorder={}
  newBorder[start]=1
  count=0
  while(newBorder):
    border=newBorder
    newBorder={}
    for k,v in border.items():
      position, quantity=k,v
      if position[1]>maxY:
        count=count+quantity
        continue
      if grid.get(position, None)=="^":
        tentative=sumTupleValueByValue(position, (1,1))
        if tentative[0]>=0 and tentative[0]<=maxX:
          newBorder[tentative]=newBorder.get(tentative, 0)+quantity
        else:
          count=count+quantity
        tentative=sumTupleValueByValue(position, (-1,1))
        if tentative[0]>=0 and tentative[0]<=maxX:
          newBorder[tentative]=newBorder.get(tentative, 0)+quantity
        else:
          count=count+quantity
      else:
        newBorder[sumTupleValueByValue(position, (0,1))]=newBorder.get(sumTupleValueByValue(position, (0,1)), 0)+quantity
  return count

print(solve2())
