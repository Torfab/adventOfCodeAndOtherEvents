from utility import *

def parseRows(rows, part):
  if(part=="a"):
    expansion=2
  if(part=="b"):
    expansion=1000000
  grid={}
  addY=0
  for y in range(len(rows)):
    anyY=0
    for x in range(len(rows[y])):
      if(rows[y][x]=="#"):
        grid[(x,y+addY)]="#"
        anyY=anyY+1
    if(anyY==0):
      addY=addY+expansion-1

  maxX=max(grid.keys(), key=lambda x: x[0])[0]+1
  
  x=0
  arrayOfJumps=[]
  while(x<maxX):
    if(not any(x == key[0] for key in grid.keys())):
      arrayOfJumps.append(x)
    x=x+1

  newGrid={}

  for k,v in grid.items():
    idx=0
    while(idx<len(arrayOfJumps)):
      if (k[0]<arrayOfJumps[idx]):
        break
      idx=idx+1
    newGrid[(k[0]+idx*(expansion-1), k[1])]=v

  return newGrid

def stampaGrid(grid):
  maxX=max(grid.keys(), key=lambda x: x[0])[0]+1
  maxY=max(grid.keys(), key=lambda x: x[1])[1]+1

  for y in range(maxY):
    for x in range(maxX):
      if(grid.get((x,y))==None):
        print(".", end="")
      else:
        print("#", end="")
    print()
    

def solve(part):
  rows=getOldAocInput(11)
  grid=parseRows(rows, part)
  newArray=list(grid.keys())
  result=0
  for firstElement in range(len(newArray)-1):
    for secondElement in range(firstElement, len(newArray)):
      result=result+distanceBetweenTwoTuples(newArray[firstElement], newArray[secondElement])
  return result


print(solve("a"))
print(solve("b"))