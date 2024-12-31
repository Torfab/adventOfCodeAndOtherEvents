from utility import *

def parseRows(rows):
  rowSplitted=rows[0].split("-")
  return int(rowSplitted[0]), int(rowSplitted[1])


greaterOrEqualsTo= lambda x,y: x>=y
equalsTo= lambda x,y: x==y

def check(num, func):
  counter=1
  num=str(num)
  oldI=int(num[0])
  twoAdjacent=False
  for i in num[1:]:
    i=int(i)
    if i==oldI:
      counter=counter+1
    else:
      if func(counter,2):
        twoAdjacent=True
      counter=1
    if i<oldI:
      return 0
    oldI=i
  if func(counter,2):
    twoAdjacent=True
  if twoAdjacent==False:
    return 0
  return 1


def solve(part):
  rows=getOldAocInput(4)
  lowerBound, upperBound=parseRows(rows)
  ris=0
  if(part=="a"):
    func=greaterOrEqualsTo
  else:
    func=equalsTo
  for i in range(lowerBound, upperBound+1):
    ris=ris+check(i, func)
  return ris

print(solve("a"))
print(solve("b"))