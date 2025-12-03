from utility import *

def parseRows(rows):
  ranges=rows[0].split(",")
  toCheck=[]
  for range in ranges:
    realRange=range.split("-")
    toCheck.append((int(realRange[0]), int(realRange[1])))
  return toCheck


def isValid(idx):
  idx=str(idx)
  lenId=len(idx)
  if (idx[:lenId//2]==idx[lenId//2:]):
    return False
  return True

def isValid2(idx):
  idx=str(idx)
  lenId=len(idx)
  for i in range(1,lenId):
    if(lenId%i==0 and idx[:i]*(lenId//i)==idx):
      return False
  return True

def solve(f):
  raw=getOldAocInput(2)
  toCheck=parseRows(raw)
  count=0
  for element in toCheck:
    for idx in range(element[0], element[1]+1):
      if(not f(idx)):
        count=count+idx
  return count
  

print(solve(isValid))
print(solve(isValid2))
