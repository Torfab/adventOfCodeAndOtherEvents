from utility import *

def parseRows(rows):

  newRows=[]
  for row in rows:
    newItem={}
    splittedRow=row.split(" ")
    for singleElement in splittedRow:
      splittedElement=singleElement.split("=")
      newItem[splittedElement[0]]=int(splittedElement[1])
    newRows.append(newItem)
  return newRows

def eni1(N, exp, mod):
  result=[]
  start=1
  for _ in range(exp):
    start=(start*N)%mod
    result.insert(0, str(start))
  return int("".join(result))

def eni2(N, exp, mod):
  chain=dict()
  chainResult=["1"]
  start=1
  indexFound=0
  for _ in range(exp):
    newStart=(start*N)%mod
    chain[start]=newStart
    chainResult.append(str(newStart))
    if(chain.get(newStart)!=None):
      if(newStart!=1):
        indexFound=chainResult.index(str(newStart))
        # print("index", indexFound, N, chain)
        chainResult=chainResult[indexFound:]
        
      chainResult.pop()
      # print(chainResult)
      break
    start=newStart
  lenchain=len(chainResult)
  if(exp<=lenchain):
    result=""
    for i in range(exp,0,-1):
      result=result+chainResult[i]
    return int(result)
  tempExp=exp-indexFound
  tempExp=tempExp%lenchain
  result=""
  for _ in range(min(exp, 5)):
    result=result+chainResult[tempExp%len(chainResult)]
    tempExp=tempExp-1
  return int(result)
  
def eni3(N, exp, mod):
  chain=dict()
  chainResult=[]
  start=1
  indexFound=0
  result=0
  for _ in range(exp):
    newStart=(start*N)%mod
    chain[start]=newStart
    chainResult.append(newStart)
    if(chain.get(newStart)!=None):
      if(newStart!=1):
        indexFound=chainResult.index(newStart)
        for element in range(1, indexFound):
          result=result+chainResult[element]
        chainResult=chainResult[indexFound:]
        chainResult.pop()
      break
    start=newStart
  lenchain=len(chainResult)
  if(exp<=lenchain):
    result=""
    for i in range(exp,0,-1):
      result=result+chainResult[i]
    return int(result)
  tempExp=exp-indexFound
  loops=tempExp//lenchain
  for element in chainResult:
    result=result+loops*element
  tempExp=tempExp%lenchain
  for element in range(tempExp):
    result=result+chainResult[element]
  return result

# print(eni3(2,7,5)) 
# print(eni3(3,8,16))
# print(eni3(4,3000,110)) 
# print(eni3(4,14000,110)) 
# print(eni3(6,15000,110)) 

def solve(theFunction):
  rows=openFile("raw.txt")
  rows=parseRows(rows)
  maxResult=0
  i=0
  for row in rows:
    first=theFunction(row["A"], row["X"], row["M"])
    second=theFunction(row["B"], row["Y"], row["M"])
    third=theFunction(row["C"], row["Z"], row["M"])
    maxResult=max(maxResult, first+second+third)
    i=i+1
    
  return maxResult

# print(solve(eni1))
# print(solve(eni2))
print(solve(eni3))