from utilityz import *

directions={"U":(0,-1), "D":(0,1), "R":(1,0), "L":(-1,0)}

def parseRows(rows):
  lines=[]
  for row in rows:
    lines.append(row.split(","))
  return lines

def fillGridWithLine(line, grid, filler, intersection):
  current=(0,0)
  for command in line:
    d=directions[command[0]]
    for _ in range(int(command[1:])):
      current=sumTupleValueByValue(current, d)
      if grid.get(current, filler)!=filler:
        grid[current]=intersection
      else:
        grid[current]=filler

def findRoutes(line, keysToCheck):
  wire={}
  current=(0,0)
  i=0
  for command in line:
    d=directions[command[0]]
    for _ in range(int(command[1:])):
      i=i+1
      current=sumTupleValueByValue(current, d)
      if current in keysToCheck and current not in wire:
        wire[current]=i
  return wire

def solve(part):
  rows=getOldAocInput(3)
  lines=parseRows(rows)
  grid={}
  fillGridWithLine(lines[0], grid, 1, 0)
  grid={k:1 if v==2 else v for k,v in grid.items()}
  fillGridWithLine(lines[1], grid, 2, 0)
  keysToCheck=set([k for k,v in grid.items() if v==0])
  if part=="a":
    keysToCheck=[distanceBetweenTwoTuples((0,0), k) for k in keysToCheck]
    return min(keysToCheck)
  firstWire=findRoutes(lines[0], keysToCheck)
  secondWire=findRoutes(lines[1], keysToCheck)
  result=[]
  for element in keysToCheck:
    result.append(firstWire[element]+secondWire[element])
  return min(result)

print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))
