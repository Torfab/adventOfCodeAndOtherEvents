from utility import *

# to evaluate an approach of another grid with cumulative sum of eveything starting at 1,1 and ending at 300,300. then include/exclude rectangles
# so if i've to compute size 5 at 3,4  i have to just see cumulative sum at 8,9 then remove 2,9 then remove 8,3 and since i removed twice the corner just re-add 2,3
# This precompute 90k elements but litterally bring a O(n^5) to a O(n^3) where instead of doing a lot of lookups, every box have same number of lookups, always 4.

def parseRows(rows):
  return int(rows[0])

def evaluatePower(x,y, gridSerialNumber):
  rackId=x+10
  power=rackId
  power=power*y
  power=power+gridSerialNumber
  power=power*rackId
  power=(power//100)%10
  power=power-5
  return power

# print(evaluatePower(2,1,18))

def evaluateBox(myGrid, x, y, size):
  result=0
  for j in range(size):
    for i in range(size):
      result=result+myGrid[(x+i, y+j)]
  return result

def solve(part):
  rows=getOldAocInput(11)
  gridSerialNumber=parseRows(rows)

  myGrid={}
  for j in range(1,301):
    for i in range(1, 301):
      myGrid[(i,j)]=evaluatePower(i,j, gridSerialNumber)
      # myGrid[(i,j)]=evaluatePower(i,j, 18)

  # print(myGrid)

  if(part==1):
    maxBox=-float("inf")
    maxCoords=(0,0)
    for y in range(1, 299):
      for x in range(1, 299):
        tentative= evaluateBox(myGrid, x,y, 3)
        if(tentative>maxBox):
          maxBox=tentative
          maxCoords=(x, y)
        
    return str(maxCoords[0])+","+str(maxCoords[1])

  if(part==2):
    maxBox=-float("inf")
    maxCoords=(0,0)
    for size in range(1, 30): #this heuristic works since expected single cell vaule is -0.5 so the bigger the more average and the sum will decreases. Local anomalies should be small
      for y in range(1, 302-size):
        for x in range(1, 302-size):
          tentative= evaluateBox(myGrid, x,y, size)
          if(tentative>maxBox):
            maxBox=tentative
            maxCoords=(x, y, size)
      # print(maxCoords, size)
        
    return str(maxCoords[0])+","+str(maxCoords[1])+","+str(maxCoords[2])


print(solve(1))
print(solve(2))
