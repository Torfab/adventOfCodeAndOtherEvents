from utility import *
import functools

def parseRow(row):
  splittedRow=row.split(" ")
  pattern=splittedRow[0]
  theSplits=[int(x) for x in splittedRow[1].split(",")]
  return pattern, theSplits

@functools.cache
def checkPossibleArrangement(pattern, theSplits):
  size=len(pattern)
  if (len(theSplits) == 0):
    if all(c in '.?' for c in pattern):
      return 1
    return 0

  currentSplit = theSplits[0]
  otherSplits = theSplits[1:]
  after = sum(otherSplits) + len(otherSplits) 

  count = 0

  for before in range(size-after-currentSplit+1):
    tentative = '.' * before + '#' * currentSplit + '.'
    if all(p == t or p=='?' for p,t in zip(pattern, tentative)):
      count += checkPossibleArrangement(pattern[len(tentative):], otherSplits)

  return count

def solve(part):

  if(part=="a"):
    multiply=1
  if(part=="b"):
    multiply=5

  rows=getOldAocInput(12)

  result=0
  for row in rows:
    pattern, theSplits= parseRow(row)
    newPattern=pattern
    newSplit=theSplits*multiply
    for _ in range(multiply-1):
      newPattern=newPattern+"?"+pattern
    result=result+checkPossibleArrangement(newPattern, tuple(newSplit))
  return result


print(solve("a"))
print(solve("b"))