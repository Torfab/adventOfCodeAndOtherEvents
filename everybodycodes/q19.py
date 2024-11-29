from utilityz import *

directions=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]


def parseRows(rows):
  key=rows[0]
  grid,maxX,maxY=buildGrid(rows[2:], None)
  return key, grid, maxX, maxY

def specialOptimizedCycleDetection(point, theGrid):
  i=1
  result=set()
  result.add(point)
  current=theGrid[point]
  while(current not in result):
    i=i+1
    result.add(current)
    current=theGrid[current]

  return i

def rotate(point, orientation, grid):
  inHandOld="k"
  if(orientation=="R"):
    directionToUse=directions
  if(orientation=="L"):
    directionToUse=list(reversed(directions))
  for d in directionToUse:
    movingPoint=sumTupleValueByValue(d,point)
    inHandNew=grid[movingPoint]
    grid[movingPoint]=inHandOld
    inHandOld=inHandNew
  grid[sumTupleValueByValue(directionToUse[0],point)]=inHandOld

def cycle(point, theGrid):
  lenDetection=specialOptimizedCycleDetection(point, theGrid)
  banana=[]
  for _ in range(lenDetection):
    banana.append(point)
    point=theGrid[point]
  return lenDetection, banana

def solve(repeat, file):
  rows=openFile(file)
  keyIndex=0
  key, grid, maxX, maxY=parseRows(rows)

  maggiore=[k for k,v in grid.items() if v==">"][0]
  minore=[k for k,v in grid.items() if v=="<"][0]

  weirdGrid={k:k for k in grid.keys()}

  for y in range(1,maxY):
    for x in range(1,maxX):
      rotate((x,y), key[keyIndex], weirdGrid)
      keyIndex=(keyIndex+1)%len(key)
  keyIndex=0
  
  reversedWeirdGrid={v:k for k,v in weirdGrid.items()}

  lenmaggiore, arraymaggiore=cycle(maggiore, reversedWeirdGrid)
  lenminore, arrayminore=cycle(minore, reversedWeirdGrid)

  finalPositionMaggiore=arraymaggiore[repeat%lenmaggiore]
  finalPositionMinore=arrayminore[repeat%lenminore]

  res=""
  for x in range(finalPositionMaggiore[0]+1, finalPositionMinore[0]):
    lenElement, arrayElement=cycle((x,finalPositionMaggiore[1]), weirdGrid)
    position=arrayElement[repeat%lenElement]
    res=res+grid[position]

  # QUESTA PARTE SERVE ESCLUSIVAMENTE PER STAMPARE TUTTA LA GRIGLIA FINALE, INUTILE PER IL RISULTATO ma bella per l'easter egg
  #
  # newGrid={}
  # for x in range(maxX+1):
  #   for y in range(maxY+1):
  #     lenElement, arrayElement=cycle((x,y), weirdGrid)
  #     position=arrayElement[repeat%lenElement]
  #     newGrid[(x,y)]=grid[position]
  # stampaGrid(newGrid)


  return res



print(solve(1, "raw.txt"))
print(solve(100, "raw2.txt"))
print(solve(1048576000, "raw3.txt"))
