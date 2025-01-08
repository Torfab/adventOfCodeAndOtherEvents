from utility import *
from intCode import *

directions=[(0,1), (-1,0), (0,-1), (1,0)]

def solve(part):
  rows=getOldAocInput(17)
  commands=parseIntCode(rows)
  _, outputs, _, _, _=runCommands(commands)
  rawGrid=""
  for element in outputs:
    rawGrid=rawGrid+chr(element)
  rawGrid=rawGrid.split("\n")
  grid, _, _=buildGrid(rawGrid)
  if part=="a":
    walls=set([k for k in grid.keys()])
    intersections=[]
    for wall in walls:
      neighbours=0
      for d in directions:
        if sumTupleValueByValue(wall, d) in walls:
          neighbours=neighbours+1
      if neighbours==4:
        intersections.append(wall)
    intersections=[x[0]*x[1] for x in intersections]
    return sum(intersections)
  if part=="b":
    # First Thing First, check our things
    startPoint=[k for k,v in grid.items() if v!="#"][0]
    walls=set([k for k,v in grid.items() if v=="#"])
    if grid[startPoint]=="^":
      currentDirection=2
    elif grid[startPoint]=="v":
      currentDirection=0
    elif grid[startPoint]==">":
      currentDirection=3
    elif grid[startPoint]=="<":
      currentDirection=1
    currentPoint=startPoint
    instructions=[]
    currentPath=0
    while(True):
      tentativePoint=sumTupleValueByValue(currentPoint, directions[currentDirection])
      if tentativePoint not in walls:
        instructions.append(currentPath)
        newDirection=(currentDirection+1)%len(directions)
        if sumTupleValueByValue(currentPoint, directions[newDirection]) in walls:
          instructions.append("R")
          currentDirection=newDirection
          currentPath=0
          continue
        newDirection=(currentDirection-1)%len(directions)
        if sumTupleValueByValue(currentPoint, directions[newDirection]) in walls:
          instructions.append("L")
          currentDirection=newDirection
          currentPath=0        
          continue
        break
      currentPoint=tentativePoint
      currentPath=currentPath+1
    instructions.pop(0)
    # stampaGrid(grid)
    # return instructions
    
    # Not easy to find generic solution on patterns, but elements were just a few and i did it by hand
    # Maybe it's possible to find some subroutine and force them under 20 element in 3 groups, but it's over the scope of the problem
    # A [R,10,L,8,R,10,R,4]
    # B [L,6,L,6,R,10]
    # C [L,6,R,12,R,12,R,10]
    # ABACBCABAC      

    mainInput="A,B,A,C,B,C,A,B,A,C"
    A="R,10,L,8,R,10,R,4"
    B="L,6,L,6,R,10"
    C="L,6,R,12,R,12,R,10"
    theInput=[ord(x) for x in mainInput]
    theInputA=[ord(x) for x in A]
    theInputB=[ord(x) for x in B]
    theInputC=[ord(x) for x in C]
    realInput=theInput+[10]+theInputA+[10]+theInputB+[10]+theInputC+[10]+[ord("n")]+[10]

    commands=parseIntCode(rows)
    commands[0]=2
    commands, outputs, _, _, _=runCommands(commands, inputs=realInput)
    return outputs[-1]


print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
