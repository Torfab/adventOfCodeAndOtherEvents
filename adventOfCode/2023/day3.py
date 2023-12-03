from utility import *

def parseRow(rows):
  grid={}
  for y in range(len(rows)):
    x=0
    while(x<len(rows[y])):
      if(rows[y][x]=='.'):
        x=x+1
        continue
      number=''
      coord=(x,y)
      while( x<len(rows[y]) and rows[y][x].isnumeric()):
        number=number+rows[y][x]
        x=x+1
      if(number!=''):
        grid[coord]=number
        continue
      grid[(x,y)]=rows[y][x]
      x=x+1
  return grid

def isValid(grid, element):
  if(grid[element].isnumeric()):
    for x in range(element[0]-1, element[0]+len(grid[element])+1):
      upper=element[1]-1
      lower=element[1]+1
      if(grid.get((x, upper))!=None or grid.get((x, lower))!=None):
        return True
    left=element[0]-1
    right=element[0]+ len(grid[element])
    if(grid.get((left, element[1]))!= None or grid.get((right, element[1]))!=None):
      return True
  return False

def putInGears(gears, element, x, y):
  if(gears.get((x,y))==None):
    gears[(x,y)]=[int(element)]
  else:
    gears[x,y].append(int(element))

def checkIfGear(grid, element, gears):
  if(grid[element].isnumeric()):
    for x in range(element[0]-1, element[0]+len(grid[element])+1):
      upper=element[1]-1
      lower=element[1]+1
      if(grid.get((x, upper))=="*"):
        putInGears(gears, grid[element], x, upper)
        return
      if(grid.get((x, lower))=="*"):
        putInGears(gears, grid[element], x, lower)
        return
    left=element[0]-1
    right=element[0]+ len(grid[element])
    if(grid.get((left, element[1]))== "*"):
      putInGears(gears, grid[element], left, element[1])
      return
    if(grid.get((right, element[1]))=="*"):
      putInGears(gears, grid[element], right, element[1])

def solve(part):
  rows=getOldAocInput(3)
  grid=parseRow(rows)
  result=0
  gears={}
  for element in grid:
    checkIfGear(grid, element, gears)
    if(isValid(grid, element)):
      result=result+int(grid[element])
  if(part=="a"):
    return result
  else:
    gearsResult=0
    for element in gears:
      if (len(gears[element])==2):
        gearsResult=gearsResult+gears[element][0]*gears[element][1]
    return gearsResult

print(solve("a"))
print(solve("b"))