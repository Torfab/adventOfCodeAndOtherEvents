from utility import *

distanceVector=[(0,1), (0,-1), (1,0), (-1,0)]

def parseRowsA(rows):
  grid=[]
  for singleRow in rows:
    newRow=[]
    for singleColumn in singleRow:
      newRow.append(int(singleColumn))
      
    grid.append(newRow)
  return grid

def parseRowsB(rows: list):
  grid=[]
  for singleRow in rows:
    newRow=[]
    for singleColumn in singleRow:
      newRow.append(int(singleColumn))
      
    grid.append(newRow)

  for i in range(1,5):
    for singleRow in rows:
      newRow=[]
      for singleColumn in singleRow:
        element=int(singleColumn)+i
        if(element>9):
          element=element-9
        newRow.append(element)
      grid.append(newRow)

  for row in grid:
    extendedRows=[]
    for i in range(1,5):
      extendedRow=[]
      for element in row:
        elementToAdd=element+i
        if(elementToAdd>9):
          elementToAdd=elementToAdd-9
        extendedRow.append(elementToAdd)
      extendedRows.append(extendedRow)
    for element in extendedRows:
      row+=element      
  return grid

def printGrid(grid):
  for row in grid:
    for element in row:
      print(element, end="")
    print()


def solve(part):
  rows=getOldAocInput(15)
  if(part=="a"):
    grid=parseRowsA(rows)
  else:
    grid=parseRowsB(rows)
  # printGrid(grid)
  startPoint=(0,0)
  endPoint=(len(grid)-1, len(grid[0])-1)
  border=[{"coords":startPoint, "value":0, "heur": distanceBetweenTwoTuples(startPoint, endPoint)}]
  done=dict()

  while(len(border)>0):
    findElement=border.pop(0)
    coords=findElement["coords"]
    if done.get(coords)!=None:
      continue
    for direction in range(4):
      candidate=sumTupleValueByValue(distanceVector[direction], coords)
      if(candidate[0]<0 or candidate[0]>=len(grid) or candidate[1]<0 or candidate[1]>=len(grid[0])):
        continue
      newValue=findElement["value"]+grid[candidate[0]][candidate[1]]
      if(candidate==endPoint):
        return newValue
      if done.get(candidate)!=None:
        continue
      foundInBorder=False
      for item in border:
        if (item["coords"]==candidate):
          foundInBorder=True
          item["value"]=min(newValue, item["value"])
          item["heur"]=item["value"]+distanceBetweenTwoTuples(candidate, endPoint)
      if(not foundInBorder):
        heur=newValue+distanceBetweenTwoTuples(candidate, endPoint)
        flagFound=False
        for elementIdx in range(len(border)):
          if border[elementIdx]["heur"]>heur:
            flagFound=True
            border.insert(elementIdx, {"coords": candidate, "value": newValue, "heur": newValue+distanceBetweenTwoTuples(candidate, endPoint)})
            break
        if(not flagFound):
          border.append({"coords": candidate, "value": newValue, "heur": newValue+distanceBetweenTwoTuples(candidate, endPoint)})

    done[findElement["coords"]]=True

print(solve("a"))
print(solve("b"))
