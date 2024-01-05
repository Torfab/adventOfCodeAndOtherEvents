from utility import *


def checkValidRowA(row):
  rowSplitted=row.split(" ")
  validRange=[int(x) for x in rowSplitted[0].split("-")]
  letter=rowSplitted[1][0]
  pwdToValid=rowSplitted[2]
  insideCount=0
  for element in pwdToValid:
    if(letter==element):
      insideCount=insideCount+1
  if(validRange[0]<=insideCount<=validRange[1]):
    return 1
  return 0

def checkValidRowB(row):
  rowSplitted=row.split(" ")
  validElement=[int(x) for x in rowSplitted[0].split("-")]
  letter=rowSplitted[1][0]
  pwdToValid=rowSplitted[2]
  insideCount=0
  if(pwdToValid[validElement[0]-1]==letter):
    insideCount=insideCount+1
  if(pwdToValid[validElement[1]-1]==letter):
    insideCount=insideCount+1
  if(insideCount==1):
    return 1
  return 0

def solve(part):
  
  rows= getOldAocInput(2)

  count=0
  for row in rows:
    if(part=="a"):
      count=count+checkValidRowA(row)
    elif(part=="b"):
      count=count+checkValidRowB(row)
  return count

print(solve("a"))
print(solve("b"))
