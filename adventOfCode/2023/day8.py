from utility import *

def parseRows(rows):
  pattern=rows[0]
  nodes={}
  for row in rows[2:]:
    rowSplitted=row.split(" = ")
    start=rowSplitted[0]
    endSplitted=rowSplitted[1][1:-1].split(", ")
    nodes[start]={"L": endSplitted[0], "R": endSplitted[1]}
  return pattern, nodes
def solveA():
  rows=getOldAocInput(8)
  pattern, nodes = parseRows(rows)
  currentLocation="AAA"
  count=0
  while(currentLocation!="ZZZ"):
    for element in pattern:
      currentLocation=nodes[currentLocation][element]
      count=count+1
      if(currentLocation=="ZZZ"):
        break
  return count

def solveB():
  rows=getOldAocInput(8)
  pattern, nodes = parseRows(rows)
  
  currentLocations=[]
  for element in nodes.keys():
    if element[2]=="A":
      currentLocations.append(element)

  finalSteps=[]

  for startPoint in currentLocations:
    count=0
    foundRepetition=False
    while (not foundRepetition):
      for direction in pattern:
        startPoint=nodes[startPoint][direction]
        count=count+1
        if(startPoint[2]=="Z"):
          finalSteps.append(count)
          foundRepetition=True

  dividends=[]
  for element in finalSteps:
    for dividend in arrayDividends(element):
      if(dividend not in dividends):
        dividends.append(dividend)
        
  result=1
  for dividend in dividends:
    result=result*dividend
  return result

print(solveA())
print(solveB())