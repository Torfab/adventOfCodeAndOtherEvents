from utilityz import *



def solve():
  rows=openFile("raw.txt")
  rows=[int(x) for x in rows]
  minRows=min(rows)
  count=0
  for element in rows:
    count=count+element-minRows
  return count

def newSolve():
  rows=openFile("raw.txt")
  rows=[int(x) for x in rows]
  rows.sort()
  median=rows[len(rows)//2]
  median2=rows[len(rows)//2+1]

  firstCount=0
  for element in rows:
    firstCount=firstCount+abs(element-median)
  secondCount=0
  for element in rows:
    secondCount=secondCount+abs(element-median2)
  return min(firstCount, secondCount)

print(solve())
print(newSolve())

