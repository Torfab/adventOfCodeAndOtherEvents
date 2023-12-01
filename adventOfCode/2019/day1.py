from utility import *


def fuelNeed(part, element):
  if(part=="a"):
    fuel= element//3-2
  if(part=="b"):
    newElement=element//3-2
    fuel=newElement
    while (True):
      newElement=newElement//3-2
      if(newElement<=0):
        break
      fuel=fuel+newElement
  return fuel

def solve(part):
  
  rows = getAocInput(-1)
  rowsButInt=[int(x) for x in rows]

  result=0
  for element in rowsButInt:
    result=result+fuelNeed(part, element)
  return result

print(solve("a"))
print(solve("b"))
