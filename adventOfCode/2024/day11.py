from utility import *
import functools

@functools.cache
def explodeNumber(number):
  if(number==0):
    return [1]
  strNum=str(number)
  a=len(strNum)
  if a%2==0:
    return [int(strNum[:a//2]), int(strNum[a//2:])]
  return [number*2024]

def solve(iterations):
  rows=getOldAocInput(11)
  oldDict={int(x):1 for x in rows[0].split()}
  for _ in range(iterations):
    newDict= {}
    for element, v in oldDict.items():
      stoneExploded=explodeNumber(element)
      for subStone in stoneExploded:
        newDict[subStone]=newDict.get(subStone,0)+v

    oldDict=newDict
  

  return sum(oldDict.values())

print(solve(25))
print(solve(75))

# def timeElapse():
#   print(solve(25))
#   print(solve(75))

# evaluateTime(timeElapse)