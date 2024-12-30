from utilityz import *



def parseRows(rows):
  return [int(x) for x in rows[0]]

def doATurn(cups: list):
  print("valuto", cups)
  first=cups.pop(1)
  second=cups.pop(1)
  third=cups.pop(1)
  current=cups[0]
  destination=current-1
  while(destination not in cups):
    if(destination==0):
      destination=9
    else:
      destination=destination-1
  toPut=cups.index(destination)+1
  cups.insert(toPut, third)
  cups.insert(toPut, second)
  cups.insert(toPut, first)
  return cups[1:]+cups[:1]



def solve():
  rows=getOldAocInput(23)
  cups=parseRows(rows)

  for _ in range(100):
    cups=doATurn(cups)

  idResult=cups.index(1)
  result=cups[idResult+1:]+cups[:idResult]
  print("final", result)
  return "".join([str(x) for x in result])

print(solve())
# print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))
