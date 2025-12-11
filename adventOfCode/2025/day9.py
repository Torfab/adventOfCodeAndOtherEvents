from utilityz import *


def solve():
  rows=getOldAocInput(9)
  points=parseRows(rows)
  listKey=list(points)
  maxArea=0

  for i in range(len(listKey)-1):
    for j in range(i+1, len(listKey)):
      a=listKey[i]
      b=listKey[j]
      tentative=(abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)
      maxArea=max(maxArea, tentative)
  return maxArea

def parseRows(rows):
  coords=[]
  for row in rows:
    rowSplitted=row.split(",")
    coords.append((int(rowSplitted[0]), int(rowSplitted[1])))
  return coords

def isValid(x1, y1, x2, y2, spans):
  if x1 > x2: x1,x2 = x2,x1
  if y1 > y2: y1,y2 = y2,y1
  for y in range(y1, y2+1):
    sx1, sx2 = spans[y]
    if x1 < sx1 or x1 > sx2 or x2 < sx1 or x2 > sx2:
        return False
  return True

def solve2():
  rows=getOldAocInput(9)
  coords=parseRows(rows)

  max_y = max([c[1] for c in coords])

  spans = [None for y in range(max_y+2)]
  coords.append(coords[0])

  #sorta di raycasying con amssima grandezza ricalcolata volta per volta
  for i in range(1, len(coords)):
    x1, y1 = coords[i-1]
    x2, y2 = coords[i]

    if x1 > x2: x1,x2 = x2,x1
    if y1 > y2: y1,y2 = y2,y1

    for y in range(y1,y2+1):
      if spans[y] is None:
        spans[y] = [x1, x2]
      else:
        sx1, sx2 = spans[y]
        spans[y] = [min(x1, sx1), max(x2, sx2)]
  coords.pop()


  maxArea=0
  for i in range(len(coords)-1):
    for j in range(i+1, len(coords)):
      a=coords[i]
      b=coords[j]
      tentative=(abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)
      if tentative<maxArea:
        continue
      else:
        if(isValid(a[0],a[1], b[0],b[1], spans)):
          maxArea=tentative
  return maxArea

print(solve())
print(solve2())
