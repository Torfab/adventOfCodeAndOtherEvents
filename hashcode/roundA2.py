
def sumLeftPancake(idx, Lmap, arrPancake):
  if(Lmap.get(idx)!=None):
    return Lmap[idx]
  else:
    
    foundElement=-1
    for elementIdx in reversed(range(idx-1)):
      if(Lmap.get(elementIdx)!=None):
        foundElement=elementIdx
        break
    if(foundElement==-1):
      Lmap[0]=arrPancake[0]
      foundElement=0
    mySum=Lmap[foundElement]
    for elementIdx in range(foundElement+1, idx+1):
      mySum=mySum+arrPancake[elementIdx]
      Lmap[elementIdx]=mySum
    return mySum
  
def sumRightPancake(idx, Rmap, arrPancake, lenPancake):
  if(Rmap.get(idx)!=None):
    return Rmap[idx]
  else:
    
    foundElement=-1
    for elementIdx in range(idx, lenPancake):
      if(Rmap.get(elementIdx)!=None):
        foundElement=elementIdx
        break
    if(foundElement==-1):
      Rmap[lenPancake-1]=arrPancake[-1]
      foundElement=lenPancake-1
    mySum=Rmap[foundElement]
    for elementIdx in reversed(range(idx, foundElement)):
      mySum=mySum+arrPancake[elementIdx]
      Rmap[elementIdx]=mySum
    return mySum

numberOfTestCases=int(input())



for testCase in range(numberOfTestCases):
  input()
  numPancake=[int(x) for x in input().split(" ")]
  lenPancake=len(numPancake)
  La, Ra, Lb, Rb= [int(x)-1 for x in input().split(" ")]

  mySum=0
  if (Ra<=Lb):
    distance=Lb-Ra
    taking=distance//2
    for idx in range(Ra+taking+1):
      mySum=mySum+numPancake[idx]
  elif (La>=Rb):
    distance=La-Rb
    taking=distance//2
    for idx in range(La-taking, lenPancake):
      mySum=mySum+numPancake[idx]
  else:
    LMap={}
    RMap={}
    bestMaxMin=0
    result=0

    Lintersection=max(La, Lb)
    Rintersection=min(Ra, Rb)

    if(Lintersection==Lb):
      Lintersection=Lintersection+1
      result=sumLeftPancake(Lb, LMap, numPancake)
      # print("check id", Lb, "intersezione sinistra risultat", result)
    bestMaxMin=max(result, bestMaxMin)

    if(Rintersection==Rb):
      Rintersection=Rintersection-1
      result=sumRightPancake(Rb, RMap, numPancake, lenPancake)
      # print("check id", Rb, "intersezione destra risultat", result)

    bestMaxMin=max(result, bestMaxMin)

    for idx in range(Lintersection, Rintersection+1):
      result1=sumLeftPancake(idx, LMap, numPancake)
      result2=sumRightPancake(idx, RMap, numPancake, lenPancake)
      # print("check id", idx, "ho risultati", result1, result2)
      result=min(result1, result2)
      bestMaxMin=max(result, bestMaxMin)
    
    mySum=bestMaxMin
    # print(LMap, RMap)

  print("Case #", end="")
  print(testCase+1, end="")
  print(": ", end="")
  print(mySum)