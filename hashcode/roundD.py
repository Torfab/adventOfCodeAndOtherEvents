

numberOfTestCases=int(input())
for testCase in range(numberOfTestCases):
  line=[x for x in input()]
  lenLine=len(line)
  oldLetter=None
  cursor=0
  counter=0
  changes=0

  if (len(set(line)) == 1):
    changes=lenLine//2+lenLine%2
  else:

    while(line[0]==line[-1]):
      line.insert(0, line.pop())
    while(cursor<lenLine):
      if(line[cursor]==oldLetter):
        counter=counter+1
      else:
        oldLetter=line[cursor]
        counter=1
      if(counter==2):
        changes=changes+1
        counter=counter%2
      cursor=cursor+1

  print("Case #", end="")
  print(testCase+1, end="")
  print(": ", end="")
  print(changes)