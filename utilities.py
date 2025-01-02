from datetime import date
import math
import aocd

#rotations in 3d, 3,4,5 means -x,-y,-z
rotations=[(0,1,2), (3,4,2), (1,3,2), (4,0,2), (3,1,5), (0,4,5), (1,0,5), (4,3,5),(0,5,1), (3,2,1), (5,3,1), (2,0,1), (3,5,4), (0,2,4), (5,0,4), (2,3,4), (2,1,3), (5,4,3), (1,5,3), (4,2,3), (5,1,0), (2,4,0), (1,2,0), (4,5,0)]

simplifiedSin={0:0, 90:-1, 180:0, 270:1}
simplifiedCos={0:1, 90:0, 180:-1, 270:0}

def simpleRotation(x,y,degree):
  return x*simplifiedCos[degree]-y*simplifiedSin[degree], x*simplifiedSin[degree]+y*simplifiedCos[degree]


def openFile(path):
  file = open(path, "r")
  rows = []
  for line in file:
    rows.append(line.rstrip("\r\n"))
  return rows

def sumTupleValueByValue(a,b):
  return a[0]+b[0], a[1]+b[1]

def sumTupleValueByValueWithLoop(a, b, maxX, maxY):
  return (a[0]+b[0])%(maxX+1), (a[1]+b[1])%(maxY+1)

def sumTriplettesValueByValue(a,b):
  return a[0]+b[0], a[1]+b[1], a[2]+b[2]

def multiplyTupleByValue(a,value):
  return value*a[0], value*a[1],

def mergeDicts(a,b):
  return {key: a.get(key, 0) + b.get(key, 0) for key in a}

def fromDistanceBuildSetOfDirections(distance):
  x=0
  y=distance

  resultSet=set()
  while(x<distance+1):
    resultSet.add((x,y))
    resultSet.add((x,-y))
    resultSet.add((-x,y))
    resultSet.add((-x,-y))
    x=x+1
    y=y-1
  return resultSet

def fromDistanceBuildListOfDirections(distance):
  return list(fromDistanceBuildSetOfDirections(distance))

def fromDistanceBuildSetOfRadialDirections(distance):
  resultSet=set()
  for x in range(-distance, distance+1):
    for y in range(-distance, distance+1):
      resultSet.add((x,y))
  resultSet.remove((0,0))
  return resultSet

def fromDistanceBuildSetOfRadialDirections3D(distance):
  resultSet=set()
  for x in range(-distance, distance+1):
    for y in range(-distance, distance+1):
      for z in range(-distance, distance+1):
        resultSet.add((x,y,z))
  resultSet.remove((0,0,0))
  return resultSet

def distanceBetweenTwoTuples(a,b):
  return abs(a[0]-b[0])+abs(a[1]-b[1])

def distanceBetweenTwoTriplettes(a,b):
  return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])


def sumArrayValueByValue(a, b):
  return list(map(sum, zip(a, b)))

def multiplyArrayByValue(array, value):
  return [value*a for a in array]

def thingInCommonArray(a,b):
  for elementA in a:
    if elementA in b:
      return True
  return False

def thingInCommonArrayWithValue(a,b, ignore=None):
  for elementA in [x for x in a if a!=ignore]:
    if elementA in b:
      return True, elementA
  return False, None

def getAocInput(day, year=date.today().year):
  if(day==-1):
    return openFile("test.txt")
  return aocd.get_data(day=day, year=year).split("\n")

def submitToday(answer):
  return aocd.submit(answer)

def fromBinaryToInteger(binary):
  return int(str(binary),2)

def fromIntegerToBinary(integer):
  return bin(integer)[2:]

def fromHexToInteger(num):
  return int(num, 16)

def arrayDividends(M, itself=True):
  if(M==2):
    return []
  if(M==3):
    return []
  i=1
  temporaryM=M
  collection=[]
  maxFactor= math.floor(math.sqrt(M))
  while(temporaryM%2==0):
    collection.append(2)
    temporaryM=temporaryM//2
  while(temporaryM!=1):
    i+=2
    if(temporaryM%i==0):
      collection.append(i)
      temporaryM=temporaryM//i
      i=1
    if(i>maxFactor):
      if(M!=temporaryM):
        collection.append(temporaryM)
      break
  if(temporaryM==M and itself):
    collection.append(M)
  return collection



def cycleDetection(arrayToCheck, subSequenceMin):

  def findLastIndex(arr, element):
    idx=-1
    for i in range(len(arr)):
      if(arr[i]==element):
        idx=i
    return idx
  
  subSequence=[]
  arrayResults=[]
  startSubSequence=None
  for element in arrayToCheck:
    if(startSubSequence==None):
      idx=findLastIndex(arrayResults, element)
      if(idx!=-1):
        startSubSequence=idx
        subSequence.append(element)
    else:
      if(element==arrayResults[startSubSequence] and len(subSequence)>subSequenceMin):
        #idx start, and sequenece
        return startSubSequence, subSequence
      

      if(element==arrayResults[idx+1]):
        subSequence.append(element)
        idx=idx+1

      else:
        subSequence=[]
        idx=findLastIndex(arrayResults, element)
        if(idx!=-1):
          startSubSequence=idx
          subSequence.append(element)

    arrayResults.append(element)
  print(arrayResults)
  return None, None

def maxGrid(grid):
  return max(a[0] for a in grid), max(a[1] for a in grid)

def minGrid(grid):
  return min(a[0] for a in grid), min(a[1] for a in grid)

