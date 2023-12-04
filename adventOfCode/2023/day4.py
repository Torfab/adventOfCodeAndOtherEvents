from utility import *
import re

def solve(part):
  rows=getOldAocInput(4)
  result=0

  instances={}
  for index in range(1,len(rows)+1):
    instances[index]=1

  for row in rows:
    row=row.split(":")
    numbers=row[1].split("|")

    winningNumbers=re.split("\s+", numbers[0].strip())
    potentialNumbers=re.split("\s+", numbers[1].strip())
    game=int(re.split("\s+", row[0].strip())[1])
    
    commonElements=len([element for element in winningNumbers if element in potentialNumbers])
    for element in range(1, commonElements+1):
      instances[game+element]=instances[game+element]+instances[game]
    if(commonElements!=0):
      result=result+2**(commonElements-1)

  if(part=="a"):
    return result
  else:
    return sum(instances.values())

print(solve("a"))
print(solve("b"))