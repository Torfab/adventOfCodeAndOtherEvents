from utility import *

mynumbers={"nine":9,"eight":8,"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "sixteen":16}

def solve(part):
  rows=getOldAocInput(1)
  result=0
  for element in rows:
    first=-1
    last=-1
    newElement=element
    if(part=="b"):
      for thingy in mynumbers.keys():
        
        while(thingy in newElement):
          theindex=newElement.index(thingy)
          newElement=newElement[:theindex+2]+str(mynumbers[thingy])+newElement[theindex+2:]

    for digit in newElement:
      if(digit.isnumeric() and first==-1):
        first=digit
      if(digit.isnumeric()):
        last=digit
    newNumber=int(first+last)
    result=result+newNumber

  return result


print(solve("a"))
print(solve("b"))