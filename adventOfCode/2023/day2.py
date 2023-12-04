from utility import *

aLimits={"red": 12, "green": 13, "blue": 14}

def solveA(row):
  parsedRow=row.split(": ")
  rounds=parsedRow[1].split("; ")
  isValidGame=True
  for singleRound in rounds:
    estrazioni=singleRound.split(", ")

    for singleEstrazione in estrazioni:
      parsedSingleEstrazione=singleEstrazione.split(" ")
      if (aLimits[parsedSingleEstrazione[1]]<int(parsedSingleEstrazione[0])):
        isValidGame=False
  
  if(isValidGame):
    return int(parsedRow[0].split(" ")[1])
  return 0

def solveB(row):
  parsedRow=row.split(": ")
  rounds=parsedRow[1].split("; ")
  minCubes={"red":0, "blue": 0, "green": 0}
  
  for singleRound in rounds:
    estrazioni=singleRound.split(", ")
    for singleEstrazione in estrazioni:
      parsedSingleEstrazione=singleEstrazione.split(" ")
      if (minCubes[parsedSingleEstrazione[1]]<int(parsedSingleEstrazione[0])):
        minCubes[parsedSingleEstrazione[1]]=int(parsedSingleEstrazione[0])
  
  return minCubes["red"]*minCubes["blue"]*minCubes["green"]

def solve(part):
  rows=getOldAocInput(2)
  result=0
  for row in rows:
    if(part=="a"):
      result=result+solveA(row)
    elif(part=="b"):
      result=result+solveB(row)
  return result

print(solve("a"))
print(solve("b"))
