from utility import *

def insertInTable(label, depth, lookupTree, alreadyIn):
  item={"depth":depth}
  if(lookupTree.get(label)==None):
    lookupTree[label]=[]
  for node in lookupTree[label]:
    if node in alreadyIn:
      continue
    newAlreadyIn=alreadyIn.copy()
    newAlreadyIn.append(node)
    item[node]= insertInTable(node, depth+1, lookupTree, newAlreadyIn)
  return item

def parseRows(rows):
  tree={}
  for row in rows:
    root, leaves=row.split(":")
    tree[root]=leaves.split(",")
    tree["@"]=[]

  newTree={}
  newTree["RR"]=insertInTable("RR", 0, tree, ["RR"])
  return newTree



def appleEvaluator(item,evaluations, isFruit):
  if isFruit and len(item)==1:
    evaluations[item["depth"]]=evaluations.get(item["depth"],0)+1
  for node, value in item.items():
    if node=="depth":
      continue
    appleEvaluator(value, evaluations, node=="@")
    

def findRouteForWinnerLeaf(pathComposition, item, targetDepth, onlyFirstLetter=False):
  if len(item)==1:
    if(targetDepth==item["depth"]):
      return pathComposition
    return False
  for node, value in item.items():
    if node=="depth":
      continue
    if(onlyFirstLetter):
      nodeString=node[0]
    else:
      nodeString=node
    checkFound=findRouteForWinnerLeaf(pathComposition+nodeString, value, targetDepth, onlyFirstLetter)
    if(checkFound):
      return checkFound


def solve(onlyFirstLetter):
  rows=openFile("raw.txt")
  tree=parseRows(rows)
  evaluations={}
  appleEvaluator(tree["RR"], evaluations, False)

  winnerDepth=[k for k,v in evaluations.items() if v==1 ][0]

  if(onlyFirstLetter):
    labelToStart="R"
  else:
    labelToStart="RR"
  return findRouteForWinnerLeaf(labelToStart,tree["RR"], winnerDepth, onlyFirstLetter)

print(solve(False))
print(solve(True))
print(solve(True))


