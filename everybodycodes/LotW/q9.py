from utility import *

def parseRows(rows):
  trees={}
  for row in rows:
    rowSplitted=row.split(", ")
    newObject={}
    for element in rowSplitted:
      elementSplitted=element.split("=")
      if elementSplitted[0]=="id":
        id=int(elementSplitted[1])
        trees[id]={}
      else:
        newObject[elementSplitted[0]]=int(elementSplitted[1])
    trees[id]=newObject
  return trees

def calculateTree(growth, limit):
  seconds=0
  elements=0
  border={0:1}
  while(elements<limit):
    seconds=seconds+1
    newBorder={}
    maximum=0
    for branchSize, branchNumbers in border.items():
      newSize=branchSize+1
      elements=elements+branchNumbers
      if newSize==growth:
        realNumber=(growth-1)//2
        newBorder[realNumber]=newBorder.get(realNumber,0)+2*branchNumbers
        newBorder[1]=newBorder.get(1,0)+branchNumbers
        elements=elements+branchNumbers
        maximum=max(realNumber,maximum)
      else:
        newBorder[newSize]=newBorder.get(newSize, 0)+branchNumbers
        maximum=max(newSize, maximum)
    border=newBorder
  return seconds

def calculateTree3(growth, limit):
  seconds=1
  foglie=1
  border={1:1}
  fastForward=growth-1
  while(foglie<limit):
    seconds=seconds+fastForward
    newBorder={}
    maximum=0
    for branchSize, branchNumbers in border.items():
      newSize=branchSize+fastForward
      if newSize==growth:

        realNumber=(growth-1)//2
        newBorder[realNumber]=newBorder.get(realNumber,0)+2*branchNumbers
        newBorder[1]=newBorder.get(1,0)+branchNumbers
        foglie=foglie+branchNumbers
        maximum=max(realNumber,maximum)
      else:
        newBorder[newSize]=newBorder.get(newSize, 0)+branchNumbers
        maximum=max(newSize, maximum)
    border=newBorder
    fastForward=growth-maximum

  return seconds

def solve(part):
  rows=openFile("raw.txt")
  trees=parseRows(rows)
  result=0

  if(part==1):
    f=calculateTree
  else:
    f=calculateTree3
  
  for tree in trees.values():
    growth=tree["growth"]
    limit=tree["limit"]
    seconds=f(growth, limit)
    result=result+seconds
  return result

def solve3():
  rows=openFile("raw.txt")
  trees=parseRows(rows)

  result=0
  
  for tree in trees.values():
    growth=tree["growth"]
    limit=tree["limit"]
    seconds=calculateTree3(growth, limit)
    result=result+seconds
  return result

print(solve(3))
