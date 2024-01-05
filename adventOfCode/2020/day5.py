from utility import *

def findRowColSeat(row):
  rowS=''
  for element in row[:7]:
    if (element=="F"):
      rowS=rowS+"0"
    else:
      rowS=rowS+"1"
  colS=''
  for element in row[7:]:
    if(element=="L"):
      colS=colS+"0"
    else:
      colS=colS+"1"
  return fromBinaryToInteger(rowS), fromBinaryToInteger(colS)

def evaluateSeat(seat):
  rowS, colS=findRowColSeat(seat)
  return rowS*8+colS

def solve(part):
  rows= getOldAocInput(5)
  if(part=="a"):
    maxID=0
    for row in rows:
      maxID=max(maxID, evaluateSeat(row))
    return maxID
  else:
    seats={}
    for row in rows:
      theRow, theCols=findRowColSeat(row)
      if(seats.get(theRow)==None):
        seats[theRow]=[]
      seats[theRow].append(theCols)
    for k,v in seats.items():
      if(len(v)==7):
        shouldBeIn=[0,1,2,3,4,5,6,7]
        for element in shouldBeIn:
          if(element not in v):
            return k*8+element
print(solve("a"))
print(solve("b"))