def buildGrid(rows, neutralElement="."):
  grid={}
  for y in range(len(rows)):
    for x in range(len(rows[y])):
      if(rows[y][x]!=neutralElement):
        grid[(x,y)]=rows[y][x]
  limits=maxGrid(grid)
  return grid, limits[0], limits[1]

# mi ritorna un set di coordinate invalide per gli spostamenti che circonda una griglia
def cageGridWithWalls(maxLimits, minLimits=(0,0)):
  solution=set()
  for x in range(minLimits[0]-1, maxLimits[0]+2):
    solution.add((x,minLimits[1]-1))
    solution.add((x,maxLimits[1]+1))
  for y in range(minLimits[1], maxLimits[1]+1):
    solution.add((minLimits[0]-1, y))
    solution.add((maxLimits[0]+1, y))
  return solution

def stampaGrid(data, minBound=None, maxBound=None, void="."):
  if isinstance(data, dict):  
      def getValue(x, y):
          return data.get((x, y), void)  
  elif isinstance(data, (set, list)):  
      points=set(data)  
      def getValue(x, y):
          return "#" if (x, y) in points else void
  if(minBound==None):
    minBound=minGrid(data)
  if(maxBound==None):
    maxBound=maxGrid(data)
  for y in range(minBound[1], maxBound[1]+1):
    for x in range(minBound[0], maxBound[0]+1):
      print(getValue(x,y), end="")
    print()

def rotateGrid90(grid, boundaries=None):
  if boundaries==None:
    boundaries=maxGrid(grid)
  rotatedGrid={}
  for k, v in grid.items():
    newX=boundaries[1]-k[1]
    newY=k[0]
    rotatedGrid[(newX, newY)]=v

  return rotatedGrid

def flipGrid(grid, boundaries=None):
  if boundaries==None:
    boundaries=maxGrid(grid)
  return {(boundaries[0]-k[0], k[1]):v for k,v in grid.items()}

def stampaGridFile(grid, maxX=None, maxY=None, void=".", toss=False):
  if toss:
    open("output.txt", "w").close()
  f=open("output.txt", "a")
  if(maxX==None or maxY==None):
    maxX, maxY= maxGrid(grid)
  for y in range(maxY+1):
    for x in range(maxX+1):
      f.write(grid.get((x,y), void))
    f.write("\n")
  f.write("\n")

def removeRowsAndColumnsFromGrid(grid, rowsToRemove=[], columnsToRemove=[]):
  rowsToRemove=sorted(rowsToRemove)
  columnsToRemove=sorted(columnsToRemove)

  rowsShift={}
  columnShift={}
  maxCol, maxRow=maxGrid(grid)
  shift=0
  for rowIdx in range(maxRow+1):
    if rowIdx in rowsToRemove:
      shift=shift+1
    rowsShift[rowIdx]=rowIdx-shift

  shift=0
  for colIdx in range(maxCol+1):
    if colIdx in columnsToRemove:
      shift=shift+1
    columnShift[colIdx]=colIdx-shift

  newGrid={}
  for k,value in grid.items():
    if k[0] in columnsToRemove or k[1] in rowsToRemove:
      continue
    
    newGrid[(columnShift[k[0]], rowsShift[k[1]])]= value

  return newGrid
  

def homeMadePermutations(elements, subPermutation, totalLength, result):
  """
  Build all permutations and put them in parameter result

  Parameters
  __________
  elements: dict
    elements are in the form {"a":3, "b":5}
  subPermutation: str
    subPermutation is in the form of empty string at start
  totalLength: int
    length of the permutations
  result: list
    list of all permutations it found
  """
  if(totalLength==len(subPermutation)):
    result.append(subPermutation)
    return
  
  for element in elements:
    if elements[element]>0:
      elements[element]=elements[element]-1
      homeMadePermutations(elements, subPermutation+element, totalLength, result)
      elements[element]=elements[element]+1

def mergeRanges(ranges):
  sortedRanges= sorted(ranges, key=lambda x: x[0])
  finalList=[]
  for current in sortedRanges:
    if not finalList or finalList[-1][1]<current[0]:
      finalList.append(current)
    else:
      finalList[-1] = (finalList[-1][0], max(finalList[-1][1], current[1]))
  
  return finalList

def numDigit(a):
  return math.floor(math.log10(a)) + 1

def concatenateIntegers(a,b):
  return a * (10 ** numDigit(b)) + b

def modInverse(a,modH):
  return pow(a,-1,modH)

#Cricca Graph Subgraph 
#BronKerbosh trova la cricca massimale più grande, quindi il sottografo completamente connesso piu grande
def bronKerbosh(cricca, tentatives, excludes, graph, maxCricca):
  if len(tentatives)==0 and len(excludes)==0:
    if len(cricca)> len(maxCricca[0]):
      maxCricca[0]=cricca
    return  
  
  #the pivot improve by far, in my problems about one magnitude
  thingsToCheck=[]
  if len(tentatives)>0:
    pivotVertex=next(iter(tentatives))
    thingsToCheck=tentatives.difference(graph[pivotVertex])

  for t in thingsToCheck:
    bronKerbosh(cricca.union({t}), tentatives.intersection(graph[t]), excludes.intersection(graph[t]), graph, maxCricca)
    tentatives.remove(t)
    excludes.add(t)


def evaluateTime(f):
  import time
  t0=time.time()
  f()
  t1=time.time()
  print("time elapsed:", round(t1-t0,3), "s")
  print("time elapsed:", round((t1-t0)*1000, 3), "ms")
  return t1-t0
