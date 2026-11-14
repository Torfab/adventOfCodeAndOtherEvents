from utility import *
import heapq

directions={(1,0):[(1,0), (0,-1), (0,1)], (-1,0):[(-1,0), (0,-1), (0,1)], (0,1): [(0,1), (1,0), (-1,0)], (0,-1): [(0,-1), (1,0), (-1,0)]}

def parseRows(rows):
  return rows

def explore(start,walls, allSulfurs, end):
  
  border=[(start[0], start[1], (1,0), tuple())]
  shortCuts={}
  allSulfurLocation=[(x[0], x[1]) for x in allSulfurs]

  found=set()

  alreadyDone=set()
  step=0
  while len(shortCuts) < (len(allSulfurs)+1):
    newBorder=[]
    step=step+1
    print(step)
    for element in border:
      cell=(element[0], element[1])
      comingDirection=element[2]
      status=element[3]

      #Se già passato ignora
      if(element in alreadyDone):
        continue
      else:
        alreadyDone.add(element)

        #per tutte le direzioni
      for d in directions[comingDirection]:
        tentative=sumTupleValueByValue(cell, d)
        # print("valuto", tentative, "allo step", step)

        # SE BECCA IL MURO
        if tentative in walls:
          continue

        if d==(1,0) or d==(0,1):
          flagDirection=1
        else:
          flagDirection=-1
        realPosition=(tentative[0], tentative[1], flagDirection) 

        # SE BECCA UN SULFURE
        if tentative in allSulfurLocation:
          #RAGGIUNTA DA OVEST NORD 1, EST SUD -1
          # print("sulfur")

          if realPosition in found:
            continue
          else:
            found.add(realPosition)
            shortCuts[realPosition]=step
            newBorder.append((tentative[0], tentative[1], d, tuple(sorted(set(status)|{realPosition}))))

        # se becca la fine
        elif tentative == end:
          print("end")
          if realPosition in found:
            continue
          found.add(realPosition)
          shortCuts[realPosition]=step

        # NEL CASO STRADA PUlitA
        else:
          thingToAppend=(tentative[0], tentative[1], d,tuple(sorted(set(status)|{realPosition})))
          if(thingToAppend in alreadyDone):
            continue
          newBorder.append(thingToAppend)
    border=newBorder
  return shortCuts



def solve():
  rows=openFile("raw.txt")
  grid, maxX, maxY=buildGrid(rows)

  start=[x for x,y in grid.items() if y=="S"][0]
  end=[x for x,y in grid.items() if y=="E"][0]
  print(end)
  sulfurs=[x for x,y in grid.items() if y=="@"]
  walls=set([x for x,y in grid.items() if y=="#"])
  additionalWalls=cageGridWithWalls((maxX,maxY))
  walls=walls|additionalWalls

  allSulfurs=[]
  for sulfur in sulfurs:
    allSulfurs.append((sulfur[0], sulfur[1], -1))
    allSulfurs.append((sulfur[0], sulfur[1], 1))

  explorations={}
  print(explore(start, walls, allSulfurs, end))
  
  #1 espora da start

  #2 esplora dai sulfur

  ## PARE TRPPO COMPLESSO, meglio sfruttare la regolarità, 
  ## il testo dice che i tunnel non si incontrano quidi io ogni volta che incont un tunnel posso TELETRASPORTARMI alla fine

  #3 dajkstra con status le cose già prese
  
  #RAGGIUNTA DA OVEST SUD 1, EST NORD -1

  #explore from every sulfur

  # stampaGrid(grid)
  
  return 

# evaluateTime(solve, repetitions=1)
print(solve())
