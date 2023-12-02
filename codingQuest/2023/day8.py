from utility import *
from itertools import permutations 

def findMinIndexNotInBorder(points:list , border:list):
  temp=points.copy()
  border.sort(reverse=True)
  for element in border:
    temp.pop(element)
  minimum=min(temp)

  return points.index(minimum)


def buildRows(rows):
  tempRows=[]
  for element in rows:
    tempElement=element.split(" ")
    tempRows.append([int(x) for x in tempElement])
  return tempRows

def solve():
  rows=openFile("input.txt")
  rows=buildRows(rows)

  minScore=2345623456

  points=[1,2,3,4,5,6,7,8,9,10,11]
  for singleP in permutations(points):
    score=0
    lastElement=0
    for element in singleP:
      score=score+rows[lastElement][element]
      lastElement=element
    score=score+rows[lastElement][0]
    if(score<minScore):
      minScore=score

  return minScore

print(solve())
