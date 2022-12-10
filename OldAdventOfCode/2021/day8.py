from utility import *


def buildDictOfLetters(input):
  newDict=dict()
  for element in input:
    for letter in element:

      newDict[letter]=(newDict.get(letter) or 0)+1
  
  return newDict

def discriminateLAandLC(candidates, input):
  if(candidates[0] in next(a for a in input if len(a)==4)):
    return candidates[1], candidates[0]
  else:
    return candidates[0], candidates[1]

def discriminateLDandLG(candidates, input):
  if(candidates[1] in next(a for a in input if len(a)==4)):
    return candidates[1], candidates[0]
  else:
    return candidates[0], candidates[1]

def fromInputBuildComprehension(input: list):
  myDict=buildDictOfLetters(input)
  LA,LC=discriminateLAandLC([a for a in myDict if myDict[a]==8], input)
  LB=[a for a in myDict if myDict[a]==6][0]
  LD,LG=discriminateLDandLG([a for a in myDict if myDict[a]==7], input)
  LE=[a for a in myDict if myDict[a]==4][0]
  LF=[a for a in myDict if myDict[a]==9][0]
  return dict([(''.join(sorted(LA+LB+LC+LE+LF+LG)), 0), (''.join(sorted(LC+LF)), 1), (''.join(sorted(LA+LC+LD+LE+LG)), 2), (''.join(sorted(LA+LC+LD+LF+LG)), 3), (''.join(sorted(LB+LC+LD+LF)), 4), (''.join(sorted(LA+LB+LD+LF+LG)),5), (''.join(sorted(LA+LB+LD+LE+LF+LG)), 6), (''.join(sorted(LA+LC+LF)),7), (''.join(sorted(LA+LB+LC+LD+LE+LF+LG)),8), (''.join(sorted(LA+LB+LC+LD+LF+LG)),9)])


def solve(countArray):
  rows= getAoCInputGeneric(2021, 8)

  accumulatore=0  

  for row in rows:
    line= row.split(" | ")
    input=line[0].split(" ")
    output=line[1].split(" ")

    resolvingDictionary=fromInputBuildComprehension(input)

    for element in output:
      myNumber=resolvingDictionary[''.join(sorted(element))]
      if(myNumber in countArray):
        accumulatore=accumulatore+1

  return accumulatore


def solve2():
  rows= getAoCInputGeneric(2021, 8)
  
  accumulatore=0  

  for row in rows:
    line= row.split(" | ")
    input=line[0].split(" ")
    output=line[1].split(" ")

    resolvingDictionary=fromInputBuildComprehension(input)

    singleOutputNumber=0

    for idx, element in enumerate(output):
      myNumber=resolvingDictionary[''.join(sorted(element))]
      singleOutputNumber=singleOutputNumber+myNumber*(10**(3-idx))

    accumulatore=accumulatore+singleOutputNumber

  return accumulatore

print(solve([1,4,7,8]))
print(solve2())