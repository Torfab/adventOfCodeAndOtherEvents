from utilityz import *

def parseRows(rows):
  grid={}
  for row in rows:
    rowSplitted=row.split(",")
    grid[int(rowSplitted[0]), int(rowSplitted[1])]="#"

  return grid

def solve():
  rows=getOldAocInput(9)
  grid=parseRows(rows)
  listKey=list(grid.keys())

  maxArea=0
  for i in range(len(listKey)-1):
    for j in range(i+1, len(listKey)):
      a=listKey[i]
      b=listKey[j]
      tentative=(abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)
      maxArea=max(maxArea, tentative)
  return maxArea
print(solve())
