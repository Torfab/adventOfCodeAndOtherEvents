def codify(realMap, word):
  tempArray=[]
  for element in word:
    tempArray.append(str(realMap[element]))
  return "".join(tempArray)

numberOfTestCases=int(input())



mapAlphabetDigital=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for testCase in range(numberOfTestCases):
  codeAlphabet=input()
  alphabetDigital= [int(x) for x in codeAlphabet.split(" ")]
  realMap={}
  for idx in range(len(mapAlphabetDigital)):
    realMap[mapAlphabetDigital[idx]]=alphabetDigital[idx]

  numberOfWords=int(input())
  newMap={}
  oldLenSet=0
  isFine=True
  for element in range(numberOfWords):
    if(isFine==False):
      input()
      continue
    codified=codify(realMap, input().lower())
    if(newMap.get(codified)==None):
      newMap[codified]=True
    else:
      isFine=False
  
  print("Case #", end="")
  print(testCase+1, end="")
  print(": ", end="")
  if(isFine):
    print("NO")
  else:
    print("YES")
