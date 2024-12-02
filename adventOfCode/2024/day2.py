from utility import *

def isSafe(rowElements):

  if(rowElements[0]-rowElements[1]<0):
    isIncreasing=True
  else:
    isIncreasing=False
  old=rowElements[0]
  for element in rowElements[1:]:
    if(old==element):
      return False
    if(abs(old-element)>3):
      return False
    if(isIncreasing and old>element):
      return False
    if(not isIncreasing and old<element):
      return False
    old=element
  return True

def countIsSafe(possibilities):
  for rowElements in possibilities:
    if(isSafe(rowElements)):
      return 1
  return 0

def buildPossibilities(rowElements):
  possibilities=[]
  possibilities.append(rowElements)
  for idx in range(len(rowElements)-1):
    possibilities.append(rowElements[:idx]+rowElements[idx+1:])
  possibilities.append(rowElements[:len(rowElements)-1])
  return possibilities

def solve(part):
  rows=getOldAocInput(2)
  count=0
  for row in rows:
    rowElements=[int(x) for x in row.split()]
    if part=="a":
      count=count+countIsSafe([rowElements])
    if part=="b":
      possibilities=buildPossibilities(rowElements)
      count=count+countIsSafe(possibilities)
  return count

print(solve("a"))
print(solve("b"))