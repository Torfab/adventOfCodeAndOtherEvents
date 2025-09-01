from datetime import date
import math
import aocd

#rotations in 3d, 3,4,5 means -x,-y,-z
rotations=[(0,1,2), (3,4,2), (1,3,2), (4,0,2), (3,1,5), (0,4,5), (1,0,5), (4,3,5),(0,5,1), (3,2,1), (5,3,1), (2,0,1), (3,5,4), (0,2,4), (5,0,4), (2,3,4), (2,1,3), (5,4,3), (1,5,3), (4,2,3), (5,1,0), (2,4,0), (1,2,0), (4,5,0)]

blockChar="█"

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

def gcd(a, b):
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a,b):
  return abs(a*b)//gcd(a,b)

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
  

def homeMadePermutationsDeprecated(elements, subPermutation, totalLength, result):
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
      homeMadePermutationsDeprecated(elements, subPermutation+element, totalLength, result)
      elements[element]=elements[element]+1

def homeMadeDispositions(elements, slots):
    """
    elements: dict
        e.g. {"a": 3, "b": 2}
        meaning we can use 'a' up to 3 times, 'b' up to 2 times
    slots: int
        the length of the arrangement
    
    Returns:
        list of lists with all dispositions (ordered sequences)
    """
    results = []
    items = list(elements.items())

    def backtrack(path, remaining):
        if len(path) == slots:
            results.append(path[:])
            return
        if remaining == 0:
            return

        for i, (elem, count) in enumerate(items):
            if count > 0:
                items[i] = (elem, count - 1)
                path.append(elem)
                backtrack(path, remaining - 1)
                path.pop()
                items[i] = (elem, count)

    backtrack([], slots)
    return results

def homeMadeCombinations(elements, slots):
  """
  elements: dict
    elements are in the form {"a":3, "b":5}
  slots: int
    slots are the length of the word of the combination
  """
  results = []
  items = list(elements.items()) 

  def backtrack(start, path, remaining):
      if len(path) == slots:
          results.append(path[:])
          return
      if remaining == 0:
          return
      
      for i in range(start, len(items)):
          elem, count = items[i]
          if count > 0:
              items[i] = (elem, count - 1)
              path.append(elem)
              backtrack(i, path, remaining - 1)
              path.pop()
              items[i] = (elem, count)

  backtrack(0, [], slots)
  return results

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

def extended_gcd(a, b): #useful for diophantine linear equation and Chinese reminder theorem
  if b == 0:
    return (a, 1, 0)  # base case: gcd(a, 0) = a
  else:
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)
  
def combine_congruences(a1, n1, a2, n2):  # Congruence with CRT
  # Combine two congruences: t ≡ a1 mod n1 and t ≡ a2 mod n2
  # It is achievable even just counting if numbers are not too high
  # So you reach the first cycle, and cycle until you get next one
  # so as long as cycle are not on the 10^6 it is easily achievable
  g, m1, m2 = extended_gcd(n1, n2)
  if (a2 - a1) % g != 0:
    return None, None  # No solution
  lcm = (n1 * n2) // g
  t = (a1 + (a2 - a1) // g * m1 * n1) % lcm
  return t, lcm