from utility import *
import functools

# Primo approccio floodfill e complete* (with little heuristic) search for optimal number of spells, SUPERLENTO, la memoization aiuta e si arriva alla soluzione ma chiaramente l'approcico era da cmbiare
# Secondo approccio aiutati da LLM, è guardare il problema come "Minimum Vertex Cover", quindi divido la griglia in linee orizzontali e verticali che si connettono nelle singole celle
# Quando il grafo è bipartito e non ci sono elementi del primo gruppo che toccano altr elemnti de primo gruppo, risolverlo è triviale nel senso che il lowerbound è garantito
# L'idea dietro è che per ottenree il lowerbound provi a incastrare le linee orizzontali e verticali e se non è possible l'incastro "chiedi" ai precedenti se hanno altri posti dove andare
# Così ricorsivamente e pian piano ogni linea riesce a trovare il suo miglior posizionamento, e mi ritorna il valore del lowerbound


directions=fromDistanceBuildSetOfDirections(1)

@functools.cache
def removeALine(reached, quantity):
  if(not reached):
    return quantity
  reached=set(reached)
  # print()
  minX=min(x[0] for x in reached)
  maxX=max(x[0] for x in reached)
  minY=min(x[1] for x in reached)
  maxY=max(x[1] for x in reached)

  horizontalLines=[]
  for row in range(minY, maxY+1):
    newLine=[]
    for column in range(minX, maxX+1):
      if((column, row) in reached):
        newLine.append((column, row))  
      else:
        horizontalLines.append(newLine)
        newLine=[]
    horizontalLines.append(newLine)
  horizontalLines.append(newLine)

  foundHorizontal=max((len(x),e) for e,x in enumerate(horizontalLines))
  foundHorizontal=horizontalLines[foundHorizontal[1]]

  verticalLines=[]
  for column in range(minX, maxX+1):
    newLine=[]
    for row in range(minY, maxY+1):
      if((column, row) in reached):
        newLine.append((column, row))  
      else:
        verticalLines.append(newLine)
        newLine=[]
    verticalLines.append(newLine)
  verticalLines.append(newLine)

  foundVertical=max((len(x),e) for e,x in enumerate(verticalLines))
  foundVertical=verticalLines[foundVertical[1]]
  return min(removeALine(tuple(sorted(reached-set(foundHorizontal))), quantity+1),  removeALine(tuple(sorted(reached-set(foundVertical))), quantity+1) )

def buildReached(grid, x, y):
  border=[(x,y)]
  newBorder=list(border)
  reached=set()
  reached.add((x,y))
  while(newBorder):
    border=list(newBorder)
    newBorder=[]
    for element in border:
      for d in directions:
        tentative=sumTupleValueByValue(element, d)
        if tentative in reached:
          continue
        if tentative in grid:
          reached.add(tentative)
          newBorder.append(tentative)
  return reached


def checkAndUpdateRectangle2(grid, x, y):

  result=0
  reached=buildReached(grid,x,y)
  
  result=removeALine(tuple(sorted(reached)), 0)
  for element in reached:
    grid.pop(element)
  return result



def solve():
  rows=openFile("test.txt")
  grid, _, _=buildGrid(rows)
  result=0
  while(grid):
    key=next(iter(grid))
    result=result+checkAndUpdateRectangle2(grid, key[0], key[1])
  return result


def labelRuns(grid):
  horizontalId={}
  verticalId={}
  horizontalCount=0
  verticalCount=0
  for (x, y) in grid.keys():
    if (x-1, y) in grid:
      horizontalId[(x, y)]=horizontalId[(x-1, y)]
    else:
      horizontalId[(x, y)]=horizontalCount
      horizontalCount=horizontalCount+1
    if (x, y-1) in grid:
      verticalId[(x, y)]=verticalId[(x, y-1)]
    else:
      verticalId[(x, y)]=verticalCount
      verticalCount=verticalCount+1
  return horizontalId, verticalId, horizontalCount

def buildNeighbors(grid):
  horizontalId, verticalId, horizontalCount=labelRuns(grid)
  neighbors=[[] for _ in range(horizontalCount)]
  for cell in grid:
    neighbors[horizontalId[cell]].append(verticalId[cell])
  return neighbors

def tryToMatch(h, neighbors, matchOfVertical, visited):
  for v in neighbors[h]:
    if v in visited:
      continue
    visited.add(v)
    # v is free, or whoever holds v can switch to another vertical run
    if v not in matchOfVertical or tryToMatch(matchOfVertical[v], neighbors, matchOfVertical, visited):
      matchOfVertical[v]=h
      return True
  return False

def minSpells(grid):
  neighbors=buildNeighbors(grid)
  matchOfVertical={}
  for h in range(len(neighbors)):
    tryToMatch(h, neighbors, matchOfVertical, set())
  return len(matchOfVertical)

def solve2():
  rows=openFile("raw.txt")
  grid, _, _=buildGrid(rows)
  return minSpells(grid)

# evaluateTime(solve, repetitions=1)
evaluateTime(solve2)
