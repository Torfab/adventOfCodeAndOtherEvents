from utility import *

def checkValid(current, k, v, operators):
  if current>k:
    return 0
  
  if(len(v)==1):
    for o in operators:
      if o(current, v[0])==k:
        return k
    return 0
  for o in operators:
    if checkValid(o(current, v[0]), k, v[1:], operators)==k:
      return k
  
  return 0 

def checkValidRow(row, part):
  rowSplitted=row.split(": ")
  k=int(rowSplitted[0])
  v=[int(x) for x in rowSplitted[1].split(" ")]
  if part=="a":
    operators=[lambda a,b: a+b, lambda a,b: a*b]
  if part=="b":
    operators=[lambda a,b: a+b, lambda a,b: a*b, concatenateIntegers]
  return checkValid(v[0],k,v[1:], operators)

def solve(part):
  rows=getOldAocInput(7)
  ris=0
  for row in rows:
    ris=ris+checkValidRow(row, part)
  return ris

print(solve("a"))
print(solve("b"))

