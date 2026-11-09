from utility import *

def parseRows(rows):
  return  rows

def evaluateIds(id):
  newDict={}
  for char in id:
    newDict[char]=newDict.get(char,0)+1

  values = newDict.values()
  return int(2 in values), int(3 in values)
  

def solve():
  rows=getOldAocInput(2)
  ids=parseRows(rows)
  resultTwo=0
  resultThree=0
  for id in ids:
    two, three=evaluateIds(id)
    resultTwo=resultTwo+two
    resultThree=resultThree+three
  return resultTwo*resultThree

def hammingDistance(id1, id2):
  lenId=len(id1)
  result=0
  for i in range(lenId):
    if(id1[i]==id2[i]):
      result=result+1
  return lenId-result


def solve2():
  rows=getOldAocInput(2)
  ids=parseRows(rows)
  idDict={}
  for id1 in ids:
    idDict[id1]=[]
    for id2 in ids:
      if(id1==id2):
        continue
      idDict[id1].append(hammingDistance(id1,id2))

  minHammingDistance=float("inf")
  minimalElements=[]
  for key, value in idDict.items():
    minDistance=min(value)
    if(minHammingDistance==minDistance):
      minimalElements.append(key)
    elif (minDistance<minHammingDistance):
      minimalElements=[]
      minimalElements.append(key)
      minHammingDistance=minDistance

  id1=[x for x in minimalElements[0]]
  id2=[x for x in minimalElements[1]]

  result=""
  lenId=len(id1)
  for i in range(lenId):
    if(id1[i]==id2[i]):
      result=result+id1[i]
  
  return result

print(solve())
print(solve2())