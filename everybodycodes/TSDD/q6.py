from utility import *
from functools import cmp_to_key

def parseRows(rows):
  return [int(x) for x in rows[0].split(":")[1].split(",")], rows[0].split(":")[0]

def parseRows2(rows):
  parsedRows=[]
  for row in rows:
    parsedRows.append({"elements":[int(x) for x in row.split(":")[1].split(",")], "id": row.split(":")[0]})
  return parsedRows

def insertInWeirdTree(weirdTree, value):
  if(weirdTree.get("value")==None):
    weirdTree["value"]=value
    return
  if(value<weirdTree["value"]):
    if(weirdTree.get("left")==None):
      weirdTree["left"]=value
      return    
  if(value>weirdTree["value"]):
    if(weirdTree.get("right")==None):
      weirdTree["right"]=value
      return
  if (weirdTree.get("down")==None):
    weirdTree["down"]={}
  insertInWeirdTree(weirdTree["down"], value)

def readSpine(weirdTree):
  solution=""
  while(weirdTree):
    solution =solution+str(weirdTree["value"])
    weirdTree=weirdTree.get("down")
  return solution

def calculateSpire(rows, id=None):
  weirdTree={}
  for element in rows:
    insertInWeirdTree(weirdTree, element)
  return {"score":int(readSpine(weirdTree)), "tree":weirdTree, "id": id}

def solve():
  rows=openFile("raw.txt")
  row, _=parseRows(rows)
  return calculateSpire(row["elements"])["score"]


def solve2():
  rows=openFile("raw.txt")
  parsedRows=parseRows2(rows)
  swordValues=[]
  for row in parsedRows:
    swordValues.append(int(calculateSpire(row["elements"])["score"]))
  
  return max(swordValues)-min(swordValues)

def sortInsideTree(a,b):
  if(a):
    aValue=int(str(a.get("left", ''))+str(a.get("value"))+ str(a.get("right", '')))
  else:
    aValue=0
  if(b):
    bValue=int(str(b.get("left", ''))+str(b.get("value"))+ str(b.get("right", '')))
  else:
    bValue=0
    if(aValue==0 and bValue==0):
      return 0
  if(aValue<bValue):
    return 1
  if(aValue>bValue):
    return -1
  return sortInsideTree(a.get("down"), b.get("down"))

def checkSum(sortedSwords):
  result=0
  for i, sword in enumerate(sortedSwords):
    result=result+(i+1)*int(sword["id"])
  return result


def sortTree(a,b):
  if(a.get("score")<b.get("score")):
    return 1
  elif(a.get("score")>b.get("score")):
    return -1
  else:
    valueOfSort=sortInsideTree(a.get("tree"), b.get("tree"))
    if(valueOfSort!=0):
      return valueOfSort
    else:
      if(int(a.get("id"))<int(b.get("id"))):
        return 1
      else:
        return -1

def solve3():
  rows=openFile("raw.txt")
  parsedRows=parseRows2(rows)
  swords=[]
  for row in parsedRows:
    swords.append(calculateSpire(row["elements"], row["id"]))
  
  sortedSwords=sorted(swords, key=cmp_to_key(sortTree))

  # for x in sortedSwords:
  #   print(x["id"])
  return checkSum(sortedSwords)

# print(solve())
# print(solve2())
print(solve3())
