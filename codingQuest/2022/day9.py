from utility import *


rows=openFile("input.txt")

directionVector=[(1,0), (-1,0), (0,1), (0,-1)]

def stampaMap(realMap):
  for row in range(len(rows)):
    for column in range(len(rows[0])):
      if(realMap.get((column,row))):
        print(realMap.get((column, row)), end="")
      else:
        print(" ", end="")
    print()

def solve():
  realMap={}

  for idxr, row in enumerate(rows):
    for idxc, column in enumerate(row):
      if(column=="#"):
        realMap[(idxc, idxr)]="#"

  start=(rows[0].index(" "), 0)
  end=(rows[0].index(" "), len(rows) )

  realMap[rows[0].index(" "),-1]="#"

  border=set()
  border.add(start)
  i=0
  while(len(border)>0):
    i=i+1
    newBorderSet=set()

    for element in border:
      # print(element)
      realMap[element]="."
      for direction in directionVector:
        tentative=sumTupleValueByValue(element, direction)
        if (tentative==end):
          return i-2
        if(realMap.get(tentative)==None):
          newBorderSet.add(tentative)
    border=newBorderSet
      
print(solve())
