def buildArrayOfDistances(secondLine):
  tempArray=[]
  for idx in range(len(secondLine)-1):
    tempArray.append(secondLine[idx+1]-secondLine[idx])
  return tempArray

numberOfTestCases=int(input())

for testCase in range(numberOfTestCases):
  M,R,_= [int(x) for x in input().split(" ")]
  secondLine= [int(x) for x in input().split(" ")]
  secondLine.insert(0, -R)
  secondLine.append(M+R)
  secondLineDistance=buildArrayOfDistances(secondLine)
  cursor=0
  lenDistance=len(secondLineDistance)
  isImpossible=False
  bulbs=0
  while(True):
    if(cursor>=lenDistance):
      break
    if(secondLineDistance[cursor]>(2*R)):
      isImpossible=True
      break
    else:
      partialSum=secondLineDistance[cursor]
      cursor=cursor+1
      if(cursor>=lenDistance):
        break
      while(partialSum+secondLineDistance[cursor]<=(2*R)):
        partialSum=partialSum+secondLineDistance[cursor]
        cursor=cursor+1
        if(cursor>=lenDistance):
          break
      if(cursor>=lenDistance):
        break
      bulbs=bulbs+1
  
  print("Case #", end="")
  print(testCase+1, end="")
  print(": ", end="")
  if(isImpossible):
    print("IMPOSSIBLE")
  else:
    print(bulbs)
