from utilityz import *

valueOfSymbol={"A":1, "B":2, "C":3, "D":4, "E":5, "F": 6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}

collectionOfborderIdx=[0,1,6,7]

def solve():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows, "*")
  
  elementsMissing=[x for x in grid if grid[x]=="."]

  result=""
  for element in elementsMissing:
    horizontalLine=[]
    for idx in range(0,maxX+1):
      horizontalLine.append(grid[(idx,element[1])])
    verticalLine=[]
    for idx in range(0,maxY+1):
      verticalLine.append(grid[(element[0], idx)])
    result=result+thingInCommonArray2(horizontalLine,verticalLine,".")[1]

  return result

def findEasyElements(rune, elementsMissing):
  result={}
  for x in range(2,6):
    for y in range(2,6):
      if(rune.get((x,y))!="."):
        result[(x,y)]=rune[(x,y)]

  for element in elementsMissing:
    horizontalLine=[]
    for idx in collectionOfborderIdx:
      if(rune[(idx,element[1])]=="?"):
        continue
      horizontalLine.append(rune[(idx,element[1])])

    verticalLine=[]
    for idx in collectionOfborderIdx:
      if(rune[(element[0], idx)]=="?"):
        continue
      verticalLine.append(rune[(element[0], idx)])
    
    foundCommonElement=thingInCommonArray2(horizontalLine,verticalLine,".")[1]
    if(foundCommonElement!=None):
      result[element]=foundCommonElement
      rune[element]=foundCommonElement
    else:
      result[element]="."
  return result

def fixGrid(rune, result):
  partsToFix=[k for k,v in result.items() if v=="."]
  fixedSomething=True
  isUnfixable=False

  collectionOfFixedParts={}

  while(fixedSomething and len(partsToFix)>0 and isUnfixable==False):
    newPartsToFix=[]
    fixedSomething=False
    for broken in partsToFix:
      countUnknown=0
      placeUnknown=[]
      horizontalLine=[]
      for idx in collectionOfborderIdx:
        if(rune[(idx,broken[1])]=="?"):
          countUnknown=countUnknown+1
          placeUnknown.append((idx, broken[1]))
          continue
        horizontalLine.append(rune[(idx,broken[1])])

      verticalLine=[]
      for idx in collectionOfborderIdx:
        if(rune[(broken[0],idx)]=="?"):
          countUnknown=countUnknown+1
          placeUnknown.append((broken[0],idx))
          continue
        verticalLine.append(rune[(broken[0],idx)])

      
      if countUnknown==0:
        if(thingInCommonArray2(horizontalLine,verticalLine,".")[1]!=None):
          result[broken]=thingInCommonArray2(horizontalLine,verticalLine,".")[1]
          fixedSomething=True
        else:
          isUnfixable=True


      if countUnknown>1:
        newPartsToFix.append(broken)
        continue
      
      if countUnknown==1:
        keyUnknown=placeUnknown[0]
        alreadyFoundElements=[]

        if(keyUnknown[0]<2 or keyUnknown[0]>5):
          lineToTake=verticalLine
          for idx in range (2,6):
            if(result.get((broken[0], idx))!=None):
              if(result[(broken[0], idx)]=="."):
                continue
              alreadyFoundElements.append(result[(broken[0], idx)])

        elif(keyUnknown[1]<2 or keyUnknown[1]>5):
          lineToTake=horizontalLine
          for idx in range (2,6):
            if(result.get((idx, broken[1]))!=None):
              if(result.get((idx, broken[1]))=="."):
                continue
              alreadyFoundElements.append(result[idx, broken[1]])

        if(len(alreadyFoundElements)==3):

          fixedElementsymbol=[x for x in list(set(lineToTake)-set(alreadyFoundElements)) if x!="."]
          fixedElementsymbol=fixedElementsymbol[0]

          fixedSomething=True

          #Note that i'm changing state of the system here, i use it on purpose for efficiency but this function now have collateral effect you have to understand
          result[broken]=fixedElementsymbol
          rune[broken]=fixedElementsymbol
          rune[keyUnknown]=fixedElementsymbol
          collectionOfFixedParts[keyUnknown]=fixedElementsymbol
    
    partsToFix=newPartsToFix
  
  #Note that i use reference variable and i change the state of the system in other parts other than this explicit return
  return isUnfixable, collectionOfFixedParts

def fixAndEvaluateRune(rune, elementsMissing):

  result=findEasyElements(rune, elementsMissing)
  isUnfixable, collectionOfFixedParts=fixGrid(rune, result)


  if isUnfixable:
    return 0, {}
  if '.' in result.values():
    return 0, collectionOfFixedParts
  
  resultNumber=0
  i=1
  for y in range(2,6):
    for x in range(2,6):
      resultNumber=resultNumber+i*valueOfSymbol[result[(x,y)]]
      i=i+1
  return resultNumber, collectionOfFixedParts

