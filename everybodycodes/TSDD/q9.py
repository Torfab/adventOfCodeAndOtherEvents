from utility import *

def parseRows(rows):
  candidates= {}
  for row in rows:
    splittedRow=row.split(":")
    candidates[splittedRow[0]]=splittedRow[1]
  return candidates

def checkPotentialParents(seq1, seq2, seq3):
  seq2Count=0
  seq3Count=0
  for i in range(len(seq1)):
    inside=False
    if seq1[i]==seq2[i]:
      inside=True
      seq2Count=seq2Count+1
    if seq1[i]==seq3[i]:
      inside=True
      seq3Count=seq3Count+1
    if not inside:
      return -1
    
  return seq2Count*seq3Count

def homeMadeCombinationAt2(arr):
  resultArr=[]
  for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
      resultArr.append([arr[i], arr[j]])
  return resultArr

def solve():
  rows=openFile("raw.txt") # it returns an array of lines of the file
  candidates=parseRows(rows)

  for k,v in candidates.items():

    arr=list(candidates.keys())
    arr.remove(k)
    print(arr)
    for potentialParents in homeMadeCombinationAt2(arr):
      result=checkPotentialParents(v, candidates[potentialParents[0]], candidates[potentialParents[1]])
      if result==-1:
        continue
      else:
        return result
  return -1

def solve2():
  rows=openFile("raw.txt") # it returns an array of lines of the file
  candidates=parseRows(rows)
  resultArray=[]


  for k,v in candidates.items():

    arr=list(candidates.keys())
    arr.remove(k)
    for potentialParents in homeMadeCombinationAt2(arr):
      result=checkPotentialParents(v, candidates[potentialParents[0]], candidates[potentialParents[1]])
      if result==-1:
        continue
      else:
        resultArray.append(result)
  return sum(resultArray)

def solve3():
  rows=openFile("raw.txt") # it returns an array of lines of the file
  candidates=parseRows(rows)
  families=[]
  for k,v in candidates.items():
    arr=list(candidates.keys())
    arr.remove(k)
    for potentialParents in homeMadeCombinationAt2(arr):
      result=checkPotentialParents(v, candidates[potentialParents[0]], candidates[potentialParents[1]])
      if result==-1:
        continue
      else:
        idxs=[]

        for idx, family in enumerate(families):
          if potentialParents[0] in family:
            idxs.append(idx)
          if potentialParents[1] in family and idx not in idxs:
            idxs.append(idx)
          if k in family and idx not in idxs:
            idxs.append(idx)

        if len(idxs)==0:
          families.append({potentialParents[0], potentialParents[1], k})
        else:
          bigJoin={potentialParents[0], potentialParents[1], k}
          idxs.sort(reverse=True)
          for idx in idxs:
            bigJoin.update(families[idx])
            families.pop(idx)
          families.append(bigJoin)
        break
  maxFamily=len(families[0])
  idx=0
  for id, family in enumerate(families):
    if(len(family)>maxFamily):
      maxFamily=len(family)
      idx=id
  return sum([int(x) for x in families[idx]])

# print(solve())
# print(solve2())
print(solve3())

