from utility import *

def parseRows(rows):
  return  rows


def putInGrid(offset, size, grid):
  offSetX=int(offset[0])
  offSetY=int(offset[1])
  width=int(size[0])
  height=int(size[1])

  for j in range(offSetY, offSetY+height):
    for i in range(offSetX, offSetX+width):
      grid[(j,i)]=grid.get((j,i), 0)+1

def findIsolated(offset, size, grid):
  offSetX=int(offset[0])
  offSetY=int(offset[1])
  width=int(size[0])
  height=int(size[1])
  for j in range(offSetY, offSetY+height):
    for i in range(offSetX, offSetX+width):
      if(grid.get((j,i))!=1):
        return False
  return True

def solve(part):
  rows=getOldAocInput(3)
  rows=parseRows(rows)

  grid={}
  for row in rows:
    rowSplitted=row.split(" ")
    offset=rowSplitted[2][:-1].split(",")
    size=rowSplitted[3].split("x")
    putInGrid(offset, size, grid)
  if(part==1):
    return len([y for y in grid.values() if y>1])
  if(part==2):
    for idx, row in enumerate(rows):
      rowSplitted=row.split(" ")
      offset=rowSplitted[2][:-1].split(",")
      size=rowSplitted[3].split("x")
      if(findIsolated(offset, size, grid)):
        return idx+1

# print(solve(1))
print(solve(2))