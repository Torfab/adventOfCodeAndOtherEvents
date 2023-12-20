from utility import *

directions={"U": (0,-1), "R": (1,0), "D": (0,1), "L": (-1,0), '3': (0,-1), '0': (1,0), '1': (0,1), '2': (-1,0)}

def solve(part):
  rows=getOldAocInput(18)
  
  currentPoint=(0,0)
  grid=[currentPoint]
  perimeter=0
  for row in rows:
    element=row.split(" ")
    if(part=="a"):
      direction=element[0]
      quantity=int(element[1])
    else:
      quantity=fromHexToInteger(element[2][2:7])
      direction=element[2][7]
    currentPoint=sumTupleValueByValue(currentPoint, multiplyTupleByValue(directions[direction], quantity))
    grid.append(currentPoint)
    perimeter=perimeter+quantity
  result=0
  for idx in range(len(grid)-1):
    result=result+grid[idx][0]*grid[idx+1][1]-grid[idx][1]*grid[idx+1][0]
  return abs(result//2)+3+(perimeter-4)//2

print(solve("a"))
print(solve("b"))