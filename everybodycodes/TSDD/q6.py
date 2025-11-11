from utility import *

def parseRows(rows):
  nameArray=rows[0].split(',')

  rulesRaw=rows[2:]
  rules={}
  for rule in rulesRaw:
    key, values=rule.split(" > ")
    rules[key]=values.split(',')
  return nameArray, rules

def solve(part):
  rows=openFile("raw.txt")
  nameArray, rules=parseRows(rows)
  resultArray=[]
  for i, name in enumerate(nameArray):
    good=True
    for cIdx in range(len(name)-1):
      if name[cIdx+1] not in rules[name[cIdx]]:
        good=False
        break
    if good:
      resultArray.append(i+1)

  if part=="a":
    return nameArray[resultArray[0]-1]
  else:
    return sum(resultArray)

def countNames(name, minLen, maxLen, rules, mySet):

  if(len(name)>=minLen):
    mySet.add(name)
    result=1
  else:
    result=0

  if len(name)==maxLen:
    mySet.add(name)
    return result
  
  for r in rules.get(name[-1], []):
    result=result+countNames(name+r, minLen, maxLen, rules, mySet)
  return result

def solve3():
  rows=openFile("raw.txt")
  nameArray, rules=parseRows(rows)
  minLen=7
  maxLen=11
  result=0
  mySet=set()
  for name in nameArray:
    good=True
    for cIdx in range(len(name)-1):
      if name[cIdx+1] not in rules[name[cIdx]]:
        good=False
        break
    if good:
      result=result+countNames(name, minLen, maxLen, rules, mySet)
  
  return len(mySet)

print(solve("a"))
print(solve("b"))
# print(solve3())
