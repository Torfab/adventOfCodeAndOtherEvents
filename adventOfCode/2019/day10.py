from utility import *

def solve(part):
  rows=getOldAocInput(10)
  grid, _, _=buildGrid(rows)
  keysInGrid=set(grid.keys())
  maximumAsteroids=0
  theKey=-1
  for key in keysInGrid:
    asteroidOnSight=0
    for innerKey in keysInGrid.difference(set([key])):
      innerKey=sumTupleValueByValue(innerKey, (-key[0], -key[1]))
      theGcd=gcd(innerKey[0], innerKey[1])
      if theGcd==1:
        asteroidOnSight=asteroidOnSight+1
      else:
        reducedInnerKey=(innerKey[0]//theGcd, innerKey[1]//theGcd)
        currentReducedInnerKey=sumTupleValueByValue(reducedInnerKey,key)
        multiplicativeIndex=1
        notPrevious=True
        innerKey=sumTupleValueByValue(innerKey,key)
        while(currentReducedInnerKey!=innerKey):
          if currentReducedInnerKey in keysInGrid:
            notPrevious=False
            break
          multiplicativeIndex=multiplicativeIndex+1
          currentReducedInnerKey=multiplyTupleByValue(reducedInnerKey, multiplicativeIndex)
          currentReducedInnerKey=sumTupleValueByValue(currentReducedInnerKey, key)

        if(notPrevious):
          asteroidOnSight=asteroidOnSight+1

    if (maximumAsteroids<asteroidOnSight):
      maximumAsteroids=asteroidOnSight
      theKey=key
  if part=="a":
    return maximumAsteroids
  if part=="b":
    key=theKey
    keysToCheck=list(grid.keys())
    keysToCheck.remove(key)
    keysToCheck=[sumTupleValueByValue(x, (-key[0], -key[1])) for x in keysToCheck]
    keysRight=[x for x in keysToCheck if x[0]>0]
    keysLeft=[x for x in keysToCheck if x[0]<0]

    currentDestroy=1 #one up
    keysRight=sorted(keysRight, key=lambda x: x[1]/x[0])
    for innerKey in keysRight:
      theGcd=gcd(innerKey[0], innerKey[1])
      if theGcd==1:
        currentDestroy=currentDestroy+1
        if(currentDestroy==200):
          innerKey=sumTupleValueByValue(innerKey,key)
          break
      else:
        reducedInnerKey=(innerKey[0]//theGcd, innerKey[1]//theGcd)
        currentReducedInnerKey=sumTupleValueByValue(reducedInnerKey,key)
        multiplicativeIndex=1
        notPrevious=True
        innerKey=sumTupleValueByValue(innerKey,key)
        while(currentReducedInnerKey!=innerKey):
          if currentReducedInnerKey in keysInGrid:
            notPrevious=False
            break
          multiplicativeIndex=multiplicativeIndex+1
          currentReducedInnerKey=multiplyTupleByValue(reducedInnerKey, multiplicativeIndex)
          currentReducedInnerKey=sumTupleValueByValue(currentReducedInnerKey, key)

        if(notPrevious):
          currentDestroy=currentDestroy+1
          if(currentDestroy==200):
            break
    currentDestroy=currentDestroy+1 #one down

    keysLeft=sorted(keysLeft, key=lambda x: x[1]/x[0])
    for innerKey in keysLeft:
      theGcd=gcd(innerKey[0], innerKey[1])
      if theGcd==1:
        currentDestroy=currentDestroy+1
        if(currentDestroy==200):
          innerKey=sumTupleValueByValue(innerKey,key)
          break
      else:
        reducedInnerKey=(innerKey[0]//theGcd, innerKey[1]//theGcd)
        currentReducedInnerKey=sumTupleValueByValue(reducedInnerKey,key)
        multiplicativeIndex=1
        notPrevious=True
        innerKey=sumTupleValueByValue(innerKey,key)
        while(currentReducedInnerKey!=innerKey):
          if currentReducedInnerKey in keysInGrid:
            notPrevious=False
            break
          multiplicativeIndex=multiplicativeIndex+1
          currentReducedInnerKey=multiplyTupleByValue(reducedInnerKey, multiplicativeIndex)
          currentReducedInnerKey=sumTupleValueByValue(currentReducedInnerKey, key)

        if(notPrevious):
          currentDestroy=currentDestroy+1
          if(currentDestroy==200):
            break
    return innerKey[0]*100+innerKey[1]

print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
