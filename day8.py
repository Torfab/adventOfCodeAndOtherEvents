from utilities import *


def markLines(trees):
  for i in range(len(trees)):
    minHeight=-1
    for j in range(len(trees)):
      if(trees[i][j]["height"]>minHeight):
        minHeight=trees[i][j]["height"]
        trees[i][j]["marked"]=True

  for i in range(len(trees)):
    minHeight=-1
    for j in reversed(range(len(trees))):
      if(trees[i][j]["height"]>minHeight):
        minHeight=trees[i][j]["height"]
        trees[i][j]["marked"]=True

def markColumn(trees):
  for j in range(len(trees)):
    minHeight=-1
    for i in range(len(trees)):
      if(trees[i][j]["height"]>minHeight):
        minHeight=trees[i][j]["height"]
        trees[i][j]["marked"]=True
  for j in range(len(trees)):
    minHeight=-1
    for i in reversed(range(len(trees))):
      if(trees[i][j]["height"]>minHeight):
        minHeight=trees[i][j]["height"]
        trees[i][j]["marked"]=True


def markTrees(trees):
  markLines(trees)
  markColumn(trees)

def solve1():
  rows=getAocInput(8)

  trees=[]
  for idx, element in enumerate(rows):
    trees.append([])
    for tree in element:
      trees[idx].append(dict(height=int(tree), marked=False))
  markTrees(trees)

  accumulatore=0
  for lineOfTrees in trees:
    for tree in lineOfTrees:
      if (tree["marked"]==True):
        accumulatore=accumulatore+1

  return accumulatore

def checkScore(trees, i, j):
  maxHeight=trees[i][j]

  sum=0
  result=1
  for jdx in range(j+1, len(trees[i])):
    sum=sum+1
    if(trees[i][jdx]>=maxHeight):
      break
  result=result*sum

  sum=0
  for jdx in reversed(range(j)):
    sum=sum+1
    if(trees[i][jdx]>=maxHeight):
      break
  result=result*sum

  sum=0
  for idx in range(i+1, len(trees)):
    sum=sum+1
    if(trees[idx][j]>=maxHeight):
      break
  result=result*sum
  sum=0

  for idx in reversed(range(i)):
    sum=sum+1
    if(trees[idx][j]>=maxHeight):
      break
  result=result*sum

  return result

def solve2():
  rows=getAocInput(8)

  trees=[]
  for idx, element in enumerate(rows):
    trees.append([])
    for tree in element:
      trees[idx].append(int(tree))

  score=0
  for idx,lineOfTrees in enumerate(trees):
    for jdx, tree in enumerate(lineOfTrees):
      score=max(score, checkScore(trees, idx, jdx))
        

  return score

print(solve1())
print(solve2())