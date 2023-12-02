from utility import *


def solve1(howMuch):
  
  rows= getOldAocInput(1)
  rows=[int(x) for x in rows]

  for x in range(len(rows)):
    for y in range(x+1, len(rows)):
      if(rows[x]+rows[y]==howMuch):
        return(rows[x]*rows[y])

def solve2(howMuch):
  
  rows= getOldAocInput(1)
  rows=[int(x) for x in rows]

  for x in range(len(rows)):
    for y in range(x+1, len(rows)):
      for z in range(y+1, len(rows)):
        if(rows[x]+rows[y]+rows[z]==howMuch):
          return(rows[x]*rows[y]*rows[z])

print(solve1(2020))
print(solve2(3))
