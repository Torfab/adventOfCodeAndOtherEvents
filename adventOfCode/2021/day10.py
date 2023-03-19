from utility import *

scoreCursorsDict=dict([('(',(')',1)), (')',('(',3)), ('[',(']',2)), (']',('[',57)), ('{',('}',3)), ('}',('{',1197)), ('<',('>',4)), ('>',('<',25137)) ])

def scorePartA(a):
  arrayOfStatus=[]
  for element in a:
    cursorsDict=dict([('(',0), ('[',0), ('<',0), ('{',0)])
    if (element in cursorsDict):
      arrayOfStatus.append(element)
    else:
      if(scoreCursorsDict[element][0]!=arrayOfStatus[-1]):
        return scoreCursorsDict[element][1]
      else:
        arrayOfStatus.pop()
  return 0

def scorePartB(a):
  arrayOfStatus=[]
  for element in a:
    cursorsDict=dict([('(',0), ('[',0), ('<',0), ('{',0)])
    if (element in cursorsDict):
      arrayOfStatus.append(element)
    else:
      if(scoreCursorsDict[element][0]!=arrayOfStatus[-1]):
        return -1
      else:
        arrayOfStatus.pop()

  result=0
  for idx in reversed(range(len(arrayOfStatus))):
    result=result*5
    result=result+scoreCursorsDict[arrayOfStatus[idx]][1]
  return result

def evaluateResultPartA(a: list):
  return sum(a)

def evaluateResultPartB(b: list):
  newArray=b.copy()
  newArray.sort()
  return newArray[len(newArray)//2]

def solve(score, evaluateResult):
  rows= getAocInput(10,2021)

  result=[]
  for element in rows:
    computedScore=score(element)
    if(computedScore!=-1):
      result.append(score(element))

  return evaluateResult(result)

print(solve(scorePartA, evaluateResultPartA))
print(solve(scorePartB, evaluateResultPartB))