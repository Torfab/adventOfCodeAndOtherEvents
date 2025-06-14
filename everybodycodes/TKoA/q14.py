from utility import *
import heapq

directionLabels={"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
directionLabels3D={"U":(0,1,0), "D":(0,-1,0), "R":(1,0,0), "L":(-1,0,0), "F": (0,0,1), "B": (0,0,-1)}

def parseRows(rows):
  plants=[]
  for row in rows:
    commands=row.split(",")
    commands=[(x[0], int(x[1:])) for x in commands]
    plants.append(commands)
  return plants

def solve(part):
  rows=openFile("raw.txt")
  plants=parseRows(rows)
  specialLeaves=[]
  grid={}
  for commands in plants:
    current=(0,0,0)
    for command in commands:
      if directionLabels3D.get(command[0])!=None:
        for _ in range(command[1]):
          current=sumTriplettesValueByValue(current, directionLabels3D[command[0]])
          grid[current]="#"
    specialLeaves.append(current)

  if part=="1":
    return max([x[1] for x in grid.keys()])
  if part=="2":
    return len(grid)
  if part=="3":
    mainTrunk={k:v for k,v in grid.items() if k[0]==0 and k[2]==0}

    allSolutions=[]
    for possibleSap in mainTrunk.keys():
      border=[]
      visited=[]
      found={}
      heapq.heappush(border, (0,possibleSap))
      while(len(border)>0 and len(found)!=len(specialLeaves)):
        distance, current=heapq.heappop(border)
        if(current in visited):
          continue
        visited.append(current)
        for direction in directionLabels3D.values():
          tentative=sumTriplettesValueByValue(current, direction)
          doesExist=grid.get(tentative)
          if(doesExist!=None and tentative not in border):
            if(tentative in specialLeaves and tentative not in found.keys()):
              found[tentative]=distance+1
            heapq.heappush(border, (distance+1, tentative))
      allSolutions.append(sum(found.values()))

      
    return min(allSolutions)

print(solve("1"))
print(solve("2"))
print(solve("3"))
