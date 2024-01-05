from utility import *


def solve(part):
  
  rows= getOldAocInput(3)
  grid, maxX, maxY=buildGridWithDots(rows)
  

  if(part=="a"):
    movements=[(3,1)]
  if(part=="b"):
    movements=[(1,1),(3,1),(5,1),(7,1),(1,2)]

  count=[]
  for movement in movements:
    singleCount=0
    current=(0,0)
    while(current[1]<maxY):
      current=sumTupleValueByValue(current, movement)
      if(current[0]>maxX):
        current=(current[0]%(maxX+1), current[1])
      if(grid.get(current)!=None):
        singleCount=singleCount+1
    count.append(singleCount)
  finalCount=1
  for element in count:
    finalCount=finalCount*element
  return finalCount

print(solve("a"))
print(solve("b"))
