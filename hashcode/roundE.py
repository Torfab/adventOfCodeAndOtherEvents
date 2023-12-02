alphabet={
  1:"A",
  2:"B",
  3:"C",
  4:"D",
  5:"E",
  6:"F",
  7:"G",
  8:"H",
  9:"I",
  10:"J",
  11:"K",
  12:"L",
  13:"M",
  14:"N",
  15:"O",
  16:"P",
  17:"Q",
  18:"R",
  19:"S",
  20:"T",
  21:"U",
  22:"V",
  23:"W",
  24:"X",
  25:"Y",
  26:"Z"
}

def findResultLetter(n):
  if(n<27):
    return alphabet[n]
  else:
    currentAlphabet=26
    counter=1
    while (n>currentAlphabet):
      counter=counter+1
      oldAlphabet=currentAlphabet
      currentAlphabet=currentAlphabet+26*counter
    cursor=0
    lettera=0
    while(oldAlphabet+cursor<n):
      cursor=cursor+counter
      lettera=lettera+1
    return alphabet[lettera]
    

numberOfTestCases=int(input())
for testCase in range(numberOfTestCases):
  resultLetter=findResultLetter(int(input()))
  print("Case #", end="")
  print(testCase+1, end="")
  print(": ", end="")
  print(resultLetter)