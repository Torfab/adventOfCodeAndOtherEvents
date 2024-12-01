from utility import *

def parseRows(rows):
  left=[]
  right=[]
  for row in rows:
    rowLeft, rowRight=row.split("   ")
    left.append(int(rowLeft))
    right.append(int(rowRight))

  left.sort()
  right.sort()
  return left, right


def solve(part):
  rows=getOldAocInput(1)
  left, right=parseRows(rows)

  result=0

  if(part=="a"):
    for i in range(len(left)):
      result=result+abs(left[i]-right[i])
  
  if part=="b":
    for l in left:
      count=0
      for r in right:
        if l==r:
          count=count+1
        if l<r:
          break
      result=result+l*count

  return result



print(solve("a"))
print(solve("b"))