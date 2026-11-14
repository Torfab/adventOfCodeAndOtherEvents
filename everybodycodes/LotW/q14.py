from utility import *

directions=fromDistanceBuildSetOfDirections(1)

def countBindings(cell, grid, lettersReached):
  result=0
  letter=grid[cell]
  border=[cell]
  reached=set()
  while(border):
    newBorder=[]
    for currentCell in border:
      if currentCell in reached:
        continue
      reached.add(currentCell)
      for d in directions:
        tentative=sumTupleValueByValue(currentCell, d)
        if tentative in reached:
          continue
        if grid.get(tentative) in lettersReached:
          continue
        if grid.get(tentative)!=letter:
          result=result+1
        else:
          newBorder.append(tentative)
    border=newBorder
  return result
      

def solve():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows)
  result=0
  letters=set(grid.values())
  lettersReached=set()
  for letter in letters:
    cell=next((x for x,y in grid.items() if y==letter))
    
    result=result+countBindings(cell, grid, lettersReached)
    lettersReached.add(letter)
    
  return result

def buildLinking(cell, grid, linking):
  letter=grid[cell]
  linking[letter]=linking.get(letter, {})
  border=[cell]
  reached=set()
  while(border):
    newBorder=[]
    for currentCell in border:
      if currentCell in reached:
        continue
      reached.add(currentCell)
      for d in directions:
        tentative=sumTupleValueByValue(currentCell, d)
        if tentative in reached:
          continue
        if grid.get(tentative)==None:
          linking[letter]["void"]=linking.get(letter).get("void", 0)+1
          linking["void"]=linking.get("void", {})
          linking["void"][letter]=linking["void"].get(letter, 0)+1
          continue
        if grid.get(tentative)!=letter:
          linking[letter][grid[tentative]]=linking[letter].get(grid[tentative], 0)+1
          linking[grid[tentative]]=linking.get(grid[tentative], {})
          linking[grid[tentative]][letter]=linking[grid[tentative]].get(letter, 0)+1
        else:
          newBorder.append(tentative)
    border=newBorder
  return linking
      

def halveTheThings(linking):
  for k, v in linking.items():
    if k=="void":
      continue
    for k1 in v.keys():
      if(k1!="void"):
        v[k1]=v[k1]//2

def findBestUntilVoid(linking, letter, currentSolve, lettersSolved, totalSolved, quantity):
  if("void" in currentSolve):
    return quantity
  
  possibleLinks=linking[letter]

  findMin=min(possibleLinks, key=possibleLinks.get)

  quantity=quantity+possibleLinks[findMin]
  lettersSolved.add(letter)

  if findMin in lettersSolved:
    for possibleSolve in totalSolved:
      #find WHICH ONE and aggregate tehre
      return quantity

  print(letter, findMin, possibleLinks)
  
def addALink(reached, reachables, linking):
  findMin=min((k for k in reachables if k not in reached), key=reachables.get)
  reached.add(findMin) 
  result=reachables[findMin]
  for k in linking[findMin]:
    reachables[k]=min(reachables.get(k, float("inf")), linking[findMin][k])
  return result

def solveLinking(reached, reachables, linking):

  result=0
  while([k for k in reachables if k not in reached]):
    result=result+addALink(reached, reachables, linking)
  return result

def solve2():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows)
  letters=set(grid.values())
  linking={}

  for letter in letters:
    cell=next((x for x,y in grid.items() if y==letter))
    
    buildLinking(cell, grid, linking)
  halveTheThings(linking)

  reached=set()
  reached.add("void")
  reachables={}
  for k,v in linking["void"].items():
    reachables[k]=v

  return solveLinking(reached, reachables, linking)

def solveLinking3(reachable1, reachable2, reached1, reached2, linking):
  print("SIBBALLA")
  reachables=[reachable1, reachable2]
  reached=[reached1, reached2]
  result=0

  while(True):
    findMin1=min((k for k in reachable1 if k not in reached1), key=reachable1.get)
    findMin2=min((k for k in reachable2 if k not in reached2), key=reachable2.get)
    findsKeys=[findMin1, findMin2]
    findsValues=[reachable1[findMin1], reachable2[findMin2]]
    if(reachable1[findMin1]<=reachable2[findMin2]):
      index=0
    else:
      index=1
    result=result+findsValues[index]
    reached[index].add(findsKeys[index])

    for k in linking[findsKeys[index]]:
      if k in reached[index]:
        continue
      reachables[index][k]=min(reachables[index].get(k, float("inf")), linking[findsKeys[index]][k])

    if(findsKeys[index] in reached[(index+1)%2]):
      #POSSIAMO UNIRE FESTA
      reached=reached1 | reached2
      reachables= {
        k: min(reachable1.get(k, float("inf")), reachable2.get(k, float("inf"))) for k in reachable1.keys() |reachable2.keys()
      }
      return result+ solveLinking(reached, reachables, linking)

    

def solve3():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows)
  letters=set(grid.values())
  linking={}

  for letter in letters:
    cell=next((x for x,y in grid.items() if y==letter))
    
    buildLinking(cell, grid, linking)

  halveTheThings(linking)
  minResult=float("inf")

  flagDebug=False

  for letter1 in letters:
    for letter2 in [x for x in letters if x not in linking[letter1] and x not in ["void", letter1]]:
      print(letter1, letter2)

      reachable1=dict(linking[letter1])
      for k in linking[letter1]:
        for j in linking[k]:
          reachable1[j]=min(reachable1.get(j, float("inf")), linking[k][j])
      reachable2=dict(linking[letter2])
      for k in linking[letter2]:
        for j in linking[k]:
          reachable2[j]=min(reachable2.get(j, float("inf")), linking[k][j])

      if(flagDebug==True):
        print("reachables", reachable1)
        print("reachables", reachable2)
        breakpoint()

      if not reachable1.keys().isdisjoint(reachable2.keys()):
        reachables= {
          k: min(reachable1.get(k, float("inf")), reachable2.get(k, float("inf"))) for k in reachable1.keys() |reachable2.keys()
        } 
        reached=set()
        reached.add(letter1)
        reached.add(letter2)
        reached=reached | linking[letter1].keys() | linking[letter2].keys()
        subResult=solveLinking(reached, reachables, linking)
        print("caso facile", subResult)
        minResult=min(minResult, subResult)
        continue

      reached1=set()
      reached1.add(letter1)
      reached1=reached1 | linking[letter1].keys()
      reached2=set()
      reached2.add(letter2)
      reached2=reached2 | linking[letter2].keys()
      subResult=solveLinking3(reachable1, reachable2, reached1, reached2, linking)
      print("caso interessante", subResult)
      minResult=min(minResult, subResult)

  # per tutte le lettere prendine due che non si toccano
  # costruisci reached e reachables partendo
  # risolvi e tieni il più basso
  
  return minResult


# evaluateTime(solve, repetitions=1)
print(solve3())
