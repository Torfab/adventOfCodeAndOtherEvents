from utility import *

def parseRows(rows):
  nailOrder= [int(x)-1 for x in rows[0].split(',')]
  return nailOrder

def solve():
  rows=openFile("raw.txt") # it returns an array of lines of the file
  nailOrder=parseRows(rows)
  nails=256
  halfNails=nails//2
  result=0
  for idx in range(len(nailOrder)-1):
    if (nailOrder[idx]+halfNails)%nails==nailOrder[idx+1]:
      result=result+1

  return result

def solve2():
  rows=openFile("raw.txt")
  nailOrder=parseRows(rows)
  status={}
  result=0

  for idx in range(len(nailOrder)-1):

    start=min(nailOrder[idx], nailOrder[idx+1])
    end=max(nailOrder[idx], nailOrder[idx+1])

    for element in range(start+1, end):
      for innerElement in status.get(element,[]):
        if innerElement<start or innerElement>end:
          result=result+1

    status.setdefault(nailOrder[idx], set()).add(nailOrder[idx+1])
    status.setdefault(nailOrder[idx+1], set()).add(nailOrder[idx])

  return result
  
def solve3():
  rows=openFile("raw.txt")
  nailOrder=parseRows(rows)
  nails=256
  status={}

  for idx in range(len(nailOrder)-1):

    status[nailOrder[idx]]=status.get(nailOrder[idx], [])+[nailOrder[idx+1]]
    status[nailOrder[idx+1]]=status.get(nailOrder[idx+1], [])+[nailOrder[idx]]

  couples=[]
  for i in range(nails-1):
    for j in range(i+1, nails):
      couples.append((i,j))

  maxTentative=0
  for couple in couples:

    innerResult=0
    for element in range(couple[0]+1, couple[1]):
      for innerElement in status.get(element, []):
        if innerElement<couple[0] or innerElement>couple[1]:
          innerResult=innerResult+1

    if innerResult>maxTentative:
      maxTentative=innerResult

  return maxTentative


# print(solve())
print(solve2())
# print(solve3())

