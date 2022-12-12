from utilities import *

distanceVector=[[0,1],[0,-1],[1,0],[-1,0]]

def heightOfElement(element):
  return ord(element)-97

def comprehension(rows):
  newRows=[]
  for idx, element in enumerate(rows):
    newRows.append([])
    for jdx, height in enumerate(element):
      if(height=='S'):
        startingPoint=[idx,jdx]
        newRows[idx].append(heightOfElement('a'))
        continue
      if(height=='E'):
        endingPoint=[idx, jdx]
        newRows[idx].append(heightOfElement('z'))
        continue
      newRows[idx].append(heightOfElement(height))
  
  return newRows, startingPoint, endingPoint



def solve():
  rows= getAocInput(-1)
  newRows, startingPoint, EndingPoint= comprehension(rows)

  currentPoint=startingPoint

  print(newRows)



solve()