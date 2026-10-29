from utility import *

def parseRows(rows):
  return [int(x) for x in rows[0].split(",")]


def solve1():
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  result=0
  for element in rows:
    a=int(element**0.5)
    aSquared=a**2
    diff=element-aSquared
    if(diff==0):
      continue
    nextSquared=a+1
    nextSquared=nextSquared**2
    diff=nextSquared-element
    result=result+diff
  return result

def solve2():
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  result=0
  for element in rows:
    a=(element+4)//4
    if ((a*4-4)==element and a>=3):
      continue
    a=a+1
    while(a<3):
      a=a+1
    totalCones=a*4-4
    diff=totalCones-element
    result=result+diff
  return result

def solve3():
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  result=0
  for element in rows:
    a=int((element+1)**0.5)
    if ((a**2-1)==element and a>=3 and a%2!=0):
      # print("perfetto, ho ", element, "cones e mi riempiono perfettamente un quadrato di lato", a)
      continue
    a=a+1
    while(a<3 or a%2==0):
      a=a+1
    totalCones=a**2-1
    diff=totalCones-element
    # print("per l'elemento", element, "trovo che la diff mancante è ", diff, "perchè devo riempire un lato di ", a, "per un totale di", totalCones)
    result=result+diff
  return result


print(solve3())