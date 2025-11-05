from utility import *
import math

def sumComplex(tup1, tup2):
  return (tup1[0]+tup2[0], tup1[1]+tup2[1])

def multiplyComplex(tup1, tup2):
  return (tup1[0]*tup2[0]-tup1[1]*tup2[1], tup1[0]*tup2[1]+tup1[1]*tup2[0])

def divComplex(tup1,tup2):
  return (math.trunc(tup1[0]/tup2[0]), math.trunc(tup1[1]/tup2[1]))

def parseRows(rows):
  return rows[0]



def solve():
  rows=openFile("raw.txt")
  complexNumber=parseRows(rows)
  complexNumber=tuple(complexNumber.split("[")[1][:-1].split(","))
  complexNumber=(int(complexNumber[0]), int(complexNumber[1]))

  result=(0,0)
  for _ in range(3):
    result=multiplyComplex(result, result)
    result=divComplex(result,(10,10))
    result=sumComplex(result, complexNumber)

  finalResult="["+str(result[0])+","+str(result[1])+"]"
  return finalResult

def isToEngrave(coords):
  current=(0,0)
  for _ in range(100):
    current=multiplyComplex(current, current)
    current=divComplex(current, (100000,100000))
    current=sumComplex(current, (coords[0],coords[1]))
    if(current[0]<-1000000 or current[1]<-1000000 or current[0]>1000000 or current[1]>1000000):
      return False
  return True

def solve2(step):
  rows=openFile("raw.txt")
  complexNumber=parseRows(rows)
  complexNumber=tuple(complexNumber.split("[")[1][:-1].split(","))
  complexNumber=(int(complexNumber[0]), int(complexNumber[1]))

  
  count=0
  for y in range(complexNumber[1], complexNumber[1]+1000+step, step):
    for x in range(complexNumber[0], complexNumber[0]+1000+step, step):
      if (isToEngrave((x,y))):
        count=count+1

  return count


# print (isToEngrave((36250, -64270)))
# print(solve())
# print(solve2(10))
print(solve2(1))
