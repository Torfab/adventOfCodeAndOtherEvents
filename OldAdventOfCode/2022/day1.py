from utility import *


def solve(howMany):
  
  rows= getOldAocInput(1)
  singleElf=0
  values=[]

  for element in rows:
    if (element==''):
      values.append(singleElf)
      singleElf=0
      continue

    singleElf+=int(element)

  values.sort()

  accumulatore=0
  for element in range(howMany):
    accumulatore=accumulatore+values[-element-1]

  return accumulatore

print(solve(1))
print(solve(3))
