from utility import *

directions=fromDistanceBuildSetOfRadialDirections(1)

states={"X":"M", "M":"A", "A":"S"}

#ho messo X e A solo per non far andare in errore l'accesso per indice
pairDict={"M":"S", "S":"M", "X":0, "A":0}
diagonals=[((1,1),(-1,-1)), ((-1,1),(1,-1))]

def countOccurrance(grid, position, currentState, way):
  letter=grid[position]
  if letter==states[currentState]:
    if letter=="S":
      return 1
    else:
      tentative=sumTupleValueByValue(way, position)
      if(grid.get(tentative)!=None):
        return countOccurrance(grid, tentative, letter, way)
  return 0

def solve():
  rows=getOldAocInput(4)
  grid, _, _=buildGrid(rows)
  ris=0
  for element in grid:
    if(grid[element]=="X"):
      for d in directions:
        tentative=sumTupleValueByValue(d, element)
        if (grid.get(tentative)!=None):
          ris=ris+countOccurrance(grid, tentative, "X", d)
  return ris

def checkDiagonals(grid, position):
  for d in diagonals:
    tentative1=sumTupleValueByValue(d[0],position)
    tentative2=sumTupleValueByValue(d[1],position)
    if(grid.get(tentative1)==None or grid.get(tentative2)==None):
      return 0
    if(pairDict[grid[tentative1]]!=grid[tentative2]):
      return 0
  return 1

def solveB():
  rows=getOldAocInput(4)
  grid, _, _=buildGrid(rows)
  ris=0
  for element in grid:
    if(grid[element]=="A"):
      ris=ris+checkDiagonals(grid, element)
      
  return ris

print(solve())
print(solveB())
