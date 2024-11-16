from datetime import date
import math
import aocd

#rotations in 3d, 3,4,5 means -x,-y,-z
rotations=[(0,1,2), (3,4,2), (1,3,2), (4,0,2), (3,1,5), (0,4,5), (1,0,5), (4,3,5),(0,5,1), (3,2,1), (5,3,1), (2,0,1), (3,5,4), (0,2,4), (5,0,4), (2,3,4), (2,1,3), (5,4,3), (1,5,3), (4,2,3), (5,1,0), (2,4,0), (1,2,0), (4,5,0)]

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

def distanceBetweenTwoTuples(a,b):
  return abs(a[0]-b[0])+abs(a[1]-b[1])

def distanceBetweenTwoTriplettes(a,b):
  return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])


def sumArrayValueByValue(a, b):
  return list(map(sum, zip(a, b)))

def multiplyArrayByValue(array, value):
  return [value*a for a in array]

def sumArrayValueByValueSeparated(a, b, c):
  return a+c[0], b+c[0]

def thingInCommonArray(a,b):
  for elementA in a:
    for elementB in b:
      if(elementA==elementB):
        return True
  return False

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

def buildGrid(rows, neutralElement="."):
  grid={}
  for y in range(len(rows)):
    for x in range(len(rows[y])):
      if(rows[y][x]!=neutralElement):
        grid[(x,y)]=rows[y][x]
  limits=maxGrid(grid)
  return grid, limits[0], limits[1]

def buildGridWithDots(rows):
  return buildGrid(rows, ".")

def stampaGrid(grid, maxX=None, maxY=None, void="."):
  if(maxX==None or maxY==None):
    maxX, maxY= maxGrid(grid)
  for y in range(maxY+1):
    for x in range(maxX+1):
      print(grid.get((x,y), void), end="")
    print()

def homeMadePermutations(elements, subPermutation, totalLength, result):
  if(totalLength==len(subPermutation)):
    result.append(subPermutation)
    return
  
  for element in elements:
    if elements[element]>0:
      elements[element]=elements[element]-1
      homeMadePermutations(elements, subPermutation+element, totalLength, result)
      elements[element]=elements[element]+1