from utility import *


def parseRows(rows):
  tower={}
  for row in rows:
    parts=row.split(" ")
    myTuple=(int(parts[0].split("=")[1]),int(parts[1].split("=")[1]))
    ring=(myTuple[0]+myTuple[1])-1
    tower[ring]=tower.get(ring, [])+[myTuple]

  return tower



  # return leftTree, rightTree

def calculatePositionScore(tower):
  result=0
  for k,v in tower.items():
    for element in v:
      reminder=100%k
      newX=(element[0]-1+reminder)%k+1
      newY=k-newX+1
      result=result+newX+100*newY
  print(tower)
  return result

def calculateSunDay(tower):
  firstOffset=0
  firstGCD=1
  for k,v in tower.items():
    item=v[0]
    secondOffset=item[1]-1
    secondGCD=k
    firstOffset, firstGCD=combine_congruences(firstOffset, firstGCD, secondOffset, secondGCD)
  return firstOffset
    


def solve(part):
  rows=openFile("raw.txt")
  tower=parseRows(rows)
  if part=="a":
    return calculatePositionScore(tower)
  if part=="b":
    return calculateSunDay(tower)

  
# print(solve("a"))
print(solve("b"))