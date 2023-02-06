from utility import *


def solve(quantity):
  rows=getOldAocInput(6)

  for idx in range(len(rows[0])-quantity):
    mySet=set()
    for element in range(quantity):
      mySet.add(rows[0][idx+element])
    if(len(mySet)==quantity):
      return idx+quantity
  return 'absurd'

print(solve(4))
print(solve(14))