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

def solveLinking(linking):
  halveTheThings(linking) #i have double entries for everything but void
  reached=set()
  reached.add("void")
  reachables={}
  for k,v in linking["void"].items():
    reachables[k]=v
  result=0
  while([k for k in reachables if k not in reached]):
    print([k for k in reachables if k not in reached])
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
    print(linking)
  return solveLinking(linking)


# evaluateTime(solve, repetitions=1)
print(solve2())
