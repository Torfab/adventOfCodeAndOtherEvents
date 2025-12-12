from utilityz import *

def parseRows(rows):
  spaces=[]
  for row in rows:
    if row=="":
      continue
    if row[-1].isdigit():
      rowSplitted=row.split(": ")
      size=tuple([int(x) for x in rowSplitted[0].split("x")])
      packages=tuple([int(x) for x in rowSplitted[1].split(" ")])
      spaces.append((size, packages))
  return spaces


def solve():
  rows=getOldAocInput(12)
  spaces=parseRows(rows)
  count=0
  for space in spaces:
    totalSize=space[0][0]*space[0][1]
    packages=sum(space[1])*9
    if totalSize>=packages:
      count=count+1
  return count

print(solve())