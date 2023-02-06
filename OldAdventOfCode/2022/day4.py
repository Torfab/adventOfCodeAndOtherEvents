from utility import *


def checkFullyContained(a: list,b: list):
  a=[int(a) for a in a]
  b=[int(b) for b in b]
  a.sort()
  b.sort()
  if((a[0]<=b[0] and a[1]>=b[1]) or (b[0]<=a[0] and b[1]>=a[1])):
    return True
  return False

def checkPartialContained(a: list,b: list):
  a=[int(a) for a in a]
  b=[int(b) for b in b]
  a.sort()
  b.sort()

  if((a[0]<=b[0] and a[1]>=b[0]) or (b[0]<=a[0] and b[1]>=a[0])):
    return True
  return False

def solve():
  rows=getOldAocInput(4)

  accumulatore=0
  for element in rows:
    splitted=element.split(",")
    firstElf=splitted[0].split("-")
    secondElf=splitted[1].split("-")

    if(checkFullyContained(firstElf,secondElf)):
      accumulatore=accumulatore+1
  
  return accumulatore

def solve2():
  rows=getOldAocInput(4)

  accumulatore=0
  for element in rows:
    splitted=element.split(",")
    firstElf=splitted[0].split("-")
    secondElf=splitted[1].split("-")

    if(checkPartialContained(firstElf,secondElf)):
      accumulatore=accumulatore+1
  
  return accumulatore

print(solve())
print(solve2())