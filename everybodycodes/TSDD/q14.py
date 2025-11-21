from utility import *

directions=[(1,1), (1,-1), (-1,-1), (-1,1)]

def parseRows(rows):
  for idx, element in enumerate(rows):
    rows[idx]="             "+element+"             "
  for _ in range(13):
    rows.append("                                ")
    rows.insert(0, "                                ")
  grid, _, _ =buildGrid(rows, " ")
  return grid

def solve():
  rows=openFile("raw.txt")
  grid=parseRows(rows)
  result=0
  for _ in range(10):
    roundCount=0
    newGrid={}
    for k, v in grid.items():
      count=0
      if v=="#":
        for d in directions:
          tentative=sumTupleValueByValue(k, d)
          if grid.get(tentative)!="#":
            count=count+1
        if(count%2==0):
          newGrid[k]="."
        else:
          newGrid[k]="#"
          roundCount=roundCount+1
      elif v==".":
        for d in directions:
          tentative=sumTupleValueByValue(k, d)
          if grid.get(tentative)!="#":
            count=count+1
        if(count%2==0):
          newGrid[k]="#"
          roundCount=roundCount+1
        else:
          newGrid[k]="."
    result=result+roundCount
    grid=newGrid
    

  return result



def solve3():
  rows=openFile("raw.txt")
  centerGrid=parseRows(rows)
  grid={}
  for i in range(34):
    for j in range(34):
      grid[(i,j)]="."
  
  arrayResult=[]
  arrayCenterResult=[]

  result=0
  for round in range(1000000000):
    roundCount=0
    newGrid={}
    for k, v in grid.items():
      count=0
      if v=="#":
        for d in directions:
          tentative=sumTupleValueByValue(k, d)
          if grid.get(tentative)!="#":
            count=count+1
        if(count%2==0):
          newGrid[k]="."
        else:
          newGrid[k]="#"
          roundCount=roundCount+1
      elif v==".":
        for d in directions:
          tentative=sumTupleValueByValue(k, d)
          if grid.get(tentative)!="#":
            count=count+1
        if(count%2==0):
          newGrid[k]="#"
          roundCount=roundCount+1
        else:
          newGrid[k]="."
    result=result+roundCount
    grid=newGrid
    for element in arrayResult:
      if grid==element:
        # print(len(arrayResult), [x[1] for x in arrayResult])
        result=0
        cycleCount=sum([x[1] for x in arrayCenterResult])
        howMany=1000000000//len(arrayResult)
        howRemaining=1000000000%len(arrayResult)

        result=result+cycleCount*howMany
        for element in arrayCenterResult:
          if element[2]<howRemaining:
            result=result+element[1]
          else:
            break
        return result


    is_subset= all(item in grid.items() for item in centerGrid.items())
    if(is_subset):
      arrayCenterResult.append((grid, roundCount, round))
    arrayResult.append(grid)



print(solve3())