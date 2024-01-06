from utility import *

def parseRows(rows):
  return [int(x) for x in rows]

def checkNumbers(arrToCheck, number):

  for element in arrToCheck:
    if (element==number/2):
      continue
    if(number-element in arrToCheck):
      return False
  return True

def solve(part):
  rows= getOldAocInput(9)
  numbers=parseRows(rows)

  for idx in range(25, len(numbers)):
    if(checkNumbers(numbers[idx-25:idx],numbers[idx])):
      resultA=numbers[idx]
      break
  if(part=="a"):
    return resultA
  
  idx=0
  currentIdx=0
  count=0
  arrayContainer=[]
  while(count!=resultA or len(arrayContainer)<2):
    count=count+numbers[currentIdx]
    arrayContainer.append(numbers[currentIdx])
    currentIdx=currentIdx+1
    if(count>resultA):
      idx=idx+1
      count=0
      currentIdx=idx
      arrayContainer=[]
  return min(arrayContainer)+max(arrayContainer)
  
print(solve("a"))
print(solve("b"))
