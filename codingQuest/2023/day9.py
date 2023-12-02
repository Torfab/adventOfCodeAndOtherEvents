from utility import *

def evaluateDepth(tree: dict):
  if(tree.get("value")==None):
    return 0
  else:
    score=max(tree["depth"], evaluateDepth(tree["left"]),evaluateDepth(tree["right"]))
  return score

def updateWidthList(widthList, tree:dict):
  if(tree.get("value")==None):
    return
  else:
    widthList[tree["depth"]-1]=widthList[tree["depth"]-1]+1
    updateWidthList(widthList, tree["left"])
    updateWidthList(widthList, tree["right"])

def evaluateWidth(depth, tree):
  widthList=[0 for _ in range(depth)]
  updateWidthList(widthList, tree)
  return max(widthList)

def insertElementInTree(element, depth, tree:dict):
  if(tree.get("value")==None):
    tree["value"]=element
    tree["left"]={}
    tree["right"]={}
    tree["depth"]=depth
  else:
    if(element>tree["value"]):
      insertElementInTree(element, depth+1, tree["right"])
    else:
      insertElementInTree(element, depth+1, tree["left"])
  return

def solve():
  rows=openFile("input.txt")

  tree={}

  for element in rows:
    insertElementInTree(element, 1, tree)

  depth = evaluateDepth(tree)
  width = evaluateWidth(depth, tree)

  return depth*width
  
print(solve())