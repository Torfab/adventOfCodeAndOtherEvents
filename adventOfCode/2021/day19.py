from utility import *

def parseRows(rows):
  scanners=[]
  currentScanner=-1
  for element in rows:
    if element=="":
      continue
    if element[1]=="-":
      currentScanner=currentScanner+1
      scanners.append(set())
      continue
    tempElement=element.split(',')
    scanners[currentScanner].add((int(tempElement[0]), int(tempElement[1]), int(tempElement[2])))
  return scanners

rotations=[(0,1,2), (3,4,2), (1,3,2), (4,0,2), (3,1,5), (0,4,5), (1,0,5), (4,3,5),(0,5,1), (3,2,1), (5,3,1), (2,0,1), (3,5,4), (0,2,4), (5,0,4), (2,3,4), (2,1,3), (5,4,3), (1,5,3), (4,2,3), (5,1,0), (2,4,0), (1,2,0), (4,5,0)]

def rotate(arrayOfCoords, rotation):
  currentRotation=rotations[rotation]
  firstOpposite=1
  secondOpposite=1
  thirdOpposite=1
  
  firstElement=currentRotation[0]
  secondElement=currentRotation[1]
  thirdElement=currentRotation[2]

  if(firstElement>2):
    firstElement=firstElement-3
    firstOpposite=-1
  if(secondElement>2):
    secondElement=secondElement-3
    secondOpposite=-1
  if(thirdElement>2):
    thirdElement=thirdElement-3
    thirdOpposite=-1

  newArray=[]
  for element in arrayOfCoords:
    newArray.append((element[firstElement]*firstOpposite, element[secondElement]*secondOpposite, element[thirdElement]*thirdOpposite))

  return newArray

# the 24 rotations
#
# 0=x, 1=y, 2=z, 3=-x, 4=-y, 5=-z 

#  z,  y, -x   2,1,3
# -z, -y, -x   5,4,3
#  y, -z, -x   1,5,3
# -y,  z, -x   4,2,3

# -z,  y,  x   5,1,0
#  z, -y,  x   2,4,0
#  y,  z,  x   1,2,0
# -y, -z,  x   4,5,0

#  x,  y,  z   0,1,2
# -x, -y,  z   3,4,2
#  y, -x,  z   1,3,2
# -y,  x,  z   4,0,2

# -x,  y, -z   3,1,5
#  x, -y, -z   0,4,5
#  y,  x, -z   1,0,5
# -y, -x, -z   4,3,5

#  x, -z,  y   0,5,1
# -x,  z,  y   3,2,1
# -z, -x,  y   5,3,1
#  z,  x,  y   2,0,1

# -x, -z, -y   3,5,4
#  x,  z, -y   0,2,4
# -z,  x, -y   5,0,4
#  z, -x, -y   2,3,4

def solve(part):
  rows=getOldAocInput(19)
  scanners=parseRows(rows)

  keysOfAllScanners=[(0,0,0)]
  while(len(scanners)>1):
    j=1
    while(j<len(scanners)):
      for k in range(len(rotations)):
        candidates={}
        afterRotation=rotate(scanners[j], k)
        for element1 in scanners[0]:
          for element2 in afterRotation:
            newElement=(element2[0]*-1, element2[1]*-1, element2[2]*-1)
            candidate=sumTriplettesValueByValue(element1, newElement)
            if(candidates.get(candidate)==None):
              candidates[candidate]=0
            candidates[candidate]=candidates.get(candidate)+1
        if(max(candidates.values())>=12):
          # print("trovato", k, max(candidates.values()), candidates.values())
          break
      # print("ora lo cerco")
      flag=False
      for key, value in candidates.items():
        if (value>=12):
          flag=True
          keysOfAllScanners.append(key)
          break

      if(flag):
        # print(len(scanners[0]))
        for element in afterRotation:
          scanners[0].add(sumTriplettesValueByValue(key, element))
        
        scanners.pop(j)
        j=0
      j=j+1
      
  if(part=="a"):
    return len(scanners[0])

  maxManhattan=0
  # print(keysOfAllScanners)
  for i in range(len(keysOfAllScanners)):
    for j in range(i+1, len(keysOfAllScanners)):
      maxManhattan=max(distanceBetweenTwoTriplettes(keysOfAllScanners[i], keysOfAllScanners[j]), maxManhattan)
  if(part=="b"):
    return maxManhattan

print(solve("a")) 
print(solve("b")) 