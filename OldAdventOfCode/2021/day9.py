from utility import *

distanceVector=[(0,1), (0,-1), (1,0), (-1,0)]

def solve1():
  rows= getAocInput(9,2021)
  dictOfHeights=dict()

  for idx, row in enumerate(rows):
    for jdx, columun in enumerate(row):
      dictOfHeights[(idx,jdx)]=int(columun)

  result=0
  for element in dictOfHeights:
    isLowerAllDirection=4
    
    for distance in distanceVector:
      valueToCheck=dictOfHeights.get(sumTupleValueByValue(element,distance))
      if(valueToCheck==None):
        isLowerAllDirection=isLowerAllDirection-1
        continue
      if (dictOfHeights[element]<valueToCheck):
        isLowerAllDirection=isLowerAllDirection-1
      else:
        break
    if(isLowerAllDirection==0):
      result=result+1+dictOfHeights[element]

  return result

def solve2():
  rows= getAocInput(9,2021)
  dictOfHeights=dict()

  for idx, row in enumerate(rows):
    for jdx, columun in enumerate(row):
      dictOfHeights[(idx,jdx)]=int(columun)

  lowPoints=[]
  for element in dictOfHeights:
    isLowerAllDirection=4
    
    for distance in distanceVector:
      valueToCheck=dictOfHeights.get(sumTupleValueByValue(element,distance))
      if(valueToCheck==None):
        isLowerAllDirection=isLowerAllDirection-1
        continue
      if (dictOfHeights[element]<valueToCheck):
        isLowerAllDirection=isLowerAllDirection-1
      else:
        break
    if(isLowerAllDirection==0):
      lowPoints.append(element)

  basins=[]
  for lowPoint in lowPoints:
    visited=[lowPoint]
    border=[lowPoint]
    while (len(border)>0):
      for idx in reversed(range(len(border))):
        for distance in distanceVector:
          newCandidate=sumTupleValueByValue(border[idx], distance)
          if(dictOfHeights.get(newCandidate)!=None and (newCandidate not in visited)):
            if(dictOfHeights[newCandidate]!=9):
              visited.append(newCandidate)
              border.append(newCandidate)
        border.pop(idx)
    basins.append(len(visited))

  basins.sort()

  result=1
  for element in basins[-3:]:
    result=result*element

  return result

print(solve2())