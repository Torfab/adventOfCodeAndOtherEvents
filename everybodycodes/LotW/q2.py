from utility import *

# technically solved it but man if that's some good spaghetti, the idea looks fine findinig the hardest everytimes but there are more clean, elegant anf faster approaches
# happy that solution went to the right direction from the start tho.

def parseRows(rows):

  return [x.split(" ") for x in rows]

def findHardest(rowCopy):
  startRow=list(rowCopy)
  hardest=rowCopy[0][0]
  i=0
  while(i<len(rowCopy)):
    element=rowCopy[i]
    if hardest not in element:
      i=i+1
      continue
    if (hardest==element[0] and element[1]=="<"):
      hardest=element[2]
      i=0
    elif (hardest==element[2] and element[1]==">"):
      hardest=element[0]
      i=0
    else:
      i=i+1
  i=len(rowCopy)-1
  while(i>=0):
    if(hardest in rowCopy[i]):
      rowCopy.pop(i)
    i=i-1
  return hardest

def solve1():
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  arrayResult=[]
  for row in rows:
    rowCopy=list(row)
    result=""
    while(rowCopy):
      if(len(rowCopy)==1):
        lastTwo=[rowCopy[0][0], rowCopy[0][2]]
        hardest=findHardest(rowCopy)
        lastTwo.remove(hardest)
        result=result+hardest+lastTwo[0]
      else:
        hardest=findHardest(rowCopy)
        result=result+hardest
    arrayResult.append(result)

  result=0
  for element in arrayResult:
    result=result+int(element)
  return result

print(solve1())