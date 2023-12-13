from utility import *

def parseRows(rows):
  grids=[]
  grid={}
  offSetY=0
  for y in range(len(rows)):
    for x in range(len(rows[y])):
      if (rows[y][x]=="#"):
        grid[(x,y-offSetY)]="#"
    if(rows[y]==""):
      grids.append(grid)
      grid={}
      offSetY=y+1
  grids.append(grid)
  return grids

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
    
def valutaGrid(grid, ignoreValue=-1):
  maxX=max(grid.keys(), key=lambda x: x[0])[0]+1
  maxY=max(grid.keys(), key=lambda x: x[1])[1]+1
  keys=grid.keys()


  for tentativeVer in range(1,maxX):
    if (tentativeVer<maxX/2):
      limitX=2*tentativeVer-1
      superior=True
    else:
      limitX=maxX-2*(maxX-tentativeVer)
      superior=False
    good=True
    for element in keys:
      if(superior and element[0]>limitX):
        continue
      if(not superior and element[0]<limitX):
        continue
      if(tentativeVer>=element[0]):
        if(grid.get((tentativeVer+(tentativeVer-element[0])-1,element[1]))==None):
          good=False
          break
      if(tentativeVer<element[0]):
        if(grid.get((tentativeVer-(element[0]-tentativeVer+1),element[1]))==None):
          good=False
          break
    if(good and tentativeVer!=ignoreValue):
      return tentativeVer
    
  for tentativeHor in range(1,maxY):
    if (tentativeHor<maxY/2):
      limitY=2*tentativeHor-1
      superior=True
    else:
      limitY=maxY-2*(maxY-tentativeHor)
      superior=False
    good=True
    for element in keys:
      if(superior and element[1]>limitY):
        continue
      if(not superior and element[1]<limitY):
        continue
      if(tentativeHor>=element[1]):
        if(grid.get((element[0],tentativeHor+(tentativeHor-element[1])-1))==None):
          good=False
          break
      if(tentativeHor<element[1]):
        if(grid.get((element[0], tentativeHor-(element[1]-tentativeHor)-1))==None):
          good=False
          break
    if(good and tentativeHor*100!=ignoreValue):
      return tentativeHor*100

def valutaSmudgedGrid(grid: dict, oldValue):
  maxX=max(grid.keys(), key=lambda x: x[0])[0]+1
  maxY=max(grid.keys(), key=lambda x: x[1])[1]+1

  for x in range(maxX):
    for y in range(maxY):
      if(grid.get((x,y))==None):
        grid[(x,y)]="#"
        newValue=valutaGrid(grid, oldValue)
        if(newValue!=None):
          return newValue
        else:
          grid.pop((x,y))
      else:
        grid.pop((x,y))
        newValue=valutaGrid(grid, oldValue)
        if(newValue!=None):
          return newValue
        else:
          grid[(x,y)]="#"

  print("non dovrebbe arrivare qua")
      

def solve(part):
  rows=getOldAocInput(13)
  grids=parseRows(rows)
  result=0
  for grid in grids:
    valutaPlain=valutaGrid(grid)
    if(part=="a"):
      result=result+valutaPlain
    if(part=="b"):
      result=result+valutaSmudgedGrid(grid, valutaPlain)

  return result


print(solve("a"))
print(solve("b"))