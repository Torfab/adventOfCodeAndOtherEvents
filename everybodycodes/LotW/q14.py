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
  for v in linking.values():
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
  
  

def solveLinking(linking):
  halveTheThings(linking) #i have double entries for everything but void
  result=0
  letters=list(linking.keys())
  print(letters)
  totalSolved=[]
  lettersSolved=set()
  #Solve the one forced
  # solved=[]
  # forced=[(x,y) for x,y in linking.items() if len(y)==1]
  # for element in forced:
  #   insertInSolved(solved, )
  # print(forced)
  for letter in letters:
    if letter in lettersSolved:
      continue
    currentSolve=[]
    result=result+findBestUntilVoid(linking, letter, currentSolve, lettersSolved, totalSolved, 0)

  


def solve2():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows)
  result=0
  letters=set(grid.values())
  linking={}

  for letter in letters:
    cell=next((x for x,y in grid.items() if y==letter))
    
    buildLinking(cell, grid, linking)
    print(linking)
  return solveLinking(linking)


# evaluateTime(solve, repetitions=1)
print(solve2())
