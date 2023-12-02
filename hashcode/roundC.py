

numberOfTestCases=int(input())
for testCase in range(numberOfTestCases):
  input()
  secondLine=[int(x) for x in input().split(" ")]
  mapResult={}
  arrayResult=[]
  lastElement=None
  isImpossible=False
  for element in secondLine:
    if(lastElement==element):
      continue
    else:
      if(mapResult.get(element)!=None):
        isImpossible=True
        break
      mapResult[element]=True
      arrayResult.append(str(element))
      lastElement=element

  print("Case #", end="")
  print(testCase+1, end="")
  print(": ", end="")
  if(isImpossible):
    print("IMPOSSIBLE")
  else:
    print(" ".join(arrayResult))