def evaluateRune(rune):
  elementsMissing=[x for x in rune if rune[x]=="."]
  maxX, maxY=maxGrid(rune)

  result=""
  for element in elementsMissing:
    horizontalLine=[]
    for idx in range(0,maxX+1):
      horizontalLine.append(rune[(idx,element[1])])
    verticalLine=[]
    for idx in range(0,maxY+1):
      verticalLine.append(rune[(element[0], idx)])
    result=result+thingInCommonArray2(horizontalLine,verticalLine,".")[1]

  resultNumber=0

  for i in range(1, len(result)+1):
    resultNumber=resultNumber+i*valueOfSymbol[result[(i-1)]]
  return resultNumber

def evaluateHealthyCollectionOfRunics(collectionOfRunics):
  resultSum=0
  for v in collectionOfRunics.values():
    resultSum=resultSum+evaluateRune(v)
  
  return resultSum

def solve2():
  rows=openFile("raw.txt")
  grid, _, _=buildGrid(rows, "*")
  collectionOfRunics=buildCollectionOfRunics(grid)
  return evaluateHealthyCollectionOfRunics(collectionOfRunics)

def expansion(rows):
  rows=[list(row) for row in rows]
  expanded=[]
  expanded.append(rows[0])
  expanded.append(rows[1])
  cursor=2
  while(cursor+1<len(rows)):
    for i in range(6):
      expanded.append(rows[cursor+i])
    expanded.append([" " for _ in rows[cursor-1]])
    expanded.append(rows[cursor+i-1].copy())
    expanded.append(rows[cursor+i].copy())
    cursor=cursor+6
  
  expanded=expanded[:-3]

  cursor=8
  while(cursor<len(expanded[0])):
    for element in expanded:
      element.insert(cursor,element[cursor-1])
      element.insert(cursor,element[cursor-2])
      element.insert(cursor," ")
    cursor=cursor+9
  
  return expanded

def buildCollectionOfRunics(grid):
  maxX, maxY=maxGrid(grid)
  collectionOfRunics={}

  for y in range(0, maxY+1):
    subElementY=y//9
    subIdxY=y%9
    for x in range(0, maxX+1):
      subElementX=x//9
      subIdxX=x%9

      if(grid.get((x,y))==None):
        continue
      else:

        if(collectionOfRunics.get((subElementX,subElementY))==None):
          collectionOfRunics[(subElementX, subElementY)]={}
        collectionOfRunics[(subElementX, subElementY)][(subIdxX, subIdxY)]=grid[(x,y)]
  return collectionOfRunics

def updateListOfRunesWithfix(fixedRuneIdx, collectionOfRunics,fixedElements):
  changed=False
  for coords, value in fixedElements.items():
    if(coords[0]<2):
      runeToChange=sumTupleValueByValue(fixedRuneIdx, (-1,0))
      if collectionOfRunics.get(runeToChange)!=None:
        changed=True
        collectionOfRunics[runeToChange][(coords[0]+6,coords[1])]=value
    if(coords[0]>5):
      runeToChange=sumTupleValueByValue(fixedRuneIdx, (1,0))
      if collectionOfRunics.get(runeToChange)!=None:
        changed=True
        collectionOfRunics[runeToChange][(coords[0]-6,coords[1])]=value
    if(coords[1]<2):
      runeToChange=sumTupleValueByValue(fixedRuneIdx, (0,-1))
      if collectionOfRunics.get(runeToChange)!=None:
        changed=True
        collectionOfRunics[runeToChange][(coords[0],coords[1]+6)]=value
    if(coords[1]>5):
      runeToChange=sumTupleValueByValue(fixedRuneIdx, (0,1))
      if collectionOfRunics.get(runeToChange)!=None:
        changed=True
        collectionOfRunics[runeToChange][(coords[0],coords[1]-6)]=value
  return changed


def solvePartial():
  rows=openFile("raw.txt")
  rows=expansion(rows)
  grid, _, _=buildGrid(rows, " ")
  collectionOfRunics=buildCollectionOfRunics(grid)
  
  collectionOfResults={}
  changed=True
  listOfSingleRunes=list(collectionOfRunics.keys())
  while(changed):
    changed=False

    for singleRuneIdx in listOfSingleRunes:
      elementsMissing=[x for x in collectionOfRunics[singleRuneIdx] if collectionOfRunics[singleRuneIdx][x]=="."]
      if(len(elementsMissing)!=0):
        valueOfSingleRune, fixedElements=fixAndEvaluateRune(collectionOfRunics[singleRuneIdx], elementsMissing)
        collectionOfResults[singleRuneIdx]=valueOfSingleRune
        changedOtherRunes=updateListOfRunesWithfix(singleRuneIdx, collectionOfRunics, fixedElements)
        changed=(changed or changedOtherRunes)

  return sum(collectionOfResults.values())


# print(solve())
print(solve2())
# print(solvePartial())