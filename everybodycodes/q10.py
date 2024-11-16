from utilityz import *

valueOfSymbol={"A":1, "B":2, "C":3, "D":4, "E":5, "F": 6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}

def solve():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows, "*")
  
  insideGrid=[x for x in grid if grid[x]=="."]

  result=""
  for element in insideGrid:
    horizontalLine=[]
    for idx in range(0,maxX+1):
      horizontalLine.append(grid[(idx,element[1])])
    verticalLine=[]
    for idx in range(0,maxY+1):
      verticalLine.append(grid[(element[0], idx)])
    result=result+thingInCommonArray2(horizontalLine,verticalLine,".")[1]

  return result

def fixAndEvaluateRune(rune):

  insideGrid=[x for x in rune if rune[x]=="."]
  maxX, maxY=maxGrid(rune)

  result={}
  # for x in range(2,6):
  #   for y in range(2,6):
  #     result[(x,y)]="."

  for element in insideGrid:
    horizontalLine=[]
    for idx in range(0,maxX+1):
      if(rune[(idx,element[1])]=="?"):
        continue
      horizontalLine.append(rune[(idx,element[1])])
    verticalLine=[]
    for idx in range(0,maxY+1):
      if(rune[(element[0], idx)]=="?"):
        continue
      verticalLine.append(rune[(element[0], idx)])
    if(thingInCommonArray2(horizontalLine,verticalLine,".")[1]!=None):
      result[element]=thingInCommonArray2(horizontalLine,verticalLine,".")[1]
    else:
      result[element]="."

  #FIXING PART
  partsToFix=[k for k,v in result.items() if v=="."]
  fixedSomething=True
  unFixable=False

  collectionOfFixedParts={}

  while(fixedSomething and len(partsToFix)>0 and unFixable==False):
    newPartsToFix=[]
    fixedSomething=False
    for broken in partsToFix:
      countUnknown=0
      placeUnknown=[]
      horizontalLine=[]
      for idx in range(0,maxX+1):
        if(rune[(idx,broken[1])]=="?"):
          countUnknown=countUnknown+1
          placeUnknown.append((idx, broken[1]))
          continue
        horizontalLine.append(rune[(idx,broken[1])])

      verticalLine=[]
      for idx in range(0,maxY+1):
        if(rune[(broken[0],idx)]=="?"):
          countUnknown=countUnknown+1
          placeUnknown.append((broken[0],idx))
          continue
        verticalLine.append(rune[(broken[0],idx)])
      if countUnknown>1:
        newPartsToFix.append(broken)
      
      if countUnknown==0:
        if(thingInCommonArray2(horizontalLine,verticalLine,".")[1]!=None):
          result[broken]=thingInCommonArray2(horizontalLine,verticalLine,".")[1]
          fixedSomething=True
        else:
          unFixable=True
          break  
      
      if countUnknown==1:
        # print("SONO ENTRATO per", placeUnknown[0])
        keyUnknown=placeUnknown[0]
        theRestToTake=[]
        if(keyUnknown[0]<2 or keyUnknown[0]>5):
          lineToTake=verticalLine
          for idx in range (2,6):
            if(result.get((broken[0], idx))!=None):
              if(result[(broken[0], idx)]=="."):
                continue
              theRestToTake.append(result[(broken[0], idx)])

        elif(keyUnknown[1]<2 or keyUnknown[1]>5):
          lineToTake=horizontalLine
          for idx in range (2,6):
            
            if(result.get((idx, broken[1]))!=None):
              if(result.get((idx, broken[1]))=="."):
                continue
              theRestToTake.append(result[idx, broken[1]])

        if(len(theRestToTake)!=3):
          continue
        else:
          fixedElementsymbol=[x for x in list(set(lineToTake)-set(theRestToTake)) if x!="."][0]
          fixedSomething=True
          result[broken]=fixedElementsymbol
          rune[keyUnknown]=fixedElementsymbol
          collectionOfFixedParts[keyUnknown]=fixedElementsymbol
    
    partsToFix=newPartsToFix


  if unFixable or '.' in result.values():
    return 0, collectionOfFixedParts, result
  
  else:
    resultNumber=0
    i=1
    # print(result)
    # stampaGrid(rune, None, None, " ")
    # stampaGrid(result, None, None, " ")
    for element in result.values():
      resultNumber=resultNumber+i*valueOfSymbol[element]
      i=i+1
    return resultNumber, collectionOfFixedParts, result

def evaluateRune(rune):


  insideGrid=[x for x in rune if rune[x]=="."]
  maxX, maxY=maxGrid(rune)

  result=""
  for element in insideGrid:
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
  for k,v in collectionOfRunics.items():
    resultSum=resultSum+evaluateRune(v)
  
  return resultSum

def solve2():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows, "*")
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

def wizardry(grid, part):

  collectionOfRunics=buildCollectionOfRunics(grid)
  
  collectionOfResults={}
  changed=True
  listOfSingleRunes=list(collectionOfRunics.keys())
  listOfSingleRunes.reverse()

  while(changed):
    changed=False

    for singleRuneIdx in listOfSingleRunes:
      subSum, fixedElements, resultOfRound=fixAndEvaluateRune(collectionOfRunics[singleRuneIdx])
      collectionOfResults[singleRuneIdx]=subSum

      roundChanged=updateListOfRunesWithfix(singleRuneIdx, collectionOfRunics, fixedElements)
      changed=changed or roundChanged

  # whatshappening ={k:"T" for k,v in collectionOfResults.items() if v>0}
  # stampaGrid(collectionOfRunics[k])
  # print(whatshappening)

  return sum(collectionOfResults.values())

def solvePartial():
  rows=openFile("raw.txt")
  rows=expansion(rows)
  grid, _, _=buildGrid(rows, " ")
  return wizardry(grid, 3)





  
# print(solve2())
print(solvePartial())