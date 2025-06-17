from utilityz import *

def extractNumberAndLetter(row):
  splittedRow=row.split(" ")
  id1=int(splittedRow[1][3:])
  splittedRowLeft=splittedRow[2].split("=[")
  splittedRowLeft=splittedRowLeft[1][:-1]
  splittedRowLeft=splittedRowLeft.split(",")
  num, letter=int(splittedRowLeft[0]), splittedRowLeft[1]
  splittedRowRight=splittedRow[3].split("=[")
  splittedRowRight=splittedRowRight[1][:-1]
  splittedRowRight=splittedRowRight.split(",")
  num2, letter2=int(splittedRowRight[0]), splittedRowRight[1]
  return id1, num, letter, id1, num2, letter2

def insertElementInTree(id, num, letter, depth, tree):
  if not tree:
    tree["id"]=id
    tree["depth"]=depth
    tree["value"]=num
    tree["letter"]=letter
    tree["left"]={}
    tree["right"]={}
    return
  
  if(num<tree["value"]):
    insertElementInTree(id, num, letter, depth+1, tree["left"])
  else:
    insertElementInTree(id, num, letter, depth+1, tree["right"])

def newCountDepthTree(tree, depth, results):
  if(not tree):
    return
  results[depth]=results.get(depth,0)+1
  tree["depth"]=depth
  newCountDepthTree(tree["left"], depth+1,  results)
  newCountDepthTree(tree["right"], depth+1, results)

def readDepthTree(depth, tree, word):
  if not tree:
    return
  if tree["depth"]==depth:
    word.append(tree["letter"])
    return
  readDepthTree(depth, tree["left"], word)
  readDepthTree(depth, tree["right"], word)

def extrapolateWordingFromTree(tree):
  results={}
  newCountDepthTree(tree, 0, results)
  print(results)
  maxV=0
  maxK=-1
  for k,v in results.items():
    if v>maxV:
      maxV=v
      maxK=k
  word=[]
  print(maxK)
  readDepthTree(maxK, tree, word)
  return "".join(word)

def findElementId(tree, id1, results):
  border=[tree]
  while(border):
    item=border.pop()
    if item["id"]==id1:
      results.append(item)
    else:
      if(item["left"]):
        border.append(item["left"])
      if(item["right"]):
        border.append(item["right"])

def swapElementsValues(leftTree, rightTree, swap1):
  results=[]
  findElementId(leftTree, swap1, results)
  findElementId(rightTree, swap1, results)
  leftElement=results[0]
  rightElement=results[1]
  tempNum=leftElement["value"]
  tempLetter=leftElement["letter"]
  leftElement["value"]=rightElement["value"]
  leftElement["letter"]=rightElement["letter"]
  rightElement["value"]=tempNum
  rightElement["letter"]=tempLetter

def swapElementsNodes(leftTree, rightTree, swap1):
  results=[]
  findElementId(leftTree, swap1, results)
  findElementId(rightTree, swap1, results)
  leftElement=results[0]
  rightElement=results[1]
  tempNum=leftElement["value"]
  tempLetter=leftElement["letter"]
  tempNodesLeft=leftElement["left"]
  tempNodesRight=leftElement["right"]
  tempNodesDepth=leftElement["depth"]
  leftElement["value"]=rightElement["value"]
  leftElement["letter"]=rightElement["letter"]
  leftElement["left"]=rightElement["left"]
  leftElement["right"]=rightElement["right"]
  leftElement["depth"]=rightElement["depth"]
  rightElement["value"]=tempNum
  rightElement["letter"]=tempLetter
  rightElement["left"]=tempNodesLeft
  rightElement["right"]=tempNodesRight
  rightElement["depth"]=tempNodesDepth


def parseRows(rows, swapMode):
  leftTree={}
  rightTree={}
  for row in rows:
    if row[0]=="A":
      lId, lNum, lLetter, rId, rNum, rLetter=extractNumberAndLetter(row)
      insertElementInTree(lId, lNum, lLetter, 0, leftTree)
      insertElementInTree(rId, rNum, rLetter, 0, rightTree)
    if row[0]=="S":
      swapMode(leftTree, rightTree, int(row.split(" ")[1]))
    print(row, "left", leftTree)
    print(row, "right", rightTree)

  return extrapolateWordingFromTree(leftTree)+extrapolateWordingFromTree(rightTree)



  # return leftTree, rightTree


def solve(swapMode):
  rows=openFile("raw.txt")
  rows=parseRows(rows, swapMode)
  return rows
  
# print(solve(swapElementsValues))
print(solve(swapElementsNodes))