from utility import *

def parseRows(rows):
  layer=0
  line=0
  grid={}
  for row in rows:
    if not row:
      layer=layer+1
      line=0
      continue
    for idx, char in enumerate(row):
      grid[(idx, line, layer)]=char
    line=line+1

      
  return grid

def sumColor(color1, color2):
  if(color1=="K" or color2=="K"):
    return "K"
  if color1==color2:
    return color1
  
  if color1>color2:
    color1, color2=color2, color1
  if(color1=="C" and color2=="M"):
    return "B"
  if(color1=="C" and color2=="Y"):
    return "G"
  if(color1=="M" and color2=="Y"):
    return "R"
  print("non posso arrivare qui AAAAA", color1, color2)

def computeFinalLayer(grid):
  maxX=max(x[1] for x in grid)
  maxY=max(x[0] for x in grid)
  lastLayer={}
  for i in range(maxY+1):
    for j in range(maxX+1):
      lastLayer[(i,j)]=sumColor(grid[(i,j,0)], grid[(i,j,1)])
  return lastLayer

def calculateTop3(finalLayer):
  resultDict={}
  for element in finalLayer.values():
    resultDict[element]=resultDict.get(element, 0)+1

  resultValues=list(resultDict.values())
  resultValues.sort(reverse=True)
  return resultValues[0]*resultValues[1]*resultValues[2], resultDict

def solve():
  rows=openFile("raw.txt")
  grid=parseRows(rows)
  # print(grid)

  finalLayer=computeFinalLayer(grid)
  return calculateTop3(finalLayer)[0]

def solve2():
  rows=openFile("raw.txt")
  grid=parseRows(rows)
  # print(grid)
  elements={"C":1, "M": 1, "Y": 1, "K": 1}


  dispositions=homeMadeDispositions(elements, 4)
  maxDisposition=0
  for disposition in dispositions:
    tempGrid=dict(grid)
    for k,v in tempGrid.items():
      if k[2]==1:
        tempGrid[k]=disposition[int(v)-1]
    finalLayer=computeFinalLayer(tempGrid)
    maxDisposition=max(maxDisposition, calculateTop3(finalLayer)[0])
  return maxDisposition

def solve3():
  rows=openFile("raw.txt")
  grid, _, _=buildGrid(rows)

  colorOccurrances=calculateTop3(grid)[1]

  # we have 4 bars, we can't move the K bar, so we have 3 bars we can works with, given the possible combination we can easily move content of one bar to content of another
  # so we can easily put one bar at 0 and max the other 2, or put all 3 bars at an *almost* even level (with little remainder if not divisible)
  # IF all 3 bars are equal and K is higher? that means if K is higher than sum of the 3 bars /3, optimum is maximize just 2 bar
  # else optimum is evenize the 3 bars. Anyway it's computationally easier to just calculate and doublecheck

  cellsM=colorOccurrances["M"]
  cellsC=colorOccurrances["C"]
  cellsY=colorOccurrances["Y"]
  cellsK=colorOccurrances["K"]
  sumOfColors=cellsM+cellsC+cellsY

  result, reminder=divmod(sumOfColors,2)    
  twoBars=result*(result+reminder)*cellsK
  result, reminder=divmod(sumOfColors,3)
  threeBars=1
  for i in range(3):
    threeBars=threeBars*(result+int((i<reminder)))
  return max(twoBars, threeBars)
  
# print(solve())
# print(solve2())
print(solve3())