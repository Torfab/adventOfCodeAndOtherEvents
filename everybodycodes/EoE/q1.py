from utilityz import *

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

def eni(N, exp, mod):
  result=[]
  start=1
  for _ in range(exp):
    start=(start*N)%mod
    result.insert(0, str(start))
  return int("".join(result))

def eniSmart(N, exp, mod):
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
  lenchain=len(chain)
  oldExp=exp
  exp=exp-indexFound
  exp=exp%lenchain
  result=""
  for _ in range(min(oldExp, 5)):
    exp=exp-1
    result=result+chainResult[exp%len(chainResult)]
  return int(result)
  

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
    print(first, second, third)
    i=i+1
    
  return maxResult

# print(solve(eni))
print(solve(eniSmart))