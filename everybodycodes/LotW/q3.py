from utility import *

# not happy about bruteforce part 3, could prune a lot doing reverse direction search but it is what it is and the texts werent's o long so i had no optimizaiton problems

def parseRows(rows):
  newRows=[]
  for row in rows:
    newRows.append(row.split("-")[1].split(" "))
  return newRows

def evaluateIso(potenze, valori):
  valori=str(valori)
  result=0
  size=len(valori)-1
  i=size
  sizeJ=len(potenze)-1
  j=sizeJ
  while(i>=0):
    result=result+int(valori[i])*int(potenze[j])**(size-i)
    i=i-1
    j=j-1
    if(j<0):
      j=sizeJ
  return result

def findMinimum(potenze, result):
  test=0
  while(True):
    test=test+1
    if(result==evaluateIso(potenze, test)):
      return test

def solve3():
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  arrayResult=[]
  for pair in rows:
    potenze=pair[0]
    valori=pair[1]
    result=evaluateIso(potenze, valori)
    minimum=findMinimum(potenze, result)
    print("ho trovato", minimum)
    if minimum==int(valori):
      arrayResult.append(result)

  return sum(arrayResult)

# print(solve1())
print(solve3())
