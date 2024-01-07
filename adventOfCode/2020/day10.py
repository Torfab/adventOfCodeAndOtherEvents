from utilityz import getOldAocInput

def buildAdaptersChain(rows):
  return [int(x) for x in rows]

def solveA():
  rows= getOldAocInput(10)
  adapters=buildAdaptersChain(rows)+[0]
  adapters.sort()
  adaptersDifference={1:0,2:0,3:1}
  for idx in range(1, len(adapters)):
    adaptersDifference[adapters[idx]-adapters[idx-1]]+=1

  return adaptersDifference[1]*adaptersDifference[3]

def checkRemovable(adapters, idx):
  if(adapters[idx+1]-adapters[idx-1]>3):
    return False
  return True

def solveB():
  rows= getOldAocInput(10)
  adapters=buildAdaptersChain(rows)+[0]
  adapters.sort()
  removables=[]
  for idx in range(1, len(adapters)-1):
    if(checkRemovable(adapters, idx)):
      removables.append(idx)

  print(removables)
  print(len(removables))
  print(2**len(removables))

def solveC():
  rows= getOldAocInput(10)
  adapters=buildAdaptersChain(rows)+[0]
  adapters.sort()
  adapters.append(adapters[-1]+3)

  adapterDifferences=[]
  for i in range(1, len(adapters)):
    adapterDifferences.append(adapters[i]-adapters[i-1])
  groupsOfOnes=[]
  insideGroup=0
  for difference in adapterDifferences:
    if(difference==3):
      if(insideGroup!=0):
        groupsOfOnes.append(insideGroup)
        insideGroup=0
      continue
    insideGroup=insideGroup+1


  print(adapters)
  print(adapterDifferences)
  print(groupsOfOnes)
  

# print(solveA())
# print(solveB())
print(solveC())
