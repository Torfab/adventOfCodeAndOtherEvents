from utilityz import *
import heapq

def parseRows(rows):
  junctionBoxes=[]
  for row in rows:
    rowSplitted=row.split(",")
    junctionBoxes.append((int(rowSplitted[0]), int(rowSplitted[1]), int(rowSplitted[2])))
  return junctionBoxes

def solve():
  rows=getOldAocInput(8)
  junctionBoxes=parseRows(rows)
  distances=[]

  for idx in range(len(junctionBoxes)-1):
    for jdx in range(idx+1, len(junctionBoxes)):
      heapq.heappush(distances, (eucledianDistance(junctionBoxes[idx], junctionBoxes[jdx], 3), idx, jdx))


  groups=[]
  for _ in range(1000):
    _, idx, jdx=heapq.heappop(distances)
    idxGroup=None
    jdxGroup=None
    for i, group in enumerate(groups):
      if idx in group:
        idxGroup=i
        break
    for i, group in enumerate(groups):
      if jdx in group:
        jdxGroup=i
        break
    
    if idxGroup!=None:
      if idxGroup==jdxGroup:
        continue
      if jdxGroup!=None:
        newUnion=groups[idxGroup].union(groups[jdxGroup])
        groups[min(idxGroup, jdxGroup)]=newUnion
        groups.pop(max(idxGroup, jdxGroup))
      else:
        groups[idxGroup].add(jdx)
    else:
      if jdxGroup!=None:
        groups[jdxGroup].add(idx)
      else:
        newSet=set()
        newSet.add(idx)
        newSet.add(jdx)
        groups.append(newSet)

  results=[]
  for group in groups:
    heapq.heappush(results, -len(group))
  
  result=1
  for _ in range(3):
    element=heapq.heappop(results)
    result=result*(-element)


  return result

def solve2():
  rows=getOldAocInput(8)
  junctionBoxes=parseRows(rows)
  distances=[]

  for idx in range(len(junctionBoxes)-1):
    for jdx in range(idx+1, len(junctionBoxes)):
      heapq.heappush(distances, (eucledianDistance(junctionBoxes[idx], junctionBoxes[jdx], 3), idx, jdx))

  dictGroup={}
  existentGroups=[]
  count=0
  while(len(existentGroups)!=1 or len(dictGroup)!=len(junctionBoxes)):
    count=count+1
    _, idx, jdx=heapq.heappop(distances)
    idxGroup=None
    jdxGroup=None
    if dictGroup.get(idx)!=None:
      idxGroup=dictGroup[idx]
    if dictGroup.get(jdx)!=None:
      jdxGroup=dictGroup[jdx]
      if idxGroup==jdxGroup:
        continue

    if idxGroup!=None:
      if jdxGroup!=None:
        theMin=min(idxGroup, jdxGroup)
        theMax=max(idxGroup, jdxGroup)
        existentGroups.remove(theMax)
        for k in dictGroup:
          if dictGroup[k]==theMax:
            dictGroup[k]=theMin
      else:
        dictGroup[jdx]=idxGroup
    else:
      if jdxGroup!=None:
        dictGroup[idx]=jdxGroup
      else:
        existentGroups.append(count)
        dictGroup[idx]=count
        dictGroup[jdx]=count
      
  return junctionBoxes[idx][0]*junctionBoxes[jdx][0]


print(solve2())
