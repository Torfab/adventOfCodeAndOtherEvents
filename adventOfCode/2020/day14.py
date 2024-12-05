from utility import *


def putMask(numb, mask):
  a=fromIntegerToBinary(numb).zfill(36)
  result=[]
  for i in range(len(a)):
    if(mask[i]=="X"):
      result.append(a[i])
    else:
      result.append(mask[i])
  return fromBinaryToInteger("".join(result))

def dfs(preSub, postSub):
  if(postSub[0]!="X"):
    if(len(postSub)==1):
      return [preSub+postSub]
    return dfs(preSub+postSub[0], postSub[1:])
  else:
    if(len(postSub)==1):
      return [preSub+"0", preSub+"1"]
    return dfs(preSub+"0", postSub[1:])+dfs(preSub+"1", postSub[1:])

def findAddresses(mainAddress, mask):
  mainAddress=fromIntegerToBinary(mainAddress).zfill(36)
  result=[]
  for i in range(len(mask)):
    if(mask[i]=="0"):
      result.append(mainAddress[i])
    else:
      result.append(mask[i])
  result="".join(result)
  allResults=dfs("", result)
  return allResults

def solve(part):
  rows=getOldAocInput(14)
  myMem={}
  for row in rows:
    if row[1]=="a":
      currentBitmask=[x for x in row.split(" ")[2]]
    else:
      idxMemory=int(row[4:].split("]")[0])
      if part=="a":
        myMem[idxMemory]=putMask(int(row.split(" ")[2]), currentBitmask)
      if part=="b":
        addresses=findAddresses(idxMemory,currentBitmask)
        currentValue=int(row.split(" ")[2])
        for address in addresses:
          myMem[address]=currentValue
      
  return sum([x for x in myMem.values()])
  
print(solve("a"))
print(solve("b"))
