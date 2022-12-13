from utility import *


def distanceA(crabs, index):
  result=0
  for element in crabs:
    result=result+abs(element-index)
  return result

def distanceB(crabs, index):
  result=0
  for element in crabs:
    distance=abs(element-index)
    result=result+(distance*(distance+1)//2)
  return result

def solve(distance):
  rows=getAocInput(7, 2021)

  crabs=[int(a) for a in rows[0].split(",")]
  maxCrab=max(crabs)

  minFuel=99999999999999
  for candidate in range(maxCrab+1):
    minFuel=min(distance(crabs, candidate), minIndex)
  return minFuel



print(solve(distanceA))
print(solve(distanceB))